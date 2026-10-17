---
title: ARGHHHHHHHHHHHHH!
date: '2008-01-04T10:37:00+02:00'
url: /2008/01/04/arghhhhhhhhhhhhh/
aliases:
- /blog-static/2008/01/04/arghhhhhhhhhhhhh/
wp_id: 956
authors:
- pallotron
avatar: pallotron.jpg
categories:
- niente-a-senso
tags: []
comments:
- id: 2678
  author: fabio
  date: '2008-01-04T11:18:00+02:00'
  body: <p>6 anni di esperienza in java sono come 6 giorni di esperienza a raccogliere pomodori!</p>
  author_url: http://www.unoamolti.it/blog
- id: 2681
  author: Barrett
  date: '2008-01-04T15:11:00+02:00'
  body: <p>Hahahhaahhahahahaha ma che figata, un espertone sto qua eh :D</p>
- id: 2685
  author: Berry
  date: '2008-01-04T20:05:00+02:00'
  body: '<p>Ma porkodio.<br/>

    Questa cosa mi e’ successa tipo 7 anni fa con dei consulenti di 20esimo livello Accenture.<br/>

    Che massa di imbecilli… hanno iniziato ad adorare il mio pene quando hanno scoperto che si poteva girare piu’ di un’instanza Tomcat su un unico server (bastava cambiare le porte nel fottuto file di configurazione).</p>

    <p>Dio Nerone Catilina Catalina</p>'
- id: 2686
  author: pallotron
  date: '2008-01-04T20:41:00+02:00'
  body: '<p>@Berry: ’sta cosa di far girare due tomcat sullo stesso server non la capisco: ho preso parte ad un progetto; un’applicazione web su tomcat. Fu scritta e tutto funziono’. Dopo qualche tempo e’ stata richiesta una Change Request, ed invece di estendere l’applicazione precedente, fu richiesto un’altra applicazione web, indipendente da quella precendente, per questioni di design e scalabilita’. Ma ’sta di fatto che alla fine fu’ installata sulla stessa macchina dell’applicazione precedente… ed invece di deployarla sullo stesso tomcat l’hanno messa su un altro tomcat sulla stessa macchina… non ho mai capito perche’ hanno scelto cosi’… secondo me si poteva fare tutto sull’unico tomcat e lo dissi… poi magari sono ignorante di tomcat ed erro…</p>

    <p>parlando invece di Accenture, una volta mentre mi trovavo a Milano in $grandeaziendaditlc affianco a me c’era un tipo Accenture che non riusciva manco ad installarlo tomcat! cioe’ manco tar xvfz sapeva fare… gliel’ho dovuto spiegare io…<br/>

    2 settimane fa uscendo con la mia donna ho conosciuto una tipa laureata in ing. gestionale, dipendente accenture a londra, molto competente. gli ho raccontato la vicenda di cui sopra e quasi si e’ offesa… penso che la situazione accenture italia sia molto diversa da accenture $restodelmondo…</p>'
  author_url: http://www.pallotron.net
  by_post_author: true
- id: 2688
  author: B_Berry
  date: '2008-01-06T20:24:00+02:00'
  body: '<p>@Pallotron: eheh hai ragione forse la media dell’idiozia italiana supera quella mondiale :D</p>'
- id: 2699
  author: fukikoma
  date: '2008-01-07T18:51:00+02:00'
  body: '<p>@B_Berry: e in tutti i campi, tutti tutti</p>'
---
> **Senior Testing Engineer** : potresti dirmi come faccio ad aggiornare la jvm su una macchina?
> 
> **Angelo (pallotron) Failla** : basta installare la nuova jvm sul disco e cambiare le variabili di ambiente…
> 
> **Senior Testing Engineer** : ok e per installare la jvm ?
> 
> **Angelo (pallotron) Failla** : scarichi la jvm, chmod +x file && ./file, leggi lo schermo, e poi aggiorni le variabili di ambiente…
> 
> **Senior Testing Engineer** : ok

Dopo un po’…

> **Senior Testing Engineer** : puoi venire? 

Non aveva impostato JAVA_HOME alla nuova directory della jvm, ne’ il PATH per avere $JAVA_HOME/bin/…

Glielo dico e torno a sedere… dopo un po’:

> **Senior Testing Engineer** : puoi venire? se faccio java -version mi spunta ancora la versione vecchia! 

Mi rialzo, vado a vedere, aveva messo “:$JAVA_HOME/bin/” alla fine della catena dei PATH… e la shell gli prendeva con precedenza il comando java di default dentro”/usr/bin/java” …

ARRRRRRRRRRRRRRRRRRRGGGGGGGGGGGGGGGGGGGGHHHHHHHHHHHHHHHH!!!!!!!!

![argh.jpg](/wp-content/upload/2008/01/argh.jpg)

Sentirsi dire questo da un Senior… con 6 anni di esperienza… e’ abbastanza deprimente…
