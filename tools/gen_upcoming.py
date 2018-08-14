#!/usr/bin/env python3

import sys
import logging
import locale
from pprint import pprint
from dateutil.parser import parse
from datetime import datetime, timedelta
from dateutil.rrule import rruleset, rrulestr

import icalendar


def vevent_to_event(event, rrstart=None):
	if rrstart == None:
		begin = parse(event['DTSTART'].to_ical())
	else:
		begin = rrstart
	return { "name": event['SUMMARY'].to_ical(), "url": event['URL'].to_ical(), "begin": begin }


def parse_single_event(event, start, end):
	logging.info("Processing single event %s" % event['SUMMARY'].to_ical().decode('utf-8'))
	dtstart = parse(event['DTSTART'].to_ical())
	if dtstart >= start and dtstart < end:
		return vevent_to_event(event)
	else:
		return None


def parse_recurring_event(event, start, end):
	logging.info("Processing recurring event %s" % event['SUMMARY'].to_ical().decode('utf-8'))
	dtstart = parse(event['DTSTART'].to_ical())
	rs = rruleset()
	rs.rrule(rrulestr(event['RRULE'].to_ical().decode('utf-8'), dtstart=dtstart))
	if 'EXDATE' in event.keys():
		exdates = event['EXDATE']
		for exdate in exdates:
			rs.exdate(parse(exdate.to_ical()))

	dates = list(rs)
	events = []
	for date in dates:
		if date >= start and date < end:
			events.append(vevent_to_event(event, date))
	return events


def find_events(icsfilestr, start, end, num):
	with open(icsfilestr, 'r') as icsfile:
		cal=icalendar.Calendar.from_ical(icsfile.read())

	events=[]
	for event in cal.subcomponents:
		if event.name == 'VEVENT':
			if 'RRULE' in event.keys():
				events = events + parse_recurring_event(event, start, end)
			else:
				ev = parse_single_event(event, start, end)
				if ev != None:
					events.append(ev)

	events = sorted(events, key=lambda k: k['begin'])
	events = events[0:num]
	return events


def format_events(events):
	print('<table class="table table-condensed">')
	for event in events:
		dateStr = event['begin'].strftime("%A, %d.%m um %H:%M Uhr")
		#print("<li><a href=\"%s\">%s: %s</a></li>" % (event['url'].decode('utf-8'), dateStr, event['name'].decode('utf-8')))
		print("<tr><td>%s</td><td><a href=\"%s\">%s</a></td></tr>"
			% (dateStr, event['url'].decode('utf-8'), event['name'].decode('utf-8')))
	print('</table>')


if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Usage: %s calendar max_days max_items" % sys.argv[0])
		sys.exit(-1)

	locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")
	calendar=sys.argv[1]
	max_days=int(sys.argv[2])
	max_items=int(sys.argv[3])

	events=find_events(calendar, datetime.now(), datetime.now() + timedelta(days=max_days), max_items)
	format_events(events)

