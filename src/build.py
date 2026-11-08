#!/usr/bin/env python3
"""Builds the three language versions of the one-page site.

Run from anywhere:  python3 src/build.py
Writes:  index.html (es), va/index.html (Valencian), en/index.html (English),
         sitemap.xml and robots.txt in the repo root.

To change wording, edit STRINGS below and rebuild. To change layout or
styling, edit TEMPLATE / CSS. Contact details live in CONFIG (in the JS block
of TEMPLATE) and apply to all three languages.
"""
import html
import json
import os
from string import Template

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://set0panda.github.io/SEOCastellon/"  # change if a custom domain is used

# code, html lang, folder, label shown in switcher, full name, og:locale
LANGS = [
    ("es", "es", "", "ES", "Castellano", "es_ES"),
    ("va", "ca-valencia", "va/", "VAL", "Valencià", "ca_ES"),
    ("en", "en", "en/", "EN", "English", "en_GB"),
]

STRINGS = {
    # ------------------------------------------------------------------ ES
    "es": {
        "title": "Tu ficha de Google, bien hecha | Negocios de Castellón",
        "desc": "Arreglo la ficha de Google de tu negocio en Castellón en 48 horas: horarios, reseñas, contacto por WhatsApp y reservas. Precio cerrado y sin permanencia. Empieza con un test gratuito de 2 minutos.",
        "og_title": "Tu ficha de Google, bien hecha",
        "og_desc": "Test gratuito de 2 minutos y arreglo en 48 horas para negocios de Castellón.",
        "brand": "Ficha de Google",
        "brand_place": "· Castellón",
        "hdr_book": "Reservar 15 min",
        "hdr_wa": "WhatsApp",
        "hdr_default": "Hablemos",
        "lang_label": "Idioma",
        "eyebrow": "Para negocios de Castellón",
        "h1": "Que tus clientes te encuentren y te contacten desde Google.",
        "lead": "Arreglo la ficha de Google de tu negocio en 48 horas: horarios, reseñas, contacto por WhatsApp y reservas. Precio cerrado y sin permanencia.",
        "cta_test": "Hacer el test de 2 minutos",
        "cta_prices": "Ver precios",
        "facts": ["Hecho en 48 horas", "Sin permanencia", "Nunca necesito tu contraseña", "Redactado con IA, revisado por mí"],
        "leaks_h2": "Tres fugas que veo una y otra vez",
        "leaks_p": "Muchos clientes miran tu ficha de Google antes de llamarte o de venir. Si algo falla ahí, lo notas en el negocio y no sabes por qué.",
        "leaks": [
            ("Horario incorrecto", "Festivos sin poner o horarios antiguos. El cliente llega y está cerrado, o no viene porque cree que lo está."),
            ("Reseñas sin responder", "Una respuesta amable y cuidada a una reseña dice mucho de un negocio a quien la lee, incluso si la reseña es mala."),
            ("Sin forma fácil de contactar", "Si reservar o escribir por WhatsApp cuesta más de un toque, una parte de los clientes se rinde."),
        ],
        "prices_h2": "Qué hago y cuánto cuesta",
        "prices_p": "Precios en euros, claros desde el principio.",
        "tiers": [
            {"tag": "Para empezar", "name": "Prueba piloto", "price": "99 €", "small": "una vez", "feat": False,
             "items": ["Limpio y completo tu ficha: horarios, categorías, descripción", "Enlace de contacto o reserva", "Lista de fotos que conviene subir", "5 respuestas a reseñas redactadas"]},
            {"tag": "Más completo", "name": "Plan mensual", "price": "199 €", "small": "de alta + 35 €/mes", "feat": True,
             "items": ["Todo lo de la prueba piloto", "WhatsApp Business: saludo, mensaje de ausencia y respuestas rápidas", "Respuesta a tus reseñas cada mes", "2 publicaciones al mes en tu ficha"]},
            {"tag": "Hostelería", "name": "Plan mensual + carta", "price": "A medida", "small": "según tu carta", "feat": False,
             "items": ["Todo lo del plan mensual", "Carta revisada o creada en español, inglés y alemán", "Textos claros y sin errores"]},
        ],
        "prices_note": "No hago publicidad, páginas web ni gestión completa de redes sociales. Y no prometo posiciones ni un número de clientes nuevos: arreglo lo que depende de tu ficha.",
        "how_h2": "Cómo funciona",
        "steps": [
            ("Hablamos 15 minutos", "Gratis. Reviso tu ficha contigo y te enseño qué arreglaría primero."),
            ("Me das acceso, sin contraseña", "Me añades como gestor de tu ficha desde tu correo. Tú sigues siendo el propietario."),
            ("Listo en 48 horas", "Te envío capturas de antes y después, y tú decides si quieres que lo mantenga cada mes."),
        ],
        "test_h2": "Test de 2 minutos: ¿te está haciendo perder clientes tu ficha?",
        "test_p": "Abre Google Maps, busca tu negocio y marca lo que ya cumples.",
        "checks": [
            "Tu ficha aparece como tuya (sin el enlace «¿Eres el propietario?»)",
            "La categoría principal es la correcta",
            "El horario está completo, incluidos los festivos",
            "Un cliente puede llamarte, escribirte por WhatsApp o reservar desde la ficha",
            "Tienes web o un enlace de reserva",
            "Hay una descripción clara de tu negocio",
            "Tienes 10 fotos o más, alguna de los últimos 6 meses",
            "Has respondido a 8 de tus últimas 10 reseñas",
            "Tu carta o tus servicios aparecen en la ficha",
            "Has publicado algo en los últimos 60 días",
        ],
        "msg_prompt": "Marca lo que ya cumples para ver tu resultado.",
        "msg_low": "Es probable que haya clientes que no te encuentran o no te contactan. Hay mucho margen de mejora y casi todo se arregla rápido.",
        "msg_mid": "Tienes una buena base y fugas fáciles de arreglar.",
        "msg_high": "Vas bien. Te ayudo a mantenerlo al día.",
        "test_book": "Reservar mis 15 minutos gratis",
        "test_wa": "Escribirme por WhatsApp",
        "test_note": "Todo se calcula en tu móvil; esta página no guarda ni envía nada.",
        "faq_h2": "Preguntas frecuentes",
        "faq": [
            ("¿Necesitas mi contraseña de Google?", "No. Me añades como gestor desde la configuración de tu ficha, con tu correo. Puedes quitarme cuando quieras."),
            ("¿Hay permanencia?", "No. La prueba piloto es un pago único. El plan mensual lo puedes dejar cuando quieras."),
            ("¿Me aseguras más clientes?", "No, y desconfía de quien lo haga. Me ocupo de que lo que ven tus clientes sea correcto y de que contactarte sea fácil."),
            ("¿Y si tengo reseñas malas?", "Las respondo con un tono profesional y amable. No compro ni invento reseñas, y no puedo borrar las reales."),
            ("¿Haces páginas web?", "De momento no. Me centro en la ficha de Google, el contacto por WhatsApp y las cartas de hostelería."),
            ("¿Usas inteligencia artificial?", "Sí, para redactar borradores más rápido: textos, respuestas a reseñas y traducciones. Lo reviso todo yo antes de publicarlo y lo adapto a tu negocio."),
        ],
        "about_h2": "Quién está detrás",
        "about_p": "Soy Sherbaz y vivo en Castellón. Hablo español, inglés y alemán, y trabajo con negocios pequeños de aquí. Si me escribes, hablas conmigo directamente.",
        "contact_h2": "Empieza con 15 minutos gratis",
        "contact_p": "Te enseño qué arreglaría primero en tu ficha, sin compromiso.",
        "contact_book": "Reservar 15 minutos",
        "contact_wa": "Escribir por WhatsApp",
        "soon": "Contacto disponible muy pronto.",
        "footer": "Hecho en Castellón por",
        "wa_generic": "Hola {name}, he visto tu web y me gustaría la revisión gratuita de 15 minutos.",
        "wa_score": "Hola {name}, he hecho el test de la ficha de Google y he sacado {score}/10. Me gustaría la revisión gratuita de 15 minutos.",
    },
    # ------------------------------------------------------------------ VA
    "va": {
        "title": "La teua fitxa de Google, ben feta | Negocis de Castelló",
        "desc": "Arregle la fitxa de Google del teu negoci a Castelló en 48 hores: horaris, ressenyes, contacte per WhatsApp i reserves. Preu tancat i sense permanència. Comença amb un test gratuït de 2 minuts.",
        "og_title": "La teua fitxa de Google, ben feta",
        "og_desc": "Test gratuït de 2 minuts i arranjament en 48 hores per a negocis de Castelló.",
        "brand": "Fitxa de Google",
        "brand_place": "· Castelló",
        "hdr_book": "Reservar 15 min",
        "hdr_wa": "WhatsApp",
        "hdr_default": "Parlem",
        "lang_label": "Idioma",
        "eyebrow": "Per a negocis de Castelló",
        "h1": "Que els teus clients et troben i et contacten des de Google.",
        "lead": "Arregle la fitxa de Google del teu negoci en 48 hores: horaris, ressenyes, contacte per WhatsApp i reserves. Preu tancat i sense permanència.",
        "cta_test": "Fer el test de 2 minuts",
        "cta_prices": "Vore els preus",
        "facts": ["Fet en 48 hores", "Sense permanència", "Mai no necessite la teua contrasenya", "Redactat amb IA, revisat per mi"],
        "leaks_h2": "Tres fugues que veig una vegada i una altra",
        "leaks_p": "Molts clients miren la teua fitxa de Google abans de telefonar-te o de vindre. Si alguna cosa falla a la fitxa, ho notes al negoci i no saps per què.",
        "leaks": [
            ("Horari incorrecte", "Festius sense posar o horaris antics. El client arriba i està tancat, o no ve perquè pensa que ho està."),
            ("Ressenyes sense respondre", "Una resposta amable i cuidada a una ressenya diu molt d'un negoci a qui la llig, fins i tot si la ressenya és negativa."),
            ("Sense una manera fàcil de contactar", "Si reservar o escriure per WhatsApp costa més d'un toc, una part dels clients es rendix."),
        ],
        "prices_h2": "Què faig i quant costa",
        "prices_p": "Preus en euros, clars des del principi.",
        "tiers": [
            {"tag": "Per a començar", "name": "Prova pilot", "price": "99 €", "small": "una vegada", "feat": False,
             "items": ["Netege i complete la teua fitxa: horaris, categories, descripció", "Enllaç de contacte o de reserva", "Llista de fotos que convé pujar", "5 respostes a ressenyes redactades"]},
            {"tag": "Més complet", "name": "Pla mensual", "price": "199 €", "small": "d'alta + 35 €/mes", "feat": True,
             "items": ["Tot el de la prova pilot", "WhatsApp Business: salutació, missatge d'absència i respostes ràpides", "Resposta a les teues ressenyes cada mes", "2 publicacions al mes a la teua fitxa"]},
            {"tag": "Hostaleria", "name": "Pla mensual + carta", "price": "A mesura", "small": "segons la teua carta", "feat": False,
             "items": ["Tot el del pla mensual", "Carta revisada o creada en castellà, anglés i alemany", "Textos clars i sense errors"]},
        ],
        "prices_note": "No faig publicitat, pàgines web ni gestió completa de xarxes socials. I no promet posicions ni un nombre de clients nous: arregle el que depén de la teua fitxa.",
        "how_h2": "Com funciona",
        "steps": [
            ("Parlem 15 minuts", "Gratis. Revise la teua fitxa amb tu i t'ensenye què arreglaria primer."),
            ("Em dones accés, sense contrasenya", "M'afigs com a gestor de la teua fitxa des del teu correu. Tu continues sent el propietari."),
            ("Llest en 48 hores", "T'envie captures d'abans i després, i tu decidixes si vols que ho mantinga cada mes."),
        ],
        "test_h2": "Test de 2 minuts: la teua fitxa et fa perdre clients?",
        "test_p": "Obri Google Maps, busca el teu negoci i marca el que ja complixes.",
        "checks": [
            "La teua fitxa apareix com a teua (sense l'enllaç «Ets el propietari?»)",
            "La categoria principal és la correcta",
            "L'horari està complet, inclosos els festius",
            "Un client pot telefonar-te, escriure't per WhatsApp o reservar des de la fitxa",
            "Tens web o un enllaç de reserva",
            "Hi ha una descripció clara del teu negoci",
            "Tens 10 fotos o més, alguna dels últims 6 mesos",
            "Has respost a 8 de les teues últimes 10 ressenyes",
            "La teua carta o els teus serveis apareixen a la fitxa",
            "Has publicat alguna cosa en els últims 60 dies",
        ],
        "msg_prompt": "Marca el que ja complixes per a vore el teu resultat.",
        "msg_low": "És probable que hi haja clients que no et troben o no et contacten. Hi ha molt de marge de millora i quasi tot s'arregla ràpid.",
        "msg_mid": "Tens una bona base i fugues fàcils d'arreglar.",
        "msg_high": "Vas bé. T'ajude a mantindre-ho al dia.",
        "test_book": "Reservar els meus 15 minuts gratis",
        "test_wa": "Escriure'm per WhatsApp",
        "test_note": "Tot es calcula al teu mòbil; esta pàgina no guarda ni envia res.",
        "faq_h2": "Preguntes freqüents",
        "faq": [
            ("Necessites la meua contrasenya de Google?", "No. M'afigs com a gestor des de la configuració de la teua fitxa, amb el teu correu. Pots llevar-me quan vulgues."),
            ("Hi ha permanència?", "No. La prova pilot és un pagament únic. El pla mensual el pots deixar quan vulgues."),
            ("M'assegures més clients?", "No, i desconfia de qui ho faça. M'ocupe que el que veuen els teus clients siga correcte i que contactar-te siga fàcil."),
            ("I si tinc ressenyes negatives?", "Les responc amb un to professional i amable. No compre ni m'invente ressenyes, i no puc esborrar les reals."),
            ("Fas pàgines web?", "De moment no. Em centre en la fitxa de Google, el contacte per WhatsApp i les cartes d'hostaleria."),
            ("Utilitzes intel·ligència artificial?", "Sí, per a redactar esborranys més ràpid: textos, respostes a ressenyes i traduccions. Ho revise tot jo abans de publicar-ho i ho adapte al teu negoci."),
        ],
        "about_h2": "Qui hi ha darrere",
        "about_p": "Sóc Sherbaz i visc a Castelló. Parle castellà, anglés i alemany, i treballe amb negocis xicotets d'ací. Si m'escrius, parles amb mi directament.",
        "contact_h2": "Comença amb 15 minuts gratis",
        "contact_p": "T'ensenye què arreglaria primer a la teua fitxa, sense compromís.",
        "contact_book": "Reservar 15 minuts",
        "contact_wa": "Escriure per WhatsApp",
        "soon": "Contacte disponible molt prompte.",
        "footer": "Fet a Castelló per",
        "wa_generic": "Hola {name}, he vist la teua web i voldria la revisió gratuïta de 15 minuts.",
        "wa_score": "Hola {name}, he fet el test de la fitxa de Google i he tret {score}/10. Voldria la revisió gratuïta de 15 minuts.",
    },
    # ------------------------------------------------------------------ EN
    "en": {
        "title": "Your Google profile, done properly | Castellón businesses",
        "desc": "I fix your business's Google profile in Castellón within 48 hours: opening hours, reviews, WhatsApp contact and bookings. Fixed price, no lock-in. Start with a free 2-minute test.",
        "og_title": "Your Google profile, done properly",
        "og_desc": "Free 2-minute test and a 48-hour fix for businesses in Castellón.",
        "brand": "Google Profile",
        "brand_place": "· Castellón",
        "hdr_book": "Book 15 min",
        "hdr_wa": "WhatsApp",
        "hdr_default": "Let's talk",
        "lang_label": "Language",
        "eyebrow": "For businesses in Castellón",
        "h1": "Help customers find you and contact you from Google.",
        "lead": "I fix your business's Google profile in 48 hours: opening hours, reviews, WhatsApp contact and bookings. Fixed price, no lock-in.",
        "cta_test": "Take the 2-minute test",
        "cta_prices": "See prices",
        "facts": ["Done in 48 hours", "No lock-in", "I never need your password", "Drafted with AI, checked by me"],
        "leaks_h2": "Three leaks I see again and again",
        "leaks_p": "Many customers look at your Google profile before they call or visit. If something is wrong there, you feel it in the business and don't know why.",
        "leaks": [
            ("Wrong opening hours", "Holiday hours missing or out of date. Customers turn up to a closed door, or stay away because they think you're shut."),
            ("Unanswered reviews", "A friendly, careful reply tells whoever reads it a lot about your business, even when the review is a bad one."),
            ("No easy way to get in touch", "If booking or messaging on WhatsApp takes more than a tap, some customers give up."),
        ],
        "prices_h2": "What I do and what it costs",
        "prices_p": "Prices in euros, clear from the start.",
        "tiers": [
            {"tag": "To get started", "name": "Pilot", "price": "€99", "small": "one-off", "feat": False,
             "items": ["I clean up and complete your profile: hours, categories, description", "A contact or booking link", "A list of photos worth uploading", "5 review replies written for you"]},
            {"tag": "More complete", "name": "Monthly plan", "price": "€199", "small": "set-up + €35/month", "feat": True,
             "items": ["Everything in the pilot", "WhatsApp Business: greeting, away message and quick replies", "Replies to your reviews every month", "2 posts a month on your profile"]},
            {"tag": "Hospitality", "name": "Monthly plan + menu", "price": "Quoted", "small": "depending on your menu", "feat": False,
             "items": ["Everything in the monthly plan", "Menu proofread or created in Spanish, English and German", "Clear, error-free text"]},
        ],
        "prices_note": "I don't do advertising, websites or full social media management. And I don't promise rankings or a number of new customers: I fix what's within your profile's control.",
        "how_h2": "How it works",
        "steps": [
            ("We talk for 15 minutes", "Free. I go through your profile with you and show you what I'd fix first."),
            ("You give me access, not your password", "You add me as a manager of your profile using your email. You stay the owner."),
            ("Done in 48 hours", "I send you before-and-after screenshots, and you decide whether you want me to maintain it each month."),
        ],
        "test_h2": "2-minute test: is your profile costing you customers?",
        "test_p": "Open Google Maps, search for your business and tick what you already have.",
        "checks": [
            "Your profile shows as yours (no “Own this business?” link)",
            "The main category is correct",
            "Opening hours are complete, including holidays",
            "A customer can call you, message you on WhatsApp or book from the profile",
            "You have a website or a booking link",
            "There is a clear description of your business",
            "You have 10 or more photos, some from the last 6 months",
            "You've replied to 8 of your last 10 reviews",
            "Your menu or services are listed on the profile",
            "You've posted something in the last 60 days",
        ],
        "msg_prompt": "Tick what you already have to see your result.",
        "msg_low": "There are probably customers who can't find you or can't reach you. There's plenty of room to improve and most of it is quick to fix.",
        "msg_mid": "You have a solid base and some easy leaks to fix.",
        "msg_high": "You're doing well. I can help you keep it up to date.",
        "test_book": "Book my free 15 minutes",
        "test_wa": "Message me on WhatsApp",
        "test_note": "Everything is calculated on your phone; this page doesn't save or send anything.",
        "faq_h2": "Frequently asked questions",
        "faq": [
            ("Do you need my Google password?", "No. You add me as a manager from your profile's settings, using your email. You can remove me at any time."),
            ("Is there a contract?", "No. The pilot is a one-off payment. You can stop the monthly plan whenever you like."),
            ("Do you guarantee more customers?", "No, and be wary of anyone who does. I make sure what your customers see is correct and that getting in touch is easy."),
            ("What about bad reviews?", "I reply in a professional, friendly tone. I don't buy or invent reviews, and I can't delete genuine ones."),
            ("Do you build websites?", "Not for now. I focus on the Google profile, WhatsApp contact and hospitality menus."),
            ("Do you use artificial intelligence?", "Yes, to draft faster: texts, review replies and translations. I check everything myself before it goes live and adapt it to your business."),
        ],
        "about_h2": "Who's behind this",
        "about_p": "I'm Sherbaz and I live in Castellón. I speak Spanish, English and German, and I work with small local businesses. If you message me, you're talking to me directly.",
        "contact_h2": "Start with 15 free minutes",
        "contact_p": "I'll show you what I'd fix first on your profile, no strings attached.",
        "contact_book": "Book 15 minutes",
        "contact_wa": "Message on WhatsApp",
        "soon": "Contact details coming very soon.",
        "footer": "Made in Castellón by",
        "wa_generic": "Hi {name}, I saw your website and I'd like the free 15-minute review.",
        "wa_score": "Hi {name}, I took the Google profile test and scored {score}/10. I'd like the free 15-minute review.",
    },
}

CSS = """
  :root{
    --bg:#faf8f4; --paper:#fff; --ink:#1d2330; --muted:#586072; --line:#e3dfd6;
    --accent:#c2410c; --accent-d:#9a3412; --soft:#fdf0e8; --ok:#166534;
    --serif:Georgia,"Iowan Old Style","Palatino Linotype",serif;
    --sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  }
  *{box-sizing:border-box}
  [hidden]{display:none !important}
  html{scroll-behavior:smooth}
  body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 var(--sans)}
  .wrap{max-width:980px;margin:0 auto;padding:0 20px}
  section{padding:56px 0}
  h1,h2,h3{font-family:var(--serif);line-height:1.15;margin:0 0 14px;letter-spacing:-.01em}
  h1{font-size:clamp(2rem,6vw,3.2rem)}
  h2{font-size:clamp(1.55rem,4vw,2.1rem)}
  h3{font-size:1.2rem}
  p{margin:0 0 14px}
  .muted{color:var(--muted)}
  .eyebrow{font:600 .8rem/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin-bottom:14px}

  header{border-bottom:1px solid var(--line);background:var(--bg);position:sticky;top:0;z-index:5}
  .bar{display:flex;align-items:center;gap:12px;height:60px}
  .brand{font:700 1.05rem var(--serif);text-decoration:none;color:var(--ink);white-space:nowrap}
  .brand span{color:var(--accent)}
  .lang{display:flex;gap:2px;margin-left:auto}
  .lang a{padding:6px 9px;border-radius:8px;text-decoration:none;color:var(--muted);font:600 .82rem var(--sans)}
  .lang a:hover{color:var(--ink)}
  .lang a[aria-current="true"]{background:var(--soft);color:var(--accent-d)}

  .btn{display:inline-block;text-decoration:none;font-weight:600;border-radius:10px;padding:13px 20px;
    border:1px solid transparent;cursor:pointer;font-size:1rem;font-family:var(--sans)}
  .btn.primary{background:var(--accent);color:#fff}
  .btn.primary:hover{background:var(--accent-d)}
  .btn.ghost{background:#fff;color:var(--ink);border-color:var(--line)}
  .btn.ghost:hover{border-color:#bdb7a8}
  .btn.small{padding:9px 14px;font-size:.92rem;white-space:nowrap}
  .btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
  [data-cta]{display:none}
  [data-cta].on{display:inline-block}

  .hero{padding:64px 0 48px}
  .hero p.lead{font-size:1.2rem;max-width:34em;color:var(--muted)}
  .facts{display:flex;flex-wrap:wrap;gap:8px 22px;margin-top:26px;padding:0;list-style:none;font-size:.95rem}
  .facts li::before{content:"✓ ";color:var(--ok);font-weight:700}

  .grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
  .card{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:22px}
  .card h3{margin-bottom:8px}
  .card p{margin:0;color:var(--muted);font-size:.98rem}

  .price{font:700 1.9rem var(--serif);margin:4px 0 2px}
  .price small{font:500 .95rem var(--sans);color:var(--muted)}
  .card ul{margin:14px 0 0;padding-left:18px;color:var(--muted);font-size:.95rem}
  .card li{margin-bottom:6px}
  .card.feat{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent) inset}
  .tag{display:inline-block;font:600 .72rem var(--sans);letter-spacing:.08em;text-transform:uppercase;
    background:var(--soft);color:var(--accent-d);padding:4px 9px;border-radius:99px;margin-bottom:10px}
  .note{font-size:.92rem;color:var(--muted);margin-top:18px}

  .steps{counter-reset:s;list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
  .steps li{counter-increment:s;background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:22px}
  .steps li::before{content:counter(s);display:grid;place-items:center;width:34px;height:34px;border-radius:50%;
    background:var(--soft);color:var(--accent-d);font:700 1rem var(--serif);margin-bottom:12px}
  .steps h3{margin-bottom:6px}
  .steps p{margin:0;color:var(--muted);font-size:.98rem}

  #test{background:var(--soft);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
  .test-box{max-width:640px}
  ol.checks{list-style:none;padding:0;margin:20px 0;counter-reset:q}
  ol.checks li{counter-increment:q}
  .checks label{display:flex;gap:12px;align-items:flex-start;background:var(--paper);border:1px solid var(--line);
    border-radius:10px;padding:13px 14px;margin-bottom:10px;cursor:pointer}
  .checks label:hover{border-color:#c9c3b6}
  .checks .t::before{content:counter(q) ". ";color:var(--muted)}
  .checks input{width:22px;height:22px;margin-top:2px;flex:none;accent-color:var(--accent)}
  .checks label:has(input:checked){border-color:var(--ok);background:#f2f9f4}
  .result{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:20px}
  .score{font:700 2.4rem/1 var(--serif)}
  .score small{font:500 1rem var(--sans);color:var(--muted)}
  .msg{margin:10px 0 0}

  details{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin-bottom:10px}
  summary{font-weight:600;cursor:pointer}
  details p{margin:10px 0 0;color:var(--muted)}

  .about{max-width:640px}
  .contact{background:var(--ink);color:#fff;border-radius:18px;padding:36px 28px;text-align:center}
  .contact h2{color:#fff}
  .contact p{color:#cfd3dc}
  .contact .btns{justify-content:center}
  .contact .btn.ghost{background:transparent;color:#fff;border-color:#59627a}
  .soon{font-size:.95rem}
  footer{padding:30px 0 50px;color:var(--muted);font-size:.88rem;border-top:1px solid var(--line)}

  :focus-visible{outline:3px solid #1d4ed8;outline-offset:2px}
  @media (max-width:760px){
    .grid3,.steps{grid-template-columns:1fr}
    section{padding:44px 0}
    .hero{padding:44px 0 36px}
  }
  @media (max-width:520px){
    .brand span{display:none}
    #hdrcta{display:none !important}
  }
"""

TEMPLATE = Template("""<!DOCTYPE html>
<html lang="$htmllang">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title</title>
<meta name="description" content="$desc">
<link rel="canonical" href="$canonical">
<link rel="icon" href="$icon_href" type="image/svg+xml">
<link rel="apple-touch-icon" href="$apple_href">
$alternates
<meta property="og:title" content="$og_title">
<meta property="og:description" content="$og_desc">
<meta property="og:type" content="website">
<meta property="og:url" content="$canonical">
<meta property="og:locale" content="$og_locale">
<meta property="og:image" content="$og_image">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="$og_alt">
<meta name="twitter:card" content="summary_large_image">
<style>$css</style>
</head>
<body>

<header>
  <div class="wrap bar">
    <a class="brand" href="#">$brand <span>$brand_place</span></a>
    <nav class="lang" aria-label="$lang_label">$switcher</nav>
    <a class="btn primary small" id="hdrcta" href="#" hidden>$hdr_default</a>
  </div>
</header>

<main>
  <section class="hero">
    <div class="wrap">
      <p class="eyebrow">$eyebrow</p>
      <h1>$h1</h1>
      <p class="lead">$lead</p>
      <div class="btns">
        <a class="btn primary" href="#test">$cta_test</a>
        <a class="btn ghost" href="#precios">$cta_prices</a>
      </div>
      <ul class="facts">$facts</ul>
    </div>
  </section>

  <section id="fugas">
    <div class="wrap">
      <h2>$leaks_h2</h2>
      <p class="muted" style="max-width:40em">$leaks_p</p>
      <div class="grid3" style="margin-top:24px">$leaks</div>
    </div>
  </section>

  <section id="precios" style="padding-top:8px">
    <div class="wrap">
      <h2>$prices_h2</h2>
      <p class="muted">$prices_p</p>
      <div class="grid3" style="margin-top:24px">$tiers</div>
      <p class="note">$prices_note</p>
    </div>
  </section>

  <section id="como" style="padding-top:8px">
    <div class="wrap">
      <h2>$how_h2</h2>
      <ol class="steps" style="margin-top:22px">$steps</ol>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <div class="test-box">
        <h2>$test_h2</h2>
        <p class="muted">$test_p</p>
        <ol class="checks" id="checks"></ol>
        <div class="result" aria-live="polite">
          <div class="score"><span id="score">0</span><small> / 10</small></div>
          <p class="msg" id="msg"></p>
          <div class="btns">
            <a class="btn primary" data-cta="book" href="#">$test_book</a>
            <a class="btn ghost" data-cta="wa" href="#">$test_wa</a>
          </div>
        </div>
        <p class="note">$test_note</p>
      </div>
    </div>
  </section>

  <section id="faq">
    <div class="wrap">
      <h2>$faq_h2</h2>
      <div style="margin-top:20px;max-width:720px">$faq</div>
    </div>
  </section>

  <section id="sobre">
    <div class="wrap about">
      <h2>$about_h2</h2>
      <p>$about_p</p>
    </div>
  </section>

  <section id="contacto" style="padding-top:8px">
    <div class="wrap">
      <div class="contact">
        <h2>$contact_h2</h2>
        <p>$contact_p</p>
        <div class="btns">
          <a class="btn primary" data-cta="book" href="#">$contact_book</a>
          <a class="btn ghost" data-cta="wa" href="#">$contact_wa</a>
        </div>
        <p class="soon" id="soon" hidden>$soon</p>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">$footer <span id="who"></span>.</div>
</footer>

<script>
/* ---- Fill in before sharing the site (applies to all languages) ---- */
const CONFIG = {
  name: "Sherbaz",
  whatsapp: "",   // digits only with country code, e.g. 34600000000
  bookingUrl: ""  // link to your 15-minute booking calendar
};
/* -------------------------------------------------------------------- */

const T = $strings_json;

document.getElementById("who").textContent = CONFIG.name;

function fill(s, vars){
  return s.replace(/\\{(\\w+)\\}/g, (m, k) => (k in vars ? vars[k] : m));
}
function waLink(text){
  return "https://wa.me/" + CONFIG.whatsapp + "?text=" + encodeURIComponent(text);
}

function applyCTAs(score){
  const generic = fill(T.wa_generic, {name: CONFIG.name});
  const scored = fill(T.wa_score, {name: CONFIG.name, score: score});
  document.querySelectorAll('[data-cta="book"]').forEach(a => {
    if (CONFIG.bookingUrl){ a.href = CONFIG.bookingUrl; a.classList.add("on"); }
  });
  document.querySelectorAll('[data-cta="wa"]').forEach(a => {
    if (CONFIG.whatsapp){
      const inTest = a.closest(".result");
      a.href = waLink(inTest && score !== null ? scored : generic);
      a.classList.add("on");
    }
  });
  document.getElementById("soon").hidden = !!(CONFIG.bookingUrl || CONFIG.whatsapp);

  const hdr = document.getElementById("hdrcta");
  if (CONFIG.bookingUrl){ hdr.href = CONFIG.bookingUrl; hdr.textContent = T.hdr_book; hdr.hidden = false; }
  else if (CONFIG.whatsapp){ hdr.href = waLink(generic); hdr.textContent = T.hdr_wa; hdr.hidden = false; }
}

const list = document.getElementById("checks");
T.checks.forEach(text => {
  const li = document.createElement("li");
  li.innerHTML = '<label><input type="checkbox"><span class="t"></span></label>';
  li.querySelector(".t").textContent = text;
  list.appendChild(li);
});

const scoreEl = document.getElementById("score");
const msgEl = document.getElementById("msg");
let touched = false;

function messageFor(n){
  if (n <= 4) return T.msg_low;
  if (n <= 7) return T.msg_mid;
  return T.msg_high;
}

function update(){
  const n = document.querySelectorAll("#checks input:checked").length;
  scoreEl.textContent = n;
  msgEl.textContent = touched ? messageFor(n) : T.msg_prompt;
  applyCTAs(touched ? n : null);
}
list.addEventListener("change", () => { touched = true; update(); });
update();
</script>
</body>
</html>
""")


def esc(s):
    return html.escape(s, quote=True)


def page_url(folder):
    return BASE + folder


def render(code, htmllang, folder, _short, _full, og_locale):
    s = STRINGS[code]
    depth = folder.count("/")
    prefix = "../" * depth

    # language switcher (relative links so it works on any host)
    sw = []
    for c, _hl, f, short, full, _og in LANGS:
        href = (prefix + f) or "./"
        cur = ' aria-current="true"' if c == code else ""
        sw.append(f'<a href="{href}" hreflang="{"ca" if c == "va" else c}" lang="{_hl}" '
                  f'title="{esc(full)}" aria-label="{esc(full)}"{cur}>{short}</a>')

    alts = []
    for c, _hl, f, _short2, _full2, _og in LANGS:
        alts.append(f'<link rel="alternate" hreflang="{"ca" if c == "va" else c}" href="{page_url(f)}">')
    alts.append(f'<link rel="alternate" hreflang="x-default" href="{page_url("")}">')

    facts = "".join(f"<li>{esc(x)}</li>" for x in s["facts"])
    leaks = "".join(f'<div class="card"><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for h, p in s["leaks"])

    tiers = []
    for t in s["tiers"]:
        items = "".join(f"<li>{esc(i)}</li>" for i in t["items"])
        cls = "card feat" if t["feat"] else "card"
        tiers.append(
            f'<div class="{cls}"><span class="tag">{esc(t["tag"])}</span><h3>{esc(t["name"])}</h3>'
            f'<div class="price">{esc(t["price"])} <small>{esc(t["small"])}</small></div><ul>{items}</ul></div>'
        )

    steps = "".join(f"<li><h3>{esc(h)}</h3><p>{esc(p)}</p></li>" for h, p in s["steps"])
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in s["faq"])

    js_keys = ["checks", "msg_prompt", "msg_low", "msg_mid", "msg_high", "wa_generic", "wa_score", "hdr_book", "hdr_wa"]
    strings_json = json.dumps({k: s[k] for k in js_keys}, ensure_ascii=False).replace("</", "<\\/")

    simple = {k: esc(s[k]) for k in (
        "title", "desc", "og_title", "og_desc", "brand", "brand_place", "hdr_default", "lang_label", "eyebrow", "h1",
        "lead", "cta_test", "cta_prices", "leaks_h2", "leaks_p", "prices_h2", "prices_p", "prices_note", "how_h2",
        "test_h2", "test_p", "test_book", "test_wa", "test_note", "faq_h2", "about_h2", "about_p", "contact_h2",
        "contact_p", "contact_book", "contact_wa", "soon", "footer")}

    return TEMPLATE.substitute(
        htmllang=htmllang, canonical=page_url(folder), alternates="\n".join(alts),
        og_locale=og_locale, css=CSS, switcher="".join(sw), facts=facts, leaks=leaks,
        icon_href=prefix + "favicon.svg", apple_href=prefix + "apple-touch-icon.png",
        og_image=BASE + "og-" + code + ".png", og_alt=esc(s["og_title"]),
        tiers="".join(tiers), steps=steps, faq=faq, strings_json=strings_json, **simple)


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    for code, hl, folder, short, full, og in LANGS:
        write(os.path.join(folder, "index.html"), render(code, hl, folder, short, full, og))

    urls = "".join(
        f'  <url>\n    <loc>{page_url(f)}</loc>\n' +
        "".join(f'    <xhtml:link rel="alternate" hreflang="{"ca" if c2 == "va" else c2}" href="{page_url(f2)}"/>\n'
                for c2, _a, f2, _b, _c, _d in LANGS) +
        '  </url>\n'
        for _c, _hl, f, _s, _fu, _og in LANGS)
    write("sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          + urls + '</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
    print("built:", ", ".join((f or "") + "index.html" for _c, _h, f, *_ in LANGS))


if __name__ == "__main__":
    main()
