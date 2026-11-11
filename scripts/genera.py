#!/usr/bin/env python3
"""Genera le pagine del sito in tutte le lingue.

Uso:  python3 scripts/genera.py
I testi stanno nel dizionario T (una voce per lingua). Le pagine HTML nella
radice (italiano) e in en/, fr/, de/ sono generate: non modificarle a mano.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://brizzolari.pressart.work"  # dominio pubblico, per canonical e hreflang
LINGUE = ["it", "en", "fr", "de"]

# percorso pubblico e file di ogni pagina, per lingua
PAGINE = {
    "it": {"home": ("/", "index.html"), "orari": ("/orari", "orari.html"), "contatti": ("/contatti", "contatti.html")},
    "en": {"home": ("/en/", "en/index.html"), "orari": ("/en/hours", "en/hours.html"), "contatti": ("/en/contact", "en/contact.html")},
    "fr": {"home": ("/fr/", "fr/index.html"), "orari": ("/fr/horaires", "fr/horaires.html"), "contatti": ("/fr/contact", "fr/contact.html")},
    "de": {"home": ("/de/", "de/index.html"), "orari": ("/de/zeiten", "de/zeiten.html"), "contatti": ("/de/kontakt", "de/kontakt.html")},
}

def url(lang, pagina, ancora=""):
    return PAGINE[lang][pagina][0] + ancora

# ---------------------------------------------------------------- testi
T = {
"it": dict(
    nome_lingua="Italiano", locale="it_IT",
    salta="Vai al contenuto", menu="Menu", nav_label="Principale", lingua_label="Lingua",
    barra="dal 1954 · Peschiera del Garda",
    nav_home="Home", nav_forno="Il forno", nav_pane="Pane", nav_pasticceria="Pasticceria",
    nav_orari="Orari e dove siamo", nav_contatti="Contatti", ordina="Ordina una torta",
    sotto_marchio="Panificio Pasticceria",
    logo_alt="Brizzo, la pagnotta con gli occhiali da sole, logo del Panificio Brizzolari",
    dal1954="dal 1954", f_orari="Orari", f_tutti_orari="Tutti gli orari", f_contatti="Contatti",
    privacy="Privacy", cookie="Cookie", piva="P.IVA",
    tag_appena="Appena sfornato", tag_integrale="Integrale", tag_novita="Novità",
    # home
    h_title="Panificio Pasticceria Brizzolari · Peschiera del Garda, dal 1954",
    h_desc="Pane, dolci e torte su ordinazione fatti in casa ogni giorno a Peschiera del Garda. Il forno di famiglia Brizzolari, dal 1954.",
    hero_accento="dal 1954, con le mani in pasta",
    hero_sotto="Pane, dolci e lievitati fatti in casa, ogni giorno, a Peschiera del Garda.",
    cta_banco="Scopri il banco", cta_dove="Dove siamo",
    nastro=["Appena sfornato", "Dal 1954", "Il pane ha gli occhiali", "Con le mani in pasta", "Peschiera del Garda", "Torte su ordinazione"],
    forno_h2="Un forno di famiglia con l'animo giovane",
    forno_p1="Abbiamo acceso il forno nel 1954 e da allora non abbiamo più smesso. Oltre settant'anni dopo l'impasto si fa ancora qui, ogni giorno, con le mani in pasta.",
    forno_p2="[DESCRIZIONE: la storia della famiglia Brizzolari e del forno]",
    val1=("Sfornato ogni giorno.", "Il pane di oggi è di oggi. [DESCRIZIONE]"),
    val2=("Di famiglia, da sempre.", "[DESCRIZIONE]"),
    val3=("Serio sul pane, meno su tutto il resto.", "Il pane ha gli occhiali, del resto."),
    forno_accento="una storia che profuma di crosta",
    forno_anno="L'anno in cui abbiamo sfornato la prima pagnotta a Peschiera del Garda.",
    bollino="dal",
    pane_occhiello="Il nostro banco", pane_h2="Il pane di ogni giorno",
    pane_p="Dalla pagnotta della domenica al panino della merenda. [DESCRIZIONE]",
    past_h2="Dolci per colazione, merenda e scuse",
    past_p="Lievitati, paste e biscotti preparati nel nostro laboratorio. [DESCRIZIONE]",
    oggi_banco="Oggi al banco",
    torte_occhiello="Torte su ordinazione", torte_h2="La torta la pensi tu, al forno pensiamo noi",
    torte_p="Compleanni, battesimi, anniversari o un martedì qualsiasi che merita di più. Raccontaci cosa ti serve e la prepariamo per te. [DESCRIZIONE: tipi di torte disponibili]",
    passo1=("Raccontaci la festa", "Chiamaci, passa in negozio o scrivici: quante persone, che gusto, che occasione."),
    passo2=("Fissiamo i dettagli", "Scegliamo insieme gusto, formato e decorazione. Serve un preavviso di [PREAVVISO]."),
    passo3=("Passi a ritirarla", "Il giorno concordato la trovi pronta al banco. Le candeline sono affar tuo."),
    su_ordinazione="Su ordinazione", torte_prezzo="Torte a partire da [PREZZO] €",
    richiedi_torta="Richiedi una torta", chiama_forno="Chiama il forno",
    rec_occhiello="Recensioni", rec_h2="Lo dicono loro, mica noi", rec_tutte="Leggi tutte le recensioni",
    fascia_h2="Il pane ha gli occhiali.", vieni="Vieni a trovarci",
    # orari
    o_title="Orari e dove siamo · Panificio Brizzolari, Peschiera del Garda",
    o_desc="Orari di apertura e indirizzo del Panificio Pasticceria Brizzolari a Peschiera del Garda (VR).",
    o_h1="Il forno è acceso. Ecco quando.",
    o_sotto="Passa a prendere il pane caldo: ti aspettiamo a Peschiera del Garda.",
    o_card="Orari del forno",
    giorni=["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"],
    o_festivi="Festivi e chiusure:", o_dove="Dove siamo", o_parcheggio="Come arrivare e parcheggio:",
    o_maps="Apri in Google Maps", o_mappa="Mappa",
    o_mappa_testo="La mappa è fornita da Google. Caricandola accetti i suoi cookie.",
    o_mappa_btn="Mostra la mappa", o_mappa_titolo="Mappa: Panificio Pasticceria Brizzolari, Peschiera del Garda",
    # contatti
    c_title="Contatti · Panificio Brizzolari, Peschiera del Garda",
    c_desc="Telefono, email e modulo per ordinare torte e chiedere informazioni al Panificio Pasticceria Brizzolari.",
    c_h1="Due chiacchiere col forno",
    c_sotto="Per una torta, un'informazione o per sapere se è rimasto del pane: chiamaci, scrivici o passa.",
    c_recapiti="Recapiti",
    c_tel=("Telefono", "Il modo più veloce, negli orari di apertura.", "Chiama"),
    c_mail=("Email", "Per richieste con calma, preventivi e torte.", "Scrivici"),
    c_negozio=("In negozio", "Orari e mappa"),
    c_h2="Ordina una torta o chiedi quello che vuoi",
    c_p1="Compila il modulo: si aprirà il tuo programma di posta con il messaggio già pronto, tu devi solo premere invia.",
    c_p2="Per le torte su ordinazione serve un preavviso di [PREAVVISO]. Ti richiamiamo noi per confermare.",
    c_accento="rispondiamo tra un'infornata e l'altra",
    f_motivo="Di cosa hai bisogno?", f_opzioni=("Informazioni", "Torta su ordinazione", "Altro"),
    f_nome="Nome e cognome", f_tel="Telefono", f_email="Email", f_facolt="(facoltativa)",
    f_data="Data di ritiro", f_msg="Messaggio", f_aiuto="Per una torta: occasione, numero di persone, gusto, scritta.",
    f_privacy="Ho letto l'<a href=\"[LINK PRIVACY]\">informativa privacy</a> e acconsento al trattamento dei dati per rispondere alla mia richiesta.",
    f_invia="Prepara il messaggio",
    f_errore="Manca qualcosa: compila i campi obbligatori e accetta l'informativa privacy.",
    f_mail_richiesta="Richiesta",
),
"en": dict(
    nome_lingua="English", locale="en_GB",
    salta="Skip to content", menu="Menu", nav_label="Main", lingua_label="Language",
    barra="since 1954 · Peschiera del Garda",
    nav_home="Home", nav_forno="Our bakery", nav_pane="Bread", nav_pasticceria="Pastries",
    nav_orari="Hours & location", nav_contatti="Contact", ordina="Order a cake",
    sotto_marchio="Bakery & Pastry shop",
    logo_alt="Brizzo, the loaf of bread wearing sunglasses, logo of Panificio Brizzolari",
    dal1954="since 1954", f_orari="Opening hours", f_tutti_orari="All opening hours", f_contatti="Contact",
    privacy="Privacy", cookie="Cookies", piva="VAT no.",
    tag_appena="Fresh from the oven", tag_integrale="Wholemeal", tag_novita="New",
    h_title="Panificio Pasticceria Brizzolari · Bakery in Peschiera del Garda since 1954",
    h_desc="Bread, pastries and made-to-order cakes baked in-house every day in Peschiera del Garda. The Brizzolari family bakery, since 1954.",
    hero_accento="since 1954, hands in the dough",
    hero_sotto="Bread, cakes and pastries made in-house every day in Peschiera del Garda.",
    cta_banco="See the counter", cta_dove="Find us",
    nastro=["Fresh from the oven", "Since 1954", "Our bread wears shades", "Hands in the dough", "Peschiera del Garda", "Cakes to order"],
    forno_h2="A family bakery with a young soul",
    forno_p1="We lit the oven in 1954 and we haven't stopped since. More than seventy years later, the dough is still made right here, every day, with our own hands.",
    forno_p2="[DESCRIZIONE: la storia della famiglia Brizzolari e del forno]",
    val1=("Baked every day.", "Today's bread is today's bread. [DESCRIZIONE]"),
    val2=("Family-run, always.", "[DESCRIZIONE]"),
    val3=("Serious about bread, less so about everything else.", "Our bread wears sunglasses, after all."),
    forno_accento="a story that smells of fresh crust",
    forno_anno="The year we baked our very first loaf in Peschiera del Garda.",
    bollino="since",
    pane_occhiello="On our counter", pane_h2="Everyday bread",
    pane_p="From the Sunday loaf to the after-school roll. [DESCRIZIONE]",
    past_h2="Sweets for breakfast, snack time and apologies",
    past_p="Leavened bakes, pastries and biscuits made in our own workshop. [DESCRIZIONE]",
    oggi_banco="Today on the counter",
    torte_occhiello="Cakes to order", torte_h2="You dream up the cake, we handle the oven",
    torte_p="Birthdays, christenings, anniversaries or just a Tuesday that deserves more. Tell us what you need and we'll make it for you. [DESCRIZIONE: tipi di torte disponibili]",
    passo1=("Tell us about the party", "Call us, drop by the shop or write to us: how many people, which flavour, what occasion."),
    passo2=("We sort out the details", "Together we choose flavour, size and decoration. Please order [PREAVVISO] in advance."),
    passo3=("You pick it up", "On the agreed day it's ready and waiting at the counter. The candles are up to you."),
    su_ordinazione="Made to order", torte_prezzo="Cakes from [PREZZO] €",
    richiedi_torta="Request a cake", chiama_forno="Call the bakery",
    rec_occhiello="Reviews", rec_h2="Don't just take our word for it", rec_tutte="Read all reviews",
    fascia_h2="Our bread wears shades.", vieni="Come and see us",
    o_title="Opening hours & location · Panificio Brizzolari, Peschiera del Garda",
    o_desc="Opening hours and address of Panificio Pasticceria Brizzolari, bakery in Peschiera del Garda (Verona).",
    o_h1="The oven's on. Here's when.",
    o_sotto="Come by for warm bread: we're waiting for you in Peschiera del Garda.",
    o_card="Bakery opening hours",
    giorni=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    o_festivi="Public holidays and closures:", o_dove="Where we are", o_parcheggio="Getting here and parking:",
    o_maps="Open in Google Maps", o_mappa="Map",
    o_mappa_testo="The map is provided by Google. Loading it means accepting its cookies.",
    o_mappa_btn="Show the map", o_mappa_titolo="Map: Panificio Pasticceria Brizzolari, Peschiera del Garda",
    c_title="Contact · Panificio Brizzolari, Peschiera del Garda",
    c_desc="Phone, email and a form to order cakes or ask Panificio Pasticceria Brizzolari anything.",
    c_h1="Have a chat with the bakery",
    c_sotto="For a cake, a question or to check if there's any bread left: call, write or drop by.",
    c_recapiti="Contact details",
    c_tel=("Phone", "The quickest way, during opening hours.", "Call"),
    c_mail=("Email", "For questions that can wait, quotes and cakes.", "Write to us"),
    c_negozio=("In the shop", "Hours and map"),
    c_h2="Order a cake or ask us anything",
    c_p1="Fill in the form: your email app will open with the message ready to go, you just hit send.",
    c_p2="Cakes need to be ordered [PREAVVISO] in advance. We'll call you back to confirm.",
    c_accento="we reply between one batch and the next",
    f_motivo="What do you need?", f_opzioni=("Information", "Cake to order", "Something else"),
    f_nome="Full name", f_tel="Phone", f_email="Email", f_facolt="(optional)",
    f_data="Pick-up date", f_msg="Message", f_aiuto="For a cake: occasion, number of people, flavour, writing on top.",
    f_privacy="I have read the <a href=\"[LINK PRIVACY]\">privacy policy</a> and agree to my data being used to reply to my request.",
    f_invia="Prepare the message",
    f_errore="Something's missing: fill in the required fields and accept the privacy policy.",
    f_mail_richiesta="Request",
),
"fr": dict(
    nome_lingua="Français", locale="fr_FR",
    salta="Aller au contenu", menu="Menu", nav_label="Principal", lingua_label="Langue",
    barra="depuis 1954 · Peschiera del Garda",
    nav_home="Accueil", nav_forno="La boulangerie", nav_pane="Pain", nav_pasticceria="Pâtisserie",
    nav_orari="Horaires et accès", nav_contatti="Contact", ordina="Commander un gâteau",
    sotto_marchio="Boulangerie Pâtisserie",
    logo_alt="Brizzo, la miche de pain à lunettes de soleil, logo du Panificio Brizzolari",
    dal1954="depuis 1954", f_orari="Horaires", f_tutti_orari="Tous les horaires", f_contatti="Contact",
    privacy="Confidentialité", cookie="Cookies", piva="N° TVA",
    tag_appena="Tout juste sorti du four", tag_integrale="Complet", tag_novita="Nouveau",
    h_title="Panificio Pasticceria Brizzolari · Boulangerie à Peschiera del Garda depuis 1954",
    h_desc="Pains, viennoiseries et gâteaux sur commande faits maison chaque jour à Peschiera del Garda. La boulangerie familiale Brizzolari, depuis 1954.",
    hero_accento="depuis 1954, les mains dans la pâte",
    hero_sotto="Pains, gâteaux et viennoiseries faits maison chaque jour à Peschiera del Garda.",
    cta_banco="Découvrir le comptoir", cta_dove="Nous trouver",
    nastro=["Tout juste sorti du four", "Depuis 1954", "Le pain à lunettes", "Les mains dans la pâte", "Peschiera del Garda", "Gâteaux sur commande"],
    forno_h2="Une boulangerie familiale à l'esprit jeune",
    forno_p1="Nous avons allumé le four en 1954 et depuis, on ne s'est jamais arrêtés. Plus de soixante-dix ans plus tard, la pâte se fait toujours ici, chaque jour, de nos propres mains.",
    forno_p2="[DESCRIZIONE: la storia della famiglia Brizzolari e del forno]",
    val1=("Cuit chaque jour.", "Le pain du jour est vraiment du jour. [DESCRIZIONE]"),
    val2=("En famille, depuis toujours.", "[DESCRIZIONE]"),
    val3=("Sérieux sur le pain, beaucoup moins sur le reste.", "Après tout, notre pain porte des lunettes de soleil."),
    forno_accento="une histoire qui sent bon la croûte",
    forno_anno="L'année où nous avons sorti notre toute première miche du four à Peschiera del Garda.",
    bollino="depuis",
    pane_occhiello="Notre comptoir", pane_h2="Le pain de tous les jours",
    pane_p="De la miche du dimanche au petit pain du goûter. [DESCRIZIONE]",
    past_h2="Des douceurs pour le petit-déjeuner, le goûter et les excuses",
    past_p="Viennoiseries, pâtisseries et biscuits préparés dans notre atelier. [DESCRIZIONE]",
    oggi_banco="Aujourd'hui au comptoir",
    torte_occhiello="Gâteaux sur commande", torte_h2="Vous imaginez le gâteau, on s'occupe du four",
    torte_p="Anniversaires, baptêmes, fêtes de famille ou un mardi ordinaire qui mérite mieux. Dites-nous ce qu'il vous faut, on le prépare pour vous. [DESCRIZIONE: tipi di torte disponibili]",
    passo1=("Parlez-nous de la fête", "Appelez-nous, passez à la boutique ou écrivez-nous : combien de personnes, quel goût, quelle occasion."),
    passo2=("On fixe les détails", "Ensemble, on choisit le goût, la taille et la décoration. Merci de commander [PREAVVISO] à l'avance."),
    passo3=("Vous passez le chercher", "Le jour convenu, il vous attend au comptoir. Les bougies, c'est votre affaire."),
    su_ordinazione="Sur commande", torte_prezzo="Gâteaux à partir de [PREZZO] €",
    richiedi_torta="Demander un gâteau", chiama_forno="Appeler la boulangerie",
    rec_occhiello="Avis", rec_h2="Ce n'est pas nous qui le disons", rec_tutte="Lire tous les avis",
    fascia_h2="Le pain à lunettes.", vieni="Venez nous voir",
    o_title="Horaires et accès · Panificio Brizzolari, Peschiera del Garda",
    o_desc="Horaires d'ouverture et adresse du Panificio Pasticceria Brizzolari, boulangerie à Peschiera del Garda (Vérone).",
    o_h1="Le four est allumé. Voici quand.",
    o_sotto="Passez chercher votre pain chaud : on vous attend à Peschiera del Garda.",
    o_card="Horaires de la boulangerie",
    giorni=["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"],
    o_festivi="Jours fériés et fermetures :", o_dove="Où nous trouver", o_parcheggio="Accès et stationnement :",
    o_maps="Ouvrir dans Google Maps", o_mappa="Carte",
    o_mappa_testo="La carte est fournie par Google. En l'affichant, vous acceptez ses cookies.",
    o_mappa_btn="Afficher la carte", o_mappa_titolo="Carte : Panificio Pasticceria Brizzolari, Peschiera del Garda",
    c_title="Contact · Panificio Brizzolari, Peschiera del Garda",
    c_desc="Téléphone, e-mail et formulaire pour commander un gâteau ou poser une question au Panificio Pasticceria Brizzolari.",
    c_h1="Un brin de causette avec la boulangerie",
    c_sotto="Pour un gâteau, une question ou pour savoir s'il reste du pain : appelez, écrivez ou passez nous voir.",
    c_recapiti="Coordonnées",
    c_tel=("Téléphone", "Le plus rapide, pendant les heures d'ouverture.", "Appeler"),
    c_mail=("E-mail", "Pour les demandes sans urgence, les devis et les gâteaux.", "Écrivez-nous"),
    c_negozio=("En boutique", "Horaires et carte"),
    c_h2="Commandez un gâteau ou posez-nous vos questions",
    c_p1="Remplissez le formulaire : votre messagerie s'ouvrira avec le message déjà prêt, il ne vous restera qu'à l'envoyer.",
    c_p2="Les gâteaux sur commande demandent un délai de [PREAVVISO]. Nous vous rappelons pour confirmer.",
    c_accento="on répond entre deux fournées",
    f_motivo="De quoi avez-vous besoin ?", f_opzioni=("Renseignements", "Gâteau sur commande", "Autre"),
    f_nome="Nom et prénom", f_tel="Téléphone", f_email="E-mail", f_facolt="(facultatif)",
    f_data="Date de retrait", f_msg="Message", f_aiuto="Pour un gâteau : occasion, nombre de personnes, goût, inscription.",
    f_privacy="J'ai lu la <a href=\"[LINK PRIVACY]\">politique de confidentialité</a> et j'accepte le traitement de mes données pour répondre à ma demande.",
    f_invia="Préparer le message",
    f_errore="Il manque quelque chose : remplissez les champs obligatoires et acceptez la politique de confidentialité.",
    f_mail_richiesta="Demande",
),
"de": dict(
    nome_lingua="Deutsch", locale="de_DE",
    salta="Zum Inhalt springen", menu="Menü", nav_label="Hauptmenü", lingua_label="Sprache",
    barra="seit 1954 · Peschiera del Garda",
    nav_home="Start", nav_forno="Die Bäckerei", nav_pane="Brot", nav_pasticceria="Konditorei",
    nav_orari="Zeiten & Anfahrt", nav_contatti="Kontakt", ordina="Torte bestellen",
    sotto_marchio="Bäckerei Konditorei",
    logo_alt="Brizzo, das Brot mit Sonnenbrille, Logo des Panificio Brizzolari",
    dal1954="seit 1954", f_orari="Öffnungszeiten", f_tutti_orari="Alle Öffnungszeiten", f_contatti="Kontakt",
    privacy="Datenschutz", cookie="Cookies", piva="USt-IdNr.",
    tag_appena="Frisch aus dem Ofen", tag_integrale="Vollkorn", tag_novita="Neu",
    h_title="Panificio Pasticceria Brizzolari · Bäckerei in Peschiera del Garda seit 1954",
    h_desc="Brot, Gebäck und Torten auf Bestellung, jeden Tag hausgemacht in Peschiera del Garda. Die Familienbäckerei Brizzolari, seit 1954.",
    hero_accento="seit 1954 mit den Händen im Teig",
    hero_sotto="Brot, Kuchen und Gebäck, jeden Tag hausgemacht in Peschiera del Garda.",
    cta_banco="Zur Theke", cta_dove="So findest du uns",
    nastro=["Frisch aus dem Ofen", "Seit 1954", "Brot mit Sonnenbrille", "Mit den Händen im Teig", "Peschiera del Garda", "Torten auf Bestellung"],
    forno_h2="Eine Familienbäckerei mit jungem Herzen",
    forno_p1="1954 haben wir den Ofen angeheizt und seitdem nicht mehr aufgehört. Über siebzig Jahre später entsteht der Teig immer noch hier, jeden Tag, mit unseren eigenen Händen.",
    forno_p2="[DESCRIZIONE: la storia della famiglia Brizzolari e del forno]",
    val1=("Jeden Tag frisch gebacken.", "Das Brot von heute ist von heute. [DESCRIZIONE]"),
    val2=("Familienbetrieb, schon immer.", "[DESCRIZIONE]"),
    val3=("Ernst beim Brot, locker beim Rest.", "Unser Brot trägt schließlich Sonnenbrille."),
    forno_accento="eine Geschichte, die nach Kruste duftet",
    forno_anno="Das Jahr, in dem wir in Peschiera del Garda unser allererstes Brot gebacken haben.",
    bollino="seit",
    pane_occhiello="Unsere Theke", pane_h2="Brot für jeden Tag",
    pane_p="Vom Sonntagslaib bis zum Pausenbrötchen. [DESCRIZIONE]",
    past_h2="Süßes zum Frühstück, für zwischendurch und als Entschuldigung",
    past_p="Hefegebäck, Teilchen und Kekse aus unserer eigenen Backstube. [DESCRIZIONE]",
    oggi_banco="Heute an der Theke",
    torte_occhiello="Torten auf Bestellung", torte_h2="Du denkst dir die Torte aus, wir kümmern uns um den Ofen",
    torte_p="Geburtstage, Taufen, Jubiläen oder ein ganz normaler Dienstag, der mehr verdient. Sag uns, was du brauchst, und wir backen es für dich. [DESCRIZIONE: tipi di torte disponibili]",
    passo1=("Erzähl uns vom Fest", "Ruf an, komm vorbei oder schreib uns: wie viele Personen, welcher Geschmack, welcher Anlass."),
    passo2=("Wir klären die Details", "Gemeinsam wählen wir Geschmack, Größe und Deko. Bitte bestell [PREAVVISO] im Voraus."),
    passo3=("Du holst sie ab", "Am vereinbarten Tag steht sie an der Theke bereit. Um die Kerzen kümmerst du dich."),
    su_ordinazione="Auf Bestellung", torte_prezzo="Torten ab [PREZZO] €",
    richiedi_torta="Torte anfragen", chiama_forno="Bäckerei anrufen",
    rec_occhiello="Bewertungen", rec_h2="Sagen die anderen, nicht wir", rec_tutte="Alle Bewertungen lesen",
    fascia_h2="Brot mit Sonnenbrille.", vieni="Komm vorbei",
    o_title="Öffnungszeiten & Anfahrt · Panificio Brizzolari, Peschiera del Garda",
    o_desc="Öffnungszeiten und Adresse des Panificio Pasticceria Brizzolari, Bäckerei in Peschiera del Garda (Verona).",
    o_h1="Der Ofen ist an. Und zwar dann:",
    o_sotto="Hol dir dein warmes Brot ab: Wir warten in Peschiera del Garda auf dich.",
    o_card="Öffnungszeiten der Bäckerei",
    giorni=["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"],
    o_festivi="Feiertage und Betriebsferien:", o_dove="Hier findest du uns", o_parcheggio="Anfahrt und Parken:",
    o_maps="In Google Maps öffnen", o_mappa="Karte",
    o_mappa_testo="Die Karte wird von Google bereitgestellt. Wenn du sie lädst, akzeptierst du deren Cookies.",
    o_mappa_btn="Karte anzeigen", o_mappa_titolo="Karte: Panificio Pasticceria Brizzolari, Peschiera del Garda",
    c_title="Kontakt · Panificio Brizzolari, Peschiera del Garda",
    c_desc="Telefon, E-Mail und Formular, um beim Panificio Pasticceria Brizzolari eine Torte zu bestellen oder etwas zu fragen.",
    c_h1="Ein Plausch mit der Bäckerei",
    c_sotto="Für eine Torte, eine Frage oder um zu erfahren, ob noch Brot da ist: ruf an, schreib uns oder komm vorbei.",
    c_recapiti="Kontaktdaten",
    c_tel=("Telefon", "Am schnellsten, während der Öffnungszeiten.", "Anrufen"),
    c_mail=("E-Mail", "Für Anfragen ohne Eile, Angebote und Torten.", "Schreib uns"),
    c_negozio=("Im Laden", "Zeiten und Karte"),
    c_h2="Bestell eine Torte oder frag uns, was du willst",
    c_p1="Füll das Formular aus: Dein E-Mail-Programm öffnet sich mit der fertigen Nachricht, du musst nur noch auf Senden drücken.",
    c_p2="Torten bitte [PREAVVISO] im Voraus bestellen. Wir rufen dich zur Bestätigung zurück.",
    c_accento="wir antworten zwischen zwei Blechen",
    f_motivo="Was brauchst du?", f_opzioni=("Informationen", "Torte auf Bestellung", "Sonstiges"),
    f_nome="Vor- und Nachname", f_tel="Telefon", f_email="E-Mail", f_facolt="(optional)",
    f_data="Abholdatum", f_msg="Nachricht", f_aiuto="Für eine Torte: Anlass, Personenzahl, Geschmack, Aufschrift.",
    f_privacy="Ich habe die <a href=\"[LINK PRIVACY]\">Datenschutzerklärung</a> gelesen und bin mit der Verarbeitung meiner Daten zur Beantwortung meiner Anfrage einverstanden.",
    f_invia="Nachricht vorbereiten",
    f_errore="Da fehlt noch was: Füll die Pflichtfelder aus und akzeptiere die Datenschutzerklärung.",
    f_mail_richiesta="Anfrage",
),
}

# ---------------------------------------------------------------- icone (Lucide)
I = {
 "spiga": '<path d="M2 22 16 8"/><path d="M3.47 12.53 5 11l1.53 1.53a3.5 3.5 0 0 1 0 4.94L5 19l-1.53-1.53a3.5 3.5 0 0 1 0-4.94Z"/><path d="M7.47 8.53 9 7l1.53 1.53a3.5 3.5 0 0 1 0 4.94L9 15l-1.53-1.53a3.5 3.5 0 0 1 0-4.94Z"/><path d="M11.47 4.53 13 3l1.53 1.53a3.5 3.5 0 0 1 0 4.94L13 11l-1.53-1.53a3.5 3.5 0 0 1 0-4.94Z"/><path d="M20 2h2v2a4 4 0 0 1-4 4h-2V6a4 4 0 0 1 4-4Z"/><path d="M11.47 17.47 13 19l-1.53 1.53a3.5 3.5 0 0 1-4.94 0L5 19l1.53-1.53a3.5 3.5 0 0 1 4.94 0Z"/><path d="M15.47 13.47 17 15l-1.53 1.53a3.5 3.5 0 0 1-4.94 0L9 15l1.53-1.53a3.5 3.5 0 0 1 4.94 0Z"/><path d="M19.47 9.47 21 11l-1.53 1.53a3.5 3.5 0 0 1-4.94 0L13 11l1.53-1.53a3.5 3.5 0 0 1 4.94 0Z"/>',
 "cornetto": '<path d="m4.6 13.11 5.79-3.21c1.89-1.05 4.79 1.78 3.71 3.71l-3.22 5.81C8.8 23.16.79 15.23 4.6 13.11Z"/><path d="m10.5 9.5-1-2.29C9.2 6.48 8.8 6 8 6H4.5C2.79 6 2 6.5 2 8.5a7.71 7.71 0 0 0 2 4.83"/><path d="M8 6c0-1.55.24-4-2-4-2 0-2.5 2.17-2.5 4"/><path d="m14.5 13.5 2.29 1c.73.3 1.21.7 1.21 1.5v3.5c0 1.71-.5 2.5-2.5 2.5a7.71 7.71 0 0 1-4.83-2"/><path d="M18 16c1.55 0 4-.24 4 2 0 2-2.17 2.5-4 2.5"/>',
 "fetta": '<circle cx="9" cy="7" r="2"/><path d="M7.2 7.9 3 11v9c0 .6.4 1 1 1h16c.6 0 1-.4 1-1v-9c0-2-3-6-7-8l-3.6 2.6"/><path d="M16 13H3"/><path d="M16 17H3"/>',
 "torta": '<path d="M20 21v-8a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8"/><path d="M4 16s.5-1 2-1 2.5 2 4 2 2.5-2 4-2 2.5 2 4 2 2-1 2-1"/><path d="M2 21h20"/><path d="M7 8v3"/><path d="M12 8v3"/><path d="M17 8v3"/><path d="M7 4h.01"/><path d="M12 4h.01"/><path d="M17 4h.01"/>',
 "telefono": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
 "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
 "orologio": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "fiamma": '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',
 "famiglia": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 "sole": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>',
 "menu": '<path d="M4 6h16"/><path d="M4 12h16"/><path d="M4 18h16"/>',
}

def ico(n, stile=""):
    s = f' style="{stile}"' if stile else ""
    return f'<svg class="icona" viewBox="0 0 24 24" aria-hidden="true" focusable="false"{s}>{I[n]}</svg>'

FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,500;1,9..144,400;1,9..144,600&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&display=swap" rel="stylesheet">'''

def logo(dim, alt, extra=""):
    w, h = (160, 178) if dim == 160 else (640, 711)
    return (f'<picture><source srcset="/assets/brizzo-logo-{dim}.webp" type="image/webp">'
            f'<img src="/assets/brizzo-logo-{dim}.png" width="{w}" height="{h}" alt="{alt}"{extra}></picture>')

# ---------------------------------------------------------------- testata e piede
def testa(lang, pagina, title, desc, noindex=False):
    t = T[lang]
    alternate = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{url(l, pagina)}">' for l in LINGUE)
    alternate += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}{url("it", pagina)}">'
    meta_extra = '<meta name="robots" content="noindex">' if noindex else (
        f'<link rel="canonical" href="{BASE}{url(lang, pagina)}">\n{alternate}')
    lingue = "".join(
        f'<li><a href="{url(l, pagina)}" hreflang="{l}" lang="{l}" aria-label="{T[l]["nome_lingua"]}"'
        + (' aria-current="true"' if l == lang else "") + f'>{l.upper()}</a></li>'
        for l in LINGUE)
    voci = [(url(lang, "home"), t["nav_home"], pagina == "home"),
            (url(lang, "home", "#forno"), t["nav_forno"], False),
            (url(lang, "home", "#pane"), t["nav_pane"], False),
            (url(lang, "home", "#pasticceria"), t["nav_pasticceria"], False),
            (url(lang, "orari"), t["nav_orari"], pagina == "orari"),
            (url(lang, "contatti"), t["nav_contatti"], pagina == "contatti")]
    nav = "\n".join(f'        <li><a href="{h}"' + (' aria-current="page"' if c else "") + f'>{n}</a></li>' for h, n, c in voci)
    nav += f'\n        <li><a class="btn btn--oro" href="{url(lang, "contatti", "?tipo=torta#modulo")}">{t["ordina"]}</a></li>'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{meta_extra}
<meta name="theme-color" content="#FAF2DF">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{t["locale"]}">
<meta property="og:image" content="{BASE}/assets/brizzo-logo-640.png">
<link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon-48.png">
<link rel="icon" type="image/png" sizes="512x512" href="/assets/favicon-512.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
{FONTS}
<script>document.documentElement.classList.add("js")</script>
<link rel="stylesheet" href="/tokens.css">
<link rel="stylesheet" href="/css/sito.css">
<script src="/js/sito.js" defer></script>
</head>
<body>
<a class="salta" href="#contenuto">{t["salta"]}</a>

<div class="barra-alta">
  <div class="contenitore barra-alta__riga">
    <p>{t["barra"].split(" · ")[0]}<span class="solo-largo"> · {t["barra"].split(" · ")[1]}</span></p>
    <nav aria-label="{t["lingua_label"]}"><ul class="lingue">{lingue}</ul></nav>
  </div>
</div>

<header class="testata">
  <div class="contenitore testata__barra">
    <a class="marchio" href="{url(lang, "home")}">
      {logo(160, "")}
      <span><span class="marchio__nome">Brizzolari</span><span class="marchio__sotto">{t["sotto_marchio"]}</span></span>
    </a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-principale">
      {ico("menu")}<span>{t["menu"]}</span>
    </button>
    <nav class="nav" id="nav-principale" aria-label="{t["nav_label"]}">
      <ul>
{nav}
      </ul>
    </nav>
  </div>
</header>

<main id="contenuto">
'''

def piede(lang):
    t = T[lang]
    return f'''</main>

<footer class="footer sezione bordo-onda">
  <div class="contenitore">
    <div class="footer__griglia">
      <div class="logo-riquadro">
        {logo(160, t["logo_alt"])}
      </div>
      <div>
        <h2>Panificio Pasticceria Brizzolari</h2>
        <p class="accento">{t["dal1954"]}</p>
        <address class="indirizzo">[INDIRIZZO]<br>37019 Peschiera del Garda (VR)</address>
      </div>
      <div>
        <h2>{t["f_orari"]}</h2>
        <div class="card-orari__riga"><span>[GIORNI]</span><span>[ORARIO]</span></div>
        <div class="card-orari__riga"><span>[GIORNI]</span><span>[ORARIO]</span></div>
        <p style="margin-top:var(--s-3)"><a href="{url(lang, "orari")}">{t["f_tutti_orari"]}</a></p>
      </div>
      <div>
        <h2>{t["f_contatti"]}</h2>
        <ul>
          <li><a href="tel:[TELEFONO]">[TELEFONO]</a></li>
          <li><a href="mailto:[EMAIL]">[EMAIL]</a></li>
          <li><a href="[LINK INSTAGRAM]">Instagram</a></li>
          <li><a href="[LINK FACEBOOK]">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__fondo">
      <p>© <span data-anno>2026</span> Panificio Pasticceria Brizzolari · {t["piva"]} [P.IVA]</p>
      <p><a href="[LINK PRIVACY]">{t["privacy"]}</a> · <a href="[LINK COOKIE]">{t["cookie"]}</a></p>
    </div>
  </div>
</footer>

</body>
</html>
'''

def card(nome, media_bg, icona, tag=None, unita="€", extra=""):
    tg = f'\n          <span class="tag {tag[0]}">{tag[1]}</span>' if tag else ""
    return f'''      <article class="card card-prodotto {extra}" data-rivela>
        <div class="card-prodotto__media" style="background:var({media_bg})">{tg}
          {ico(icona)}
          <span class="media-nota">[FOTO]</span>
        </div>
        <div class="card-prodotto__corpo">
          <h3 class="card-prodotto__nome">{nome}</h3>
          <p style="margin:0">[DESCRIZIONE]</p>
          <span class="card-prodotto__prezzo">[PREZZO] {unita}</span>
        </div>
      </article>'''

def recensione(stile=""):
    s = f' style="{stile}"' if stile else ""
    return f'''      <figure class="card recensione"{s} data-rivela>
        <span class="recensione__virgolette" aria-hidden="true">“</span>
        <blockquote><p style="margin:0">[RECENSIONE]</p></blockquote>
        <figcaption>[NOME CLIENTE] · <span style="font-weight:400">[FONTE]</span></figcaption>
      </figure>'''

# ---------------------------------------------------------------- pagine
def home(lang):
    t = T[lang]
    torta = url(lang, "contatti", "?tipo=torta#modulo")
    nastro = "".join(f"<span>{x}</span>" for x in t["nastro"])
    vals = "\n".join(f'        <li>{ico(i)}<span><strong>{v[0]}</strong> {v[1]}</span></li>'
                     for i, v in zip(("fiamma", "famiglia", "sole"), (t["val1"], t["val2"], t["val3"])))
    passi = "\n".join(
        f'''      <li class="card passo" data-rivela{f' style="--ritardo:{i * 120}ms"' if i else ""}>
        <h3>{p[0]}</h3>
        <p>{p[1]}</p>
      </li>''' for i, p in enumerate((t["passo1"], t["passo2"], t["passo3"])))
    return testa(lang, "home", t["h_title"], t["h_desc"]) + f'''
<!-- HERO -->
<section class="sezione">
  <div class="contenitore hero">
    <div class="hero__testo">
      <p class="accento">{t["hero_accento"]}</p>
      <h1 class="display">Panificio<br>Pasticceria<br>Brizzolari</h1>
      <p class="sottotitolo">{t["hero_sotto"]}</p>
      <div class="riga">
        <a class="btn btn--primario" href="#pane">{t["cta_banco"]}</a>
        <a class="btn btn--oro" href="{torta}">{t["ordina"]}</a>
        <a class="btn btn--contorno" href="{url(lang, "orari")}">{t["cta_dove"]}</a>
      </div>
    </div>
    <div class="hero__scena">
      <div class="logo-riquadro hero__logo">
        {logo(640, t["logo_alt"], ' fetchpriority="high"')}
      </div>
      <span class="vapore vapore--1" aria-hidden="true"></span><span class="vapore vapore--2" aria-hidden="true"></span><span class="vapore vapore--3" aria-hidden="true"></span>
    </div>
  </div>
</section>

<!-- NASTRO -->
<div class="nastro" aria-hidden="true">
  <div class="nastro__binario">
    {nastro}
    {nastro}
  </div>
</div>

<!-- IL FORNO -->
<section class="sezione sezione--farina" id="forno" aria-labelledby="titolo-forno">
  <div class="contenitore due-colonne">
    <div data-rivela>
      <p class="occhiello">{t["nav_forno"]}</p>
      <h2 id="titolo-forno">{t["forno_h2"]}</h2>
      <p>{t["forno_p1"]}</p>
      <p>{t["forno_p2"]}</p>
      <ul class="valori">
{vals}
      </ul>
    </div>
    <div class="forno-scena" data-rivela style="--ritardo:120ms">
      <div class="card forno-box">
        <p class="accento">{t["forno_accento"]}</p>
        <p class="forno-numero" data-conta="1954">1954</p>
        <p class="sottotitolo" style="margin:var(--s-3) 0 0">{t["forno_anno"]}</p>
      </div>
      <span class="bollino" aria-hidden="true">{t["bollino"]}<br><strong>1954</strong></span>
    </div>
  </div>
</section>

<!-- PANE -->
<section class="sezione" id="pane" aria-labelledby="titolo-pane">
  <div class="contenitore">
    <div class="intro intro--centro" data-rivela>
      <p class="occhiello">{t["pane_occhiello"]}</p>
      <h2 id="titolo-pane">{t["pane_h2"]}</h2>
      <p>{t["pane_p"]}</p>
    </div>
    <div class="griglia griglia--sfalsata">
{card("[PRODOTTO]", "--oro", "spiga", ("tag--crosta", t["tag_appena"]), "€/kg")}
{card("[PRODOTTO]", "--salvia", "spiga", ("", t["tag_integrale"]), "€/kg")}
{card("[PRODOTTO]", "--crosta", "spiga", None, "€/kg")}
    </div>
  </div>
</section>

<!-- PASTICCERIA -->
<section class="sezione sezione--farina bordo-onda" id="pasticceria" aria-labelledby="titolo-pasticceria">
  <div class="contenitore vetrina">
    <div class="vetrina__testo" data-rivela>
      <p class="occhiello">{t["nav_pasticceria"]}</p>
      <h2 id="titolo-pasticceria">{t["past_h2"]}</h2>
      <p>{t["past_p"]}</p>
      <div class="cartellino cartellino--oscilla">
        <div>
          <span class="occhiello" style="color:var(--bruno)">{t["oggi_banco"]}</span>
          <div class="cartellino__titolo">[DOLCE DEL GIORNO]</div>
        </div>
        <span class="cartellino__prezzo">[€]</span>
      </div>
    </div>
    <div class="vetrina__lista">
{card("[PRODOTTO]", "--mattone", "cornetto", ("tag--blu", t["tag_novita"]), "€", "card-prodotto--orizzontale")}
{card("[PRODOTTO]", "--oro", "fetta", ("tag--crosta", t["tag_appena"]), "€", "card-prodotto--orizzontale")}
{card("[PRODOTTO]", "--salvia", "cornetto", None, "€", "card-prodotto--orizzontale")}
    </div>
  </div>
</section>

<!-- TORTE SU ORDINAZIONE -->
<section class="sezione sezione--blu bordo-onda torte" id="torte" aria-labelledby="titolo-torte">
  <div class="contenitore">
    <div class="intro" data-rivela>
      <p class="occhiello">{t["torte_occhiello"]}</p>
      <h2 id="titolo-torte">{t["torte_h2"]}</h2>
      <p>{t["torte_p"]}</p>
    </div>
    <ol class="passi">
{passi}
    </ol>
    <div class="torte-cta" data-rivela>
      <div class="cartellino cartellino--oscilla">
        {ico("torta")}
        <div>
          <span class="occhiello" style="color:var(--bruno)">{t["su_ordinazione"]}</span>
          <div class="cartellino__titolo">{t["torte_prezzo"]}</div>
        </div>
      </div>
      <div class="riga">
        <a class="btn btn--oro" href="{torta}">{t["richiedi_torta"]}</a>
        <a class="btn btn--chiaro" href="tel:[TELEFONO]">{t["chiama_forno"]}</a>
      </div>
    </div>
  </div>
</section>

<!-- RECENSIONI -->
<section class="sezione bordo-onda recensioni" id="recensioni" aria-labelledby="titolo-recensioni">
  <div class="contenitore">
    <div class="intro intro--centro" data-rivela>
      <p class="occhiello">{t["rec_occhiello"]}</p>
      <h2 id="titolo-recensioni">{t["rec_h2"]}</h2>
    </div>
    <div class="griglia griglia--biglietti">
{recensione("background:var(--oro)")}
{recensione("--ritardo:120ms")}
{recensione("background:var(--salvia); --ritardo:240ms")}
    </div>
    <p style="margin-top:var(--s-10); text-align:center"><a class="btn btn--contorno" href="[LINK RECENSIONI GOOGLE]">{t["rec_tutte"]}</a></p>
  </div>
</section>

<!-- FASCIA FINALE -->
<section class="sezione fascia bordo-onda">
  <div class="contenitore fascia__griglia">
    <div data-rivela>
      <p class="accento">{t["dal1954"]}</p>
      <h2 class="display">{t["fascia_h2"]}</h2>
      <a class="btn btn--primario" href="{url(lang, "orari")}">{t["vieni"]}</a>
    </div>
    <div class="fascia__brizzo logo-riquadro" aria-hidden="true">
      {logo(640, "", ' loading="lazy"')}
    </div>
  </div>
</section>
''' + piede(lang)

def testa_pagina(lang, occhiello, h1, sotto):
    return f'''
<section class="testa-pagina">
  <div class="contenitore testa-pagina__griglia">
    <div class="testa-pagina__brizzo" aria-hidden="true">{logo(160, "")}</div>
    <p class="occhiello">{occhiello}</p>
    <h1>{h1}</h1>
    <p class="sottotitolo">{sotto}</p>
  </div>
</section>
'''

MAPS_Q = "Panificio+Pasticceria+Brizzolari+Peschiera+del+Garda"

def orari(lang):
    t = T[lang]
    righe = "\n".join(f'        <div class="card-orari__riga"><dt>{g}</dt><dd>[ORARIO]</dd></div>' for g in t["giorni"])
    return testa(lang, "orari", t["o_title"], t["o_desc"]) + testa_pagina(lang, t["nav_orari"], t["o_h1"], t["o_sotto"]) + f'''
<section class="sezione sezione--farina" aria-labelledby="titolo-orari">
  <div class="contenitore dove">
    <div class="card card-orari" data-rivela>
      <h2 id="titolo-orari" style="font-size:1.875rem">{t["o_card"]}</h2>
      <dl>
{righe}
      </dl>
      <p style="margin:var(--s-4) 0 0">{t["o_festivi"]} [ORARI FESTIVI E FERIE]</p>
      <p class="accento" style="margin:var(--s-3) 0 0">Peschiera del Garda</p>
    </div>
    <div>
      <p class="occhiello">{t["o_dove"]}</p>
      <h2>{t["vieni"]}</h2>
      <ul class="info-lista">
        <li>{ico("pin")}<address class="indirizzo"><strong>Panificio Pasticceria Brizzolari</strong><br>[INDIRIZZO]<br>37019 Peschiera del Garda (VR)</address></li>
        <li>{ico("telefono")}<span><a href="tel:[TELEFONO]">[TELEFONO]</a></span></li>
        <li>{ico("orologio")}<span>{t["o_parcheggio"]} [INFO PARCHEGGIO]</span></li>
      </ul>
      <div class="riga" style="margin-top:var(--s-6)">
        <a class="btn btn--primario" href="https://www.google.com/maps/search/?api=1&amp;query={MAPS_Q}" target="_blank" rel="noopener">{t["o_maps"]}</a>
        <a class="btn btn--contorno" href="{url(lang, "contatti")}">{t["nav_contatti"]}</a>
      </div>
    </div>
  </div>
</section>

<section class="sezione" aria-labelledby="titolo-mappa">
  <div class="contenitore">
    <h2 id="titolo-mappa" class="visivamente-nascosto">{t["o_mappa"]}</h2>
    <div class="mappa" data-mappa="https://www.google.com/maps?q={MAPS_Q}&amp;hl={lang}&amp;output=embed" data-titolo="{t["o_mappa_titolo"]}">
      <div style="height:100%; display:grid; place-items:center; text-align:center; padding:var(--s-6)">
        <div>
          {ico("pin", "width:56px;height:56px")}
          <p style="margin:var(--s-3) 0 var(--s-4); max-width:420px">{t["o_mappa_testo"]}</p>
          <button class="btn btn--oro" type="button" data-carica-mappa>{t["o_mappa_btn"]}</button>
        </div>
      </div>
    </div>
  </div>
</section>
''' + piede(lang)

def contatti(lang):
    t = T[lang]
    testi_js = json.dumps({
        "errore": t["f_errore"], "richiesta": t["f_mail_richiesta"], "nome": t["f_nome"],
        "telefono": t["f_tel"], "email": t["f_email"], "data": t["f_data"], "lingua": lang.upper(),
    }, ensure_ascii=False).replace('"', "&quot;")
    op = t["f_opzioni"]
    return testa(lang, "contatti", t["c_title"], t["c_desc"]) + testa_pagina(lang, t["nav_contatti"], t["c_h1"], t["c_sotto"]) + f'''
<section class="sezione sezione--farina" style="padding-top:clamp(40px,6vw,64px)" aria-label="{t["c_recapiti"]}">
  <div class="contenitore griglia">
    <article class="card contatto" data-rivela>
      <span class="contatto__icona" style="background:var(--oro)">{ico("telefono")}</span>
      <h2>{t["c_tel"][0]}</h2>
      <p>{t["c_tel"][1]}</p>
      <p><strong>[TELEFONO]</strong></p>
      <a class="btn btn--primario" href="tel:[TELEFONO]">{t["c_tel"][2]}</a>
    </article>
    <article class="card contatto" data-rivela>
      <span class="contatto__icona" style="background:var(--salvia)">{ico("mail")}</span>
      <h2>{t["c_mail"][0]}</h2>
      <p>{t["c_mail"][1]}</p>
      <p><strong>[EMAIL]</strong></p>
      <a class="btn btn--primario" href="mailto:[EMAIL]">{t["c_mail"][2]}</a>
    </article>
    <article class="card contatto" data-rivela>
      <span class="contatto__icona" style="background:var(--crosta)">{ico("pin")}</span>
      <h2>{t["c_negozio"][0]}</h2>
      <p>[INDIRIZZO]<br>37019 Peschiera del Garda (VR)</p>
      <a class="btn btn--contorno" href="{url(lang, "orari")}">{t["c_negozio"][1]}</a>
    </article>
  </div>
</section>

<section class="sezione" id="modulo" aria-labelledby="titolo-modulo">
  <div class="contenitore due-colonne" style="align-items:start">
    <div>
      <p class="occhiello">{t["c_mail"][2]}</p>
      <h2 id="titolo-modulo">{t["c_h2"]}</h2>
      <p>{t["c_p1"]}</p>
      <p>{t["c_p2"]}</p>
      <p class="accento" style="margin-top:var(--s-6)">{t["c_accento"]}</p>
    </div>
    <form class="card modulo" data-rivela id="modulo-contatti" data-email="[EMAIL]" data-testi="{testi_js}" novalidate>
      <div class="campo">
        <label for="f-motivo">{t["f_motivo"]}</label>
        <select id="f-motivo" name="motivo">
          <option value="info">{op[0]}</option>
          <option value="torta">{op[1]}</option>
          <option value="altro">{op[2]}</option>
        </select>
      </div>
      <div class="modulo__riga">
        <div class="campo">
          <label for="f-nome">{t["f_nome"]}</label>
          <input id="f-nome" name="nome" type="text" autocomplete="name" required>
        </div>
        <div class="campo">
          <label for="f-telefono">{t["f_tel"]}</label>
          <input id="f-telefono" name="telefono" type="tel" autocomplete="tel" required>
        </div>
      </div>
      <div class="modulo__riga">
        <div class="campo">
          <label for="f-email">{t["f_email"]} <span class="aiuto">{t["f_facolt"]}</span></label>
          <input id="f-email" name="email" type="email" autocomplete="email">
        </div>
        <div class="campo" data-solo-torta>
          <label for="f-data">{t["f_data"]}</label>
          <input id="f-data" name="data" type="date">
        </div>
      </div>
      <div class="campo">
        <label for="f-messaggio">{t["f_msg"]}</label>
        <span class="aiuto" id="f-messaggio-aiuto" data-solo-torta>{t["f_aiuto"]}</span>
        <textarea id="f-messaggio" name="messaggio" aria-describedby="f-messaggio-aiuto" required></textarea>
      </div>
      <div class="campo">
        <label style="display:flex; gap:var(--s-3); align-items:flex-start; font-weight:400">
          <input type="checkbox" name="privacy" required style="width:20px; min-height:20px; margin-top:4px; flex:none">
          <span>{t["f_privacy"]}</span>
        </label>
      </div>
      <p class="modulo__nota" role="alert" data-errore hidden></p>
      <button class="btn btn--primario" type="submit" style="justify-self:start">{t["f_invia"]}</button>
    </form>
  </div>
</section>
''' + piede(lang)

def pagina_404():
    t = T["it"]
    altre = " · ".join(f'<a href="{url(l, "home")}" lang="{l}">{T[l]["nome_lingua"]}</a>' for l in LINGUE[1:])
    return testa("it", "home", "Pagina non trovata · Panificio Brizzolari",
                 "La pagina cercata non esiste. Torna alla home del Panificio Pasticceria Brizzolari.", noindex=True) + f'''
<section class="sezione">
  <div class="contenitore" style="text-align:center">
    <p class="occhiello">Errore 404</p>
    <h1>Questa pagina è finita come il pane alle sette di sera.</h1>
    <p class="sottotitolo" style="max-width:560px; margin:0 auto var(--s-8)">Non la troviamo più. Il resto del banco però è ancora tutto lì.</p>
    <div class="riga" style="justify-content:center">
      <a class="btn btn--primario" href="/">Torna alla home</a>
      <a class="btn btn--contorno" href="{url("it", "orari")}">{t["nav_orari"]}</a>
    </div>
    <p style="margin-top:var(--s-8)">Page not found · Page introuvable · Seite nicht gefunden: {altre}</p>
  </div>
</section>
''' + piede("it")

def main():
    scritti = []
    for lang in LINGUE:
        for nome, fn in (("home", home), ("orari", orari), ("contatti", contatti)):
            f = ROOT / PAGINE[lang][nome][1]
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(fn(lang), encoding="utf-8")
            scritti.append(str(f.relative_to(ROOT)))
    (ROOT / "404.html").write_text(pagina_404(), encoding="utf-8")
    scritti.append("404.html")
    print("Generate:", ", ".join(scritti))

if __name__ == "__main__":
    main()
