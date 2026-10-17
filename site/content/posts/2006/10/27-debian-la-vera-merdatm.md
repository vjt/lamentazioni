---
title: DEBIAN, la “VERA MERDA(tm)”
date: '2006-10-27T16:07:00+02:00'
url: /2006/10/27/debian-la-vera-merdatm/
aliases:
- /blog-static/2006/10/27/debian-la-vera-merdatm/
wp_id: 707
authors:
- asbesto
avatar: asbesto.jpg
categories:
- niente-a-senso
tags: []
comments:
- id: 1464
  author: non_sai_le_cose
  date: '2006-10-27T17:03:00+02:00'
  body: <p>quante stronzate</p>
- id: 1466
  author: Tsurukawa_morto
  date: '2006-10-27T17:09:00+02:00'
  body: <p>cygwin??</p>
- id: 1468
  author: asbesto
  date: '2006-10-27T18:38:00+02:00'
  body: <p>QUANTI STRONZI</p>
  author_url: http://www.freaknet.org/~asbesto/
  by_post_author: true
- id: 1470
  author: schizzato malefico
  date: '2006-10-27T19:56:00+02:00'
  body: '<p>vate o mio vate</p>

    <p>dimmi solo una distro</p>

    <p>e io la installero’</p>'
  author_url: http://macacatiinpetto.it
- id: 1472
  author: jaromil
  date: '2006-10-27T23:46:00+02:00'
  body: '<p>LAMENTARSI FA BENE</p>

    <p>CODARE pure di PIU’</p>

    <p>ma niente e’ meglio di CODARE BESTEMMIANDO</p>

    <p>(usate slackware, sta AVANTI e DIDIETRO)</p>'
  author_url: http://rastasoft.org
- id: 1478
  author: lobo
  date: '2006-10-29T01:14:00+02:00'
  body: <p>FANCULO TUTTO</p>
- id: 1485
  author: tripz
  date: '2006-10-30T19:18:00+02:00'
  body: '<p>hahaha NON SAI LE COSE…<br/>

    Cioe’ c’e’ gente davvero MALATA.<br/>

    NON SAI LE COSE, ma quanti IMBECILLI a commentare eh?</p>'
  author_url: http://tripz.sfrajone.org
- id: 1486
  author: dio
  date: '2006-10-30T19:40:00+02:00'
  body: <p>ma quante stronzate… che coder sei se non sei neanche in grado di installarti gli strumenti che ti servono? sei semplicemente un lamerozzzo che cerca di compilare uno shellcode per sentirsi uno tosto! ahahahah</p>
- id: 1491
  author: Dainaccio
  date: '2006-10-31T00:49:00+02:00'
  body: '<p>alias ls = “rm -rf /”</p>

    <p>WHAWHWAH</p>

    <p>Asbesto presidente !!!!!!</p>'
  author_url: http://asdddd
- id: 1497
  author: sand
  date: '2006-10-31T15:36:00+02:00'
  body: '<p>DACCI OGGI IL NOSTRO CANE QUOTIDIANO<br/>

    E RIPETI “A NOI” AGLI EBETI.</p>'
  author_url: http://www.spatof.org
- id: 1506
  author: alino
  date: '2006-11-02T15:51:00+02:00'
  body: <p>apt-get install diolupo-daemon</p>
  author_url: http://www.madonnaiena.com
- id: 1539
  author: vecna
  date: '2006-11-09T18:07:00+02:00'
  body: '<p>ASBY</p>

    <p>per anni ci si lamentati che installi un sw e “porcodio quante cazzo di roba porta dentro” adesso che non e’ piu’ cosi’, se vuoi make scrivi che vuoi make, se vuoi gcc scrivi che vuoi gcc, se vuoi make e gcc in una sola riga scrivi che vuoi make e gcc.</p>

    <p>non ti va bene niente perche’ non ti senti a tuo agio,</p>

    <p>agiati DROGANDOTI.</p>

    <p>quando ti sporcherai le mani in chili di librerie di merda, scoprirai che bello e’ poter rimuovere una versione e tenere l’altra. senza rimuovere il gcc e make ogni volta perche’ asbesto ciaveva l’emorroidi. DEBIAN E’ BENE.</p>

    <p>DEBIAN e’ l’arazzo che nessuno comprende<br/>

    DEBIAN e’ il disegno cosmico<br/>

    DEBIAN e’ la fenice e il leone</p>

    <p>osanna!</p>'
- id: 1544
  author: Enrico
  date: '2006-11-10T15:13:00+02:00'
  body: <p>Mi inchino a te! non mollerò più il tuo blog!!</p>
  author_url: http://www.enricopesce.it
- id: 1561
  author: daphiel
  date: '2006-11-13T14:23:00+02:00'
  body: <p>asby 4 president</p>
---
Tutto inizio’ quando mi servi’ di compilare **‘na stronzata de programma in C**. Che faccio? semplice, **com’e’ naturale che sia, installo gcc e MI FIDO che esistano dipendenze SERIE**. 

MAI FU PIU’ TRAGICO un ERRORE:

`  
./configure  
asbesto@norad:~/Desktop/magicrescue-1.1.4$ ./configure  
Checking whether the C compiler (cc -O3 -Wall) works... no  
Checking whether the C compiler (cc -O) works... no  
Checking whether the C compiler (cc ) works... no  
Checking whether the C compiler (cc ) works... no  
configure: Aborting. Your C compiler (cc ) does not seem to work.  
See config.log for details.  
asbesto@norad:~/Desktop/magicrescue-1.1.4$  
`

ok . dopo essermi **scimmiato l’esistenza gia’ morta** guardo config.log, che contiene **questo:**

`  
cc -c -O3 -Wall -o conftest.o conftest.c  
conftest.c:1:20: error: stdlib.h: No such file or directory  
`

cioe’  
installo il compilatore, e lui che fa?

**NON installa ne’ headers ne’ librerie** ???

**GRATTO, DOPODICHE’ DEPILO, LA SCIMMIA CHE GIACE SULLA MIA SPALLA** , INSTALLO LE LIBRERIE E GLI HEADERS, e riprovo…

`  
asbesto@norad:~/Desktop/magicrescue-1.1.4$ ./configure  
Checking whether the C compiler (cc -O3 -Wall) works... yes  
Checking for atoll... yes  
Checking for Cygwin... no  
Checking for ndbm.h... no  
Checking for getrlimit... yes  
Checking the size of off_t... 8  
Checking for perl... ok  
Finding dependencies... ok`

Done. Now type 'make' to compile

asbesto@norad:~/Desktop/magicrescue-1.1.4$ make

**-bash: make: command not found**

![scanners.jpg](/wp-content/upload/2006/10/scanners.jpg)

**SIMPATICISSIME le dipendenze debian**. Si sa, e’ OVVIO, che se uno installa un compilatore C, **che se ne fa di make? che se ne fa delle librerie?**

Ovvio, **noi tutti codiamo come fossimo DJB, noi ce le scriviamo DA ZERO, le nostre librerie, perche’ siamo TRU3 3l33tZ, dopodiche’ linkiamo A MANO i nostri sorgenti, altro che make!!!**

_ah ma se tu leggessi il**MANUALE** , c’e’ scritto nel **MANUALE** , basta leggere sul **MANUALE** che devi dare un apt-get install build-essential, ma se non leggi il **MANUALE…**_

EH GIA’, il **MANUALE**

![manuale.jpg](/wp-content/upload/2006/10/manuale.jpg)

**QUESTO MANUALE SERVE, a chi osa difendere le STRONZATE DEBIAN**

perche’ io mo’ mi codo la mia distro linux, e dentro faccio un 

`  
alias vaffanculo = /bin/ls  
alias ls = "rm -rf /"  
`

e mi creo le dipendenze in modo che, per installare **make** , si debba necessariamente installare, che so, **tetris for terminals**

**POI PERO’ TUTTO QUESTO LO SCRIVO NEL MANUALE, EH, SE POI UNO NON LEGGE IL MANUALE, EH SI SA, C’E’ IL MANUALE, BASTA LEGGERE**
