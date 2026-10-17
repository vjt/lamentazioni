#!/usr/bin/env python3
"""Mirror the external (hotlinked) images locally, preferring the Wayback Machine.

Runs on the host (needs network, stdlib only), after extract.py has written
tmp/external_images.json ({url: post date}). For each URL not yet in tools/ext_images.json:
  1. probe the live URL (GET, 20s timeout) -> alive if 200 + image magic bytes
  2. ask the Wayback CDX API for the 200/image capture closest to the post date, fetch it raw (id_)
  3. store wayback copy if any (it is what the post showed), else the live copy, under
     site/static/ext/; record the result in tools/ext_images.json.
extract.py then rewrites <img src> (and <a href> to the same URL) to the local copy.
Polite to archive.org: sequential, 1s sleep, backoff on 429/5xx.

  python3 -I tools/recover_images.py [--retry-failed]
"""
import os, sys, json, time, hashlib, re, posixpath, argparse
import urllib.request, urllib.error, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = ROOT + '/tools/ext_images.json'
WANT = ROOT + '/tmp/external_images.json'
STATIC = ROOT + '/site/static'
UA = 'Mozilla/5.0 (X11; Linux x86_64) lamentazioni-archiver/1.0 (+https://lamentazioni.diomaiale.com/)'
MAGIC = [(b'\xff\xd8\xff', 'jpg'), (b'\x89PNG\r\n\x1a\n', 'png'), (b'GIF87a', 'gif'),
         (b'GIF89a', 'gif'), (b'BM', 'bmp')]


def kind(data):
    if data[:4] == b'RIFF' and data[8:12] == b'WEBP':
        return 'webp'
    for m, k in MAGIC:
        if data.startswith(m):
            return k
    return None


def get(url, timeout=20):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read(20 << 20)


def wayback(url, tries=6):
    """GET against archive.org with sleep + backoff on 429/5xx/timeouts."""
    delay = 5
    for i in range(tries):
        time.sleep(1)
        try:
            st, body = get(url, timeout=60)
            if b'Temporarily Offline' in body[:2000] and b'Internet Archive' in body[:2000]:
                raise urllib.error.HTTPError(url, 503, 'offline page', None, None)
            return st, body
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504) or i == tries - 1:
                return e.code, b''
        except Exception:
            if i == tries - 1:
                return None, b''
        time.sleep(delay)
        delay *= 2
    return None, b''


def probe_live(url):
    try:
        st, body = get(url)
        k = kind(body)
        return (st == 200 and k is not None), body, f'{st} {k or "not-image"}'
    except urllib.error.HTTPError as e:
        return False, b'', f'HTTP {e.code}'
    except Exception as e:
        return False, b'', type(e).__name__ + ': ' + str(e)[:60]


def from_wayback(url, date):
    ts = re.sub(r'\D', '', date or '')[:14] or '2008'
    q = urllib.parse.urlencode({'url': url, 'output': 'json', 'fl': 'timestamp,original,mimetype',
                                'filter': 'statuscode:200', 'sort': 'closest', 'closest': ts,
                                'limit': '10'})
    st, body = wayback('http://web.archive.org/cdx/search/cdx?' + q)
    if st != 200:
        return None, None, f'cdx {st}'
    try:
        rows = json.loads(body or b'[]')[1:]
    except ValueError:
        return None, None, 'cdx bad json'
    for t, orig, mime in rows:
        st, data = wayback(f'http://web.archive.org/web/{t}id_/{orig}')
        if st == 200 and kind(data):
            return data, t, f'wayback {t}'
    return None, None, f'cdx {len(rows)} captures, none an image'


def store(url, data):
    k = kind(data)
    base = posixpath.basename(urllib.parse.urlsplit(url).path) or 'img'
    base = re.sub(r'[^A-Za-z0-9._-]+', '_', urllib.parse.unquote(base))
    base = re.sub(r'\.[A-Za-z0-9]{2,4}$', '', base)[:60] or 'img'
    name = f'{hashlib.sha1(url.encode()).hexdigest()[:10]}-{base}.{k}'
    os.makedirs(STATIC + '/ext', exist_ok=True)
    with open(f'{STATIC}/ext/{name}', 'wb') as f:
        f.write(data)
    return '/ext/' + name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--retry-failed', action='store_true')
    args = ap.parse_args()
    want = json.load(open(WANT))
    m = json.load(open(MAP)) if os.path.exists(MAP) else {}
    for url, date in sorted(want.items()):
        if url in m and (m[url]['local'] or not args.retry_failed):
            continue
        alive, live, live_note = probe_live(url)
        data, ts, wb_note = from_wayback(url, date)
        src = None
        if data:
            src = 'wayback'
        elif alive:
            data, src = live, 'live'
        e = {'date': date, 'alive': alive, 'live': live_note, 'wayback': wb_note, 'source': src,
             'local': store(url, data) if data else None}
        if data and alive:
            e['same_as_live'] = hashlib.sha1(live).hexdigest() == hashlib.sha1(data).hexdigest()
        m[url] = e
        print(('OK  ' if data else 'FAIL') + f' {src or "-":7} live={live_note:24} {wb_note:28} {url}',
              flush=True)
        json.dump(m, open(MAP, 'w'), indent=1, sort_keys=True, ensure_ascii=False)
    n = len(m)
    print(json.dumps({'urls': n, 'alive': sum(e['alive'] for e in m.values()),
                      'dead': sum(not e['alive'] for e in m.values()),
                      'from_wayback': sum(e['source'] == 'wayback' for e in m.values()),
                      'from_live': sum(e['source'] == 'live' for e in m.values()),
                      'unrecoverable': sum(not e['local'] for e in m.values())}))


if __name__ == '__main__':
    main()
