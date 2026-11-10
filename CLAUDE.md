# Sito Panificio Pasticceria Brizzolari — istruzioni per Claude Code

Leggi questo file prima di ogni modifica al sito. Il design system è vincolante: usa solo i token di `tokens.css` (o il preset Tailwind `tailwind.preset.js`), niente colori o font inventati.

## Il cliente
- **Panificio Pasticceria Brizzolari**, Peschiera del Garda (VR). Aperto **dal 1954**.
- Mascotte/logo: **Brizzo**, una pagnotta con occhiali da sole (file in `assets/`).
- Personalità: forno di famiglia storico ma con **animo giovane**; ambiente **caldo**, accogliente, ironico senza essere infantile.
- Lingua del sito: italiano. Tono: dare del "voi"/"tu" in modo familiare, frasi brevi, un pizzico di ironia ("Il pane ha gli occhiali."). Mai linguaggio da catena industriale.

## Dati da NON inventare
Orari, prezzi, indirizzo esatto, telefono, prodotti specifici, ingredienti, allergeni, recensioni, numeri ("70 anni di…" va bene perché è dal 1954; nient'altro). Dove mancano, usa segnaposto tra parentesi quadre: `[ORARIO]`, `[PREZZO]`, `[INDIRIZZO]`, `[TELEFONO]`, `[DESCRIZIONE]`. Elenca alla fine del lavoro i segnaposto rimasti.

## Colori (estratti dal logo)
| Token | Hex | Ruolo |
|---|---|---|
| `--blu` Blu Brizzo | `#1265A9` | Primario: titoli, pulsanti principali, link |
| `--notte` Notte | `#224968` | Fondi scuri (footer, fasce orari), hover del blu |
| `--crosta` Crosta | `#E29233` | Accento caldo: etichette, dettagli |
| `--oro` Oro Grano | `#F5C14C` | Evidenza: promo, novità, pulsante secondario |
| `--mattone` Mattone | `#E07D49` | Fuoco/forno: solo fondi o testo ≥24px bold |
| `--salvia` Salvia | `#8ABA8F` | Fresco: integrali, stagionali |
| `--bruno` Bruno Forno | `#5E230B` | Testo principale, contorni, ombre |
| `--caramello` Caramello | `#9A541F` | Testo secondario, occhielli, accento serif |
| `--crema` Crema | `#FAF2DF` | Fondo pagina (è il fondo del logo) |
| `--farina` Farina | `#FFFBF2` | Superfici: card, sezioni alternate |

Proporzioni indicative: crema/farina circa metà, blu ~18%, bruno ~14%, oro ~10%, crosta e salvia come tocchi.

Abbinamenti testo ammessi (contrasto AA): bruno su crema/farina/oro/crosta/salvia; farina su blu/notte/bruno/caramello; blu su crema/farina; caramello su crema/farina. **Mai** testo piccolo su mattone, **mai** bianco su oro/crosta/salvia.

## Tipografia (Google Fonts)
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,500;1,9..144,400;1,9..144,600&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&display=swap" rel="stylesheet">
```
- **Baloo 2** (700–800) — titoli, prezzi, pulsanti, nomi prodotto. Richiama la scritta BRIZZO.
- **Fraunces corsivo** (400) — solo accenti di tradizione: "dal 1954", citazioni, nomi ricette. Max uno per sezione, colore caramello.
- **DM Sans** (400/500/700) — testi, menu, orari, allergeni, etichette maiuscole spaziate.

Scala (desktop → mobile, via `clamp`): display 88→48, h1 64→40, h2 48→32, accento 32→24, sottotitolo 22→19, testo 17/1.55, etichetta 13 maiuscolo +0.14em.

## Stile "adesivo" (la firma visiva)
Come nell'illustrazione del logo:
- contorno **2px bruno** (`--bordo`) su card, pulsanti, etichette, immagini;
- **ombra piena spostata** `4px 4px 0` (piccola) / `6px 6px 0` (card) / `12px 12px 0` (hero), colore bruno, senza sfocatura;
- angoli morbidi: 12px (piccoli), 20px (card), 999px (pulsanti ed etichette);
- leggere rotazioni (−2°/+6°) solo su elementi decorativi (cartellino, foto hero);
- hover dei pulsanti: si spostano di 2px verso l'ombra (l'ombra si accorcia); active: ombra 0.

Da evitare: gradienti, glassmorphism, ombre sfocate, bordi colorati solo a sinistra, emoji come icone, foto stock generiche. Icone: stroke 1.6–2px bruno, angoli arrotondati (es. Lucide).

## Componenti (classi in `tokens.css`, esempi in `componenti.html`)
- `.btn .btn--primario` (blu), `.btn--oro`, `.btn--contorno`
- `.tag` + `--crosta | --salvia | --blu | --farina` ("Appena sfornato", "Integrale", "Novità", "Su ordinazione")
- `.card-prodotto` (immagine con fondo colorato + tag, nome Baloo, descrizione, prezzo blu)
- `.card-orari` (fondo notte, testo farina, città in Fraunces oro)
- `.cartellino` (fondo oro, ruotato −2°)
- `.occhiello` (etichetta di sezione: maiuscolo, caramello)

## Struttura sito consigliata
Home (hero con Brizzo + "dal 1954" + CTA) · Il forno / La nostra storia · Pane · Pasticceria · Torte su ordinazione · Orari e dove siamo (mappa) · Contatti. Footer notte con orari, indirizzo, social.

## Regole tecniche
- Stack libero (HTML statico, Astro, Next…). Importa sempre `tokens.css`. Con Tailwind v3 usa `tailwind.preset.js`; con Tailwind v4 mappa le variabili di `tokens.css` dentro `@theme`.
- Mobile first; contenitore max 1200px, gutter 16px su mobile, 24–32 desktop.
- HTML semantico, `<button>`/`<a>` veri, `alt` su tutte le immagini, focus visibile (`outline: 3px solid var(--oro)` + offset).
- Area di rispetto attorno al logo: circa metà dell'altezza della "B". Il logo va su crema o farina; su fondi scuri inserirlo in un riquadro crema con contorno bruno.
- Rispetta `prefers-reduced-motion` (niente rotazioni animate/hover che si muovono).
- Immagini prodotto: foto vere del cliente quando disponibili; finché mancano, riquadro colorato con icona e segnaposto.
