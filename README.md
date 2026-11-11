# Sito Panificio Pasticceria Brizzolari

Sito statico (HTML + CSS + un po' di JS) pubblicato su Cloudflare Workers. I percorsi sono assoluti (`/css/…`), quindi per provarlo in locale serve un server, per esempio `npx wrangler dev` (poi http://localhost:8787).

Lingue: italiano nella radice, inglese in `en/`, francese in `fr/`, tedesco in `de/`.

| Pagina | IT | EN | FR | DE |
|---|---|---|---|---|
| Home | `/` | `/en/` | `/fr/` | `/de/` |
| Orari e dove siamo | `/orari` | `/en/hours` | `/fr/horaires` | `/de/zeiten` |
| Contatti | `/contatti` | `/en/contact` | `/fr/contact` | `/de/kontakt` |

**Le pagine HTML sono generate**: i testi di tutte le lingue stanno in `scripts/genera.py` (dizionario `T`). Dopo ogni modifica:

```bash
python3 scripts/genera.py
```

- Home: hero, Il forno, Pane, Pasticceria, Torte su ordinazione, Recensioni
- Orari e dove siamo: mappa Google caricata solo su clic, per i cookie
- Contatti: modulo che apre il programma di posta con il messaggio pronto; `?tipo=torta` preseleziona la torta
- `404.html` pagina di errore (italiano, con link alle altre lingue)
- `tokens.css` design system (non modificare), `css/sito.css` layout delle pagine, `js/sito.js` menu, mappa, modulo
- `assets/` logo originale + versioni ridotte (160/640 px, PNG e WebP), favicon

## Segnaposto da sostituire
Si sostituiscono in `scripts/genera.py`, poi si rigenera. I segnaposto testuali (`[DESCRIZIONE]`, `[PRODOTTO]`, `[RECENSIONE]`…) vanno scritti in ogni lingua. Elenco: `[INDIRIZZO]`, `[TELEFONO]`, `[EMAIL]`, `[ORARIO]`, `[GIORNI]`, `[ORARI FESTIVI E FERIE]`, `[INFO PARCHEGGIO]`, `[PRODOTTO]`, `[DESCRIZIONE]`, `[PREZZO]`, `[FOTO]`, `[PREAVVISO]`, `[RECENSIONE]`, `[NOME CLIENTE]`, `[FONTE]`, `[LINK RECENSIONI GOOGLE]`, `[LINK INSTAGRAM]`, `[LINK FACEBOOK]`, `[P.IVA]`, `[LINK PRIVACY]`, `[LINK COOKIE]`, `[DOLCE DEL GIORNO]`.

La mappa e il link "Apri in Google Maps" cercano "Panificio Pasticceria Brizzolari Peschiera del Garda": con l'indirizzo esatto, aggiornare `MAPS_Q` in `scripts/genera.py`. Il dominio usato per canonical e hreflang è `BASE`, nello stesso file.
