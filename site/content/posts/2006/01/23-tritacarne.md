---
title: TRITACARNE
date: '2006-01-23T15:21:00+02:00'
url: /2006/01/23/tritacarne/
aliases:
- /blog-static/2006/01/23/tritacarne/
wp_id: 320
authors:
- tripz
avatar: tripz.jpg
categories:
- niente-a-senso
tags: []
comments:
- id: 310
  author: nightolo
  date: '2006-01-23T20:09:00+02:00'
  body: '<p>strdup: too much arguments</p>'
- id: 312
  author: tripz
  date: '2006-01-24T11:08:00+02:00'
  body: '<p>oops, hai ragione ;)</p>

    <p>ero sicuro che c’era un errore, correggo!</p>'
  author_url: http://tripz.sfrajone.org
---
void chiedi_a_collega(struct t_vittima *vittima, int domanda) {  
vittima->nome = strdup(”tripz”);  
vittima->domanda = domanda;

chiedi(vittima);  
}

int main(int argc, char **argv) {  
struct t_vittima povero_me;

while(1) {  
chiedi_a_collega(&povero_me, T_LINUX | T_MYSQL | T_PHP | T_APACHE | T_IPTABLES | T_JSP | T_HTML | T_RANDOM);  
sleep(1);  
}

return 0;  
}

![PIATTOLA](/ext/824da41d16-zecca.jpg)
