---
title: 'Hackit: ogni anno SEMPRE LA STESSA STORIA'
date: '2007-09-29T00:54:00+02:00'
url: /2007/09/29/hackit-ogni-anno-sempre-la-stessa-storia/
aliases:
- /blog-static/2007/09/29/hackit-ogni-anno-sempre-la-stessa-storia/
wp_id: 884
authors:
- pallotron
avatar: pallotron.jpg
categories:
- niente-a-senso
tags: []
comments:
- id: 2510
  author: asbesto
  date: '2007-09-29T12:04:00+02:00'
  body: <p>Sempre i soliti italiani spoghetti, pizza, mandolino, arp-spoofing!</p>
  author_url: http://www.freaknet.org/~asbesto/
- id: 2511
  author: pallotron
  date: '2007-10-01T16:11:00+02:00'
  body: '<p>interessante discussione sul mirror di questo post sul mio personal blog:<br/>

    <a>http://www.vitadiunsysadmin.net/2007/09/28/hackit-ogni-anno-sempre-la-stessa-storia/langswitch_lang/en#comment-21256</a></p>'
  author_url: http://www.pallotron.net
  by_post_author: true
- id: 2512
  author: daphiel
  date: '2007-10-17T12:12:00+02:00'
  body: <p>ph34r h4×0r 31337 fuck 0Wn 0×00007a69 sux0r ping0r asd0r</p>
  author_url: http://www.bruciati.net
---
Ci voleva un mese **DI ACCUMULO E ODIO** per scrivere qualcosa su [lamentazioni.org](</>). **ORA E’ ARRIVATO IL MOMENTO.**  
Mi trovo ad [hackit](<http://www.hackmeeting.org>). Luogo di riunione annuale della scena hacker italiana. PORCODDIO. MA CHE PUGNO DI IDIOTI CHE CI SONO! AHAHAHHA

Quasi tutti usano wireless. E guardate cos dice tcpdump:

`root@quasimodo:/home/pallotron# time tcpdump -ni eth1  
tcpdump: WARNING: eth1: no IPv4 address assigned  
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode  
listening on eth1, link-type EN10MB (Ethernet), capture size 96 bytes  
3513 packets captured  
3514 packets received by filter  
0 packets dropped by kernel`

real 0m7.789s  
user 0m0.056s  
sys 0m0.008s

In 7 (diciamo quasi 8 secondi), tcpdump ha catturato 3500 pacchetti **DI STRONZATE** :

`  
22:02:28.068483 arp who-has 172.23.159.235 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.069365 arp who-has 172.23.159.236 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.070322 arp who-has 172.23.159.237 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.071310 arp who-has 172.23.159.238 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.072224 arp who-has 172.23.159.239 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.073165 arp who-has 172.23.159.240 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.074041 arp who-has 172.23.159.241 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.075384 arp who-has 172.23.159.242 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.076278 arp who-has 172.23.159.243 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.077172 arp who-has 172.23.159.244 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.078723 arp who-has 172.23.159.245 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.079603 arp who-has 172.23.159.246 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.081145 arp who-has 172.23.159.247 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.082099 arp who-has 172.23.159.248 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.083352 arp who-has 172.23.159.249 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.084223 arp who-has 172.23.159.250 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.085207 arp who-has 172.23.159.251 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.086798 arp who-has 172.23.159.252 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.087719 arp who-has 172.23.159.253 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67  
22:02:28.088604 arp who-has 172.23.159.254 (ff:ff:ff:ff:ff:ff) tell 172.23.159.67`

oppure:

`  
00:49:55.416122 arp who-has 10.2.105.111 (ff:ff:ff:ff:ff:ff) tell 10.2.105.67  
00:49:55.417317 arp who-has 10.2.105.112 (ff:ff:ff:ff:ff:ff) tell 10.2.105.67  
00:49:55.418228 arp who-has 10.2.105.113 (ff:ff:ff:ff:ff:ff) tell 10.2.105.67  
00:49:55.419159 arp who-has 10.2.105.114 (ff:ff:ff:ff:ff:ff) tell 10.2.105.67  
00:49:55.420089 arp who-has 10.2.105.115 (ff:ff:ff:ff:ff:ff) tell 10.2.105.67  
00:49:55.420965 arp who-has 10.2.105.116 (ff:ff:ff:ff:ff:ff) tell 10.2.105.67  
00:49:55.421945 arp who-has 10.2.105.117 (ff:ff:ff:ff:ff:ff) tell 10.2.105.67  
00:49:55.573193 arp who-has 10.2.105.118 (ff:ff:ff:ff:ff:ff) tell 10.2.105.67  
00:49:55.577514 arp who-has 10.2.105.119 (ff:ff:ff:ff:ff:ff) tell 10.2.105.67  
00:49:55.578437 arp who-has 10.2.105.120 (ff:ff:ff:ff:ff:ff) tell 10.2.105.67  
00:49:55.579325 arp who-has 10.2.105.121 (ff:ff:ff:ff:ff:ff) tell 10.2.105.67`

**VENGONO AD HACKIT PER FARE GLI SBORONI. I COGLIONI CI SONO ANCHE QUA. MA ANDATE A SCASSARE LA MINCHIA DA QUALCHE ALTRA PARTE, IMBECILLI. MA FATE PORTSCANNING, SPOOFING A CASA VOSTRA NELLE VOSTRE RETI DA 2 HOST. PORCODDIO.**
