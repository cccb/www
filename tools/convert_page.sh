#!/bin/sh

if [ $# -lt 2 ]; then
  echo "Usage: $0 Mediawiki_Page_Name [page|post]"
  exit
fi

echo Converting $1...

page=$(echo $1 | sed 's,/,_,g' | tr '[:upper:]' '[:lower:]')

hugo new $2/$page.md
curl -s "https://berlin.ccc.de/api.php?action=query&prop=revisions&rvprop=content&format=json&titles=$1" \
    | jq -r '.query.pages |..| objects|.["*"]' \
    | sed '/null/d' \
    | pandoc -f mediawiki -t markdown \
    >> content/$2/$page.md
