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
