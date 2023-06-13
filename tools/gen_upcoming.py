#!/usr/bin/env python3

import sys
import logging
import locale
from dateutil.parser import parse
from datetime import datetime, timedelta
from dateutil.rrule import rruleset, rrulestr

import icalendar


def vevent_to_event(event, rrstart=None):
    if rrstart == None:
        begin = parse(event["DTSTART"].to_ical())
    else:
        begin = rrstart

    return {
        "name": event["SUMMARY"].to_ical(),
        "url": event["URL"].to_ical(),
        "begin": begin
    }


def parse_single_event(event, start, end):
    logging.info(f"Processing single event {event['SUMMARY'].to_ical().decode('utf-8')}")
    dtstart = parse(event["DTSTART"].to_ical())
    if dtstart >= start and dtstart < end:
        return vevent_to_event(event)


def parse_recurring_event(event, start, end):
    logging.info(f"Processing recurring event {event['SUMMARY'].to_ical().decode('utf-8')}")
    dtstart = parse(event["DTSTART"].to_ical())
    rs = rruleset()
    rs.rrule(rrulestr(event["RRULE"].to_ical().decode("utf-8"), dtstart=dtstart))
    if "EXDATE" in event.keys():
        for exdate in event["EXDATE"]:
            rs.exdate(parse(exdate.to_ical()))

    events = []
    for date in list(rs):
        if date >= start and date < end:
            events.append(vevent_to_event(event, date))

    return events


def find_events(icsfilestr, start, end, num):
    with open(icsfilestr, "r") as icsfile:
        cal = icalendar.Calendar.from_ical(icsfile.read())

    events = []
    for event in cal.subcomponents:
        if event.name == "VEVENT":
            if "RRULE" in event.keys():
                events.append(parse_recurring_event(event, start, end))
            elif ev := parse_single_event(event, start, end) != None:
                events.append(ev)

    events = sorted(events, key=lambda k: k["begin"])
    events = events[0:num]

    return events


def format_events(events):
    print("<table class=\"table table-condensed\">")
    for event in events:
        print(
            "<tr>"
            f"<td>{event['begin'].strftime('%A, %d.%m um %H:%M Uhr')}</td>"
            f"<td><a href=\"{event['url'].decode('utf-8')}\">{event['name'].decode('utf-8')}</a></td>"
            "</tr>"
        )
    print("</table><!--/.table /.table-condensed-->")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} calendar max_days max_items")
        sys.exit(-1)

    locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")
    calendar = sys.argv[1]
    max_days = int(sys.argv[2])
    max_items = int(sys.argv[3])

    now = datetime.now()
    events = find_events(calendar, now, now + timedelta(days=max_days), max_items)
    format_events(events)

