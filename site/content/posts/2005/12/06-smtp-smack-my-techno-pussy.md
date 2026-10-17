---
title: 'SMTP: Smack My Techno Pussy'
date: '2005-12-06T18:01:00+02:00'
url: /2005/12/06/smtp-smack-my-techno-pussy/
aliases:
- /blog-static/2005/12/06/smtp-smack-my-techno-pussy/
wp_id: 263
authors:
- tripz
avatar: tripz.jpg
categories:
- niente-a-senso
tags: []
comments:
- id: 222
  author: sand
  date: '2005-12-06T19:09:00+02:00'
  body: <p>INIETTA IL DOPOFIST NEL TUO FLUSSO <acronym title="Simple Mail Transfer Protocol">SMTP</acronym> DEL PROTOCOLLO “LO INTERNE”</p>
  author_url: http://www.spatof.org
- id: 227
  author: guly
  date: '2005-12-07T20:22:00+02:00'
  body: '<p>secondo me devi fare<br/>

    apt-get install dpkg<br/>

    poi<br/>

    dpkg-reconfigure –reconfigure –keep-old-configuration –save-new-in-tmp qmail-src-politically_correct-stupid_license-compile_by_yourself</p>

    <p>c’erano 9 flag per ripristinare il file control di qmail, devi scriverle 9 volte usando 9 dita scavando per 9 anni sul 9^ collo di roma.</p>'
---
Io vado sul server di posta e cancello un dominio.  
Non funziona piu’ il server di posta.  
Nessuno spedisce/riceve mail.

root@mail ~# telnet localhost 25  
Trying 127.0.0.1…  
421 unable to read controls (#4.3.0)  
Connection closed.  
root@mail ~#

root@mail ~# ls -lh /var/qmail/control/rcpthosts  
-rw——- 1 root root 0 Dec 6 16:26 rcpthosts.lock

MA PORCODDIO!  
MA COSA?  
MA PERCHE’?  
MA QUANDO?

Io odio quello che ha fatto sto server, e specialmente quello che poi ci ha messo le sue UNTE E STRONZE MANI.  
CHE FRANZONITICOLGA BRUTTO COGLIO DI FIGLIONE!
