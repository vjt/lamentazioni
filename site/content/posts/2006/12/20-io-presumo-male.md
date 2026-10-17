---
title: Io presumo male
date: '2006-12-20T15:36:00+02:00'
url: /2006/12/20/io-presumo-male/
aliases:
- /blog-static/2006/12/20/io-presumo-male/
wp_id: 748
authors:
- unixman
avatar: unixman.jpg
categories:
- niente-a-senso
tags: []
---
Mattina, ore 11,30, arrivato al lavoro dopo una serata stravolto,  
e’ Natale e’ gia solo per questo il mondo meriterebbe la nuclearizzazione,  
viene il cliente e mi chiede di far montare via NFS ad alcuni host  
delle directory esportate da un NAS gateway, dicendomi che  
aveva provato e che non riusciva. Con la presunzione di chi  
**sa** (visto che l’ho creata io sta rete del male) tra me e me  
penso e dico anche **ovvio, sara’ il firewall che ti droppa** ,  
conoscendo il malefico controllopunto-1. Vediamo nei log e  
analfatti manca la regola. Aggiungo la regola, ed et  
voila’.  
Et voila’ un cazzo, i pacchetti passano ma le macchine  
non montano. Gia’ un brivido mi corre lungo la schiena, conosco  
quell’oggetto maligno che e’ il NAS gateway, so che ha una command  
line anale e un’interfaccia _Javeh_ ancora peggio. Carico l’applet del  
feco, le export ci sono tutte, gli host pure, i permessi anche,  
gli hostgroup idem, c’e’ anche un cristo che mi guarda torvo, che minchia vuoi ?  
Nel mentre gia’ che ci sono testo anche la ridondanza  
di un paio di bilanciatori del male (ma questa e’ un altro film  
dell’**orrore**) e chiedo ad un collega di seguire lui sta faccenda del NAS.  
Risolta la ridondanza dei bilanciatori anali, spurgate un paio  
di mail, mi rimetto a vedere insieme a lui sta roba mefitica.  
Dopo un tripudio di bestemmie varie e in varie lingue, ci  
accorgiamo, ma toh, ma vedi un po’ che sembra che manchi  
proprio la directory esportata …. mkdir /lamorte/tiprenda sul  
malefico NAS, e finalmente gli host montano come dei mufloni infoiati.  
![edika.gif](/wp-content/upload/2006/12/edika.thumbnail.gif)  
In genere, tipicamente, prima di agire penso, se devo sharare  
qualcosa, magari anche prima la creo, POI se non funziona  
indago sul perche’ non funzioni, se tu cliente amministri quell’oggetto  
malefico presumo tu sappia cio’ che fai … ma io presumo male,  
presumo che la gente sappia cio’ che fa e cio’ e’ sbagliato.  
Cristo, e’ solo mercoledi’ ….  
![urlo.jpg](/wp-content/upload/2006/12/urlo.thumbnail.jpg)
