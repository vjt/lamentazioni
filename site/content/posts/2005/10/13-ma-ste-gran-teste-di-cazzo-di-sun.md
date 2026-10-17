---
title: MA STE GRAN TESTE DI CAZZO DI SUN
date: '2005-10-13T12:01:00+02:00'
url: /2005/10/13/ma-ste-gran-teste-di-cazzo-di-sun/
aliases:
- /blog-static/2005/10/13/ma-ste-gran-teste-di-cazzo-di-sun/
wp_id: 161
authors:
- nightolo
avatar: nightolo.jpg
categories:
- niente-a-senso
tags: []
comments:
- id: 119
  author: sand
  date: '2005-10-13T12:54:00+02:00'
  body: '<p>Ci ho bestemmiato anche io con quel COSO!<br/>

    Ora come ora non ho gli appunti sotto il naso (si, ho preso APPUNTI) ma mi sembra che c’era un servizio, forse proprio ssh, che non voleva partire perche’ dipendeva da qualcosa che non partiva. Su un solaris10 fresco di installazione…. MAH!<br/>

    Certo, a capirlo uno lo capisce, pero’ PORCO DIO davvero e’ un meccanismo OSTILE.</p>'
  author_url: http://www.spatof.org
- id: 120
  author: guly
  date: '2005-10-13T15:14:00+02:00'
  body: '<p>OSTILI AD ORE 9, OSTILI AD ORE 9<br/>

    PARLAMI FROST</p>'
- id: 122
  author: ciao
  date: '2005-10-16T14:15:00+02:00'
  body: <p>Figa.</p>
- id: 123
  author: pallotron
  date: '2005-10-19T10:57:00+02:00'
  body: <p>E’ che siccome loro sono i NONNI UNIX, si sono stufati delle cose semplici! ma si dai! STRAVOGLIAMO TUTTO AGGIUNGENDO QUALCHE ALTRO COMANDO ASTRUSO!</p>
  author_url: http://www.pallotron.freaknet.org
---
Ci sono delle cose su UNIX che funzionano BENE da trentatre anni (gli anni di GESU’).  
Un esempio? gli script di init

Cosa fa Sun? Decide di cambiare la gestione degli script di init in Solaris 10 per avere piu’ cose da vendere, la self-healing predictive, LA GRAN MINCHIAZZA DI GESU’.

Mi mettono svcadm

Quello che una volta si faceva con:  
/etc/init.d/sshd stop  
Adesso si fa con  
svcadm disable -t network/ssh:default

E STE GRAN TESTE DI MINCHIA ovviamente non prevedono il completion, quindi io che cazzo ne so che ssh corrisponde a network SBARRETTA ssh DUEPUNTI default???  
Semplice, devo greppare ssh in svcs -a

svcs -a | grep ssh  
online Oct_05 svc:/network/ssh:default

E STO GRAN CAZZO aggiungere, poi devo prendere il mio fottuto mouse e fare copia e incolla, quello che priam facevo in un comando di  
22 caratteri (spazi compresi) adesso lo devo fare con due comandi di MILIONI di caratteri CADAUNO sprecando fottuti cicli di processori.

MA del resto come cazzo puoi pretendere un ragionamento sui cicli di processore da chi ha inventato Java?? L’ottimizzazione del cardinale SUCATO (cit).

Il discorso va bene, e’ una merda, lo studio e MI ADATTO

Se ci sono dei problemi PERO’ non funziona un cazzo, se lo stoppo e PER I CAZZI SUOI decide che non gli piaccio fa questo:

online* Oct_05 svc:/network/ssh:default

Mi aggiunge un fottuto asterisco di cui ne’ google ne’ loro hanno idea  
Devo andare a studiare che cazzo e’ quell’asterisco.

MA SEI COGLIONE? USA IL KILL -9, che cazzo me ne fotte dell’asterisco.

Comunque

alla fine  
dopo venti minuti di bestemmie a scapito di una decina di utenti connessi che LAVORAVANO (a differenza di chi ha scritto svcadm)

ho riavviato la macchina
