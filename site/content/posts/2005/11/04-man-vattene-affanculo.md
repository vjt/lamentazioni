---
title: man vattene affanculo
date: '2005-11-04T15:21:00+02:00'
url: /2005/11/04/man-vattene-affanculo/
aliases:
- /blog-static/2005/11/04/man-vattene-affanculo/
wp_id: 194
authors:
- sand
avatar: sand.jpg
categories:
- niente-a-senso
tags: []
---
C’e’ qualcosa che mi **sfugge**.  
Su Linux (gentoo ahime’), perldoc NON mi escapa correttamente i caratteri, facendomi vedere fuffa tipo questa **^[[4mgrep^[[24m(1)** al posto dei colori, e non riesco a capire perche’, soprattutto quando “ _man comando_ ” **NON** presenta questo problema. Su OpenBSD tutto questo non succede, mumble e poi mumble.  
Indago (che e’ un colore mal pronun**z** iato).

openbsd:

> 31298 p2 T 0:00.01 man ls  
>  3503 p2 T 0:00.00 sh -c sh  
>  14683 p2 T 0:00.02 most /usr/share/man/cat1/ls.0

linux:

> |-zsh—man—sh—sh-+-most  
>  | `-nroff—groff—grotty

[Most](<http://www.jedsoft.org/most/>) e’ il pager che uso, scoperto di recente (provatelo), e fin qui ci siamo.  
Su openbsd c’e’ un unico e ovvio processo: **$PAGER /path/alla/man/page**  
Su linux ci sono: NROFF, TROFF, GROFF, GROTTY, SBORRY, CLITY, TIGROTTO, DJ GRUFF, PEPPE ER PANZELLA e $PAGER.  
Datemi un motivo. Avanti, forza, DATEMI UNA MOTIVAZIONE!  
I locales ? I charset? Il tristo mietitore ?

Fatto sta che su open vedo tutte le pagine man/pod **perfettamente** , e su linux **no** , non so COSA configurare, la documentazione NON esiste, ergo DIVEMPTO PATZO.
