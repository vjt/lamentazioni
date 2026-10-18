# lamentazioni

Resurrezione di **lamentazioni.org**, blog collettivo di lamentele (WordPress, 2005–2009),
oggi servito come sito statico su **https://lamentazioni.diomaiale.com**.

907 post, commenti compresi, ricostruiti da un mirror `wget` del WordPress originale
in un sito Hugo che conserva il tema originale `gloriousfuture` e i vecchi URL
`/AAAA/MM/GG/<slug>/`, così i link del 2005 funzionano ancora.

## Struttura

- `mirror/` — il dump statico originale di lamentazioni.org (fonte di verità, sola lettura)
- `tools/extract.py` — HTML → Markdown + front matter + commenti, dentro `site/content/`
- `tools/recover_images.py` — recupera da archive.org le immagini morte insieme ai loro host
- `tools/check_*.py` — controlli su testo, struttura e link, lanciati a ogni build
- `site/` — sito Hugo: configurazione, tema portato, asset statici
- `PLAN.md`, `BUILD_REPORT.md` — come è stato fatto e cosa è stato misurato

## Build

Gira tutto dentro un'immagine Docker, sull'host non si installa niente:

```sh
tools/build.sh
```

Esegue extract → `hugo` → controlli → [pagefind](https://pagefind.app/) (ricerca lato
client). Il risultato finisce in `site/public/`, pronto da copiare su qualunque web server statico.

## Licenza

I post e i commenti appartengono ai rispettivi autori.
