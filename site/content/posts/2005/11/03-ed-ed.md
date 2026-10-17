---
title: ED!!!! ED!!!!!!!
date: '2005-11-03T12:27:00+02:00'
url: /2005/11/03/ed-ed/
aliases:
- /blog-static/2005/11/03/ed-ed/
wp_id: 189
authors:
- pallotron
avatar: pallotron.jpg
categories:
- niente-a-senso
tags: []
comments:
- id: 144
  author: sand
  date: '2005-11-03T14:52:00+02:00'
  body: '<p>$EDITOR e’ un must, mentre per il crontab… e’ un CRAST.<br/>

    E’ cosi’ E BASTA!<br/>

    Sulla mia guida per installare OTRS su Solaris c’e’ appunto scritto che il crontab di solaris non supporta le frazioni tipo */5, e ti obbliga a dover scrivere:<br/>

    0,5,10,15,20,25,30,35,40,45,50,55 * * * * /bin/suca</p>

    <p>MALE</p>'
  author_url: http://www.spatof.org
---
Vuoi cambiare crontab su **SLOWLARIS 9 X86**???  
Va’! Va’! VAI! FA PURE!!!! FALLO!!!!

![FALLO!](/wp-content/upload/fallosmall.gif)

`bash-2.05# crontab -e  
477  
dfdfa  
?  
porcoddio  
?  
ma vaffanculo va'  
?  
MA CHE CAZZO MI FAI USARE ED COGLIONE!  
?  
q  
The crontab file was not changed.`

MA PORCODDIO! ED!!!! MA SE C’E’ VI AHAHAHAHAH!  
CHE SISTEMA DIMMERDA!

`# export EDITOR=vi`

E NONOSTANTE CIO’ CRON NON PARE ACCETTARE LA SINTASSI:

`*/3 * * * * comando`

ma che merda… mi tocca farmi uno script con while e sleep per checckare una cosa… e metterlo su /etc/rc2…
