import json,re,sys,os
from bs4 import BeautifulSoup
pub='/w/site/public'
man=json.load(open('/w/tmp/manifest.json'))
bad=[]
for m in man:
    p=pub+m['url']+'index.html'
    if not os.path.exists(p): bad.append((m['url'],'MISSING')); continue
    s=BeautifulSoup(open(p,encoding='utf-8').read(),'lxml')
    e=s.select_one('div.entry')
    for x in e.select('p.post-tags'): x.decompose()
    t=re.sub(r'\s+',' ',e.get_text(' ')).strip()
    if t!=m['text']:
        # find first diff
        i=next((k for k in range(min(len(t),len(m['text']))) if t[k]!=m['text'][k]),min(len(t),len(m['text'])))
        bad.append((m['url'],m['format'],m['text'][max(0,i-30):i+40],'||',t[max(0,i-30):i+40]))
print(len(man),'checked',len(bad),'differ')
for b in bad[:40]: print(b)
open('/w/tmp/text_diff.json','w').write(json.dumps(bad,ensure_ascii=False))
