---
title: perche’ DEBIAN MERDA.
date: '2005-10-08T23:22:00+02:00'
url: /2005/10/08/perche-debian-merda/
aliases:
- /blog-static/2005/10/08/perche-debian-merda/
wp_id: 153
authors:
- asbesto
avatar: asbesto.jpg
categories:
- niente-a-senso
tags: []
comments:
- id: 110
  author: eagle1
  date: '2005-10-09T23:13:00+02:00'
  body: <p>CAZZO hai ragione da vendere CAZZO</p>
  author_url: http://www.maledet.to
- id: 112
  author: lobo
  date: '2005-10-10T16:13:00+02:00'
  body: '<p>ma dai che se usassi aptitude invece di apt-get :) </p>

    <p>cmq apri google la prossima volta “debian xorg install apt-get” </p>

    <p>prrrrrrrrrrrrrrrrrrr</p>

    <p>susuca</p>

    <p>la fatica e’ dentro te<br/>

    escila</p>'
- id: 115
  author: Antonio
  date: '2005-10-11T17:09:00+02:00'
  body: <p>Cazzo cazzo cazzo figa! e ancora cazzo</p>
  author_url: http://persone.softwarelibero.org/person/baluba
- id: 158
  author: gigabytes
  date: '2005-11-14T17:41:00+02:00'
  body: '<p>A parte l’offensiva mancanza di netiquette in questo post, direi che è il classico post di uno che non ha voglia di leggere la documentazione ma solo di lamentarsi.<br/>

    Comincerei col ricordare che il tanto amato portage di gentoo è solo una versione “sorgentizzata” del sistema di pacchetti di debian, con qualche caratteristica di BSD infiltrata.<br/>

    Prima di lamentarsi bisogna *informarsi*. Per prima cosa: per quale assurdo motivo se installi fluxbox, nelle dipendenze deve esserci anche X?? Una qualsiasi applicazione X ha bisogno delle xlib per funzionare, non di tutto X, perchè potrebbe essere benissimo lanciata con una variabile d’ambiente DISPLAY particolare in modo da essere visualizzata sul server X di qualche altro host in rete. Quindi è perfettamente logico e regolare che nelle dipendenze di flux box ci siano solo le librerie di cui ha bisogno e non  tutto X.<br/>

    Secondo: per installare X basta fare `apt-get install x-window-system`. Non ci sono problemi di font, problemi di librerie, o di comandi mancanti.<br/>

    Poi si installa un vm: `apt-get install fluxbox`.<br/>

    Poi si fa partire il server e si sta zitti!<br/>

    Non serve bestemmiare per far funzionare un software. Bisogna solo usare la testa e *leggere*.</p>'
- id: 160
  author: sand
  date: '2005-11-14T20:17:00+02:00'
  body: <p>GRAZIE, VAFFANCULO, PORCO DIO</p>
  author_url: http://www.spatof.org
- id: 161
  author: CULO VERDE
  date: '2005-11-14T20:20:00+02:00'
  body: '<p>A parte la GIUSTIFICATA OFFENSIVA MANCANZA DI NETIQUETTE DI QUESTO COMMENTO E DI TUTTI STO BLOG</p>

    <p>BESTEMMIARE SERVE</p>

    <p>QUESTO BLOG = LAMENTAZIONI<br/>

    QUINDI TUTTO HA SENSO, TRANNE IL TUO COMMENTO DI “NETCQUCQUETTE”</p>'
  author_url: http://SMEGMA.com
- id: 162
  author: evernine
  date: '2005-11-14T20:21:00+02:00'
  body: <p>Infatti ANCHE GENTOO E’ MERDA!!! AHAHAHHAHAHAAH! Una sola e’ la via! SLACKWARE! IL RESTO E’ SOLO MERDA! merdoo, merdian, fetora TUTTA MERDA! e comunque DIO E’ PORCO!</p>
- id: 177
  author: bah
  date: '2005-11-19T02:26:00+02:00'
  body: '<p>“Comincerei col ricordare che il tanto amato portage di gentoo è solo una versione “sorgentizzata” del sistema di pacchetti di debian, con qualche caratteristica di BSD infiltrata.”</p>

    <p>Questo è incorretto. Portage è ispirato ai ports di FreeBSD, ben oltre “qualche caratteristica infiltrata”. Non mi pare ci sia una parentela con apt, a parte ovviamente che hanno lo stesso scopo, con approcci diversi.</p>

    <p>Maggiori informazioni in questo articolo del “padre” di gentoo: <a href="http://www-128.ibm.com/developerworks/library/l-dist1.html" rel="nofollow">http://www-128.ibm.com/developerworks/library/l-dist1.html</a></p>'
- id: 268
  author: asbesto
  date: '2006-01-12T20:35:00+02:00'
  body: '<p>A parte l’offensiva mancanza di AOH MA CHI CAZZO SEI MA ANVEDI D’ANNATTENE AFFANCULO, </p>

    <p>debian e’ UNA MERDA perche’ sto cazzo di sistema di pacchetti di MERDA e’ fatto a COPPOLA DELLA MINCHIA</p>

    <p>apt-get remove gpm</p>

    <p>e lui TI RIMUOVE TUTTO X-Windows</p>

    <p>ma siamo scemi?!?!? DEBIAN MERDA, non c’e’ altro da aggiungere</p>

    <p>ma ANVEDI QUESTO, AOH</p>'
  author_url: http://www.freaknet.org/~asbesto/
  by_post_author: true
---
Semplice.

installare X. 

su gentoo: **emerge xorg**

su debian NON LO SO, quindi penso, **beh, debian e’ FAMOSA per le DIPENDENZE, quindi mi sembra logico che se installero’ un window manager, che ovviamente gira sotto X, mi installera’ tutto X, grazie ALLE DIPENDENZE**

seee, COL CAZZO! **COL CAZZO**

apt-get install fluxbox, **installa un pugno di librerie MAI VISTE ma NIENTE X**

`  
X: command not found  
startx: command not found  
`

MAH, CHISSA’ PERCHE’

apt-get install x11-base (ora non ricordo esattamente)

tira su’ altre 28 **stronzate mai viste** , ed il risultato e’

`  
X: command not found  
startx: command not found  
`

**MA VAFFANCULO, PORCO DDIO MA CHE STRACAZZO MI RAPPRESENTI**

AH – serve apt-get install xserver-salcazzo-base

**ma allora A CHE CAZZO MI SERVE CHE MI SI SPAPPOLINO I COGLIONI CON LE FAMOSISSIME DIPENDENZE DEBIAN, PORCO DIO**

apt-get install xsalcazzo-base

ora c’e’ X  
ora c’e’ startx

mi parte il requester, MENO MALE, **posso CONFIGURARLO DA QUI, ah ha visto L’LCD, GRAZIE**

crea xfree86.cfg, allora lancio startx:

`  
Fatal server error:  
could not open default font 'fixed':  
(altre palle)  
`

**AH, LA DEBIAN, AH, LE DIPENDENZE, MA SI, TI SBRIGHI SUBITO AD INSTALLARE**

porco ddio, PORCO CRISTO DIO, E’ DA STO POMERIGGIO CHE SBATTO PER AVERE X

apt-get install xfonts-base

**ma perche’ CAZZO NON LO FAI DA SOLO**

ribadisco:

**emerge xorg-x11**  
**FINE**

**GENTOO RULEZ, DEBIAN MERDA**

e non ammetto repliche!
