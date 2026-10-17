---
title: SED ERE ROTTO
date: '2005-09-08T12:27:00+02:00'
url: /2005/09/08/sed-ere-rotto/
aliases:
- /blog-static/2005/09/08/sed-ere-rotto/
wp_id: 92
authors:
- sand
avatar: sand.jpg
categories:
- niente-a-senso
tags: []
comments:
- id: 68
  author: sand
  date: '2005-09-08T13:22:00+02:00'
  body: '<p>Al momento l’unica soluzione sembra VIM:<br/>

    :%s/^\n\+/\r/</p>

    <p>Trasforma 1+X righe vuote in una singola riga vuota.</p>'
  author_url: http://www.spatof.org
  by_post_author: true
---
Chi ha scritto **sed** probabilmente aveva GRAVI PROBLEMI NELLA COMPRENSIONE DELLA REALTA’ SOCIALE.

> Regular expressions match entire strings, not just individual lines, but a newline character is matched by \n in a sed RE; a newline character is not allowed in an RE. Also note that \n cannot be used to match a newline character at the end of an arbitrary input line; newline characters appear in the pattern space as a result of the N editing command. 

No perche’ io non capisco.  
“Le espressioni regolari matchano stringhe intere, non solo linee individuali, ma un carattere di newline e’ matchato da \n in una regexp di sed; **un carattere di newline non e’ permesso in una regexp**. Per di piu’ sappi che \n non puo’ essere usato per matchare un carattere di newline alla fine di una arbitraria linea di input; i caratteri di newline appaiono nel pattern space come risultato del comando di editing **N**.”

AH ALLORA HO CAPITO TUTTO, PERO’ NON POSSO FARE  
**s/\n\\+/\n/**

CIOE’ COMPRIMERE X LINEE VUOTE IN UNA SOLA. GRAZIE.  
E PIOVE.
