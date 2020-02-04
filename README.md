[![pipeline status](https://gitlab.berlin.ccc.de/cccb/www/badges/master/pipeline.svg)](https://gitlab.berlin.ccc.de/cccb/www/commits/master)

# CCCB Website

This is the website of CCCB.

## Getting started

Get Hugo: <https://gohugo.io/getting-started/installing>

Clone this repo
```
git clone https://github.com/cccb/www
```

Switch directory
```
cd www
```

Fetch Submodules
```
git submodule update --recursive --remote --init
```

### Run site locally

Run hugo webserver
```
hugo serve
```
Point your browser to http://localhost:1313/

To ready your site for upload, run "./build.sh", which also generates all.ics and adds the calendar table to index.html
Every change you make on the project will be reflected in your browser as long as `hugo serve` is running.

## Making a change

* Use your local dev setup (see Getting started) or via GitLab editor. 
* Make your change in `staging` branch.
* Commit (and push) your change.
* Gitlab CI is running pipeline. If successfull, check [Staging Website](https://staging.berlin.ccc.de/) if change is correct.
* Create merge request to merge changes from `staging` to `production`. Ask somebody to check merge request or if small change, merge yourself.
* Gitlab CI is running pipeline. If successfull, check [Website](https://berlin.ccc.de/) if change is correct.

