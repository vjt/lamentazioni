#!/bin/sh
# Rebuild everything from mirror/: extract -> hugo -> checks -> pagefind. No deploy.
set -e
cd "$(dirname "$0")/.."
D="docker run --rm -v $PWD:/w -u $(id -u) lamentazioni-build nice"
docker image inspect lamentazioni-build >/dev/null 2>&1 || docker build -t lamentazioni-build tools/
find site/content -mindepth 1 -maxdepth 1 ! -name posts -exec rm -rf {} +
find site/content/posts -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} +
mkdir -p tmp
$D python3 -I /w/tools/extract.py --html-list /w/tools/force_html.txt
$D sh -c 'cd /w/site && hugo --cleanDestinationDir'
$D sh -c 'python3 -I /w/tools/check_text.py; python3 -I /w/tools/check_struct.py; python3 -I /w/tools/check_links.py'
nice pagefind --site site/public
