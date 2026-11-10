# Sito Panificio Pasticceria Brizzolari

Sito statico (HTML + CSS + un po' di JS), nessuna build. Si apre `index.html` nel browser o si carica la cartella su qualsiasi hosting.

- `index.html` Home: hero, Il forno, Pane, Pasticceria, Torte su ordinazione, Recensioni
- `orari.html` Orari e dove siamo (mappa Google caricata solo su clic, per i cookie)
- `contatti.html` Recapiti e modulo (apre il programma di posta con il messaggio pronto; `?tipo=torta` preseleziona "Torta su ordinazione")
- `tokens.css` design system (non modificare), `css/sito.css` layout delle pagine, `js/sito.js` menu, mappa, modulo
- `assets/` logo originale + versioni ridotte (160/640 px, PNG e WebP), favicon

## Segnaposto da sostituire
Cercare `[` nei file HTML: `[INDIRIZZO]`, `[TELEFONO]`, `[EMAIL]`, `[ORARIO]`, `[GIORNI]`, `[ORARI FESTIVI E FERIE]`, `[INFO PARCHEGGIO]`, `[PRODOTTO]`, `[DESCRIZIONE]`, `[PREZZO]`, `[FOTO]`, `[PREAVVISO]`, `[RECENSIONE]`, `[NOME CLIENTE]`, `[FONTE]`, `[LINK RECENSIONI GOOGLE]`, `[LINK INSTAGRAM]`, `[LINK FACEBOOK]`, `[P.IVA]`, `[LINK PRIVACY]`, `[LINK COOKIE]`.

La mappa e il link "Apri in Google Maps" cercano "Panificio Pasticceria Brizzolari Peschiera del Garda": con l'indirizzo esatto, aggiornare la query in `orari.html`.
