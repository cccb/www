#!/usr/bin/env python3

from glob import glob

import pytz
import icalendar


calendars = []
merged = icalendar.Calendar()
merged.add("prodid", "-//CCCB Calendar Generator//berlin.ccc.de//")
merged.add("version", "2.0")

for icsfilestr in glob("public/*/**/*.ics", recursive=True):
	with open(icsfilestr, "r") as icsfile:
		print(f"Importing {icsfilestr}")
		calendars.append(icalendar.Calendar.from_ical(icsfile.read()))

for calendar in calendars:
	for event in calendar.subcomponents:
		merged.add_component(event)

outfile = "static/all.ics"
with open(outfile, "wb") as f:
	print(f"writing to {outfile}...")
	f.write(merged.to_ical())

