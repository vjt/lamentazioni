# lamentazioni.org → Hugo → lamentazioni.diomaiale.com

## Source (measured 2026-10-17)
- wget mirror in `mirror/` (115M, 3686 files): WordPress 2.8.3 static dump, posts 2005-2009.
- 907 posts at `/YYYY/MM/DD/<slug>/`; 495 with comments.
- Pages: `about/`, `le-lamentazioni/`. Plus tag/category/author archives (regenerated, not ported).
- Assets: theme `gloriousfuture` (style.css, bg.jpg, header.jpg, icons, author avatars
  `img/<author>.jpg`) under `www.lamentazioni.org/wp-content`; ~530 uploads (jpg/gif/png).

## Plan
1. **Extract** (Python + BeautifulSoup) → `site/content/posts/YYYY/MM/DD-<slug>.md`:
   front matter title/date/author/categories/tags/aliases, body converted to Markdown
   (fall back to raw HTML where conversion loses structure), comments preserved as data and
   rendered under the post.
2. **Hugo site** with a small custom theme porting gloriousfuture: original CSS, backgrounds,
   header, author avatars, date box. Keep the old URLs `/YYYY/MM/DD/<slug>/` so old links work.
   Taxonomies: categories, tags, authors.
3. **Assets**: copy uploads to `static/wp-content/uploads/...`, rewrite links to them, fix the
   CSS's absolute `http://www.lamentazioni.org/...` urls.
4. **pagefind** after `hugo` build (`pagefind --site public`), search box in the header.
5. **Deploy**: CF DNS `lamentazioni.diomaiale.com` → m42, nginx vhost + cert, rsync `public/`.

## Decisions
- 2026-10-17 22:50 vjt: no jail — m42 host docroot `/srv/www/lamentazioni.diomaiale.com`, served by the host nginx.
- Comments: keep them all (default, not contested).
