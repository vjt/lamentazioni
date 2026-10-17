import json,re,os,collections
from urllib.parse import unquote
from bs4 import BeautifulSoup
pub='/w/site/public'; mir='/w/mirror/lamentazioni.org/'
man=json.load(open('/w/tmp/manifest.json'))
def exists(p):
    p=unquote(p.split('#')[0].split('?')[0])
    f=pub+p
    return os.path.isfile(f) or os.path.isfile(f.rstrip('/')+'/index.html')
miss=collections.defaultdict(list); imgs_ok=0; cmt_bad=[]; posts_with_img=[]
for m in man:
    html=open(pub+m['url']+'index.html',encoding='utf-8').read()
    s=BeautifulSoup(html,'lxml')
    for el in s.select('#content [src], #content [href]'):
        v=el.get('src') or el.get('href')
        if v.startswith('/') and not v.startswith('//'):
            if exists(v):
                if el.name=='img': imgs_ok+=1
            else: miss[v].append(m['url'])
    e=s.select_one('div.entry')
    if e.select('img[src^="/wp-content/upload"]'): posts_with_img.append(m['url'])
    src=mir+m['src']
    if not os.path.exists(src): src=mir+'2007/05/17/'+os.fsdecode(b'l\xe2%80%99allegro-e-fantasioso-mondo-del-web-2')+'/index.html'
    o=BeautifulSoup(open(src,'rb').read(),'lxml')
    if len(o.select('ol.commentlist > li'))!=len(s.select('ol.commentlist > li')): cmt_bad.append(m['url'])
print('local imgs resolved',imgs_ok,'| posts w/ local upload imgs',len(posts_with_img))
print('missing local targets',len(miss))
for k,v in sorted(miss.items())[:60]: print(' ',k,len(v),v[0])
print('comment count mismatches',len(cmt_bad),cmt_bad[:5])
json.dump(posts_with_img,open('/w/tmp/posts_with_img.json','w'))
