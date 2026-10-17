import json,re,os,collections
from bs4 import BeautifulSoup
pub='/w/site/public'; mir='/w/mirror/lamentazioni.org/'
man=json.load(open('/w/tmp/manifest.json'))
norm={'b':'strong','i':'em'}
def sig(e):
    c=collections.Counter(norm.get(t.name,t.name) for t in e.find_all(['a','img','blockquote','li','strong','b','em','i','ul','ol','pre','code']))
    return c
bad=[]
for m in man:
    if m['format']!='md': continue
    o=BeautifulSoup(open(mir+m['src'],'rb').read(),'lxml').select_one('div.entry')
    for x in o.select('p.post-tags'): x.decompose()
    r=BeautifulSoup(open(pub+m['url']+'index.html',encoding='utf-8').read(),'lxml').select_one('div.entry')
    for x in r.select('p.post-tags'): x.decompose()
    so,sr=sig(o),sig(r)
    if so!=sr: bad.append((m['url'],dict(so-sr),dict(sr-so)))
print(len(bad),'md posts with tag-structure diffs')
for b in bad[:30]: print(b)
open('/w/tmp/struct_diff.txt','w').write('\n'.join(b[0] for b in bad)+('\n' if bad else ''))
