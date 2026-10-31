#!/usr/bin/env python3
"""Build the static site for yuxaconsultancy.com.

    python3 build.py

Reads content.py and writes, next to this file, the home page in each
language (index.html, en/, fr/), each person's work page in each language
(matematik/, en/maths/, fr/maths/; ahsap/, en/woodwork/, fr/bois/), atolye/,
404.html, sitemap.xml and robots.txt. Standard library only; the output is
committed and served by GitHub Pages.
"""

import html
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import quote

import content as C

ROOT = Path(__file__).resolve().parent
NBSP, NNBSP = "\u00a0", "\u202f"  # no-break space, narrow no-break space
JOINER = "\u2060"  # word joiner: no line break on either side

LANG_NAMES = {"tr": "Türkçe", "en": "English", "fr": "Français"}


def typo(lang: str, text: str) -> str:
    """Unbreakable spaces between numbers and units, unbreakable ranges of
    numbers; French spacing rules."""
    text = re.sub(r"(\d) (TL|dk|min|h)\b", r"\1" + NBSP + r"\2", text)
    text = re.sub(r"(\d)–(\d)", r"\1" + JOINER + "–" + JOINER + r"\2", text)
    if lang == "fr":
        text = re.sub(r"(\d) (\d{3})\b", r"\1" + NNBSP + r"\2", text)
        text = re.sub(r"(\d) %", r"\1" + NNBSP + "%", text)
        text = re.sub(r" :", NBSP + ":", text)
        text = re.sub(r" ([;!?])", NNBSP + r"\1", text)
    return text


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def mailto(subject: str) -> str:
    return f"mailto:{C.EMAIL}?subject={quote(subject)}"


def url(path: str) -> str:
    return f"{C.SITE}/{path}"


def prefix_of(path: str) -> str:
    """The relative way from the page at path back to the site root."""
    return "../" * path.count("/")


def page_path(key: str, lang: str) -> str:
    """Path of a page content.py refers to by key: the workshop or a work page."""
    if key == "workshop":
        return C.WORKSHOP["path"]
    return C.WORK_PAGES[key]["pages"][lang]["path"]


def jpeg_size(path: Path) -> tuple[int, int]:
    """Width and height of a JPEG file, read from its start-of-frame marker."""
    data = path.read_bytes()
    i = 2  # past the start-of-image marker
    while i + 9 <= len(data):
        marker = data[i + 1]
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            return (int.from_bytes(data[i + 7:i + 9], "big"),
                    int.from_bytes(data[i + 5:i + 7], "big"))
        i += 2 + int.from_bytes(data[i + 2:i + 4], "big")
    raise ValueError(f"{path}: no frame header")


def caption(spec, stem: str, lang: str) -> str:
    """The caption of one of a work page's photographs."""
    for name, *captions in spec["photos"]:
        if name == stem:
            return dict(zip(C.LANGS, captions))[lang]
    raise KeyError(stem)


def cover(spec, alt: str, prefix: str) -> str:
    """The <img> of a work page's cover: its picture on the home page."""
    path = spec["cover"]
    if path.endswith(".svg"):
        size = re.search(r'<svg[^>]* width="(\d+)" height="(\d+)"',
                         (ROOT / path).read_text())
        width, height = map(int, size.groups())
    else:
        width, height = jpeg_size(ROOT / path)
    return (f'<img src="{prefix}{path}" width="{width}" height="{height}" '
            f'alt="{esc(alt)}" decoding="async">')


def image(spec, stem: str, alt: str, prefix: str):
    """The <img> of a photograph's 1000 px copy, and the copy's aspect ratio."""
    path = f"{spec['photo_dir']}{stem}"
    for size in (1000, 2000):
        if not (ROOT / f"{path}-{size}.jpg").exists():
            raise SystemExit(f"{path}-{size}.jpg is missing: run `make photos` in "
                             "the private repository")
    width, height = jpeg_size(ROOT / f"{path}-1000.jpg")
    tag = (f'<img src="{prefix}{path}-1000.jpg" width="{width}" height="{height}" '
           f'alt="{esc(alt)}" loading="lazy" decoding="async">')
    return tag, width / height


def document(*, lang, prefix, title, description, canonical, locale, body,
             image="assets/og.png", jsonld=(), alternates=(), index=True):
    """A complete HTML page. prefix leads from the page to the site root;
    image is the social preview, 1200 x 630; jsonld the schema.org nodes
    describing the page; alternates the same page in each language."""
    head = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{esc(title)}</title>",
        f'<meta name="description" content="{esc(description)}">',
    ]
    if not index:
        head.append('<meta name="robots" content="noindex">')
    if canonical:
        head.append(f'<link rel="canonical" href="{canonical}">')
    head += [f'<link rel="alternate" hreflang="{h}" href="{u}">' for h, u in alternates]
    head += [
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="YUXA Consultancy">',
        f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(description)}">',
    ]
    if canonical:
        head.append(f'<meta property="og:url" content="{canonical}">')
    head += [
        f'<meta property="og:image" content="{url(image)}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        f'<meta property="og:locale" content="{locale}">',
    ]
    head += [f'<meta property="og:locale:alternate" content="{C.PAGES[h]["locale"]}">'
             for h, _ in alternates if h in C.PAGES and C.PAGES[h]["locale"] != locale]
    head += [
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="theme-color" content="#16212e">',
        f'<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">',
        f'<link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">',
    ]
    head += [f'<link rel="preload" href="{prefix}assets/fonts/{font}.woff2" as="font" '
             'type="font/woff2" crossorigin>' for font in ("Go-Regular", "Go-Medium")]
    head.append(f'<link rel="stylesheet" href="{prefix}assets/style.css">')
    if jsonld:
        graph = {"@context": "https://schema.org", "@graph": list(jsonld)}
        head.append('<script type="application/ld+json">'
                    + json.dumps(graph, ensure_ascii=False) + "</script>")
    head_html = "\n".join(head)
    return (f'<!doctype html>\n<html lang="{lang}">\n<head>\n{head_html}\n</head>\n'
            f"<body>\n{body}\n</body>\n</html>\n")


def header(*, lang, prefix, current):
    """Wordmark, the links to the work pages and to the contact section, and
    the language switch.

    current is "home", the key of a work page, or None for the pages in
    Turkish only. The home and work pages switch language in place and have a
    contact section of their own; the others link to the home page of each
    language and to its contact section.
    """
    page = C.PAGES[lang]
    home = f"{prefix}{page['path']}" or "./"
    if current == "home":
        ids, base = page["ids"], ""
    elif current in C.WORK_PAGES:
        ids, base = C.WORK_PAGES[current]["pages"][lang]["ids"], ""
    else:
        ids, base = page["ids"], home
    sections = []
    for key, label in page["nav"]:
        if key in C.WORK_PAGES:
            href = f"{prefix}{page_path(key, lang)}"
        else:
            href = f"{base}#{ids[key]}"
        mark = ' aria-current="page"' if key == current else ""
        sections.append(f'<a href="{href}"{mark}>{label}</a>')
    translated = current == "home" or current in C.WORK_PAGES
    langs = []
    for code in C.LANGS:
        path = (page_path(current, code) if current in C.WORK_PAGES
                else C.PAGES[code]["path"])
        mark = ' aria-current="page"' if translated and code == lang else ""
        target = f"{prefix}{path}" or "./"
        langs.append(f'<a href="{target}" hreflang="{code}" lang="{code}" '
                     f'title="{LANG_NAMES[code]}"{mark}>{code.upper()}</a>')
    return (
        f'<a class="skip" href="#main">{page["skip"]}</a>\n'
        '<header class="site"><div class="wrap">\n'
        f'<a class="wordmark" href="{home}">YUXA</a>\n'
        f'<nav class="sections" aria-label="{page["nav_label"]}">{"".join(sections)}</nav>\n'
        f'<nav class="langs" aria-label="Dil, Language, Langue">{"".join(langs)}</nav>\n'
        "</div></header>"
    )


def contact_buttons(page, *, email_label, subject=None, booking=True):
    """WhatsApp, the free call and e-mail; the first button is the primary one."""
    links = []
    if C.WHATSAPP_LINK:
        links.append(f'href="{C.WHATSAPP_LINK}" rel="noopener">{page["cta_whatsapp"]}')
    if booking:
        target = C.BOOKING_LINK or mailto(page["book_subject"])
        links.append(f'href="{target}">{page["cta_book"]}')
    links.append(f'href="{mailto(subject or page["mail_subject"])}">{email_label}')
    return ('<div class="buttons">'
            + "".join(f'<a class="btn{" primary" if i == 0 else ""}" {link}</a>'
                      for i, link in enumerate(links))
            + "</div>")


def price_table(rows, t):
    """Items and their prices; t applies the page language's typography."""
    body = "".join(f"<tr><td>{t(item)}</td><td>{t(price)}</td></tr>"
                   for item, price in rows)
    return f'<table class="price"><tbody>{body}</tbody></table>'


def section(anchor, title, *parts):
    """A section of a page: its anchor (None for none), heading and content."""
    opening = f'<section id="{anchor}">' if anchor else "<section>"
    return "\n".join([f'{opening}<div class="wrap">', f"<h2>{title}</h2>", *parts,
                      "</div></section>"])


def footer(text):
    return f'<footer class="site"><div class="wrap"><p>{text}</p></div></footer>'


# Structured data: one node per thing, linked by @id across the pages.
ORGANISATION, WEBSITE = url("#organisation"), url("#website")


def organisation(full=True):
    """YUXA itself; full on the home pages, a reference elsewhere."""
    node = {"@type": "ProfessionalService", "@id": ORGANISATION,
            "name": "YUXA Consultancy", "url": url("")}
    if full:
        node.update({
            "alternateName": "YUXA",
            "logo": url("assets/apple-touch-icon.png"),
            "image": url("assets/og.png"),
            "email": C.EMAIL,
            "address": {"@type": "PostalAddress", "addressLocality": "İstanbul",
                        "addressCountry": "TR"},
            "areaServed": {"@type": "City", "name": "İstanbul"},
            "knowsLanguage": C.LANGS,
            "founder": {"@id": person_id(C.TEAM[0])},
            "member": [{"@id": person_id(m)} for m in C.TEAM],
        })
    return node


def website():
    """The site, which gives search results its name."""
    return {"@type": "WebSite", "@id": WEBSITE, "name": "YUXA Consultancy",
            "alternateName": "YUXA", "url": url(""), "inLanguage": C.LANGS,
            "publisher": {"@id": ORGANISATION}}


def person_id(person):
    return url(page_path(person["page"], "tr")) + "#person"


def person_node(person, lang):
    """One of us, as their work page in lang describes them."""
    return {"@type": "Person", "@id": person_id(person), "name": person["name"],
            "jobTitle": person["role"][lang], "url": url(page_path(person["page"], lang)),
            "worksFor": {"@id": ORGANISATION}, **person.get("facts", {})}


def breadcrumbs(lang, name, path):
    """Home, then the page at path."""
    home = C.PAGES[lang]
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": home["home"],
         "item": url(home["path"])},
        {"@type": "ListItem", "position": 2, "name": name, "item": url(path)},
    ]}


def home_page(lang):
    """A panel for each person: what they do, a few prices and the way to
    their page; what is coming up; how to reach us. The page has no headline:
    its h1, the site's name, is for screen readers and search engines."""
    page = C.PAGES[lang]
    t = lambda s: typo(lang, s)  # noqa: E731
    prefix = prefix_of(page["path"])

    panels = []
    for person in C.TEAM:
        spec = C.WORK_PAGES[person["page"]]
        panel = spec["pages"][lang]["panel"]
        target = f"{prefix}{page_path(person['page'], lang)}"
        panels.append(
            '<article class="panel">'
            f'<a class="cover" href="{target}" tabindex="-1" aria-hidden="true">'
            f'{cover(spec, panel["alt"], prefix)}</a>'
            f'<p class="kicker">{person["name"]}</p>'
            f'<h2><a href="{target}">{t(panel["title"])}</a></h2>'
            f'<p>{t(panel["text"])}</p>{price_table(panel["rows"], t)}'
            f'<p><a class="btn" href="{target}">{t(panel["link"])}</a></p>'
            "</article>")
    upcoming = "".join(
        f'<p><span class="label">{t(page["upcoming_label"])}</span> '
        f'<strong>{t(event["title"])}</strong> {t(event["text"])} '
        f'<a href="{prefix}{page_path(event["page"], lang)}">{t(event["link"])}</a></p>'
        for event in page["upcoming"])

    body = "\n".join([
        header(lang=lang, prefix=prefix, current="home"),
        '<main id="main">',
        '<h1 class="visually-hidden">YUXA Consultancy</h1>',
        f'<div class="wrap panels">{"".join(panels)}</div>',
        f'<div class="upcoming"><div class="wrap">{upcoming}</div></div>' if upcoming else "",
        section(page["ids"]["contact"], t(page["contact_title"]),
                f'<p>{t(page["contact_text"])}</p>',
                contact_buttons(page, email_label=C.EMAIL, booking=False)),
        "</main>",
        footer(t(page["footer"])),
    ])
    alternates = [(code, url(C.PAGES[code]["path"])) for code in C.LANGS]
    alternates.append(("x-default", url("")))
    jsonld = [website(), organisation(), *(person_node(m, lang) for m in C.TEAM)]
    return document(lang=lang, prefix=prefix, title=page["title"],
                    description=page["description"],
                    canonical=url(page["path"]), locale=page["locale"],
                    body=body, jsonld=jsonld, alternates=alternates)


def gallery(spec, lang, prefix):
    """Photographs in justified rows; each opens its 2000 px copy."""
    figures = []
    for stem, *_ in spec["photos"]:
        text = caption(spec, stem, lang)
        img, ratio = image(spec, stem, text, prefix)
        figures.append(f'<figure style="--r:{ratio:.3f}">'
                       f'<a href="{prefix}{spec["photo_dir"]}{stem}-2000.jpg">{img}</a>'
                       f"<figcaption>{esc(text)}</figcaption></figure>")
    return '<div class="gallery">' + "".join(figures) + "</div>"


def work_page(key, lang):
    """One person's work, in the sections content.py lists before MATHS:
    photographs if any, what they offer and for how much, dated events, who
    they are, and how to reach them."""
    spec, page = C.WORK_PAGES[key], C.PAGES[lang]
    w = spec["pages"][lang]
    t = lambda s: typo(lang, s)  # noqa: E731
    prefix = prefix_of(w["path"])
    ids = w["ids"]
    person = next(m for m in C.TEAM if m["name"] == spec["person"])
    buttons = dict(subject=w["mail_subject"], booking=spec["booking"])

    sections = []
    if "photos" in spec:
        sections.append(section(ids["gallery"], t(w["gallery_title"]),
                                gallery(spec, lang, prefix),
                                f'<p class="note">{t(w["gallery_note"])}</p>'))
    offers = []
    for offer in w["offers"]:
        anchor = f' id="{offer["id"]}"' if "id" in offer else ""
        items = "".join(f"<li>{t(i)}</li>" for i in offer["items"])
        offers.append(f'<article class="card"{anchor}>'
                      f'<h3>{t(offer["title"])}</h3><p>{t(offer["body"])}</p>'
                      f"<ul>{items}</ul></article>")
    sections.append(section(
        ids["offers"], t(w["offers_title"]), f'<div class="cards">{"".join(offers)}</div>',
        f'<p class="note notes-line">{t(w["offers_note"])}</p>' if "offers_note" in w
        else ""))
    if "how" in w:
        steps = "".join(f"<li>{t(step)}</li>" for step in w["how"])
        sections.append(section(ids["how"], t(w["how_title"]),
                                f'<ol class="steps">{steps}</ol>'))
    groups = "".join(f"<div><h3>{t(name)}</h3>{price_table(rows, t)}</div>"
                     for name, rows in w["prices"])
    sections.append(section(ids["prices"], t(w["prices_title"]),
                            f'<div class="prices">{groups}</div>',
                            f'<p class="note">{t(w["prices_note"])}</p>'))
    if "events" in w:
        teasers = []
        for event in w["events"]:
            target = f"{prefix}{page_path(event['page'], lang)}"
            teasers.append(f'<div class="teaser"><h3>{t(event["title"])}</h3>'
                           f'<p>{t(event["text"])}</p>'
                           f'<p><a href="{target}">{t(event["link"])}</a></p></div>')
        sections.append(section(ids["events"], t(w["events_title"]),
                                f'<div class="teasers">{"".join(teasers)}</div>'))
    bio = "".join(f"<p>{t(p)}</p>" for p in person["bio"][lang])
    about = (f'<div><h2>{person["name"]}</h2>'
             f'<p class="role">{t(person["role"][lang])}</p>{bio}</div>')
    if "aside" in w:
        about += f'<div><h2>{t(w["aside_title"])}</h2><p>{t(w["aside"])}</p></div>'
    sections.append(f'<section class="about"><div class="wrap two">{about}</div></section>')
    sections.append(section(
        ids["contact"], t(w["contact_title"]), f'<p>{t(w["contact_text"])}</p>',
        contact_buttons(page, email_label=C.EMAIL, **buttons),
        f'<p><a href="{prefix}{page["path"]}">{t(page["back"])}</a></p>'))

    body = "\n".join([
        header(lang=lang, prefix=prefix, current=key),
        '<main id="main">',
        '<div class="hero"><div class="wrap">',
        f'<p class="kicker">{t(w["kicker"])}</p>',
        f'<h1>{t(w["heading"])}</h1>',
        f'<p class="lead">{t(w["lead"])}</p>',
        contact_buttons(page, email_label=page["cta_email"], **buttons),
        "</div></div>",
        *sections,
        "</main>",
        footer(t(page["footer"])),
    ])
    jsonld = [person_node(person, lang), organisation(full=False),
              breadcrumbs(lang, dict(page["nav"])[key], w["path"])]
    alternates = [(code, url(page_path(key, code))) for code in C.LANGS]
    alternates.append(("x-default", url(page_path(key, "tr"))))
    return document(lang=lang, prefix=prefix, title=w["title"],
                    description=w["description"], canonical=url(w["path"]),
                    locale=page["locale"], body=body, image=spec["image"],
                    jsonld=jsonld, alternates=alternates)


def workshop_page():
    w, page = C.WORKSHOP, C.PAGES["tr"]
    t = lambda s: typo("tr", s)  # noqa: E731
    prefix = prefix_of(w["path"])
    facts = "".join(f"<dt>{t(k)}</dt><dd>{t(v)}</dd>" for k, v in w["facts"])
    programme = "".join(f"<li>{t(i)}</li>" for i in w["programme"])
    takeaways = "".join(f"<li>{t(i)}</li>" for i in w["takeaways"])
    buttons = []
    if C.WORKSHOP_FORM:
        buttons.append(f'<a class="btn primary" href="{C.WORKSHOP_FORM}" '
                       f'rel="noopener">{w["register_form"]}</a>')
    kind = "btn" if C.WORKSHOP_FORM else "btn primary"
    buttons.append(f'<a class="{kind}" href="{mailto(w["register_subject"])}">'
                   f'{w["register_email"]}</a>')
    if C.WHATSAPP_LINK:
        buttons.append(f'<a class="btn" href="{C.WHATSAPP_LINK}" rel="noopener">'
                       f'{page["cta_whatsapp"]}</a>')
    teacher = next(m for m in C.TEAM if m["page"] == "maths")
    event = {
        "@type": "EducationEvent",
        "name": w["heading"],
        "description": w["description"],
        "startDate": w["start"],
        "endDate": w["end"],
        "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
        "eventStatus": "https://schema.org/EventScheduled",
        "inLanguage": "tr",
        "location": {"@type": "VirtualLocation", "url": url(w["path"])},
        "maximumAttendeeCapacity": w["capacity"],
        "organizer": organisation(full=False),
        "performer": {"@type": "Person", "@id": person_id(teacher),
                      "name": teacher["name"]},
        "offers": [{"@type": "Offer", "price": price, "priceCurrency": "TRY",
                    "validFrom": start, "validThrough": until, "url": url(w["path"]),
                    "availability": "https://schema.org/InStock"}
                   for price, start, until in w["offers"]],
        "image": url("assets/og.png"),
    }
    body = "\n".join([
        header(lang="tr", prefix=prefix, current=None),
        '<main id="main">',
        '<div class="hero"><div class="wrap">',
        f'<p class="kicker">{t(w["kicker"])}</p>',
        f'<h1>{t(w["heading"])}</h1>',
        f'<p class="lead">{t(w["lead"])}</p>',
        f'<dl class="facts">{facts}</dl>',
        "</div></div>",
        '<section><div class="wrap two">',
        f'<div><h2>{t(w["programme_title"])}</h2><ol class="plain">{programme}</ol></div>',
        f'<div><h2>{t(w["takeaways_title"])}</h2><ul class="plain">{takeaways}</ul></div>',
        "</div></section>",
        '<section id="kayit"><div class="wrap">',
        f'<h2>{t(w["register_title"])}</h2>',
        f'<p>{t(w["register_text"])}</p>',
        '<div class="buttons">' + "".join(buttons) + "</div>",
        f'<p class="note">{t(w["who"])}</p>',
        f'<p><a href="{prefix}">{t(page["back"])}</a></p>',
        "</div></section>",
        "</main>",
        footer(t(page["footer"])),
    ])
    return document(lang="tr", prefix=prefix, title=w["title"],
                    description=w["description"], canonical=url(w["path"]),
                    locale="tr_TR", body=body,
                    jsonld=[event, breadcrumbs("tr", w["heading"], w["path"])])


def not_found_page():
    page = C.PAGES["tr"]
    body = "\n".join([
        header(lang="tr", prefix="/", current=None),
        '<main id="main"><div class="hero"><div class="wrap">',
        "<h1>Sayfa bulunamadı.</h1>",
        '<p class="lead"><span lang="en">Page not found.</span> '
        '<span lang="fr">Page introuvable.</span></p>',
        '<div class="buttons"><a class="btn primary" href="/">Ana sayfa</a>'
        '<a class="btn" href="/en/">Home</a><a class="btn" href="/fr/">Accueil</a></div>',
        "</div></div></main>",
        footer(typo("tr", page["footer"])),
    ])
    return document(lang="tr", prefix="/", title="Sayfa bulunamadı – YUXA Consultancy",
                    description=page["description"], canonical=None,
                    locale="tr_TR", body=body, index=False)


def sitemap(lastmod):
    """Every page with the day it last changed: lastmod maps paths to dates."""
    urls = "".join(f"<url><loc>{url(p)}</loc><lastmod>{day}</lastmod></url>\n"
                   for p, day in lastmod.items())
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}</urlset>\n")


def write(path: str, text: str) -> bool:
    """Write text to path; whether that changed the file."""
    target = ROOT / path
    changed = not target.exists() or target.read_text(encoding="utf-8") != text
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    print(f"wrote {path}")
    return changed


def main() -> None:
    pages = {C.PAGES[lang]["path"]: lambda lang=lang: home_page(lang)
             for lang in C.LANGS}
    pages.update({page_path(key, lang): lambda key=key, lang=lang: work_page(key, lang)
                  for key in C.WORK_PAGES for lang in C.LANGS})
    pages[C.WORKSHOP["path"]] = workshop_page
    # A page keeps the date of its last change in the sitemap until it changes.
    old = ROOT / "sitemap.xml"
    known = dict(re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>",
                            old.read_text() if old.exists() else ""))
    today = date.today().isoformat()
    lastmod = {}
    for path, make in pages.items():
        changed = write(f"{path}index.html", make())
        lastmod[path] = today if changed or url(path) not in known else known[url(path)]
    write("404.html", not_found_page())
    write("sitemap.xml", sitemap(lastmod))
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {url('sitemap.xml')}\n")


if __name__ == "__main__":
    main()
