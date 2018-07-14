#!/usr/bin/env sh

hugo
tools/merge_cals.py
upcoming="$(tools/gen_upcoming.py static/all.ics 14 5|tr '\n' ' ')"
sed -i "s#CALENDAR#$upcoming#g" public/index.html
