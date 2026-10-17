---
title: TRUST, una marca DI CUI FIDARSI!
date: '2005-11-23T11:48:00+02:00'
url: /2005/11/23/trust-una-marca-di-cui-fidarsi/
aliases:
- /blog-static/2005/11/23/trust-una-marca-di-cui-fidarsi/
wp_id: 233
authors:
- tripz
avatar: tripz.jpg
categories:
- niente-a-senso
tags: []
comments:
- id: 186
  author: sand
  date: '2005-11-23T13:03:00+02:00'
  body: '<p>e’ polpa di linucs! +qualita’ -quantita’</p>

    <p>QUESTI NERD DI MERDA NON LEGGEVANO LE FAVOLE DA BANBINI</p>'
  author_url: http://www.spatof.org
- id: 191
  author: asbesto
  date: '2005-11-23T16:04:00+02:00'
  body: '<p>no,</p>

    <p>hai beccato una delle tante pcmcia del cazzo che usano gli<br/>

    8139too, che sono supportati come il PISCIO DELLA MADONNA PRENA</p>

    <p>ste schede pcmcia *NON FUNZIONANO*, il supporto linux e’ PENOSO, fermo a quanto pare ad ANNI FA, e fanno tipo 10 k/s</p>

    <p>ci scattio’ martin molti mesi fa su sta merda di pcmcia<br/>

    8139too, mettendo mani NEI DRIVER, poi ci ha LEVATO<br/>

    LE MANI, vomitando FECI DELLA FRANZONI.</p>'
  author_url: http://vaffamculo
---
Ieri mi dirigo da MERDIAWORLD a comprare una scheda di rete pissiemsiaiei. GISUS CRAIST IS GHEI.  
Compro una TRUST DI MERDA, e dico “proviamo sta CAZZATA”.  
Torno a casa, la pluggo nel portatile, accendo e VA’, su linux VA’….  
Mi dico, PORCODDIO!  
lsmod dice che carica 8139too, e dico: OH, UNA RIALTEK, VAI CHE QUESTE VANNO NA SPADA!  
SI’, ‘NA SPADA DE BROWN NELLA VENAZZA RASTASHAVED DELLA KLISTOFRANZA IN CULO!  
PORCODDIO.  
Stacco il cavo di rete, e come e’ giusto che sia la rete MUORE. RIMETTO IL CAVO DI RETE E MUOIO IO.

> cat /var/log/messages (con un po’ di grep di minchia):  
>  Mar 21 19:56:40 sanjuro kernel: eth0: Setting 100mbps half-duplex based on auto-negotiated partner ability ffff.  
>  Mar 21 19:57:28 sanjuro kernel: NETDEV WATCHDOG: eth0: transmit timed out 

Dio cane, non puo’ andare IN TIMEOUT DOPO MENO DI UN MINUTO PORCODDIO.  
Poi quando riattacco il cavo MI ASPETTO CHE RIPARTA, CHE SI RIACCENDANO LE LUCINE INVECE NIENTE.

ifconfiggo down la minchia eth0 e riprovo dhcp, che NON VA’…  
Allora tolgo il modulo, lo modprobbo e mi dice che ci sono gli irq che conflittano col porco di dio.  
CONFLITTANO? E PRIMA COME FACEVA?  
ALLORA DIO GONFIO DI SEME, LEVO TUTTA LA SCHEDA TRUST DI MERDA, LA RIFICCO… NON VA.  
LA LEVO, LA FICCO NELL’ALTRO PLUG PISSIEMSIAIEI, E VA’!  
Dico: ah sara’ il bus che ha la merda, dato che m’era pure saltato fuori un bus error a na certa, in un reboot fatto in preda alla pazzia idrofoba.  
Dico: ok allora mo qua posso staccare il cavo di rete tranquillo.  
COL CAZZO.

PORCODDIO, L’ALTRA SCHEDA DI RETE NE2000 (PORCODDIO NE CHE E’ MERDA) NON FACEVA QUESTO!

SAPETE PERCHE’?

PERCHE’ TRUST E’ MERDA!
