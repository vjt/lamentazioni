# BUILD REPORT — steps 1-4 (2026-10-17)

**Built:** `tools/extract.py` (bs4) → `site/content` → Hugo 0.131 with custom `gloriousfuture` theme (original CSS/bg/header/avatars/date box, search box in header) → pagefind 1.5.2. Rebuild: `tools/build.sh`, in the `lamentazioni-build` docker image. Nothing installed on the host. Nothing deployed.

**Output:** `/home/vjt/code/lamentazioni/site/public/` (65M)

**Measured:**
- **834 posts, not 907.** The archive dropdown adds up to 834, and the mirror has 834 unique canonical post IDs. The 907 in PLAN was wrong. All 834 are at their old `/YYYY/MM/DD/slug/`.
- 496 posts with comments, 2880 comments in total. Per-post count matches the source (0 mismatches).
- Hugo build is clean (0 warnings). about/, le-lamentazioni/ (105 pages, same as WP) and the Disclaimer home are in place. Aliases point `/blog-static/...` to the new URLs.
- Rendered text equals source text on 834/834 posts. 474 posts are in Markdown; 360 stay raw HTML because Markdown lost structure.
- 1274 local images resolve. pagefind indexes 836 pages.

**Lost (dead at the source too, all 404):** cossiga.jpg, p-codice_250.jpg, cofferati.jpg, coglioni.jpg, avatars anonymous/inna, one link to a deleted post.

**For vjt to decide:** recover the 4 lost images from archive.org? About 60 hotlinked external images (estimated count, not checked) are probably dead (download or leave). Rewrite `/blog-static/` in nginx instead of using aliases. Not checked in a browser yet.

# Image recovery, social meta, mobile search (2026-10-17)

- **Lost 6 (4 uploads + avatars anonymous/inna): 0/6 recovered.** archive.org CDX has only 404 captures of them, no image capture on any lamentazioni.org path.
- **Hotlinked images: 88 unique.** Measured live: 18 alive, 70 dead. Wayback: 47 recovered (all 18 live ones + 29 dead), 41 unrecoverable, left hotlinked. Wayback copy (closest to post date) preferred over live; 2 photobucket ones carry the photobucket watermark. Copies in `static/ext/`, map in `tools/ext_images.json`, rebuilt by `tools/recover_images.py`, applied by `extract.py`.
- **Meta:** canonical, description (≤200 chars, max 197 measured), og:* + image size/type, article:published_time, twitter:card, RSS, sitemap, robots.txt. og:image: 257 pages use their own image, 581 use `og-default.jpg` (1200x630, 112411 B). All under 300KB, JPEG/PNG.
- **Search:** results drawer no longer clipped by the header (`overflow:hidden` from style.css), fits 390px (scrollWidth 390), result titles are post titles, 836 pages indexed (posts + 2 pages). Screenshot: `tmp/search-390.png`.
- Commit e433aad pushed, deployed to m42. curl: `/ext/824da41d16-zecca.jpg` and `/ext/161412c900-Freira.jpg` 200 image/jpeg; og:image 200 image/jpeg for a post with image (13643 B), a post without (og-default, 112411 B), home (12969 B).
