#!/bin/sh

hugo $(cat .hugo-params)
./tools/merge_cals.py
upcoming="$(tools/gen_upcoming.py static/all.ics 20 5 | tr '\n' ' ')"
echo $upcoming
cat public/index.html
cp static/all.ics public/all.ics
sed -i "s#CALENDAR#$upcoming#g" public/index.html
cat public/index.html
echo $upcoming