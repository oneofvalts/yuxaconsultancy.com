"""Words and settings for yuxaconsultancy.com; build.py turns them into HTML.

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
WHATSAPP_LINK = ""
# Google Calendar appointment schedule for the free 15-minute call.
# Empty: the booking buttons open an e-mail instead.
BOOKING_LINK = ""
# Google Form for the workshop. Empty: registration by e-mail.
WORKSHOP_FORM = ""

LANGS = ["tr", "en", "fr"]

PAGES = {
    "tr": {
        "path": "",
        "locale": "tr_TR",
        "title": "YUXA Consultancy · Matematik, programlama ve LaTeX dizgi · İstanbul",
        "description": (
            "Üniversite matematiği ve programlama, IB ve Fransızca matematik, GSÜ "
            "Fransızca hazırlık; LaTeX ile tez dizgisi; n8n ile otomasyon. Türkçe, "
            "Fransızca, İngilizce; online ya da İstanbul’da yüz yüze."
        ),
        "skip": "İçeriğe geç",
        "nav_label": "Bölümler",
        "nav": [
            ("hizmetler", "Hizmetler"),
            ("ucretler", "Ücretler"),
            ("atolye", "Atölye"),
            ("hakkimda", "Hakkımda"),
            ("iletisim", "İletişim"),
        ],
        "hero_title": "Matematik, bilgisayar ve dizgi.",
        "hero_lead": (
            "Türkçe, Fransızca ve İngilizce özel ders; LaTeX ile tez ve belge "
            "dizgisi; küçük ekipler için otomasyon. Online ya da İstanbul’da yüz "
            "yüze: Beşiktaş, Kadıköy, Üsküdar, Pendik–Tuzla."
        ),
        "cta_whatsapp": "WhatsApp’tan yazın",
        "cta_book": "Ücretsiz ön görüşme",
        "cta_email": "E-posta gönderin",
        "mail_subject": "Ders talebi",
        "book_subject": "Ön görüşme",
        "services_title": "Hizmetler",
        "services": [
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
                "body": "Tezler, makaleler ve sunumlar: kurallara uygun ve göze güzel.",
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
        "notes_line": (
            "Her dersten sonra, işlediğimiz konuların ve çözdüğümüz soruların "
            "dizilmiş kısa bir PDF özeti sizinle."
        ),
        "how_title": "Nasıl çalışır",
        "how": [
            ("Tanışalım.", "15 dakikalık ücretsiz bir görüşmede ihtiyacı, seviyeyi ve "
             "hedefi konuşuruz."),
            ("Çalışalım.", "Online (Google Meet) ya da yüz yüze; ödeme dersten önce "
             "banka havalesiyle."),
            ("Kalıcı olsun.", "Her dersten sonra dizilmiş özet notlar; her işin sonunda "
             "derlenmiş kaynak dosyalar."),
        ],
        "prices_title": "Ücretler",
        "prices": [
            ("Özel ders", [
                ("Online, birebir, 60 dk", "1.500 TL"),
                ("Yüz yüze, birebir, 60 dk", "1.800 TL"),
                ("Yüz yüze, birebir, 90 dk", "2.600 TL"),
                ("IB, A-level ve Fransız müfredatı, 60 dk",
                 "2.000 TL online<br>2.300 TL yüz yüze"),
                ("Vize/Final Kampı: 3–6 kişi, 120 dk", "kişi başı 800 TL"),
                ("Beş derslik paket", "%10 indirim"),
                ("Ön görüşme, 15 dk", "ücretsiz"),
            ]),
            ("LaTeX dizgi", [
                ("Hızlı düzeltme, 60 dakikaya kadar", "1.500 TL"),
                ("Enstitü kurallarına uygun tez şablonu", "5.000 TL"),
                ("Word’den LaTeX’e dönüşüm", "sayfa başı 150 TL<br>en az 3.000 TL"),
                ("Teslim öncesi biçim denetimi", "3.000 TL"),
                ("Beamer sunum, 20 slayda kadar", "3.500 TL"),
                ("TikZ şekil", "750–1.500 TL"),
            ]),
            ("Otomasyon ve yapay zekâ", [
                ("Değerlendirme: 90 dk görüşme ve yazılı plan", "3.500 TL"),
                ("Tek iş akışı, kurulmuş ve belgelenmiş", "12.000 TL’den"),
                ("Yapay zekâ koçluğu, 60 dk", "2.000 TL"),
            ]),
        ],
        "prices_note": (
            "Kasım 2026 ücretleridir. Yüz yüze dersler Beşiktaş, Kadıköy, Üsküdar ve "
            "Pendik–Tuzla’da."
        ),
        "workshop_title": "Atölye: LaTeX ile Tez",
        "workshop_text": (
            "28 Kasım Cumartesi, 10.00–13.00, online. Şablondan teslime üç saat. "
            "600 TL; 20 Kasım’a kadar 450 TL."
        ),
        "workshop_link": "Ayrıntılar ve kayıt",
        "about_title": "Hakkımda",
        "about": [
            "Ben Abdullah Uyu. Galatasaray Üniversitesi Matematik Bölümü’nü 2025’te "
            "bitirdim; aynı üniversitede yüksek lisans yapıyorum. Eğitimimi Fransızca "
            "aldım, İngilizceyi de akıcı konuşuyorum.",
            "2015’ten beri programlama yapıyorum (Python, C, C++, Scheme). Lisans "
            "bitirme projemde Desargues teoremini Lean ile biçimselleştirdim. Bir siber "
            "güvenlik araştırma şirketinde matematikçi danışman, Ziraat Teknoloji’de "
            "yapay zekâ uygulamaları alanında yazılım danışmanı olarak çalıştım; n8n "
            "ile ajan tabanlı iş akışları geliştirdim.",
            "Onlarca belgeyi LaTeX ile dizdim. Bu sitede ve basılı her şeyde Go yazı "
            "tipini kullanıyorum; matematik için Go Math’i hazırladım.",
        ],
        "faq_title": "Sık sorulanlar",
        "faq": [
            ("Ödevimi ya da sınavımı yapar mısınız?",
             "Hayır. Notlu ödev, proje ya da sınav çözmüyorum; konuyu öğretiyor, "
             "benzer sorularla hazırlıyorum."),
            ("Ödeme nasıl?",
             "Dersten önce banka havalesiyle (IBAN/FAST) ya da yüz yüze derste nakit. "
             "Kamp ve atölyelerde yer, ödemeyle kesinleşir."),
            ("İptal edebilir miyim?",
             "24 saat öncesine kadar ücretsiz iptal ya da erteleme; daha geç "
             "iptallerde ders ücreti alınır."),
            ("Dersler nerede?",
             "Online (Google Meet) ya da yüz yüze: Beşiktaş, Kadıköy, Üsküdar ve "
             "Pendik–Tuzla. Yüz yüze derslerde 90 dakikalık blok öneririm."),
            ("Hangi dilde?",
             "Türkçe, Fransızca ya da İngilizce. GSÜ derslerinde terimler Fransızca, "
             "açıklama istediğiniz dilde."),
            ("18 yaşından küçük öğrenciler?",
             "Her şeyi veliyle konuşurum; yüz yüze dersler evde bir veli varken ya da "
             "online yapılır."),
            ("Kişisel verilerim?",
             "İletişim bilgilerinizi yalnızca dersleri planlamak için kullanırım ve "
             "kimseyle paylaşmam."),
        ],
        "contact_title": "İletişim",
        "contact_text": (
            "Hangi ders ya da iş için yazdığınızı ve seviyenizi kısaca yazın; en geç "
            "bir iş günü içinde dönerim."
        ),
        "contact_note": (
            "Mesajı tercih ederim; bilinmeyen numaralardan gelen aramalar sessizdedir."
        ),
        "footer": "© 2026 YUXA Consultancy · İstanbul · Go yazı tipleriyle dizildi.",
    },
    "en": {
        "path": "en/",
        "locale": "en_GB",
        "title": "YUXA Consultancy · Mathematics, programming and LaTeX typesetting · Istanbul",
        "description": (
            "University mathematics and programming, IB and French-curriculum maths; "
            "thesis typesetting in LaTeX; automation with n8n. In Turkish, French or "
            "English; online or in person in Istanbul."
        ),
        "skip": "Skip to content",
        "nav_label": "Sections",
        "nav": [
            ("services", "Services"),
            ("prices", "Prices"),
            ("workshop", "Workshop"),
            ("about", "About"),
            ("contact", "Contact"),
        ],
        "hero_title": "Mathematics, computing and typesetting.",
        "hero_lead": (
            "Private lessons in Turkish, French or English; theses and documents "
            "typeset in LaTeX; automation for small teams. Online, or in person in "
            "Istanbul: Beşiktaş, Kadıköy, Üsküdar, Pendik–Tuzla."
        ),
        "cta_whatsapp": "Message on WhatsApp",
        "cta_book": "Book a free call",
        "cta_email": "Send an e-mail",
        "mail_subject": "Lesson enquiry",
        "book_subject": "Free call",
        "services_title": "Services",
        "services": [
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
                "body": "Theses, papers and slides that follow the rules and read well.",
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
                    "n8n workflows and AI agents for repetitive work, and one-to-one "
                    "coaching on using AI in your daily work."
                ),
                "items": [
                    "Automation audit with a written plan",
                    "Workflows built and documented",
                    "AI coaching",
                ],
            },
        ],
        "notes_line": (
            "After every lesson you get a short, typeset PDF of what we covered and "
            "solved."
        ),
        "how_title": "How it works",
        "how": [
            ("Meet.", "A free 15-minute call to agree on the need, the level and the "
             "goal."),
            ("Work.", "Online (Google Meet) or in person; payment by bank transfer "
             "before the lesson."),
            ("Keep it.", "Typeset notes after every lesson; compiled source files at "
             "the end of every job."),
        ],
        "prices_title": "Prices",
        "prices": [
            ("Lessons", [
                ("Online, one-to-one, 60 min", "1,500 TL"),
                ("In person, one-to-one, 60 min", "1,800 TL"),
                ("In person, one-to-one, 90 min", "2,600 TL"),
                ("IB, A-level and French curricula, 60 min",
                 "2,000 TL online<br>2,300 TL in person"),
                ("Exam clinic: 3–6 students, 120 min", "800 TL per student"),
                ("Five-lesson pack", "10% off"),
                ("First call, 15 min", "free"),
            ]),
            ("LaTeX typesetting", [
                ("Quick fix, up to 60 min", "1,500 TL"),
                ("Thesis template to your graduate school’s rules", "5,000 TL"),
                ("Word to LaTeX conversion", "150 TL a page<br>minimum 3,000 TL"),
                ("Format check before submission", "3,000 TL"),
                ("Beamer slides, up to 20", "3,500 TL"),
                ("TikZ figure", "750–1,500 TL"),
            ]),
            ("Automation and AI", [
                ("Audit: 90-min call and a written plan", "3,500 TL"),
                ("One workflow, built and documented", "from 12,000 TL"),
                ("AI coaching, 60 min", "2,000 TL"),
            ]),
        ],
        "prices_note": (
            "Prices as of November 2026. In-person lessons in Beşiktaş, Kadıköy, "
            "Üsküdar and Pendik–Tuzla."
        ),
        "workshop_title": "Workshop: LaTeX ile Tez (in Turkish)",
        "workshop_text": (
            "Saturday 28 November, 10:00–13:00, online. From template to submission "
            "in three hours. 600 TL, or 450 TL until 20 November."
        ),
        "workshop_link": "Details and registration (Turkish)",
        "about_title": "About me",
        "about": [
            "I’m Abdullah Uyu. I graduated in mathematics from Galatasaray University "
            "in 2025, where teaching is in French, and I’m now a master’s student "
            "there. I speak Turkish, French and English.",
            "I’ve been programming since 2015 (Python, C, C++, Scheme). For my "
            "graduation project I formalized Desargues’s theorem in Lean. I’ve worked "
            "as a mathematician consultant at a cyber-security research company and as "
            "a programmer consultant on AI applications at Ziraat Teknoloji, building "
            "agentic workflows in n8n.",
            "I’ve typeset dozens of documents in LaTeX. This site and everything I "
            "print are set in Go; for mathematics I made Go Math.",
        ],
        "faq_title": "Questions",
        "faq": [
            ("Will you do my homework or exam?",
             "No. I don’t do graded homework, projects or exams; I teach the subject "
             "and prepare you with similar problems."),
            ("How do I pay?",
             "By bank transfer (IBAN/FAST) before the lesson, or in cash at an "
             "in-person lesson. Clinic and workshop seats are confirmed on payment."),
            ("Can I cancel?",
             "Free cancellation or rescheduling up to 24 hours before; later "
             "cancellations are charged."),
            ("Where do lessons happen?",
             "Online (Google Meet), or in person in Beşiktaş, Kadıköy, Üsküdar and "
             "Pendik–Tuzla. For in-person lessons I recommend 90-minute blocks."),
            ("In which language?",
             "Turkish, French or English. For Galatasaray courses the terms stay in "
             "French and the explanations come in the language you prefer."),
            ("Pupils under 18?",
             "I agree everything with a parent; in-person lessons happen at home with "
             "a parent around, or online."),
            ("My personal data?",
             "I use your contact details only to arrange lessons and never share "
             "them."),
        ],
        "contact_title": "Contact",
        "contact_text": (
            "Tell me briefly which course or job it is about and your level; I reply "
            "within one working day."
        ),
        "contact_note": "I prefer messages; calls from unknown numbers are silenced.",
        "footer": "© 2026 YUXA Consultancy · Istanbul · Set in the Go typefaces.",
    },
    "fr": {
        "path": "fr/",
        "locale": "fr_FR",
        "title": "YUXA Consultancy · Mathématiques, informatique et composition LaTeX · Istanbul",
        "description": (
            "Cours de mathématiques en français, du collège à la terminale, bac et "
            "IB ; mathématiques universitaires et programmation ; composition de "
            "thèses en LaTeX. À Istanbul ou en ligne."
        ),
        "skip": "Aller au contenu",
        "nav_label": "Rubriques",
        "nav": [
            ("services", "Services"),
            ("tarifs", "Tarifs"),
            ("atelier", "Atelier"),
            ("a-propos", "À propos"),
            ("contact", "Contact"),
        ],
        "hero_title": "Mathématiques, informatique et mise en page.",
        "hero_lead": (
            "Cours particuliers en français, en turc ou en anglais ; thèses et "
            "documents composés en LaTeX ; automatisation pour les petites équipes. "
            "En ligne, ou à Istanbul : Beşiktaş, Kadıköy, Üsküdar, Pendik–Tuzla."
        ),
        "cta_whatsapp": "Écrire sur WhatsApp",
        "cta_book": "Réserver un appel gratuit",
        "cta_email": "Envoyer un e-mail",
        "mail_subject": "Demande de cours",
        "book_subject": "Appel découverte",
        "services_title": "Services",
        "services": [
            {
                "title": "Cours particuliers",
                "body": (
                    "Mathématiques du collège à la terminale : programme français, "
                    "lycées francophones, bac et IB ; mathématiques universitaires et "
                    "programmation ; français pour l’année préparatoire de "
                    "l’Université Galatasaray."
                ),
                "items": [
                    "Programme français et IB Diploma (maths AA et AI)",
                    "Analyse, algèbre linéaire, probabilités, mathématiques discrètes",
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
        "notes_line": (
            "Après chaque séance, une fiche de synthèse soigneusement composée (PDF) "
            "de ce que nous avons vu et résolu."
        ),
        "how_title": "Comment ça marche",
        "how": [
            ("Faisons connaissance.", "Un appel gratuit de 15 minutes pour cerner le "
             "besoin, le niveau et l’objectif."),
            ("Travaillons.", "En ligne (Google Meet) ou en présentiel ; paiement par "
             "virement avant la séance."),
            ("Gardez une trace.", "Une fiche composée après chaque séance ; les "
             "fichiers sources compilés à la fin de chaque travail."),
        ],
        "prices_title": "Tarifs",
        "prices": [
            ("Cours", [
                ("Collège, lycée, bac et IB, 60 min",
                 "2 000 TL en ligne<br>2 300 TL à domicile"),
                ("Université, en ligne, 60 min", "1 500 TL"),
                ("Université, en présentiel, 60 min", "1 800 TL"),
                ("Université, en présentiel, 90 min", "2 600 TL"),
                ("Stage de révision : 3 à 6 élèves, 120 min", "800 TL par élève"),
                ("Forfait de cinq séances", "−10 %"),
                ("Premier appel, 15 min", "offert"),
            ]),
            ("Composition LaTeX", [
                ("Correction rapide, jusqu’à 60 min", "1 500 TL"),
                ("Gabarit de thèse selon les règles de l’institut", "5 000 TL"),
                ("Conversion de Word vers LaTeX", "150 TL la page<br>minimum 3 000 TL"),
                ("Vérification avant dépôt", "3 000 TL"),
                ("Présentation Beamer, jusqu’à 20 diapositives", "3 500 TL"),
                ("Figure TikZ", "750–1 500 TL"),
            ]),
            ("Automatisation et IA", [
                ("Diagnostic : appel de 90 min et plan écrit", "3 500 TL"),
                ("Un flux construit et documenté", "à partir de 12 000 TL"),
                ("Accompagnement IA, 60 min", "2 000 TL"),
            ]),
        ],
        "prices_note": (
            "Tarifs de novembre 2026. Séances en présentiel à Beşiktaş, Kadıköy, "
            "Üsküdar et Pendik–Tuzla."
        ),
        "workshop_title": "Atelier : LaTeX ile Tez (en turc)",
        "workshop_text": (
            "Samedi 28 novembre, de 10 h à 13 h, en ligne. Du gabarit au dépôt en "
            "trois heures. 600 TL, ou 450 TL jusqu’au 20 novembre."
        ),
        "workshop_link": "Détails et inscription (en turc)",
        "about_title": "À propos",
        "about": [
            "Je m’appelle Abdullah Uyu. Diplômé en mathématiques de l’Université "
            "Galatasaray en 2025, où l’enseignement est en français, j’y prépare "
            "aujourd’hui un master. Je parle français, turc et anglais.",
            "Je programme depuis 2015 (Python, C, C++, Scheme). Pour mon projet de fin "
            "d’études, j’ai formalisé le théorème de Desargues en Lean. J’ai été "
            "mathématicien consultant dans une entreprise de recherche en "
            "cybersécurité, puis consultant en programmation au département des "
            "applications d’IA de Ziraat Teknoloji, où je construisais des flux "
            "agentiques avec n8n.",
            "J’ai composé des dizaines de documents en LaTeX. Ce site et tous mes "
            "imprimés sont composés en Go ; pour les mathématiques, j’ai créé Go Math.",
        ],
        "faq_title": "Questions fréquentes",
        "faq": [
            ("Faites-vous les devoirs ou les examens à la place de l’élève ?",
             "Non. Je ne fais ni devoirs notés, ni projets, ni examens ; j’enseigne la "
             "matière et j’entraîne l’élève sur des exercices semblables."),
            ("Comment payer ?",
             "Par virement (IBAN) avant la séance, ou en espèces lors d’une séance en "
             "présentiel. Les places en stage et en atelier sont confirmées au "
             "paiement."),
            ("Puis-je annuler ?",
             "Annulation ou report gratuits jusqu’à 24 h avant ; au-delà, la séance "
             "est due."),
            ("Où se déroulent les séances ?",
             "En ligne (Google Meet) ou à domicile à Beşiktaş, Kadıköy, Üsküdar et "
             "Pendik–Tuzla. En présentiel, je recommande des séances de 90 minutes."),
            ("Et pour les élèves mineurs ?",
             "Tout se décide avec un parent ; les séances ont lieu à domicile en "
             "présence d’un parent, ou en ligne."),
            ("Mes données personnelles ?",
             "Vos coordonnées servent uniquement à organiser les séances et ne sont "
             "jamais partagées."),
        ],
        "contact_title": "Contact",
        "contact_text": (
            "Indiquez-moi en quelques mots la matière, le niveau et l’objectif ; je "
            "réponds sous un jour ouvré."
        ),
        "contact_note": (
            "Je préfère les messages ; les appels de numéros inconnus sont mis en "
            "silencieux."
        ),
        "footer": "© 2026 YUXA Consultancy · Istanbul · Composé en Go.",
    },
}

# The workshop page, in Turkish only: /atolye/
WORKSHOP = {
    "path": "atolye/",
    "title": "LaTeX ile Tez · Atölye · 28 Kasım 2026 · YUXA Consultancy",
    "description": (
        "Tez yazan yüksek lisans ve doktora öğrencileri için üç saatlik çevrim içi "
        "LaTeX atölyesi: 28 Kasım 2026 Cumartesi, 10.00–13.00. 600 TL; 20 Kasım’a "
        "kadar 450 TL."
    ),
    "kicker": "Atölye · 28 Kasım 2026",
    "heading": "LaTeX ile Tez",
    "lead": (
        "Üç saatte şablondan teslime. Tez yazan yüksek lisans ve doktora öğrencileri "
        "için çevrim içi atölye."
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
    "register_title": "Kayıt",
    "register_text": (
        "Kaydolduktan sonra ödeme bilgilerini iletiyorum; yeriniz ödemeyle "
        "kesinleşir."
    ),
    "register_form": "Kayıt formu",
    "register_email": "E-postayla kaydolun",
    "register_subject": "Atölye kaydı: LaTeX ile Tez",
    "who": (
        "Atölyeyi Abdullah Uyu veriyor: Galatasaray Üniversitesi Matematik mezunu, "
        "yüksek lisans öğrencisi, onlarca LaTeX belgesinin dizgicisi."
    ),
    "back": "Ana sayfa",
}
