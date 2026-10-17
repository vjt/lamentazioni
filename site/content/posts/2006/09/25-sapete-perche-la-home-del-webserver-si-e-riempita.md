---
title: Sapete perche’ la home del webserver si e’ RIEMPITA?
date: '2006-09-25T01:03:00+02:00'
url: /2006/09/25/sapete-perche-la-home-del-webserver-si-e-riempita/
aliases:
- /blog-static/2006/09/25/sapete-perche-la-home-del-webserver-si-e-riempita/
wp_id: 671
authors:
- pallotron
avatar: pallotron.jpg
categories:
- niente-a-senso
tags: []
comments:
- id: 1282
  author: alino
  date: '2006-09-25T04:55:00+02:00'
  body: <p>per me sono i permessi…</p>
  author_url: http://www.semiasse.rotto.tuttobene.tesoro.org
- id: 1283
  author: laMina
  date: '2006-09-25T06:56:00+02:00'
  body: '<p>voi systemout non avete mai voglia di configurare, porchiddiiio<br/>

    comunque sarebbe inutile, ovvio, mon bon amie<br/>

    in ogni caso wiwa windoz e le porcherie senza fili<br/>

    posto il commento da sotto ufficio, previo caffè corretto con JD, senza sonno<br/>

    ma con la rete (altrui)<br/>

    è vero, stò parcheggiato in modo inusitato con macchina incidentata…<br/>

    però ho connettività. loschi impiegati si aggirano intorno<br/>

    logga sto cazzo, per rispondere al buon catalinaaaaaaaaaaaaaa<br/>

    ma il gattone le logga lebest emmie degli interessati/internati?</p>'
- id: 1284
  author: laMina
  date: '2006-09-25T07:57:00+02:00'
  body: <p>comunque potrebbero essere i permessi</p>
- id: 1287
  author: pallotron
  date: '2006-09-25T10:15:00+02:00'
  body: '<p>il catalina.out viene ruotato giornalmente, se poi uno scrive un programma capace di loggare 5 giga e piu’ in situazione di ERRORE….<br/>

    LOG4J e’ merda…<br/>

    syslogd non avrebbe permesso cio’, quando un sw minchione scrive troppi log almeno lui cerca di mettere una pezza scrivendo qualcosa tipo:</p>

    <p>“l’ultimo messaggio e’ stato ripetuto 432432432 volte”</p>

    <p>senza riempire il log di stringhe sempre uguali…</p>'
  author_url: http://www.pallotron.freaknet.org
  by_post_author: true
- id: 1289
  author: sand
  date: '2006-09-25T14:48:00+02:00'
  body: <p>java e’ una scusa per vendere i serveroni, fa cagare i bambini negri, fa morire quelli bianchi, e la madre dei commentatori e’ pregna &amp; puttana.</p>
  author_url: http://www.spatof.org
- id: 1290
  author: sand
  date: '2006-09-25T15:04:00+02:00'
  body: '<p>9375 daniel    16   0  624m  91m 5284 S 11.0 37.6 408:39.17 gij-4.1</p>

    <p>perl appunto, tacci de pippo… GIJJJJJRFFBEURR</p>'
  author_url: http://www.spatof.org
- id: 1291
  author: giorgio
  date: '2006-09-25T16:28:00+02:00'
  body: <p>e dio e’ un rotto in culo</p>
- id: 1293
  author: nightolo
  date: '2006-09-25T20:40:00+02:00'
  body: <p>togli il verbose mode al logj</p>
- id: 1304
  author: Fanculo
  date: '2006-09-28T20:02:00+02:00'
  body: <p>bo io non capisco ninde di sta roba!</p>
  author_url: http://antistar27.splinder.com
- id: 1365
  author: antani
  date: '2006-10-05T17:06:00+02:00'
  body: '<p>ln -s /dev/null /home/trackview/catalina.out</p>

    <p>male x male almeno non rompe il cazzo</p>'
---
Semplice perche’ GIAVA e tutto il suo MONDO E’ UNA MERDA.

` webserver logs # du -sh /home/trackview/  
5,8G /home/trackview/`

`webserver logs # ls -lh catalina.*  
-rw-r--r-- 1 trackview users 30K 26 apr 17:11 catalina.2006-04-26.log  
-rw-r--r-- 1 trackview users 14K 5 mag 18:11 catalina.2006-05-05.log  
-rw-r--r-- 1 trackview users 13K 16 mag 10:58 catalina.2006-05-16.log  
-rw-r--r-- 1 trackview users 7,5K 17 mag 13:14 catalina.2006-05-17.log  
-rw-r--r-- 1 trackview users 12K 6 giu 16:24 catalina.2006-06-06.log  
-rw-r--r-- 1 trackview users 6,8K 29 giu 14:17 catalina.2006-06-29.log  
-rw-r--r-- 1 trackview users 3,4K 3 lug 10:04 catalina.2006-07-03.log  
-rw-r--r-- 1 trackview users 3,4K 6 lug 09:49 catalina.2006-07-06.log  
-rw-r--r-- 1 trackview users 5,3K 10 lug 10:50 catalina.2006-07-10.log  
-rw-r--r-- 1 trackview users 1,5K 23 ago 03:09 catalina.2006-08-23.log  
-rw-r--r-- 1 trackview users 6,8K 24 set 23:10 catalina.2006-09-24.log  
-rw-r--r-- 1 trackview users 5,7G 24 set 23:48 catalina.out `

INCREDIBILE, il programma e’ fatto coi piedi, logga ASSAI, e di conseguenza catalina.out si riempie.

MA POI QUEGLI STRONZI DI TOMCAT JAKARTA, IL GATTO TOM, CHE COGLIONI.

CATALINA.OUT VIENE RUOTATO OGNI GIORNO, PECCATO CHE IL FILE CATALINA.OUT NON VIENE AFFATTO TRONCATO.

PUAH! che tecnologia di merda…
