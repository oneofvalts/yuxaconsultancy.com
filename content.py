"""Words and settings for yuxaconsultancy.com; build.py turns them into HTML.

PAGES holds the home page in each language, TEAM the people of YUXA (adding
a person means adding an entry there), WORK_PAGES the pages that show one
person's work (the woodwork pages so far), WORKSHOP the workshop page.

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

LANGS = ["tr", "en", "fr"]

PAGES = {
    "tr": {
        "path": "",
        "locale": "tr_TR",
        "title": "YUXA Consultancy · Matematik, programlama, LaTeX dizgi ve ahşap · "
                 "İstanbul",
        "description": (
            "Üniversite matematiği ve programlama, IB ve Fransızca matematik, GSÜ "
            "Fransızca hazırlık; LaTeX ile tez dizgisi; n8n ile otomasyon; elde "
            "oyulmuş ahşap ve oyma atölyeleri. Online ya da İstanbul’da yüz yüze."
        ),
        "skip": "İçeriğe geç",
        "ids": {"services": "hizmetler", "how": "nasil", "prices": "ucretler",
                "workshops": "atolye", "team": "ekip", "faq": "sss",
                "contact": "iletisim"},
        "nav_label": "Bölümler",
        "nav": [
            ("services", "Hizmetler"),
            ("prices", "Ücretler"),
            ("woodwork", "Ahşap"),
            ("workshops", "Atölyeler"),
            ("team", "Ekip"),
            ("contact", "İletişim"),
        ],
        "hero_title": "Matematik, bilgisayar, dizgi ve ahşap.",
        "hero_lead": (
            "Türkçe, Fransızca ve İngilizce özel ders; LaTeX ile tez ve belge "
            "dizgisi; küçük ekipler için otomasyon; elde oyulmuş ahşap ve oyma "
            "atölyeleri. Dersler online ya da İstanbul’da yüz yüze: Beşiktaş, "
            "Kadıköy, Üsküdar, Pendik–Tuzla."
        ),
        "cta_whatsapp": "WhatsApp’tan yazın",
        "cta_book": "Ücretsiz ön görüşme",
        "cta_email": "E-posta gönderin",
        "mail_subject": "Bilgi talebi",
        "book_subject": "Ön görüşme",
        "services_title": "Hizmetler",
        "services": [
            {
                "title": "Özel ders",
                "by": "Abdullah Uyu",
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
                "by": "Abdullah Uyu",
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
                "by": "Abdullah Uyu",
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
            {
                "title": "Ahşap",
                "by": "Durmuş Uyu",
                "body": (
                    "Elde oyulmuş kaşık, ölçek, kuksa, kase ve kutu; oyma ve ahşap "
                    "işçiliği atölyeleri."
                ),
                "items": [
                    "Sipariş üzerine, her parça tek tek elde",
                    "Mutfak, sofra ve hediye için",
                    "Yeni başlayanlar için kaşık oyma",
                    "Okul, şirket ve dernekler için grup atölyeleri",
                ],
                "photo": "three-kuksas",
                "page": "woodwork",
                "link": "İşler ve atölyeler",
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
        "workshops_title": "Atölyeler",
        "workshops": [
            {
                "title": "LaTeX ile Tez",
                "by": "Abdullah Uyu",
                "text": (
                    "28 Kasım Cumartesi, 10.00–13.00, online. Şablondan teslime üç "
                    "saat. 600 TL; 20 Kasım’a kadar 450 TL."
                ),
                "link": "Ayrıntılar ve kayıt",
                "page": "workshop",
            },
            {
                "title": "Kaşık oyma",
                "by": "Durmuş Uyu",
                "text": (
                    "Yeni başlayanlar için, 3–4 saat: aletler ve ahşap bizden, kaşık "
                    "sizin. Kişi başı 1.250 TL. Okul, şirket ve dernekler için grup "
                    "atölyeleri; açık atölyelerin tarihleri duyurulacak."
                ),
                "link": "Ayrıntılar",
                "page": "woodwork",
                "anchor": "atolyeler",
            },
        ],
        "team_title": "Ekip",
        "faq_title": "Sık sorulanlar",
        "faq": [
            ("Ödevimi ya da sınavımı yapar mısınız?",
             "Hayır. Notlu ödev, proje ya da sınav çözmüyoruz; konuyu öğretiyor, "
             "benzer sorularla hazırlıyoruz."),
            ("Ödeme nasıl?",
             "Dersten önce banka havalesiyle (IBAN/FAST) ya da yüz yüze derste nakit. "
             "Kamp ve atölyelerde yer, ödemeyle kesinleşir."),
            ("İptal edebilir miyim?",
             "24 saat öncesine kadar ücretsiz iptal ya da erteleme; daha geç "
             "iptallerde ders ücreti alınır."),
            ("Dersler nerede?",
             "Online (Google Meet) ya da yüz yüze: Beşiktaş, Kadıköy, Üsküdar ve "
             "Pendik–Tuzla. Yüz yüze derslerde 90 dakikalık blok öneririz."),
            ("Hangi dilde?",
             "Türkçe, Fransızca ya da İngilizce. GSÜ derslerinde terimler Fransızca, "
             "açıklama istediğiniz dilde."),
            ("18 yaşından küçük öğrenciler?",
             "Her şeyi veliyle konuşuruz; yüz yüze dersler evde bir veli varken ya da "
             "online yapılır."),
            ("Kişisel verilerim?",
             "İletişim bilgilerinizi yalnızca sizinle çalışmak için kullanırız ve "
             "kimseyle paylaşmayız."),
        ],
        "contact_title": "İletişim",
        "contact_text": (
            "Ne için yazdığınızı kısaca anlatın: ders ve seviyeniz, bir dizgi ya da "
            "otomasyon işi, ya da ahşap. En geç bir iş günü içinde döneriz."
        ),
        "contact_note": (
            "Mesajı tercih ediyoruz; bilinmeyen numaralardan gelen aramalar "
            "sessizdedir."
        ),
        "footer": "© 2026 YUXA Consultancy · İstanbul · Go yazı tipleriyle dizildi.",
    },
    "en": {
        "path": "en/",
        "locale": "en_GB",
        "title": "YUXA Consultancy · Mathematics, programming, LaTeX and woodwork · "
                 "Istanbul",
        "description": (
            "University mathematics and programming, IB and French-curriculum maths; "
            "thesis typesetting in LaTeX; automation with n8n; hand-carved woodwork "
            "and carving workshops. Online or in person in Istanbul."
        ),
        "skip": "Skip to content",
        "ids": {"services": "services", "how": "how", "prices": "prices",
                "workshops": "workshop", "team": "team", "faq": "faq",
                "contact": "contact"},
        "nav_label": "Sections",
        "nav": [
            ("services", "Services"),
            ("prices", "Prices"),
            ("woodwork", "Woodwork"),
            ("workshops", "Workshops"),
            ("team", "Team"),
            ("contact", "Contact"),
        ],
        "hero_title": "Mathematics, computing, typesetting and woodwork.",
        "hero_lead": (
            "Private lessons in Turkish, French or English; theses and documents "
            "typeset in LaTeX; automation for small teams; hand-carved woodwork and "
            "carving workshops. Lessons online, or in person in Istanbul: Beşiktaş, "
            "Kadıköy, Üsküdar, Pendik–Tuzla."
        ),
        "cta_whatsapp": "Message on WhatsApp",
        "cta_book": "Book a free call",
        "cta_email": "Send an e-mail",
        "mail_subject": "Enquiry",
        "book_subject": "Free call",
        "services_title": "Services",
        "services": [
            {
                "title": "Lessons",
                "by": "Abdullah Uyu",
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
                "by": "Abdullah Uyu",
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
                "by": "Abdullah Uyu",
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
            {
                "title": "Woodwork",
                "by": "Durmuş Uyu",
                "body": (
                    "Spoons, scoops, kuksas, bowls and boxes carved by hand; carving "
                    "and woodworking workshops."
                ),
                "items": [
                    "Made to order, each piece by hand",
                    "For the kitchen, the table and as gifts",
                    "Spoon carving for beginners",
                    "Group workshops for schools, companies and associations",
                ],
                "photo": "three-kuksas",
                "page": "woodwork",
                "link": "Work and workshops",
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
        "workshops_title": "Workshops",
        "workshops": [
            {
                "title": "LaTeX ile Tez (in Turkish)",
                "by": "Abdullah Uyu",
                "text": (
                    "Saturday 28 November, 10:00–13:00, online. From template to "
                    "submission in three hours. 600 TL, or 450 TL until 20 November."
                ),
                "link": "Details and registration (Turkish)",
                "page": "workshop",
            },
            {
                "title": "Spoon carving",
                "by": "Durmuş Uyu",
                "text": (
                    "For beginners, 3–4 h: we bring the tools and the wood, you take "
                    "your spoon home. 1,250 TL per person. Group workshops for schools, "
                    "companies and associations; dates of open workshops to be "
                    "announced."
                ),
                "link": "Details",
                "page": "woodwork",
                "anchor": "workshops",
            },
        ],
        "team_title": "Team",
        "faq_title": "Questions",
        "faq": [
            ("Will you do my homework or exam?",
             "No. We don’t do graded homework, projects or exams; we teach the subject "
             "and prepare you with similar problems."),
            ("How do I pay?",
             "By bank transfer (IBAN/FAST) before the lesson, or in cash at an "
             "in-person lesson. Clinic and workshop seats are confirmed on payment."),
            ("Can I cancel?",
             "Free cancellation or rescheduling up to 24 hours before; later "
             "cancellations are charged."),
            ("Where do lessons happen?",
             "Online (Google Meet), or in person in Beşiktaş, Kadıköy, Üsküdar and "
             "Pendik–Tuzla. For in-person lessons we recommend 90-minute blocks."),
            ("In which language?",
             "Turkish, French or English. For Galatasaray courses the terms stay in "
             "French and the explanations come in the language you prefer."),
            ("Pupils under 18?",
             "We agree everything with a parent; in-person lessons happen at home with "
             "a parent around, or online."),
            ("My personal data?",
             "We use your contact details only to work with you and never share "
             "them."),
        ],
        "contact_title": "Contact",
        "contact_text": (
            "Tell us briefly what it is about: a course and your level, a "
            "typesetting or automation job, or woodwork. We reply within one working "
            "day."
        ),
        "contact_note": "We prefer messages; calls from unknown numbers are silenced.",
        "footer": "© 2026 YUXA Consultancy · Istanbul · Set in the Go typefaces.",
    },
    "fr": {
        "path": "fr/",
        "locale": "fr_FR",
        "title": "YUXA Consultancy · Mathématiques, informatique, LaTeX et travail du "
                 "bois · Istanbul",
        "description": (
            "Cours de mathématiques en français, du collège à la terminale, bac et "
            "IB ; mathématiques universitaires et programmation ; composition de "
            "thèses en LaTeX ; objets en bois sculptés à la main et ateliers. À "
            "Istanbul ou en ligne."
        ),
        "skip": "Aller au contenu",
        "ids": {"services": "services", "how": "methode", "prices": "tarifs",
                "workshops": "atelier", "team": "equipe", "faq": "questions",
                "contact": "contact"},
        "nav_label": "Rubriques",
        "nav": [
            ("services", "Services"),
            ("prices", "Tarifs"),
            ("woodwork", "Bois"),
            ("workshops", "Ateliers"),
            ("team", "Équipe"),
            ("contact", "Contact"),
        ],
        "hero_title": "Mathématiques, informatique, mise en page et bois.",
        "hero_lead": (
            "Cours particuliers en français, en turc ou en anglais ; thèses et "
            "documents composés en LaTeX ; automatisation pour les petites équipes ; "
            "objets en bois sculptés à la main et ateliers de sculpture. Cours en "
            "ligne, ou à Istanbul : Beşiktaş, Kadıköy, Üsküdar, Pendik–Tuzla."
        ),
        "cta_whatsapp": "Écrire sur WhatsApp",
        "cta_book": "Réserver un appel gratuit",
        "cta_email": "Envoyer un e-mail",
        "mail_subject": "Demande de renseignements",
        "book_subject": "Appel découverte",
        "services_title": "Services",
        "services": [
            {
                "title": "Cours particuliers",
                "by": "Abdullah Uyu",
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
                "by": "Abdullah Uyu",
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
                "by": "Abdullah Uyu",
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
            {
                "title": "Travail du bois",
                "by": "Durmuş Uyu",
                "body": (
                    "Cuillères, doseurs, kuksas, bols et boîtes sculptés à la main ; "
                    "ateliers de sculpture et de travail du bois."
                ),
                "items": [
                    "Sur commande, chaque pièce faite à la main",
                    "Pour la cuisine, la table ou à offrir",
                    "Sculpture de cuillère pour débutants",
                    "Ateliers de groupe pour écoles, entreprises et associations",
                ],
                "photo": "three-kuksas",
                "page": "woodwork",
                "link": "Réalisations et ateliers",
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
        "workshops_title": "Ateliers",
        "workshops": [
            {
                "title": "LaTeX ile Tez (en turc)",
                "by": "Abdullah Uyu",
                "text": (
                    "Samedi 28 novembre, de 10 h à 13 h, en ligne. Du gabarit au dépôt "
                    "en trois heures. 600 TL, ou 450 TL jusqu’au 20 novembre."
                ),
                "link": "Détails et inscription (en turc)",
                "page": "workshop",
            },
            {
                "title": "Sculpture de cuillère",
                "by": "Durmuş Uyu",
                "text": (
                    "Pour débutants, 3 à 4 h : nous apportons les outils et le bois, "
                    "vous repartez avec votre cuillère. 1 250 TL par personne. Ateliers "
                    "de groupe pour écoles, entreprises et associations ; dates des "
                    "ateliers ouverts à venir."
                ),
                "link": "Détails",
                "page": "woodwork",
                "anchor": "ateliers",
            },
        ],
        "team_title": "L’équipe",
        "faq_title": "Questions fréquentes",
        "faq": [
            ("Faites-vous les devoirs ou les examens à la place de l’élève ?",
             "Non. Nous ne faisons ni devoirs notés, ni projets, ni examens ; nous "
             "enseignons la matière et entraînons l’élève sur des exercices "
             "semblables."),
            ("Comment payer ?",
             "Par virement (IBAN) avant la séance, ou en espèces lors d’une séance en "
             "présentiel. Les places en stage et en atelier sont confirmées au "
             "paiement."),
            ("Puis-je annuler ?",
             "Annulation ou report gratuits jusqu’à 24 h avant ; au-delà, la séance "
             "est due."),
            ("Où se déroulent les séances ?",
             "En ligne (Google Meet) ou à domicile à Beşiktaş, Kadıköy, Üsküdar et "
             "Pendik–Tuzla. En présentiel, nous recommandons des séances de 90 "
             "minutes."),
            ("Et pour les élèves mineurs ?",
             "Tout se décide avec un parent ; les séances ont lieu à domicile en "
             "présence d’un parent, ou en ligne."),
            ("Mes données personnelles ?",
             "Vos coordonnées servent uniquement à travailler avec vous et ne sont "
             "jamais partagées."),
        ],
        "contact_title": "Contact",
        "contact_text": (
            "Dites-nous en quelques mots ce qui vous amène : la matière et le niveau, "
            "un travail de composition ou d’automatisation, ou le bois. Nous répondons "
            "sous un jour ouvré."
        ),
        "contact_note": (
            "Nous préférons les messages ; les appels de numéros inconnus sont mis en "
            "silencieux."
        ),
        "footer": "© 2026 YUXA Consultancy · Istanbul · Composé en Go.",
    },
}

# The people of YUXA, in the order the team section lists them.
TEAM = [
    {
        "name": "Abdullah Uyu",
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
                "Onlarca belgeyi LaTeX ile dizdi. Bu site ve YUXA’nın bütün basılı "
                "işleri Go yazı tipiyle dizili; matematik için Go Math’i o hazırladı.",
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
                "He has typeset dozens of documents in LaTeX. This site and everything "
                "YUXA prints are set in Go; for mathematics he made Go Math.",
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
                "Il a composé des dizaines de documents en LaTeX. Ce site et tous les "
                "imprimés de YUXA sont composés en Go ; pour les mathématiques, il a "
                "créé Go Math.",
            ],
        },
    },
    {
        "name": "Durmuş Uyu",
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
        "page": "woodwork",
        "link": {
            "tr": "İşleri ve atölyeleri",
            "en": "His work and workshops",
            "fr": "Ses réalisations et ses ateliers",
        },
    },
]

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
    ("asymmetric-bowl-bottom", "Asimetrik kase, alttan", "Asymmetric bowl, from below",
     "Bol asymétrique, vu de dessous"),
    ("wooden-ashtray", "Küllük", "Ashtray", "Cendrier"),
    ("footed-tray-side", "Ayaklı tepsi", "Footed tray", "Plateau sur pieds"),
    ("footed-tray-bottom", "Ayaklı tepsi, alttan", "Footed tray, from below",
     "Plateau sur pieds, vu de dessous"),
]

# The woodwork pages: Durmuş's pieces and workshops, one page per language.
WOODWORK = {
    "person": "Durmuş Uyu",
    "photos": WOODWORK_PHOTOS,
    "photo_dir": "assets/woodwork/",
    "image": "assets/og-woodwork.jpg",  # social preview, made in the private repo
    "pages": {
        "tr": {
            "path": "ahsap/",
            "title": "El yapımı ahşap kaşık, kuksa ve oyma atölyeleri · "
                     "YUXA Consultancy",
            "description": (
                "Durmuş Uyu’nun elde oyduğu kaşık, ölçek, kuksa, kase ve kutular; "
                "sipariş üzerine yapım. Yeni başlayanlar için kaşık oyma, gruplar için "
                "ahşap işçiliği atölyeleri; İstanbul."
            ),
            "ids": {"gallery": "isler", "offers": "siparis-ve-atolyeler",
                    "contact": "iletisim"},
            "kicker": "Ahşap · Durmuş Uyu",
            "heading": "Elde oyulmuş ahşap.",
            "lead": (
                "Kaşık, ölçek, kuksa, kase ve kutu: her parça tek tek, elde yapılır. "
                "Sipariş üzerine yapım; yeni başlayanlar ve gruplar için oyma ve ahşap "
                "işçiliği atölyeleri."
            ),
            "mail_subject": "Ahşap",
            "gallery_title": "İşler",
            "gallery_note": (
                "Gördüğünüz parçalar satılmış olabilir; benzerlerini sipariş üzerine "
                "yapıyoruz. Elde yapıldıkları için hiçbiri ötekinin tıpkısı olmaz."
            ),
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
                        "Aletler ve ahşap bizden",
                    ],
                },
            ],
            # The price group also joins the price list of the home page.
            "prices_title": "Fiyatlar",
            "prices": ("Ahşap", [
                ("Kaşık ve ölçek", "750 TL’den"),
                ("Kuksa", "2.000 TL’den"),
                ("Kase ve kutu", "2.500 TL’den"),
                ("Kaşık oyma atölyesi: 3–4 saat, 4–8 kişi; ahşap ve aletler dahil",
                 "kişi başı 1.250 TL"),
                ("Okul, şirket ya da dernek için grup atölyesi, en az 6 kişi",
                 "kişi başı 1.250 TL"),
            ]),
            "offers_note": (
                "Parçalarda kesin fiyat ölçüye ve işçiliğe göre değişir. Tepsi ve tek "
                "parça işler ile ahşap işçiliği atölyelerinin fiyatı için yazın. Açık "
                "atölyelerin tarihleri bu sayfada duyurulacak."
            ),
            "care_title": "Bakım",
            "care": (
                "Ahşap mutfak eşyalarını elde, ılık suyla yıkayın; suda bekletmeyin, "
                "bulaşık makinesine koymayın. Kuruduktan sonra arada bir gıdaya uygun "
                "bir yağla silin."
            ),
            "contact_title": "Sipariş ve iletişim",
            "contact_text": (
                "Ne istediğinizi kısaca yazın: parça ve ölçü, ya da atölye için kişi "
                "sayısı ve tarih. En geç bir iş günü içinde döneriz."
            ),
            "back": "Ana sayfa",
        },
        "en": {
            "path": "en/woodwork/",
            "title": "Hand-carved wooden spoons, kuksas and carving workshops · "
                     "YUXA Consultancy",
            "description": (
                "Spoons, scoops, kuksas, bowls and boxes carved by hand by Durmuş Uyu, "
                "made to order. Spoon carving for beginners and woodworking workshops "
                "for groups in Istanbul."
            ),
            "ids": {"gallery": "work", "offers": "commissions-and-workshops",
                    "contact": "contact"},
            "kicker": "Woodwork · Durmuş Uyu",
            "heading": "Carved by hand.",
            "lead": (
                "Spoons, scoops, kuksas, bowls and boxes, each made one at a time, by "
                "hand. Made to order; carving and woodworking workshops for beginners "
                "and for groups."
            ),
            "mail_subject": "Woodwork",
            "gallery_title": "Work",
            "gallery_note": (
                "The pieces shown may already be sold; we make similar ones to order. "
                "Being handmade, no two are ever quite alike."
            ),
            "offers_title": "Commissions and workshops",
            "offers": [
                {
                    "id": "commissions",
                    "title": "Commissions",
                    "body": (
                        "For the kitchen, the table or as a gift: tell us what you have "
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
            "prices": ("Woodwork", [
                ("Spoons and scoops", "from 750 TL"),
                ("Kuksas", "from 2,000 TL"),
                ("Bowls and boxes", "from 2,500 TL"),
                ("Spoon carving: 3–4 h, 4–8 people, wood and tools included",
                 "1,250 TL per person"),
                ("Group workshop for a school, company or association, 6 people or "
                 "more", "1,250 TL per person"),
            ]),
            "offers_note": (
                "For pieces, the final price depends on the size and the work. For "
                "trays, one-off pieces and woodworking workshops, ask us for a price. "
                "Dates of open workshops will be announced on this page. Workshops are "
                "in Turkish; ask us about English."
            ),
            "care_title": "Care",
            "care": (
                "Wash wooden kitchenware by hand in warm water; do not soak it or put "
                "it in the dishwasher. Once dry, wipe it now and then with a food-safe "
                "oil."
            ),
            "contact_title": "Orders and contact",
            "contact_text": (
                "Tell us briefly what you would like: the piece and its size, or for a "
                "workshop the number of people and a date. We reply within one working "
                "day."
            ),
            "back": "Home",
        },
        "fr": {
            "path": "fr/bois/",
            "title": "Cuillères, kuksas et ateliers de sculpture sur bois · "
                     "YUXA Consultancy",
            "description": (
                "Cuillères, doseurs, kuksas, bols et boîtes sculptés à la main par "
                "Durmuş Uyu, sur commande. Ateliers de sculpture de cuillère pour "
                "débutants et de travail du bois pour les groupes, à Istanbul."
            ),
            "ids": {"gallery": "realisations", "offers": "commandes-et-ateliers",
                    "contact": "contact"},
            "kicker": "Bois · Durmuş Uyu",
            "heading": "Sculpté à la main.",
            "lead": (
                "Cuillères, doseurs, kuksas, bols et boîtes, chaque pièce faite à la "
                "main, une à une. Sur commande ; ateliers de sculpture et de travail du "
                "bois pour débutants et pour groupes."
            ),
            "mail_subject": "Travail du bois",
            "gallery_title": "Réalisations",
            "gallery_note": (
                "Les pièces présentées sont peut-être déjà vendues ; nous en faisons de "
                "semblables sur commande. Faites à la main, elles ne sont jamais tout à "
                "fait identiques."
            ),
            "offers_title": "Commandes et ateliers",
            "offers": [
                {
                    "id": "commandes",
                    "title": "Sur commande",
                    "body": (
                        "Pour la cuisine, la table ou pour offrir : dites-nous ce que "
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
            "prices": ("Travail du bois", [
                ("Cuillères et doseurs", "à partir de 750 TL"),
                ("Kuksas", "à partir de 2 000 TL"),
                ("Bols et boîtes", "à partir de 2 500 TL"),
                ("Sculpture de cuillère : 3 à 4 h, 4 à 8 personnes, bois et outils "
                 "fournis", "1 250 TL par personne"),
                ("Atelier de groupe pour une école, une entreprise ou une association, "
                 "6 personnes au moins", "1 250 TL par personne"),
            ]),
            "offers_note": (
                "Pour les pièces, le prix final dépend de la taille et du travail. Pour "
                "les plateaux, les pièces uniques et les ateliers de travail du bois, "
                "demandez-nous un devis. Les dates des ateliers ouverts seront "
                "annoncées sur cette page. Ateliers en turc ; pour l’anglais, "
                "demandez-nous."
            ),
            "care_title": "Entretien",
            "care": (
                "Lavez les ustensiles en bois à la main, à l’eau tiède ; ne les laissez "
                "pas tremper et évitez le lave-vaisselle. Une fois secs, passez-y de "
                "temps en temps une huile alimentaire."
            ),
            "contact_title": "Commandes et contact",
            "contact_text": (
                "Dites-nous en quelques mots ce que vous souhaitez : la pièce et sa "
                "taille, ou, pour un atelier, le nombre de personnes et une date. Nous "
                "répondons sous un jour ouvré."
            ),
            "back": "Accueil",
        },
    },
}

# Pages showing one person's work, by the key the navigation and TEAM use.
WORK_PAGES = {"woodwork": WOODWORK}

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
        "Kaydolduktan sonra ödeme bilgilerini iletiyoruz; yeriniz ödemeyle "
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
