[![pipeline status](https://gitlab.berlin.ccc.de/cccb/www/badges/master/pipeline.svg)](https://gitlab.berlin.ccc.de/cccb/www/commits/master)

Running a dev setup
-------------------

* Get Hugo: <https://gohugo.io/getting-started/installing>
* Clone this repo:: `git clone https://github.com/cccb/www`
* Switch directory: `cd www`
* Fetch Submodules: `git submodule update --recursive --remote --init`
* run hugo webserver: `hugo serve`
* Point your browser to `http://localhost:1313/`
* To ready your site for upload, run "./build.sh", which also generates all.ics
  and adds the calendar table to index.html

Every change you make on the project will be reflected in your browser as
long as `hugo serve` is running.
