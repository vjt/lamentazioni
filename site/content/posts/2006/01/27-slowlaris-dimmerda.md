---
title: Slowlaris dimmerda…
date: '2006-01-27T19:13:00+02:00'
url: /2006/01/27/slowlaris-dimmerda/
aliases:
- /blog-static/2006/01/27/slowlaris-dimmerda/
wp_id: 325
authors:
- nightolo
avatar: nightolo.jpg
categories:
- niente-a-senso
tags: []
comments:
- id: 334
  author: io
  date: '2006-01-27T22:21:00+02:00'
  body: '<p>apt-get? mai sentito parlare di pkg-get?<br/>

    pkg-get -i dbg<br/>

    e vai con dio!<br/>

    la soluzione ai tuoi problemi da utonto solaris la trovi qui: <a href="http://www.blastwave.org" rel="nofollow">http://www.blastwave.org</a></p>'
- id: 335
  author: nightolo
  date: '2006-01-27T23:43:00+02:00'
  body: <p>non so se si era colto che il problema non riguardava l’installazione del pacchetto…</p>
  by_post_author: true
- id: 336
  author: io
  date: '2006-01-28T00:26:00+02:00'
  body: '<p>mi riferivo al commento: “(pfui… apt-get no eh???)”</p>'
- id: 339
  author: rdfm
  date: '2006-01-28T21:24:00+02:00'
  body: '<p>grazie per la dritta, mai sentito parlare di pkg-get, fino a 3 mesi fa ero un felice non-utente di solaris, e pure mo tendo a evitare viste ste magagne… :)</p>

    <p>cmq, la documentazione che avevo trovato finora parlava al 99% di sunfreeware senza menzionare pkg-get… puntatori a documentazione utile (ossia meno prolissa di quella sun) sono sempre graditi…</p>'
  author_url: http://www.rdfm.org/ammuzzu/
- id: 340
  author: io
  date: '2006-01-28T21:53:00+02:00'
  body: '<p>nella documentazione sun trovi solo sunfreeware perchè pkg-get non è un tool sun ma di una community open, blastwave, che cmq riceve il supporto sun.<br/>

    documentazione su come come installare ed usare pkg-get: <a href="http://www.blastwave.org/howto.html" rel="nofollow">http://www.blastwave.org/howto.html</a></p>'
---
**Realizzato da[rdfm](<http://www.rdfm.org/ammuzzu>)**

-bash-3.00$ gunzip gcc-3.4-* && pkgadd -d gcc-* && gzip gcc-* && mv gcc-* done/  
(pfui… apt-get no eh???)  
-bash-3.00$ gunzip gdb-6.0-* && pkgadd -d gdb-6* && gzip gdb-6.0-* && mv gdb-6.* done/  
(non vi tedio con la sfilza di installazioni lunga quanto il cazzo in culo della madonna….)

-bash-3.00$ scons  
[...]  
In file included from /usr/include/sys/wait.h:24,  
from exec.c:26:  
/usr/include/sys/siginfo.h:259: error: parse error before “ctid_t”  
/usr/include/sys/siginfo.h:292: error: parse error before ‘}’ token

ma porco crishto e vishnu del santo graal di sborra di dio…

google… google… [ah!](<http://archives.postgresql.org/pgsql-bugs/2004-12/msg00192.php>)

cd /usr/local/libexec/gcc/sparc-sun-solaris2.9/3.4.2/install-tools/  
./mkheaders

-bash-3.00$ scons install  
scons: done building targets.

seeee.. te credevi che il mondo era facile…

-bash-3.00$ kc_parse  
[....]  
create_disk(”/dev/sda1″, 0×21be0, 0, 3, 0)  
No such file or directory  
Errore di segmento (core dumped)

UE SPAGHETTI E MANDOLINO QUALE MERDA DI BUDDHA DEL CAZZO TI HA DETTO CHE VOGLIO I CAZZO DI MESSAGGI IN ITALIANO?????

-bash-3.00$ gdb kc_parse  
GNU gdb 6.0  
Copyright 2003 Free Software Foundation, Inc.  
GDB is free software, covered by the GNU General Public License, and you are  
welcome to change it and/or distribute copies of it under certain conditions.  
Type “show copying” to see the conditions.  
There is absolutely no warranty for GDB. Type “show warranty” for details.  
This GDB was configured as “sparc-sun-solaris2.9″…Errore di Bus (core dumped)

![](/ext/dcf3366529-carnivore.jpg)
