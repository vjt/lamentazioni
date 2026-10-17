# throwaway build image: bs4/html2text for extract.py, hugo for the site
FROM debian:trixie
RUN apt-get update && apt-get install -y --no-install-recommends python3-bs4 python3-lxml python3-yaml python3-html2text hugo ca-certificates && rm -rf /var/lib/apt/lists/*
