#!/usr/bin/env python3

from glob import glob
import icalendar
import pytz

cals=[]
merged=icalendar.Calendar()
merged.add('prodid', '-//CCCB Calendar Generator//berlin.ccc.de//')
merged.add('version', '2.0') 

for icsfilestr in glob("public/*/**/*.ics", recursive=True):
	with open(icsfilestr, 'r') as icsfile:
		print("Importing", icsfilestr)
		cals.append(icalendar.Calendar.from_ical(icsfile.read()))

for cal in cals:
	for e in cal.subcomponents:
		merged.add_component(e)

outfile="static/all.ics"
with open(outfile, 'wb') as f:
	print(f"writing to {outfile}...")
	f.write(merged.to_ical())
	
