---
title: INFAME dmalloc
date: '2006-01-20T17:14:00+02:00'
url: /2006/01/20/infame-dmalloc/
aliases:
- /blog-static/2006/01/20/infame-dmalloc/
wp_id: 316
authors:
- nightolo
avatar: nightolo.jpg
categories:
- niente-a-senso
tags: []
comments:
- id: 297
  author: ioggstream
  date: '2006-01-20T17:24:00+02:00'
  body: '<p>bravo imbecille, così ti impari a non progettare bene il software.<br/>

    se avessi usato java+eclipse non avresti avuto questi problemi!</p>

    <p>oppure hai ssh aperto e qualcuno di sta’ cambiando il codice sotto il culo.</p>'
- id: 298
  author: pallotron
  date: '2006-01-20T21:55:00+02:00'
  body: <p>eclipse + java merda, quelli si che occupano l’heap ahahahaha ;P</p>
  author_url: http://www.pallotron.freaknet.org
- id: 299
  author: sand
  date: '2006-01-21T05:44:00+02:00'
  body: '<p>QUANDO ERO PICCOLO SUCCEDEVA ANCHE A ME<br/>

    poi ho deciso di colpirlo col pirlo…</p>'
  author_url: http://www.spatof.org
---
Oggi e’ venerdi’  
il giorno in cui dio CREPO’ CROCIFISSO

per cui oggi decide di manifestare la sua porcita’

Decido di capire perche’ un programma scritto da me occupa 8K nell’heap ad ogni chiamata di una funzione

allora stamattina penso  
OH PORCO DIO FACCIO IL MEMORIFENSING con dmalloc, ora lo installo

scarico dmalloc  
Provo a scaricarlo su sourceforge e NON FUNZIONA il download  
e gia’ questo dovrebbe DISSUADERMI

Forse qualcuno non vuole che lo usi.

Decido di usare il repository locale, scarico, installo

Compilo  
gcc si incazza perche’ se include dmalloc.h (come scritto nel fottuto manuale) dmalloc decide di ridefinire.

Dopo cinque ore e un lauto pranzo capisco che in fondo basta linCare la libreria statica e via  
dmalloc C’E’

faccio partire il programma  
BAM  
segfault

MA PORCO IDDIO SEGFAULT DI COSA???

guardo il coredumpo su gdb, il segfault sta su ldap_next_entry()

DIO PORCACCIO, ci sta un segfault su una libreria il cui codice e’ proprietario (no non e’ openldap)

Provo a commentare ldap_next_entry

Mi da errore su ldap_msgfree (che chiama free, guardacaso ridefinita dal porco dmalloc).

PORCO IDDIO  
tutto spaccato

sbatto le mani sul tavolo, dico “vaffanculo dmalloc” e disinstallo e elimino dall’hard disk ogni traccia di dmalloc.

Decido di cercare il mio cazzo di fottuto memory leak da solo, con while true; pmap -x pid; sleep 5; done

starto il programma  
stamattina occupava 8K ogni chiamata INSOZZANDO l’heap  
ora non occupa un cazzo  
MA SEI PAZZO? non ho cambiato niente

o perlomeno, ho cambiato, ma non ricordo

DIO BASTARDO NON PUO’ ESERE

![](http://images.google.it/images?q=tbn:Va2JVVpD64JuOM:www.angelfire.com/blog/vampireslacker/images/desperation.jpg/)
