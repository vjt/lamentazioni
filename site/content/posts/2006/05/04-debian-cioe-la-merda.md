---
title: DEBIAN, cioe’ LA MERDA.
date: '2006-05-04T16:17:00+02:00'
url: /2006/05/04/debian-cioe-la-merda/
aliases:
- /blog-static/2006/05/04/debian-cioe-la-merda/
wp_id: 452
authors:
- asbesto
avatar: asbesto.jpg
categories:
- niente-a-senso
tags: []
---
Devo re-encodare un video in formato RealMedia in un piu’ comune e visibile .avi

Provo a farlo con **debian di merda.** Mi informo della sintassi tramite google, e siccome **ho gia’ installato mplayer** , allegro e baldanzoso scrivo 

`  
asbesto@norad:~/$mencoder -ovc lavc sterco.rm -oac mp3lame -o feci.avi  
`

Ma dovevo immaginarlo: **niente e’ ovvio, in merdebian, nemmeno le piu’ banali stronzate.**

`  
-bash: mencoder: command not found  
`

![hitler2.jpg](/wp-content/upload/2006/05/hitler2.jpg)

**AGGHIACCIANTE.** Laddove **TUTTE le distribuzioni UNIX DEL MONDO** , alla richiesta di installare mplayer, **installano GIUSTAMENTE tutta la suite di programmi, cioe’ anche mencoder** , sulla MERDOSA DEBIAN DI MERDA questo **non accade** , costringendomi a cercare ed installare **a parte** il pacchetto mencoder. **ma andate A FAN CULO, A “A FARE IN CULO”, ANDATECI**

installo INUTILMENTE sta **MERDATA DI MENCODER “A PARTE”** , e rilancio il comando.

`  
asbesto@norad:~/$ mencoder -ovc lavc sterco.rm -oac mp3lame -o feci.avi  
(...)  
Segmentation faultf ( 0%) 0.00fps Trem: 0min 0mb A-V:0.000 [6:0]  
asbesto@norad:~/$  
`

![tom5.jpg](/wp-content/upload/2006/05/tom5.jpg)

Ed un **BALLO DI FINOCCHI mi CRESCE NEL CERVELLO** , mentre mencoder crasha miseramente. Per **UN’ORA INTERA COMBATTO CON STRACE, GDB, E CERCO SU GOOGLE UN’INESISTENTE RISPOSTA.** Poi copio il filmato mp3 su gemini con gentoo, dove mesi fa ho semplicemente scritto **emerge mplayer** :

`  
asbesto@gemini:~/$ mencoder -ovc lavc sterco.rm -oac mp3lame -o feci.avi  
(...)  
Video stream: 146,321 kbit/s (18290 bps) size: 12585472 bytes 688,100 secs 6609 frames  
Audio stream: 127,956 kbit/s (15994 bps) size: 11013948 bytes 688,608 secs  
asbesto@gemini ~ $  
`

![debian merda](/wp-content/upload/2006/05/merda.jpg)

La conclusione e’ lasciata in esercizio al lettore.
