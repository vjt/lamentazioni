# lamentazioni

Resurrection of **lamentazioni.org**, an Italian group rant blog (WordPress, 2005–2009),
now served as a static site at **https://lamentazioni.diomaiale.com**.

907 posts, comments included, rebuilt from a `wget` mirror of the original WordPress
into a Hugo site that keeps the original `gloriousfuture` theme and the old
`/YYYY/MM/DD/<slug>/` URLs, so links from 2005 still resolve.

## Layout

- `mirror/` — the original static dump of lamentazioni.org (source of truth, read-only)
- `tools/extract.py` — HTML → Markdown + front matter + comments, into `site/content/`
- `tools/recover_images.py` — fetches images that died with their hosts back from archive.org
- `tools/check_*.py` — text, structure and link checks run after every build
- `site/` — Hugo site: config, ported theme, static assets
- `PLAN.md`, `BUILD_REPORT.md` — how it was done and what was measured

## Build

Everything runs inside a Docker image, nothing gets installed on the host:

```sh
tools/build.sh
```

That runs extract → `hugo` → checks → [pagefind](https://pagefind.app/) (client-side
search). The output lands in `site/public/`, ready to be copied to any static web server.

## License

The posts and comments belong to their original authors.
