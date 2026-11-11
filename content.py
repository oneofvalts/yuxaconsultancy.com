"""Words and settings for yuxaconsultancy.com; build.py turns them into HTML.

PAGES holds, in each language, the home page and the words every page
shares; TEAM the people of YUXA; WORK_PAGES one page per person, showing
their work; WORKSHOP the workshop page. Adding a person means an entry in
TEAM and one in WORK_PAGES: the home page gives each person a panel of their
own, in TEAM order, which leads to their page.

Strings may contain inline HTML. French strings are written with ordinary
spaces; build.py adds the unbreakable spaces French typography wants before
: ; ! ? and inside numbers.

Never put a phone number here: this repository is public. WhatsApp is reached
through a WhatsApp Business short link, which does not show the number.
"""

SITE = "https://yuxaconsultancy.com"
EMAIL = "contact@yuxaconsultancy.com"

# WhatsApp Business › Business tools › Short link (https://wa.me/message/...).
# Empty: no WhatsApp button anywhere on the site.
WHATSAPP_LINK = "https://wa.me/message/E5OQUKF24TRFM1"
# Google Calendar appointment schedule for the free 15-minute call.
# Empty: the booking buttons open an e-mail instead.
BOOKING_LINK = "https://calendar.app.google/b4TrMwy2mpcnn3G67"
# Google Form for the workshop. Empty: registration by e-mail.
WORKSHOP_FORM = ""
# YUXA's accounts, linked in every page's footer in this order and named in
# the structured data (schema.org sameAs). Empty: no links.
SOCIAL = [
    ("YouTube", "https://www.youtube.com/@yuxaconsultancy"),
    ("Instagram", "https://www.instagram.com/yuxaconsultancy/"),
    ("TikTok", "https://www.tiktok.com/@yuxa.consultancy"),
]

LANGS = ["tr", "en", "fr"]

# The browser tab's title on the three home pages, at the owner's word
# (11 November 2026); PAGES[...]["title"] stays the social preview's title.
HOME_TAB_TITLE = "Yuxa"

PAGES = {
    "tr": {
        "path": "",
        "locale": "tr_TR",
        "title": "YUXA: matematik dersi, LaTeX dizgi ve ahşap oyma",
        "description": (
            "Abdullah Uyu’dan matematik ve programlama dersi, LaTeX dizgi ve "
            "otomasyon; Durmuş Uyu’dan elde oyulmuş kaşık, kuksa ve oyma atölyeleri."
        ),
        "skip": "İçeriğe geç",
        "home": "Ana sayfa",
        "back": "Ana sayfaya dön",
        # The buttons of the photo viewer, as screen readers announce them.
        "viewer": {"close": "Kapat", "prev": "Önceki fotoğraf",
                   "next": "Sonraki fotoğraf"},
        "ids": {"contact": "iletisim"},
        "nav_label": "Ana menü",
        # A work page by its key in WORK_PAGES, or a section of the page.
        "nav": [
            ("maths", "Matematik ve LaTeX"),
            ("woodwork", "Ahşap"),
            ("contact", "İletişim"),
        ],
        # Dated events under the panels; remove each once it is over.
        "upcoming_label": "Yaklaşan",
        "upcoming": [
            {
                "title": "LaTeX ile Tez atölyesi:",
                "text": "28 Kasım Cumartesi, 10.00–13.00, online. 20 Kasım’a kadar "
                        "450 TL, sonra 600 TL.",
                "link": "Ayrıntılar ve kayıt",
                "page": "workshop",
            },
        ],
        "cta_whatsapp": "WhatsApp’tan yazın",
        "cta_book": "Ücretsiz ön görüşme",
        "cta_email": "E-posta gönderin",
        "mail_subject": "Bilgi talebi",
        "book_subject": "Ön görüşme",
        "contact_title": "İletişim",
        "contact_text": (
            "Ne için yazdığınızı kısaca anlatın: ders ve seviyeniz, bir dizgi ya da "
            "otomasyon işi, ya da ahşap. En geç bir iş günü içinde dönerim."
        ),
        "footer": "© 2026 YUXA Consultancy",
    },
    "en": {
        "path": "en/",
        "locale": "en_GB",
        "title": "YUXA: maths lessons, LaTeX typesetting and woodcarving",
        "description": (
            "Maths and programming lessons, LaTeX typesetting and automation with "
            "Abdullah Uyu; hand-carved spoons, kuksas and workshops with Durmuş Uyu."
        ),
        "skip": "Skip to content",
        "home": "Home",
        "back": "Back to the home page",
        "viewer": {"close": "Close", "prev": "Previous photo", "next": "Next photo"},
        "ids": {"contact": "contact"},
        "nav_label": "Main menu",
        "nav": [
            ("maths", "Maths and LaTeX"),
            ("woodwork", "Woodwork"),
            ("contact", "Contact"),
        ],
        "upcoming_label": "Coming up",
        "upcoming": [
            {
                "title": "LaTeX ile Tez, a workshop in Turkish:",
                "text": "Saturday 28 November, 10:00–13:00, online. 450 TL until "
                        "20 November, then 600 TL.",
                "link": "Details and registration (Turkish)",
                "page": "workshop",
            },
        ],
        "cta_whatsapp": "Message on WhatsApp",
        "cta_book": "Book a free call",
        "cta_email": "Send an e-mail",
        "mail_subject": "Enquiry",
        "book_subject": "Free call",
        "contact_title": "Contact",
        "contact_text": (
            "Tell me briefly what it is about: a course and your level, a "
            "typesetting or automation job, or woodwork. I reply within one working "
            "day."
        ),
        "footer": "© 2026 YUXA Consultancy",
    },
    "fr": {
        "path": "fr/",
        "locale": "fr_FR",
        "title": "YUXA : cours de maths, composition LaTeX et bois sculpté",
        "description": (
            "Cours de maths et de programmation, composition LaTeX avec Abdullah "
            "Uyu ; cuillères, kuksas et ateliers de sculpture avec Durmuş Uyu."
        ),
        "skip": "Aller au contenu",
        "home": "Accueil",
        "back": "Retour à l’accueil",
        "viewer": {"close": "Fermer", "prev": "Photo précédente",
                   "next": "Photo suivante"},
        "ids": {"contact": "contact"},
        "nav_label": "Menu principal",
        "nav": [
            ("maths", "Maths et LaTeX"),
            ("woodwork", "Bois"),
            ("contact", "Contact"),
        ],
        "upcoming_label": "À venir",
        "upcoming": [
            {
                "title": "LaTeX ile Tez, un atelier en turc :",
                "text": "samedi 28 novembre, de 10 h à 13 h, en ligne. 450 TL "
                        "jusqu’au 20 novembre, puis 600 TL.",
                "link": "Détails et inscription (en turc)",
                "page": "workshop",
            },
        ],
        "cta_whatsapp": "Écrire sur WhatsApp",
        "cta_book": "Réserver un appel gratuit",
        "cta_email": "Envoyer un e-mail",
        "mail_subject": "Demande de renseignements",
        "book_subject": "Appel découverte",
        "contact_title": "Contact",
        "contact_text": (
            "Dites-moi en quelques mots ce qui vous amène : la matière et le niveau, "
            "un travail de composition ou d’automatisation, ou le bois. Je réponds "
            "sous un jour ouvré."
        ),
        "footer": "© 2026 YUXA Consultancy",
    },
}

# The people of YUXA, in the order the home page shows them; page is the key
# of their work page in WORK_PAGES, facts what search engines read about them
# (schema.org Person properties).
TEAM = [
    {
        "name": "Abdullah Uyu",
        "page": "maths",
        "facts": {
            "alumniOf": {"@type": "CollegeOrUniversity",
                         "name": "Galatasaray Üniversitesi"},
            "knowsLanguage": ["tr", "fr", "en"],
            "knowsAbout": ["Mathematics", "Programming", "LaTeX", "Lean", "n8n"],
        },
        "role": {
            "tr": "Matematik ve bilgisayar dersleri, LaTeX dizgi, otomasyon",
            "en": "Mathematics and computing lessons, LaTeX typesetting, automation",
            "fr": "Cours de mathématiques et d’informatique, composition LaTeX, "
                  "automatisation",
        },
        "bio": {
            "tr": [
                "Galatasaray Üniversitesi Matematik Bölümü’nü 2025’te bitirdi; aynı "
                "üniversitede yüksek lisans yapıyor. Eğitimini Fransızca aldı, "
                "İngilizceyi de akıcı konuşuyor.",
                "2015’ten beri programlama yapıyor (Python, C, C++, Scheme). Lisans "
                "bitirme projesinde Desargues teoremini Lean ile biçimselleştirdi. Bir "
                "siber güvenlik araştırma şirketinde matematikçi danışman, Ziraat "
                "Teknoloji’de yapay zekâ uygulamaları alanında yazılım danışmanı olarak "
                "çalıştı; n8n ile ajan tabanlı iş akışları geliştirdi.",
                "Onlarca belgeyi LaTeX ile dizdi.",
            ],
            "en": [
                "Abdullah graduated in mathematics from Galatasaray University in 2025, "
                "where teaching is in French, and is now a master’s student there. He "
                "speaks Turkish, French and English.",
                "He has been programming since 2015 (Python, C, C++, Scheme); for his "
                "graduation project he formalized Desargues’s theorem in Lean. He has "
                "worked as a mathematician consultant at a cyber-security research "
                "company and as a programmer consultant on AI applications at Ziraat "
                "Teknoloji, building agentic workflows in n8n.",
                "He has typeset dozens of documents in LaTeX.",
            ],
            "fr": [
                "Diplômé en mathématiques de l’Université Galatasaray en 2025, où "
                "l’enseignement est en français, Abdullah y prépare aujourd’hui un "
                "master. Il parle français, turc et anglais.",
                "Il programme depuis 2015 (Python, C, C++, Scheme) ; pour son projet de "
                "fin d’études, il a formalisé le théorème de Desargues en Lean. Il a été "
                "mathématicien consultant dans une entreprise de recherche en "
                "cybersécurité, puis consultant en programmation au département des "
                "applications d’IA de Ziraat Teknoloji, où il construisait des flux "
                "agentiques avec n8n.",
                "Il a composé des dizaines de documents en LaTeX.",
            ],
        },
    },
    {
        "name": "Durmuş Uyu",
        "page": "woodwork",
        "facts": {
            "knowsAbout": ["Woodcarving", "Woodworking"],
        },
        "role": {
            "tr": "Ahşap oyma ve ahşap işçiliği",
            "en": "Woodcarving and woodworking",
            "fr": "Sculpture et travail du bois",
        },
        "bio": {
            "tr": [
                "Boğaziçi Üniversitesi’nde matematik öğretmenliği okuyor. Kaşık, ölçek, "
                "kuksa, kase ve kutu oyuyor; oyma ve ahşap işçiliği atölyeleri veriyor.",
            ],
            "en": [
                "Durmuş studies mathematics education at Boğaziçi University. He carves "
                "spoons, scoops, kuksas, bowls and boxes, and gives carving and "
                "woodworking workshops.",
            ],
            "fr": [
                "Étudiant en enseignement des mathématiques à l’Université du Bosphore "
                "(Boğaziçi), Durmuş sculpte cuillères, doseurs, kuksas, bols et boîtes, "
                "et anime des ateliers de sculpture et de travail du bois.",
            ],
        },
    },
]

# A work page has, in each language, a hero (kicker, heading, lead*) and these
# sections, in this order; those marked * are optional:
#   gallery*   photographs, when the spec lists photos, then gallery_note*
#   offers     cards of what the person offers, then offers_note*
#   how*       steps of how working together goes, one sentence each
#   prices     price groups, then prices_note
#   events*    dated events, each leading to its page
#   about      the person's bio from TEAM, and aside_title and aside* next to it
#   contact    a few words, the buttons and the way back home
# ids holds the anchors of the sections present. panel is what the home page
# shows: a title, a few words, a few prices and the link here, under the
# spec's cover picture (600 x 400, or a photograph in 3:2), described by alt.
# The spec's ornament names the drawing behind the heading, made by
# tools/make_ornaments.py.

# Abdullah's lessons, typesetting and automation, one page per language.
MATHS = {
    "person": "Abdullah Uyu",
    "cover": "assets/desargues.svg",  # made by tools/make_desargues.py
    "ornament": "cardioid",  # behind the heading: assets/cardioid.svg
    "image": "assets/og.png",  # social preview, made in the private repo
    "booking": True,  # the free 15-minute call is for lessons and jobs
    "pages": {
        "tr": {
            "path": "matematik/",
            "title": "Matematik özel ders, LaTeX tez dizgisi ve yapay zekâ – YUXA",
            "description": (
                "Üniversite matematiği, programlama, IB ve Fransız müfredatı, GSÜ "
                "hazırlık için özel ders; LaTeX ile tez dizgisi; yapay zekâ ve "
                "otomasyon. Online ya da yüz yüze."
            ),
            "ids": {"offers": "hizmetler", "how": "nasil", "prices": "ucretler",
                    "events": "atolye", "contact": "iletisim"},
            "panel": {
                "title": "Matematik, programlama, LaTeX ve yapay zekâ",
                "text": (
                    "Türkçe, Fransızca ya da İngilizce özel ders veriyor: üniversite "
                    "matematiği ve programlama, IB ve Fransız müfredatı, GSÜ Fransızca "
                    "hazırlık. LaTeX ile tez ve belge diziyor, küçük ekipler için "
                    "otomasyon kuruyor."
                ),
                "alt": (
                    "Desargues teoremi: bir noktaya göre perspektif iki üçgenin "
                    "karşılıklı kenarları, aynı doğru üzerindeki üç noktada kesişir."
                ),
                # Starting prices; keep them in step with the price list below.
                "rows": [
                    ("Özel ders, 60 dk", "1.500 TL"),
                    ("LaTeX dizgi", "1.500 TL"),
                    ("Otomasyon ve yapay zekâ", "2.000 TL"),
                ],
                "link": "Dersler, dizgi ve ücretler",
            },
            "kicker": "Abdullah Uyu",
            "heading": "Matematik, programlama, LaTeX ve yapay zekâ",
            "mail_subject": "Bilgi talebi",
            "offers_title": "Hizmetler",
            "offers": [
                {
                    "title": "Özel ders",
                    "body": (
                        "Üniversite matematiği ve programlama; IB Diploma ve Fransız "
                        "müfredatında lise matematiği; GSÜ Fransızca hazırlık desteği."
                    ),
                    "items": [
                        "Calculus, lineer cebir, olasılık, ayrık matematik, "
                        "diferansiyel denklemler",
                        "C, C++ ve Python; algoritmalar ve veri yapıları",
                        "GSÜ dersleri Fransızca terimleriyle: <i lang=\"fr\">Analyse, "
                        "Algèbre linéaire, Probabilités</i>",
                        "Birebir ya da 3–6 kişilik vize/final kampları",
                    ],
                },
                {
                    "title": "LaTeX dizgi",
                    "body": "Kurallara uyan, rahat okunan tez, makale ve sunumlar.",
                    "items": [
                        "Enstitü kılavuzuna uygun tez şablonu",
                        "Word’den LaTeX’e dönüşüm",
                        "Teslim öncesi biçim denetimi",
                        "Beamer sunumlar ve TikZ şekiller",
                    ],
                },
                {
                    "title": "Otomasyon ve yapay zekâ",
                    "body": (
                        "Tekrarlayan işler için n8n iş akışları ve yapay zekâ ajanları; "
                        "günlük işte yapay zekâ kullanımı üzerine birebir çalışma."
                    ),
                    "items": [
                        "Otomasyon değerlendirmesi ve yazılı plan",
                        "Kurulmuş ve belgelenmiş iş akışları",
                        "Yapay zekâ koçluğu",
                    ],
                },
            ],
            "offers_note": (
                "Her dersten sonra, işlediğimiz konuları ve çözdüğümüz soruları "
                "özetleyen, dizilmiş kısa bir PDF gönderiyorum."
            ),
            "how_title": "Nasıl çalışır",
            "how": [
                "15 dakikalık ücretsiz bir görüşmede ihtiyacınızı, seviyenizi ve "
                "hedefinizi konuşuruz.",
                "Dersler online (Google Meet) ya da yüz yüze olur.",
                "Her dersten sonra dizilmiş özet notlar, her işin sonunda da derlenmiş "
                "kaynak dosyalar sizde kalır.",
            ],
            "prices_title": "Ücretler",
            "prices": [
                ("Özel ders", [
                    ("Birebir, online ya da yüz yüze, 60 dk", "1.500 TL"),
                    ("IB, A-level ve Fransız müfredatı, online ya da yüz yüze, 60 dk",
                     "2.000 TL"),
                    ("Vize/Final Kampı: 3–6 kişi, 120 dk, kişi başı", "800 TL"),
                ]),
                ("LaTeX dizgi", [
                    ("Hızlı düzeltme, 60 dakikaya kadar", "1.500 TL"),
                    ("Enstitü kurallarına uygun tez şablonu", "5.000 TL"),
                    ("Word’den LaTeX’e dönüşüm, sayfa başı, en az 3.000 TL", "150 TL"),
                    ("Teslim öncesi biçim denetimi", "3.000 TL"),
                    ("Beamer sunum, 20 slayda kadar", "3.500 TL"),
                    ("TikZ şekil", "750–1.500 TL"),
                ]),
                ("Otomasyon ve yapay zekâ", [
                    ("Değerlendirme: 90 dk görüşme ve yazılı plan", "3.500 TL"),
                    ("Tek iş akışı, kurulmuş ve belgelenmiş", "12.000 TL"),
                    ("Yapay zekâ koçluğu, 60 dk", "2.000 TL"),
                ]),
            ],
            "prices_note": (
                "Kasım 2026 ücretleridir. Beş derslik pakette %10 indirim var; 15 "
                "dakikalık ön görüşme ücretsiz."
            ),
            "events_title": "Atölye",
            "events": [
                {
                    "title": "LaTeX ile Tez",
                    "text": (
                        "28 Kasım Cumartesi, 10.00–13.00, online. Tez yazanlar için üç "
                        "saatlik bir LaTeX atölyesi: enstitü şablonu, kaynakça, şekiller "
                        "ve teslim öncesi kontrol. 600 TL; 20 Kasım’a kadar 450 TL."
                    ),
                    "link": "Ayrıntılar ve kayıt",
                    "page": "workshop",
                },
            ],
            "contact_title": "İletişim",
            "contact_text": (
                "Ne için yazdığınızı kısaca anlatın: ders ve seviyeniz, ya da bir "
                "dizgi veya otomasyon işi. En geç bir iş günü içinde dönerim."
            ),
        },
        "en": {
            "path": "en/maths/",
            "title": "Maths tutoring, LaTeX thesis typesetting and AI – YUXA",
            "description": (
                "Lessons in university maths and programming, IB and French-curriculum "
                "maths; theses typeset in LaTeX; AI and automation with n8n. Online or in "
                "person."
            ),
            "ids": {"offers": "services", "how": "how", "prices": "prices",
                    "events": "workshop", "contact": "contact"},
            "panel": {
                "title": "Mathematics, programming, LaTeX and AI",
                "text": (
                    "He gives private lessons in Turkish, French or English: university "
                    "mathematics and programming, IB and French-curriculum maths, and "
                    "French for Galatasaray University’s preparatory year. He also "
                    "typesets theses and documents in LaTeX and builds automations for "
                    "small teams."
                ),
                "alt": (
                    "Desargues’s theorem: when two triangles are in perspective from a "
                    "point, their corresponding sides meet in three points on one line."
                ),
                "rows": [
                    ("Lessons, 60 min", "1,500 TL"),
                    ("LaTeX typesetting", "1,500 TL"),
                    ("Automation and AI", "2,000 TL"),
                ],
                "link": "Lessons, typesetting and prices",
            },
            "kicker": "Abdullah Uyu",
            "heading": "Mathematics, programming, LaTeX and AI",
            "mail_subject": "Enquiry",
            "offers_title": "Services",
            "offers": [
                {
                    "title": "Lessons",
                    "body": (
                        "University mathematics and programming; IB Diploma and "
                        "French-curriculum school maths; French for Galatasaray "
                        "University’s preparatory year."
                    ),
                    "items": [
                        "Calculus, linear algebra, probability, discrete mathematics, "
                        "differential equations",
                        "C, C++ and Python; algorithms and data structures",
                        "Galatasaray courses with their French terms: <i lang=\"fr\">"
                        "Analyse, Algèbre linéaire, Probabilités</i>",
                        "One-to-one, or exam clinics of three to six students",
                    ],
                },
                {
                    "title": "LaTeX typesetting",
                    "body": "Theses, papers and slides that follow the rules and read "
                            "well.",
                    "items": [
                        "Thesis templates built to your graduate school’s guide",
                        "Word to LaTeX conversion",
                        "Format check before submission",
                        "Beamer slides and TikZ figures",
                    ],
                },
                {
                    "title": "Automation and AI",
                    "body": (
                        "n8n workflows and AI agents for repetitive work, and "
                        "one-to-one coaching on using AI in your daily work."
                    ),
                    "items": [
                        "Automation audit with a written plan",
                        "Workflows built and documented",
                        "AI coaching",
                    ],
                },
            ],
            "offers_note": (
                "After every lesson you get a short, typeset PDF of what we covered and "
                "solved."
            ),
            "how_title": "How it works",
            "how": [
                "It starts with a free 15-minute call about what you need, your level "
                "and your goal.",
                "Lessons are online (Google Meet) or in person.",
                "You keep typeset notes from every lesson, and the compiled source "
                "files at the end of every job.",
            ],
            "prices_title": "Prices",
            "prices": [
                ("Lessons", [
                    ("One-to-one, online or in person, 60 min", "1,500 TL"),
                    ("IB, A-level and French curricula, online or in person, 60 min",
                     "2,000 TL"),
                    ("Exam clinic: 3–6 students, 120 min, per student", "800 TL"),
                ]),
                ("LaTeX typesetting", [
                    ("Quick fix, up to 60 min", "1,500 TL"),
                    ("Thesis template to your graduate school’s rules", "5,000 TL"),
                    ("Word to LaTeX conversion, per page, minimum 3,000 TL", "150 TL"),
                    ("Format check before submission", "3,000 TL"),
                    ("Beamer slides, up to 20", "3,500 TL"),
                    ("TikZ figure", "750–1,500 TL"),
                ]),
                ("Automation and AI", [
                    ("Audit: 90-min call and a written plan", "3,500 TL"),
                    ("One workflow, built and documented", "12,000 TL"),
                    ("AI coaching, 60 min", "2,000 TL"),
                ]),
            ],
            "prices_note": (
                "Prices as of November 2026. A five-lesson pack is 10% off, and the "
                "first 15-minute call is free."
            ),
            "events_title": "Workshop",
            "events": [
                {
                    "title": "LaTeX ile Tez (in Turkish)",
                    "text": (
                        "Saturday 28 November, 10:00–13:00, online. Three hours of LaTeX "
                        "for anyone writing a thesis: the template, the bibliography, "
                        "figures and the check before submission. 600 TL, or 450 TL "
                        "until 20 November."
                    ),
                    "link": "Details and registration (Turkish)",
                    "page": "workshop",
                },
            ],
            "contact_title": "Contact",
            "contact_text": (
                "Tell me briefly what it is about: a course and your level, or a "
                "typesetting or automation job. I reply within one working day."
            ),
        },
        "fr": {
            "path": "fr/maths/",
            "title": "Cours de maths, composition LaTeX et IA – YUXA",
            "description": (
                "Cours de maths en français, du collège à l’université, bac et IB ; "
                "programmation ; composition de thèses en LaTeX ; IA et automatisation. En "
                "ligne ou en personne."
            ),
            "ids": {"offers": "services", "how": "methode", "prices": "tarifs",
                    "events": "atelier", "contact": "contact"},
            "panel": {
                "title": "Mathématiques, informatique, LaTeX et IA",
                "text": (
                    "Il donne des cours particuliers en français, en turc ou en anglais : "
                    "mathématiques du collège à l’université, programme français, bac et "
                    "IB, programmation, et français pour l’année préparatoire de "
                    "l’Université Galatasaray. Il compose aussi thèses et documents en "
                    "LaTeX et automatise des tâches pour les petites équipes."
                ),
                "alt": (
                    "Théorème de Desargues : si deux triangles sont en perspective par "
                    "rapport à un point, leurs côtés homologues se coupent en trois "
                    "points alignés."
                ),
                "rows": [
                    ("Cours, 60 min", "1 500 TL"),
                    ("Composition LaTeX", "1 500 TL"),
                    ("Automatisation et IA", "2 000 TL"),
                ],
                "link": "Cours, composition et tarifs",
            },
            "kicker": "Abdullah Uyu",
            "heading": "Mathématiques, informatique, LaTeX et IA",
            "mail_subject": "Demande de renseignements",
            "offers_title": "Services",
            "offers": [
                {
                    "title": "Cours particuliers",
                    "body": (
                        "Mathématiques du collège à la terminale : programme français, "
                        "lycées francophones, bac et IB ; mathématiques universitaires "
                        "et programmation ; français pour l’année préparatoire de "
                        "l’Université Galatasaray."
                    ),
                    "items": [
                        "Programme français et IB Diploma (maths AA et AI)",
                        "Analyse, algèbre linéaire, probabilités, mathématiques "
                        "discrètes",
                        "C, C++ et Python ; algorithmes et structures de données",
                        "En individuel, ou en stages de révision de 3 à 6 élèves",
                    ],
                },
                {
                    "title": "Composition LaTeX",
                    "body": "Thèses, articles et présentations conformes aux règles et "
                            "agréables à lire.",
                    "items": [
                        "Gabarit de thèse selon le guide de votre institut",
                        "Conversion de Word vers LaTeX",
                        "Vérification de la mise en forme avant dépôt",
                        "Présentations Beamer et figures TikZ",
                    ],
                },
                {
                    "title": "Automatisation et IA",
                    "body": (
                        "Flux n8n et agents d’IA pour les tâches répétitives ; "
                        "accompagnement individuel à l’usage de l’IA au quotidien."
                    ),
                    "items": [
                        "Diagnostic d’automatisation et plan écrit",
                        "Flux construits et documentés",
                        "Accompagnement IA",
                    ],
                },
            ],
            "offers_note": (
                "Après chaque séance, vous recevez une courte fiche composée (PDF) qui "
                "reprend ce que nous avons vu et résolu."
            ),
            "how_title": "Comment ça marche",
            "how": [
                "Tout commence par un appel gratuit de 15 minutes pour cerner votre "
                "besoin, votre niveau et votre objectif.",
                "Les séances ont lieu en ligne (Google Meet) ou en présentiel.",
                "Vous gardez une fiche composée de chaque séance, et les fichiers "
                "sources compilés à la fin de chaque travail.",
            ],
            "prices_title": "Tarifs",
            "prices": [
                ("Cours", [
                    ("Collège, lycée, bac et IB, en ligne ou à domicile, 60 min",
                     "2 000 TL"),
                    ("Université, en ligne ou en présentiel, 60 min", "1 500 TL"),
                    ("Stage de révision : 3 à 6 élèves, 120 min, par élève", "800 TL"),
                ]),
                ("Composition LaTeX", [
                    ("Correction rapide, jusqu’à 60 min", "1 500 TL"),
                    ("Gabarit de thèse selon les règles de l’institut", "5 000 TL"),
                    ("Conversion de Word vers LaTeX, la page, minimum 3 000 TL",
                     "150 TL"),
                    ("Vérification avant dépôt", "3 000 TL"),
                    ("Présentation Beamer, jusqu’à 20 diapositives", "3 500 TL"),
                    ("Figure TikZ", "750–1 500 TL"),
                ]),
                ("Automatisation et IA", [
                    ("Diagnostic : appel de 90 min et plan écrit", "3 500 TL"),
                    ("Un flux construit et documenté", "12 000 TL"),
                    ("Accompagnement IA, 60 min", "2 000 TL"),
                ]),
            ],
            "prices_note": (
                "Tarifs de novembre 2026. Le forfait de cinq séances bénéficie de 10 % "
                "de remise, et le premier appel de 15 minutes est offert."
            ),
            "events_title": "Atelier",
            "events": [
                {
                    "title": "LaTeX ile Tez (en turc)",
                    "text": (
                        "Samedi 28 novembre, de 10 h à 13 h, en ligne. Trois heures de "
                        "LaTeX pour qui rédige une thèse : le gabarit, la bibliographie, "
                        "les figures et la vérification avant dépôt. 600 TL, ou 450 TL "
                        "jusqu’au 20 novembre."
                    ),
                    "link": "Détails et inscription (en turc)",
                    "page": "workshop",
                },
            ],
            "contact_title": "Contact",
            "contact_text": (
                "Dites-moi en quelques mots ce qui vous amène : la matière et le "
                "niveau, ou un travail de composition ou d’automatisation. Je "
                "réponds sous un jour ouvré."
            ),
        },
    },
}

# Photographs of Durmuş's work in gallery order: the file name in
# assets/woodwork/ (made by `make photos` in the private repository, which
# keeps the originals), then the caption in Turkish, English and French.
WOODWORK_PHOTOS = [
    ("three-kuksas", "Kuksalar", "Kuksas", "Kuksas"),
    ("kuksa-single-hole", "Kuksa", "Kuksa", "Kuksa"),
    ("kuksa-two-hole", "İki delikli kuksa", "Kuksa with a two-hole handle",
     "Kuksa à anse à deux trous"),
    ("painted-box-closed", "Boyalı kutu", "Painted box", "Boîte peinte"),
    ("painted-box-open", "Boyalı kutu, açık", "Painted box, open",
     "Boîte peinte, ouverte"),
    ("painted-box-top", "Boyalı kutu, kapak", "Painted box, the lid",
     "Boîte peinte, le couvercle"),
    ("three-spoons", "Üç kaşık", "Three spoons", "Trois cuillères"),
    ("spoon-bowl-closeup", "Kaşık, ayrıntı", "Spoon, detail", "Cuillère, détail"),
    ("spoon-on-rug", "Kaşık", "Spoon", "Cuillère"),
    ("notched-spoon-horizontal", "Çentikli saplı kaşık", "Spoon with a notched handle",
     "Cuillère au manche cranté"),
    ("notched-spoon-vertical", "Çentikli saplı kaşık, üstten",
     "Spoon with a notched handle, from above",
     "Cuillère au manche cranté, vue de dessus"),
    ("leaf-tip-handle", "Yaprak uçlu sap", "Handle ending in a leaf",
     "Manche terminé en feuille"),
    ("double-ended-scoop", "Çift başlı ölçek", "Double-ended scoop",
     "Doseur à deux têtes"),
    ("faceted-handle-scoop", "Köşeli saplı ölçek", "Scoop with a faceted handle",
     "Doseur au manche à facettes"),
    ("wooden-scoop", "Küçük ölçek", "Small scoop", "Petit doseur"),
    ("lidded-bowl-closed", "Kapaklı kase", "Lidded bowl", "Bol à couvercle"),
    ("lidded-bowl-open", "Kapaklı kase, açık", "Lidded bowl, open",
     "Bol à couvercle, ouvert"),
    ("wooden-ashtray", "Küllük", "Ashtray", "Cendrier"),
    ("wooden-ashtray-bottom", "Küllük, alttan", "Ashtray, from below",
     "Cendrier, vu de dessous"),
    ("footed-tray-side", "Ayaklı tepsi", "Footed tray", "Plateau sur pieds"),
    ("footed-tray-bottom", "Ayaklı tepsi, alttan", "Footed tray, from below",
     "Plateau sur pieds, vu de dessous"),
]

# The woodwork pages: Durmuş's pieces and workshops, one page per language.
WOODWORK = {
    "person": "Durmuş Uyu",
    "photos": WOODWORK_PHOTOS,
    "photo_dir": "assets/woodwork/",
    # What a photograph's alt text and search engines say of it, around its
    # caption.
    "photo_alt": {"tr": "Elde oyma ahşap: {}", "en": "Hand-carved wood: {}",
                  "fr": "Bois sculpté à la main : {}"},
    "cover": "assets/woodwork/three-kuksas-1000.jpg",
    "ornament": "rings",  # behind the heading: assets/rings.svg
    "image": "assets/og-woodwork.jpg",  # social preview, made in the private repo
    "booking": False,
    "pages": {
        "tr": {
            "path": "ahsap/",
            "title": "El yapımı ahşap kaşık, kuksa ve oyma atölyesi – YUXA",
            "description": (
                "Durmuş Uyu’nun elde oyduğu kaşık, kuksa, kase ve kutular, sipariş "
                "üzerine. Yeni başlayanlar için kaşık oyma, gruplar için ahşap "
                "atölyeleri."
            ),
            "ids": {"gallery": "isler", "offers": "siparis-ve-atolyeler",
                    "prices": "fiyatlar", "contact": "iletisim"},
            "panel": {
                "title": "Oyma",
                "text": (
                    "Sipariş üzerine kaşık, ölçek, kuksa, kase ve kutu oyuyor; her "
                    "parçayı tek tek, elde yapıyor. Yeni başlayanlara ve gruplara oyma "
                    "atölyeleri veriyor."
                ),
                "alt": "Durmuş Uyu’nun oyduğu üç kuksa",
                # Starting prices; keep them in step with the price list below.
                "rows": [
                    ("Kaşık ve ölçek", "750 TL"),
                    ("Kuksa, kase ve kutu", "2.000 TL"),
                    ("Kaşık oyma atölyesi, 3–4 saat, kişi başı", "1.250 TL"),
                ],
                "link": "İşler, sipariş ve atölyeler",
            },
            "kicker": "Durmuş Uyu",
            "heading": "Oyma",
            "mail_subject": "Ahşap",
            "gallery_title": "İşler",
            "offers_title": "Sipariş ve atölyeler",
            "offers": [
                {
                    "id": "siparis",
                    "title": "Sipariş",
                    "body": (
                        "Mutfak, sofra ya da hediye için: ne istediğinizi yazın, ölçüyü "
                        "ve biçimi birlikte belirleyelim."
                    ),
                    "items": [
                        "Kaşık ve ölçek",
                        "Kuksa (İskandinav usulü oyma bardak) ve kase",
                        "Kapaklı ve boyalı kutu",
                        "Tepsi ve tek parça işler",
                    ],
                },
                {
                    "id": "atolyeler",
                    "title": "Atölyeler",
                    "body": (
                        "El aletleriyle, adım adım oymaya ve ahşap işçiliğine giriş."
                    ),
                    "items": [
                        "Kaşık oyma: yeni başlayanlar için; kendi kaşığınızı oyup "
                        "götürürsünüz",
                        "Ahşap işçiliği: el aletleriyle temel teknikler",
                        "Okul, şirket ve dernekler için grup atölyeleri",
                        "Aletler ve ahşap benden",
                    ],
                },
            ],
            "prices_title": "Fiyatlar",
            "prices": [
                ("Parçalar", [
                    ("Kaşık ve ölçek", "750 TL"),
                    ("Kuksa", "2.000 TL"),
                    ("Kase ve kutu", "2.500 TL"),
                ]),
                ("Atölyeler", [
                    ("Kaşık oyma atölyesi: 3–4 saat, 4–8 kişi; ahşap ve aletler dahil, "
                     "kişi başı", "1.250 TL"),
                    ("Okul, şirket ya da dernek için grup atölyesi, en az 6 kişi, kişi "
                     "başı", "1.250 TL"),
                ]),
            ],
            "prices_note": (
                "Parçalarda kesin fiyat ölçüye ve işçiliğe göre değişir. Tepsi ve tek "
                "parça işler ile ahşap işçiliği atölyelerinin fiyatı için yazın. Açık "
                "atölyelerin tarihleri bu sayfada duyurulacak."
            ),
            "contact_title": "Sipariş ve iletişim",
            "contact_text": (
                "Ne istediğinizi kısaca yazın: parça ve ölçü, ya da atölye için kişi "
                "sayısı ve tarih. En geç bir iş günü içinde dönerim."
            ),
        },
        "en": {
            "path": "en/woodwork/",
            "title": "Hand-carved wooden spoons, kuksas and carving workshops – YUXA",
            "description": (
                "Spoons, scoops, kuksas, bowls and boxes carved by hand by Durmuş Uyu, "
                "made to order. Spoon carving for beginners and woodworking workshops "
                "for groups."
            ),
            "ids": {"gallery": "work", "offers": "commissions-and-workshops",
                    "prices": "prices", "contact": "contact"},
            "panel": {
                "title": "Woodcarving",
                "text": (
                    "He carves spoons, scoops, kuksas, bowls and boxes to order, by hand "
                    "and one at a time. He also runs carving workshops for beginners and "
                    "for groups."
                ),
                "alt": "Three kuksas carved by Durmuş Uyu",
                "rows": [
                    ("Spoons and scoops", "750 TL"),
                    ("Kuksas, bowls and boxes", "2,000 TL"),
                    ("Spoon carving workshop, 3–4 h, per person", "1,250 TL"),
                ],
                "link": "Work, commissions and workshops",
            },
            "kicker": "Durmuş Uyu",
            "heading": "Woodcarving",
            "mail_subject": "Woodwork",
            "gallery_title": "Work",
            "offers_title": "Commissions and workshops",
            "offers": [
                {
                    "id": "commissions",
                    "title": "Commissions",
                    "body": (
                        "For the kitchen, the table or as a gift: tell me what you have "
                        "in mind and we will settle the size and the shape together."
                    ),
                    "items": [
                        "Spoons and scoops",
                        "Kuksas (Nordic carved cups) and bowls",
                        "Lidded and painted boxes",
                        "Trays and one-off pieces",
                    ],
                },
                {
                    "id": "workshops",
                    "title": "Workshops",
                    "body": (
                        "A step-by-step introduction to carving and woodworking with "
                        "hand tools."
                    ),
                    "items": [
                        "Spoon carving for beginners: you carve your own spoon and take "
                        "it home",
                        "Woodworking: the basics with hand tools",
                        "Group workshops for schools, companies and associations",
                        "Tools and wood provided",
                    ],
                },
            ],
            "prices_title": "Prices",
            "prices": [
                ("Pieces", [
                    ("Spoons and scoops", "750 TL"),
                    ("Kuksas", "2,000 TL"),
                    ("Bowls and boxes", "2,500 TL"),
                ]),
                ("Workshops", [
                    ("Spoon carving: 3–4 h, 4–8 people, wood and tools included, per "
                     "person", "1,250 TL"),
                    ("Group workshop for a school, company or association, 6 people or "
                     "more, per person", "1,250 TL"),
                ]),
            ],
            "prices_note": (
                "For pieces, the final price depends on the size and the work. For "
                "trays, one-off pieces and woodworking workshops, ask me for a price. "
                "Dates of open workshops will be announced on this page. Workshops are "
                "in Turkish; ask me about English."
            ),
            "contact_title": "Orders and contact",
            "contact_text": (
                "Tell me briefly what you would like: the piece and its size, or for a "
                "workshop the number of people and a date. I reply within one working "
                "day."
            ),
        },
        "fr": {
            "path": "fr/bois/",
            "title": "Cuillères en bois, kuksas et ateliers de sculpture – YUXA",
            "description": (
                "Cuillères, kuksas, bols et boîtes sculptés à la main par Durmuş Uyu, "
                "sur commande ; ateliers de sculpture pour débutants et pour groupes."
            ),
            "ids": {"gallery": "realisations", "offers": "commandes-et-ateliers",
                    "prices": "tarifs", "contact": "contact"},
            "panel": {
                "title": "Sculpture sur bois",
                "text": (
                    "Il sculpte sur commande cuillères, doseurs, kuksas, bols et boîtes, "
                    "à la main et une à une. Il anime aussi des ateliers de sculpture "
                    "pour débutants et pour groupes."
                ),
                "alt": "Trois kuksas de Durmuş Uyu",
                "rows": [
                    ("Cuillères et doseurs", "750 TL"),
                    ("Kuksas, bols et boîtes", "2 000 TL"),
                    ("Sculpture de cuillère, 3 à 4 h, par personne", "1 250 TL"),
                ],
                "link": "Réalisations, commandes et ateliers",
            },
            "kicker": "Durmuş Uyu",
            "heading": "Sculpture sur bois",
            "mail_subject": "Travail du bois",
            "gallery_title": "Réalisations",
            "offers_title": "Commandes et ateliers",
            "offers": [
                {
                    "id": "commandes",
                    "title": "Sur commande",
                    "body": (
                        "Pour la cuisine, la table ou pour offrir : dites-moi ce que "
                        "vous souhaitez, nous fixerons ensemble la taille et la forme."
                    ),
                    "items": [
                        "Cuillères et doseurs",
                        "Kuksas (tasses sculptées nordiques) et bols",
                        "Boîtes à couvercle et boîtes peintes",
                        "Plateaux et pièces uniques",
                    ],
                },
                {
                    "id": "ateliers",
                    "title": "Ateliers",
                    "body": (
                        "Une initiation pas à pas à la sculpture et au travail du bois "
                        "avec des outils à main."
                    ),
                    "items": [
                        "Sculpture de cuillère pour débutants : vous repartez avec la "
                        "vôtre",
                        "Travail du bois : les bases avec des outils à main",
                        "Ateliers de groupe pour écoles, entreprises et associations",
                        "Outils et bois fournis",
                    ],
                },
            ],
            "prices_title": "Tarifs",
            "prices": [
                ("Pièces", [
                    ("Cuillères et doseurs", "750 TL"),
                    ("Kuksas", "2 000 TL"),
                    ("Bols et boîtes", "2 500 TL"),
                ]),
                ("Ateliers", [
                    ("Sculpture de cuillère : 3 à 4 h, 4 à 8 personnes, bois et outils "
                     "fournis, par personne", "1 250 TL"),
                    ("Atelier de groupe pour une école, une entreprise ou une "
                     "association, 6 personnes au moins, par personne", "1 250 TL"),
                ]),
            ],
            "prices_note": (
                "Pour les pièces, le prix final dépend de la taille et du travail. Pour "
                "les plateaux, les pièces uniques et les ateliers de travail du bois, "
                "demandez-moi un devis. Les dates des ateliers ouverts seront "
                "annoncées sur cette page. Ateliers en turc ; pour l’anglais, "
                "demandez-moi."
            ),
            "contact_title": "Commandes et contact",
            "contact_text": (
                "Dites-moi en quelques mots ce que vous souhaitez : la pièce et sa "
                "taille, ou, pour un atelier, le nombre de personnes et une date. Je "
                "réponds sous un jour ouvré."
            ),
        },
    },
}

# One page per person, by the key TEAM and the navigation use.
WORK_PAGES = {"maths": MATHS, "woodwork": WOODWORK}

# The workshop page, in Turkish only: /atolye/
WORKSHOP = {
    "path": "atolye/",
    "title": "LaTeX ile Tez atölyesi, 28 Kasım 2026, online – YUXA",
    "description": (
        "Tez yazan yüksek lisans ve doktora öğrencileri için üç saatlik çevrim içi "
        "LaTeX atölyesi: 28 Kasım 2026 Cumartesi, 10.00–13.00. 600 TL; 20 Kasım’a "
        "kadar 450 TL."
    ),
    "kicker": "Atölye, 28 Kasım 2026",
    "heading": "LaTeX ile Tez",
    "lead": (
        "Tez yazan yüksek lisans ve doktora öğrencileri için üç saatlik, çevrim içi "
        "bir LaTeX atölyesi."
    ),
    "facts": [
        ("Tarih", "28 Kasım 2026 Cumartesi, 10.00–13.00 (10 dakika ara)"),
        ("Yer", "Online, Google Meet"),
        ("Ücret", "600 TL; 20 Kasım’a kadar 450 TL"),
        ("Kontenjan", "20 kişi"),
        ("Önkoşul", "Yok. LaTeX bilgisi gerekmez; bir dizüstü bilgisayar ve ücretsiz "
                    "bir Overleaf hesabı yeterli."),
    ],
    "programme_title": "Program",
    "programme": [
        "On dakikada LaTeX; Overleaf ile çalışmak",
        "Enstitü şablonu: kapak, ön sayfalar, bölümler, numaralandırma",
        "Kaynakça: BibLaTeX ve Zotero",
        "Şekiller, tablolar ve matematik",
        "Teslim öncesi kontrol listesi; sorular",
    ],
    "takeaways_title": "Yanınızda kalanlar",
    "takeaways": [
        "Kendi enstitünüzün kurallarına göre derlenen bir tez iskeleti",
        "Kaynakça, şekil ve tablolar için hazır kalıplar",
        "Teslim öncesi kontrol listesi (PDF)",
        "31 Aralık’a kadar tez şablonu kurulumunda %15 indirim",
    ],
    # The same facts for search engines: Turkish time, prices in TL with the
    # moments each is on sale from and until.
    "start": "2026-11-28T10:00:00+03:00",
    "end": "2026-11-28T13:00:00+03:00",
    "capacity": 20,
    "offers": [
        ("450", "2026-10-29T00:00:00+03:00", "2026-11-20T23:59:59+03:00"),
        ("600", "2026-11-21T00:00:00+03:00", "2026-11-28T10:00:00+03:00"),
    ],
    "register_title": "Kayıt",
    "register_text": (
        "Kaydolduktan sonra ödeme bilgilerini iletiyorum; yeriniz ödemeyle "
        "kesinleşir."
    ),
    "register_form": "Kayıt formu",
    "register_email": "E-postayla kaydolun",
    "register_subject": "Atölye kaydı: LaTeX ile Tez",
    "who": (
        "Atölyeyi Abdullah Uyu veriyor. Galatasaray Üniversitesi Matematik "
        "Bölümü’nü bitirdi, aynı üniversitede yüksek lisans yapıyor ve onlarca "
        "belgeyi LaTeX ile dizdi."
    ),
}
