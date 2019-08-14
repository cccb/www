#!/usr/bin/env sh

hugo $(cat .hugo-params)
tools/merge_cals.py
upcoming="$(tools/gen_upcoming.py static/all.ics 20 5|tr '\n' ' ')"
cp static/all.ics public/all.ics
sed -i "s#CALENDAR#$upcoming#g" public/index.html
