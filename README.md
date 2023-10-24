![CCCB logo](static/img/logo.png)

# CCCB Website

This is the website of the CCCB.

## Getting started

1. Get Hugo: <https://gohugo.io/getting-started/installing>
2. Clone this repo
   ```shell
   git clone https://github.com/cccb/www
   ```
3. Switch directory
   ```shell
   cd www
   ```
3. Fetch Submodules
   ```shell
   git submodule update --recursive --remote --init
   ```

### Run site locally

Run hugo webserver:

```shell
hugo serve
```

Point your browser to: http://localhost:1313/

To ready your site for upload, run `./build.sh`, which also generates `all.ics` and adds the calendar table to `index.html`.
Every change you make on the project will be reflected in your browser as long as `hugo serve` is running.

## Making a change

1. Use your local dev setup (see Getting started) or via GitHub editor.
2. Make your change in `staging` branch.
3. Commit (and push) your change.
4. GitHub Actions is running the release workflow.
   - If successful, check [Staging Website](https://staging.berlin.ccc.de/) if change is correct.
5. Create merge request to merge changes from `staging` to `production` branch. Ask somebody to check merge request or if small change, merge yourself.
6. GitHub Actions is running the release workflow.
   - If successfull, check [Website](https://berlin.ccc.de/) if change is correct.
7. Profit!

---

Made with ❤️ and [Hugo](https://gohugo.io).

