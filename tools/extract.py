#!/usr/bin/env python3
"""Extract posts + pages + comments from the WordPress wget mirror into Hugo content.

Runs inside the lamentazioni-build container (bs4, html2text, yaml):
  python3 -I /w/tools/extract.py [--html-list /w/tmp/force_html.txt]
"""
import os, re, json, posixpath, argparse
from urllib.parse import unquote, unquote_to_bytes
import yaml, html2text
from bs4 import BeautifulSoup, Comment

W = '/w'
MIRROR = W + '/mirror/lamentazioni.org'
SITE = W + '/site'
CANON = re.compile(rb'^(\d{4})/(\d{2})/(\d{2})/([^/]+)/index\.html$')
MONTHS = {m: i for i, m in enumerate('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split(), 1)}
TZ = '+02:00'  # WP had a fixed gmt_offset of 2 (feed UTC 13:08 == page 3:08 pm in March)
OWN = re.compile(r'^https?://(?:www\.)?lamentazioni\.org(?:/blog-static)?(/.*)?$', re.I)

# tags that markdown (html2text + goldmark) round-trips cleanly
SIMPLE = {'p', 'br', 'a', 'strong', 'b', 'em', 'i', 'img', 'blockquote', 'ul', 'ol', 'li',
          'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'code', 'pre'}


def local_path(url, page_dir):
    """Map a link found in the mirror to a site path, or None if external."""
    if not url or url.startswith(('#', 'mailto:', 'javascript:', 'data:')):
        return None
    m = OWN.match(url)
    if m:
        p = m.group(1) or '/'
    elif re.match(r'^[a-z][a-z0-9+.-]*:', url, re.I) or url.startswith('//'):
        return None
    else:
        path, sep, frag = url.partition('#')
        p = posixpath.normpath(posixpath.join('/' + page_dir, path)) if path else '/' + page_dir
        if path.endswith('/') and not p.endswith('/'):
            p += '/'
        if frag:
            p += '#' + frag
    p = re.sub(r'^/www\.lamentazioni\.org(?=/)', '', p)
    p = re.sub(r'^/lamentazioni\.org(?=/)', '', p)
    p = re.sub(r'^/blog-static(?=/)', '', p)
    # wget artefacts: dir/index.html -> dir/ ; foo.php.html -> foo.php
    p = re.sub(r'(^|/)index\.html(\?[^#]*)?(?=#|$)', r'\1', p)
    p = re.sub(r'\.php\.html', '.php', p)
    if p.startswith('/feed') or p.startswith('/comments/feed'):
        p = re.sub(r'^/(comments/)?feed.*', '/index.xml', p)
    return p or '/'


def rewrite_links(node, page_dir, stats):
    for tag, attr in (('a', 'href'), ('img', 'src'), ('embed', 'src'), ('param', 'value'),
                      ('iframe', 'src'), ('source', 'src')):
        for el in node.find_all(tag):
            v = el.get(attr)
            if not v:
                continue
            lp = local_path(v.strip(), page_dir)
            if lp is not None:
                el[attr] = lp
                if '/wp-content/' in lp:
                    stats['local_assets'].add(lp.split('#')[0])


def fix_attachment_links(node):
    """WP attachment pages were not ported: point <a rel=attachment><img></a> at the image."""
    for a in node.find_all('a', href=True):
        h = a['href']
        if 'attachment_id=' in h or 'rel' in a.attrs and 'attachment' in a['rel'] \
                or '/uno_in_particolare/' in h:
            img = a.find('img')
            if img and img.get('src', '').startswith('/wp-content/'):
                a['href'] = img['src']


def norm_text(s):
    return re.sub(r'\s+', ' ', s).strip()


def is_simple(entry):
    for el in entry.find_all(True):
        if el.name not in SIMPLE:
            return False
        if el.get('style') or el.get('align'):
            return False
        if el.name == 'img' and (el.get('class') or el.get('width') or el.get('height')):
            return False
        if el.name in ('a',) and el.get('target'):
            return False
    return True


def to_markdown(entry_html):
    h = html2text.HTML2Text()
    h.body_width = 0
    h.unicode_snob = True
    h.inline_links = True
    h.protect_links = True
    h.wrap_links = False
    h.images_to_alt = False
    h.single_line_break = False
    return h.handle(entry_html).strip() + '\n'


def parse_date(post):
    box = post.select_one('p.box.right')
    if not box:
        return None
    mon = MONTHS[box.select_one('.month').get_text(strip=True)[:3]]
    day = int(box.select_one('.day').get_text(strip=True))
    year = int(box.select_one('.year').get_text(strip=True))
    hh, mm = 0, 0
    meta = post.select_one('.meta')
    if meta:
        m = re.search(r'Posted at (\d+):(\d+) (am|pm)', meta.get_text())
        if m:
            hh, mm = int(m.group(1)) % 12 + (12 if m.group(3) == 'pm' else 0), int(m.group(2))
    return f'{year:04d}-{mon:02d}-{day:02d}T{hh:02d}:{mm:02d}:00{TZ}'


def parse_comment_date(s):
    m = re.search(r'on (\d+) (\w{3}) (\d{4}) at (\d+):(\d+) (am|pm)', s)
    if not m:
        return None
    d, mon, y, hh, mm, ap = m.groups()
    hh = int(hh) % 12 + (12 if ap == 'pm' else 0)
    return f'{int(y):04d}-{MONTHS[mon]:02d}-{int(d):02d}T{hh:02d}:{int(mm):02d}:00{TZ}'


def extract_comments(soup, page_dir, stats):
    out = []
    ol = soup.select_one('ol.commentlist')
    if not ol:
        return out
    for li in ol.find_all('li', recursive=False):
        info = li.select_one('.cmtinfo')
        cite = info.find('cite') if info else None
        author_url = None
        if cite and cite.find('a'):
            author_url = cite.find('a').get('href')
        em = info.find('em') if info else None
        for x in li.find_all(string=lambda t: isinstance(t, Comment)):
            x.extract()
        if info:
            info.extract()
        rewrite_links(li, page_dir, stats)
        body = ''.join(str(c) for c in li.contents).strip()
        c = {
            'id': int(li.get('id', 'comment-0').split('-')[-1]),
            'author': cite.get_text(strip=True) if cite else '',
            'date': parse_comment_date(em.get_text()) if em else None,
            'body': body,
        }
        if author_url:
            c['author_url'] = author_url
        if 'authorcomment' in (li.get('class') or []):
            c['by_post_author'] = True
        out.append(c)
    return out


def clean_entry(entry):
    for x in entry.select('p.post-tags'):
        x.decompose()
    for x in entry.find_all(string=lambda t: isinstance(t, Comment)):
        x.extract()
    return entry


def dump(path, fm, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1 << 20))
        f.write('---\n')
        f.write(body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--html-list', help='file of post urls forced to raw HTML')
    args = ap.parse_args()
    force_html = set()
    if args.html_list and os.path.exists(args.html_list):
        force_html = {l.strip() for l in open(args.html_list) if l.strip()}

    stats = {'local_assets': set(), 'posts': 0, 'md': 0, 'html': 0, 'with_comments': 0,
             'comments': 0, 'terms': {'tags': {}, 'categories': {}, 'authors': {}}}
    manifest = []
    root_b = os.fsencode(MIRROR)
    for dp, dn, fn in os.walk(root_b):
        if b'index.html' not in fn:
            continue
        rel = os.path.relpath(os.path.join(dp, b'index.html'), root_b)
        m = CANON.match(rel)
        if not m:
            continue
        raw = open(os.path.join(root_b, rel), 'rb').read().decode('utf-8', 'replace')
        if 'class="pagenav"' not in raw or raw.count('class="post" id="post-') != 1:
            continue
        y, mo, d, slug_b = (g for g in m.groups())
        y, mo, d = y.decode(), mo.decode(), d.decode()
        slug = unquote_to_bytes(slug_b).decode('utf-8', 'replace')
        page_dir = posixpath.dirname(rel.decode('utf-8', 'replace')) + '/'
        url = f'/{y}/{mo}/{d}/{slug}/'

        soup = BeautifulSoup(raw, 'lxml')
        post = soup.select_one('div.post')
        title = post.select_one('h2.title').get_text(strip=True)
        date = parse_date(post)
        author_a = post.select_one('p.box.left a[href*="author/"]')
        author_slug = re.search(r'author/([^/]+)/', author_a['href']).group(1)
        author_name = author_a.get_text(strip=True)
        avatar = post.select_one('p.box.left img')
        avatar = os.path.basename(avatar['src']) if avatar else None
        if avatar and not os.path.exists(f'{SITE}/themes/gloriousfuture/static/wp-content/themes/gloriousfuture/img/{avatar}'):
            stats.setdefault('missing_avatars', []).append(avatar); avatar = None
        stats['terms']['authors'][author_slug] = author_name
        cats, tags = [], []
        for a in post.select('.meta a[rel~="category"]'):
            s = re.search(r'category/(.+?)/index\.html', a['href']).group(1).split('/')[-1]
            s = unquote(s)
            cats.append(s); stats['terms']['categories'][s] = a.get_text(strip=True)
        for a in post.select('p.post-tags a[rel="tag"]'):
            s = unquote(re.search(r'tag/([^/]+)/', a['href']).group(1))
            tags.append(s); stats['terms']['tags'][s] = a.get_text(strip=True)
        pid = int(post['id'].split('-')[1])

        entry = clean_entry(post.select_one('div.entry'))
        rewrite_links(entry, page_dir, stats)
        fix_attachment_links(entry)
        inner = ''.join(str(c) for c in entry.contents).strip()
        comments = extract_comments(soup, page_dir, stats)

        fm = {'title': title, 'date': date, 'url': url, 'aliases': [f'/blog-static{url}'],
              'wp_id': pid, 'authors': [author_slug], 'avatar': avatar,
              'categories': cats, 'tags': tags}
        if comments:
            fm['comments'] = comments
            stats['with_comments'] += 1
            stats['comments'] += len(comments)
        use_html = url in force_html or not is_simple(entry)
        base = f'{SITE}/content/posts/{y}/{mo}/{d}-{slug}'
        for ext in ('.md', '.html'):
            if os.path.exists(base + ext):
                os.remove(base + ext)
        if use_html:
            dump(base + '.html', fm, inner + '\n'); stats['html'] += 1
        else:
            dump(base + '.md', fm, to_markdown(inner)); stats['md'] += 1
        stats['posts'] += 1
        manifest.append({'url': url, 'src': rel.decode('utf-8', 'replace'), 'id': pid,
                         'format': 'html' if use_html else 'md', 'comments': len(comments),
                         'text': norm_text(BeautifulSoup(inner, 'lxml').get_text(' '))})

    # static pages
    for name in ('about', 'anche-i-nani-hanno-cominciato-da-piccoli', ''):
        rel = (name + '/' if name else '') + 'index.html'
        soup = BeautifulSoup(open(f'{MIRROR}/{rel}', encoding='utf-8').read(), 'lxml')
        post = soup.select_one('div.post')
        entry = clean_entry(post.select_one('div.entry'))
        rewrite_links(entry, posixpath.dirname(rel) + '/' if name else '', stats)
        inner = ''.join(str(c) for c in entry.contents).strip()
        fm = {'title': post.select_one('h2.title').get_text(strip=True)}
        comments = extract_comments(soup, (name + '/') if name else '', stats)
        if comments:
            fm['comments'] = comments
        if name:
            fm['url'] = f'/{name}/'
            dump(f'{SITE}/content/pages/{name}.html', fm, inner + '\n')
        else:
            fm['wp_id'] = int(post['id'].split('-')[1])
            dump(f'{SITE}/content/_index.html', fm, inner + '\n')

    dump(f'{SITE}/content/posts/_index.md', {'title': 'Le lamentazioni', 'url': '/le-lamentazioni/'}, '')
    dump(f'{SITE}/content/pages/_index.md', {'title': 'Pagine', 'build': {'render': 'never'}}, '')

    # taxonomy term pages carry the original display names; slugs stay WP's
    for tax, terms in stats['terms'].items():
        for s, name in terms.items():
            dump(f'{SITE}/content/{tax}/{unquote(s)}/_index.md', {'title': name, 'slug': s}, '')

    os.makedirs(W + '/tmp', exist_ok=True)
    json.dump(manifest, open(W + '/tmp/manifest.json', 'w'), ensure_ascii=False)
    json.dump(sorted(stats['local_assets']), open(W + '/tmp/local_assets.json', 'w'))
    s = {k: v for k, v in stats.items() if k not in ('local_assets', 'terms')}
    s.update({f'terms_{k}': len(v) for k, v in stats['terms'].items()})
    print(json.dumps(s))


if __name__ == '__main__':
    main()
