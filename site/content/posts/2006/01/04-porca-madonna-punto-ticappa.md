---
title: porca madonna punto ticappa
date: '2006-01-04T16:14:00+02:00'
url: /2006/01/04/porca-madonna-punto-ticappa/
aliases:
- /blog-static/2006/01/04/porca-madonna-punto-ticappa/
wp_id: 305
authors:
- sand
avatar: sand.jpg
categories:
- niente-a-senso
tags: []
---
Io non riesco a capire perche’ ssh-agent viene cosi’ **MALGESTITO**.  
Inizia la mia merdosa sessione ICS, e le variabili di ssh-agent sono **SBAGLIATE** :

> % ps xauw | grep agent  
>  daniel 12176 /usr/bin/ssh-agent -s  
>  % echo $SSH_AGENT_PID  
>  12103  
>  % ssh-add -l  
>  Could not open a connection to your authentication agent.  
>  % echo $SSH_AUTH_SOCK  
>  /tmp/ssh-YQyKn12102/agent.12102  
>  % ls -l /tmp/ssh-YQyKn12102/agent.12102  
>  ls: /tmp/ssh-YQyKn12102/agent.12102: No such file or directory
> 
> % export SSH_AUTH_SOCK=/tmp/ssh-iMMNR12174/agent.12174  
>  % ssh-add -l  
>  The agent has no identities. 

Componendo rime in bestemmia, _allegre ma non troppo_ , mi **illudo** che ora ESSO FUNZIONI, **MA** :

> % chiavale  
>  Identity added: /home/daniel/.ssh/…  
>  Enter passphrase for /home/daniel/.ssh/…  
>  Identity added: /home/daniel/.ssh/… 

Uhm…

> % ssh-add -l  
>  The agent has no identities. 

MADONNA SCOLOPENDRA CHE FRUSTA CRISTO “ER COLABRODO”, GESU’ MENESTRELLO CHE FUMA CIOSPE DE PAGLIA NCULO, **MR. T. PENSACI T.**!

Io porco dio non capisco perche’, nell’atto di rendermi la vita piu’ **semplice** , io debba patire queste STRONZATE, frutto di un engeneering fatto CON LA COPPOLA DI FUNCIA, dio CODER APPESO PER LE PALLE, BASTONATO DA UN CANE BUROCRATE, GESUGIUSEPPEMARYA. grr.

P.S.

> chiavale () {  
>  keychain –inherit local -q ~/.ssh/*.pub(:r)  
>  }

IL SESSO, IL SESSO DEGLI ANGELI.

P.P.S.  
ECCO PERCHE’: LA MERDA.

> [[ -e ~/.keychain/scroto-sh ]] && source ~/.keychain/scroto-sh

**VAFFANCULO AL CAZZO DI ROBERT GENTOO**.
