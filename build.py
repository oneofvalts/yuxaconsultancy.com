#!/usr/bin/env python3
"""Build the static site for yuxaconsultancy.com.

    python3 build.py

Reads content.py and writes, next to this file, the home page in each
language (index.html, en/, fr/), the work pages in each language (ahsap/,
en/woodwork/, fr/bois/), atolye/, 404.html, sitemap.xml and robots.txt.
Standard library only; the output is committed and served by GitHub Pages.
"""

import html
import json
import re
from pathlib import Path
from urllib.parse import quote

import content as C

ROOT = Path(__file__).resolve().parent
NBSP, NNBSP = "\u00a0", "\u202f"  # no-break space, narrow no-break space

LANG_NAMES = {"tr": "Türkçe", "en": "English", "fr": "Français"}


def typo(lang: str, text: str) -> str:
    """Unbreakable spaces between numbers and units; French spacing rules."""
    text = re.sub(r"(\d) (TL|dk|min|h)\b", r"\1" + NBSP + r"\2", text)
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
             image="assets/og.png", jsonld=None, alternates=()):
    """A complete HTML page. prefix leads from the page to the site root;
    image is the social preview, 1200 x 630."""
    head = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{esc(title)}</title>",
        f'<meta name="description" content="{esc(description)}">',
    ]
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
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="theme-color" content="#16212e">',
        f'<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">',
        f'<link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">',
        f'<link rel="preload" href="{prefix}assets/fonts/Go-Regular.woff2" as="font" '
        'type="font/woff2" crossorigin>',
        f'<link rel="stylesheet" href="{prefix}assets/style.css">',
    ]
    if jsonld:
        head.append('<script type="application/ld+json">'
                    + json.dumps(jsonld, ensure_ascii=False) + "</script>")
    head_html = "\n".join(head)
    return (f'<!doctype html>\n<html lang="{lang}">\n<head>\n{head_html}\n</head>\n'
            f"<body>\n{body}\n</body>\n</html>\n")


def header(*, lang, prefix, current):
    """Wordmark, section links and the language switch.

    current is "home", the key of a work page, or None for the pages in
    Turkish only. The home and work pages switch language in place; the
    others link to the home page of each language.
    """
    page = C.PAGES[lang]
    home = f"{prefix}{page['path']}" or "./"
    sections = []
    for key, label in page["nav"]:
        if key in page["ids"]:
            href = f"{'' if current == 'home' else home}#{page['ids'][key]}"
        else:
            href = f"{prefix}{page_path(key, lang)}"
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
        f'<nav class="langs" aria-label="Dil · Language · Langue">{"".join(langs)}</nav>\n'
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


def byline(name):
    return f'<p class="by">{name}</p>'


def price_table(rows, t):
    """Items and their prices; t applies the page language's typography."""
    body = "".join(f"<tr><td>{t(item)}</td><td>{t(price)}</td></tr>"
                   for item, price in rows)
    return f'<table class="price"><tbody>{body}</tbody></table>'


def footer(text):
    return f'<footer class="site"><div class="wrap"><p>{text}</p></div></footer>'


def organisation():
    return {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "YUXA Consultancy",
        "url": url(""),
        "email": f"mailto:{C.EMAIL}",
        "image": url("assets/og.png"),
        "address": {"@type": "PostalAddress", "addressLocality": "İstanbul",
                    "addressCountry": "TR"},
        "areaServed": ["Beşiktaş", "Kadıköy", "Üsküdar", "Pendik", "Tuzla"],
        "knowsLanguage": ["tr", "fr", "en"],
        "founder": {"@type": "Person", "name": "Abdullah Uyu"},
        "member": [{"@type": "Person", "name": m["name"]} for m in C.TEAM],
    }


def home_page(lang):
    page = C.PAGES[lang]
    t = lambda s: typo(lang, s)  # noqa: E731
    prefix = prefix_of(page["path"])
    ids = page["ids"]

    # Services are cards; one that shows a photograph links to its work page.
    cards, features = [], []
    for service in page["services"]:
        items = "".join(f"<li>{t(i)}</li>" for i in service["items"])
        text = (f'<h3>{t(service["title"])}</h3>{byline(service["by"])}'
                f'<p>{t(service["body"])}</p><ul>{items}</ul>')
        if "photo" not in service:
            cards.append(f'<article class="card">{text}</article>')
            continue
        spec = C.WORK_PAGES[service["page"]]
        target = f"{prefix}{page_path(service['page'], lang)}"
        img, _ = image(spec, service["photo"], caption(spec, service["photo"], lang),
                       prefix)
        features.append(
            f'<article class="card feature">'
            f'<a class="photo" href="{target}" tabindex="-1" aria-hidden="true">{img}</a>'
            f'<div>{text}<p><a href="{target}">{t(service["link"])} →</a></p></div>'
            "</article>")
    steps = "".join(f"<li><strong>{t(a)}</strong> {t(b)}</li>" for a, b in page["how"])
    # The price list ends with the price group of each work page that has one.
    groups = page["prices"] + [spec["pages"][lang]["prices"]
                               for spec in C.WORK_PAGES.values()
                               if "prices" in spec["pages"][lang]]
    price_groups = [f"<div><h3>{t(name)}</h3>{price_table(rows, t)}</div>"
                    for name, rows in groups]
    teasers = []
    for w in page["workshops"]:
        target = f"{prefix}{page_path(w['page'], lang)}"
        if "anchor" in w:
            target += f"#{w['anchor']}"
        teasers.append(f'<div class="teaser"><h3>{t(w["title"])}</h3>{byline(w["by"])}'
                       f'<p>{t(w["text"])}</p>'
                       f'<p><a href="{target}">{t(w["link"])} →</a></p></div>')
    team = []
    for m in C.TEAM:
        link = (f'<p><a href="{prefix}{page_path(m["page"], lang)}">'
                f'{t(m["link"][lang])} →</a></p>' if "page" in m else "")
        team.append(f'<article class="person"><h3>{m["name"]}</h3>'
                    f'<p class="role">{t(m["role"][lang])}</p>'
                    + "".join(f"<p>{t(p)}</p>" for p in m["bio"][lang])
                    + link + "</article>")
    faq = "".join(f"<details><summary>{t(q)}</summary><p>{t(a)}</p></details>"
                  for q, a in page["faq"])

    body = "\n".join([
        header(lang=lang, prefix=prefix, current="home"),
        '<main id="main">',
        '<div class="hero"><div class="wrap">',
        f'<h1>{t(page["hero_title"])}</h1>',
        f'<p class="lead">{t(page["hero_lead"])}</p>',
        contact_buttons(page, email_label=page["cta_email"]),
        "</div></div>",
        f'<section id="{ids["services"]}"><div class="wrap">',
        f'<h2>{t(page["services_title"])}</h2>',
        f'<div class="cards">{"".join(cards)}</div>',
        f'<p class="note notes-line">{t(page["notes_line"])}</p>',
        *features,
        "</div></section>",
        f'<section id="{ids["how"]}"><div class="wrap">',
        f'<h2>{t(page["how_title"])}</h2>',
        f'<ol class="steps">{steps}</ol>',
        "</div></section>",
        f'<section id="{ids["prices"]}"><div class="wrap">',
        f'<h2>{t(page["prices_title"])}</h2>',
        f'<div class="prices">{"".join(price_groups)}</div>',
        f'<p class="note">{t(page["prices_note"])}</p>',
        "</div></section>",
        f'<section id="{ids["workshops"]}"><div class="wrap">',
        f'<h2>{t(page["workshops_title"])}</h2>',
        f'<div class="teasers">{"".join(teasers)}</div>',
        "</div></section>",
        f'<section id="{ids["team"]}"><div class="wrap">',
        f'<h2>{t(page["team_title"])}</h2>',
        f'<div class="team">{"".join(team)}</div>',
        "</div></section>",
        f'<section id="{ids["faq"]}"><div class="wrap">',
        f'<h2>{t(page["faq_title"])}</h2>',
        faq,
        "</div></section>",
        f'<section id="{ids["contact"]}"><div class="wrap">',
        f'<h2>{t(page["contact_title"])}</h2>',
        f'<p>{t(page["contact_text"])}</p>',
        contact_buttons(page, email_label=C.EMAIL),
        "</div></section>",
        "</main>",
        footer(t(page["footer"])),
    ])
    alternates = [(code, url(C.PAGES[code]["path"])) for code in C.LANGS]
    alternates.append(("x-default", url("")))
    return document(lang=lang, prefix=prefix, title=page["title"],
                    description=page["description"],
                    canonical=url(page["path"]), locale=page["locale"],
                    body=body, jsonld=organisation(), alternates=alternates)


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
    """One person's work: photographs, what they offer, who they are."""
    spec, page = C.WORK_PAGES[key], C.PAGES[lang]
    w = spec["pages"][lang]
    t = lambda s: typo(lang, s)  # noqa: E731
    prefix = prefix_of(w["path"])
    person = next(m for m in C.TEAM if m["name"] == spec["person"])

    offers = []
    for offer in w["offers"]:
        items = "".join(f"<li>{t(i)}</li>" for i in offer["items"])
        offers.append(f'<article class="card" id="{offer["id"]}">'
                      f'<h3>{t(offer["title"])}</h3><p>{t(offer["body"])}</p>'
                      f"<ul>{items}</ul></article>")
    prices = (f'<div class="price-group"><h3>{t(w["prices_title"])}</h3>'
              f'{price_table(w["prices"][1], t)}</div>' if "prices" in w else "")
    bio = "".join(f"<p>{t(p)}</p>" for p in person["bio"][lang])
    buttons = dict(subject=w["mail_subject"], booking=False)

    body = "\n".join([
        header(lang=lang, prefix=prefix, current=key),
        '<main id="main">',
        '<div class="hero"><div class="wrap">',
        f'<p class="kicker">{t(w["kicker"])}</p>',
        f'<h1>{t(w["heading"])}</h1>',
        f'<p class="lead">{t(w["lead"])}</p>',
        contact_buttons(page, email_label=page["cta_email"], **buttons),
        "</div></div>",
        f'<section id="{w["ids"]["gallery"]}"><div class="wrap">',
        f'<h2>{t(w["gallery_title"])}</h2>',
        gallery(spec, lang, prefix),
        f'<p class="note">{t(w["gallery_note"])}</p>',
        "</div></section>",
        f'<section id="{w["ids"]["offers"]}"><div class="wrap">',
        f'<h2>{t(w["offers_title"])}</h2>',
        f'<div class="cards">{"".join(offers)}</div>',
        prices,
        f'<p class="note notes-line">{t(w["offers_note"])}</p>',
        "</div></section>",
        '<section><div class="wrap two">',
        f'<div><h2>{person["name"]}</h2>'
        f'<p class="role">{t(person["role"][lang])}</p>{bio}</div>',
        f'<div><h2>{t(w["care_title"])}</h2><p>{t(w["care"])}</p></div>',
        "</div></section>",
        f'<section id="{w["ids"]["contact"]}"><div class="wrap">',
        f'<h2>{t(w["contact_title"])}</h2>',
        f'<p>{t(w["contact_text"])}</p>',
        contact_buttons(page, email_label=C.EMAIL, **buttons),
        f'<p><a href="{prefix}{page["path"]}">← {t(w["back"])}</a></p>',
        "</div></section>",
        "</main>",
        footer(t(page["footer"])),
    ])
    jsonld = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": person["name"],
        "jobTitle": person["role"][lang],
        "url": url(w["path"]),
        "memberOf": {"@type": "Organization", "name": "YUXA Consultancy",
                     "url": url("")},
    }
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
    event = {
        "@context": "https://schema.org",
        "@type": "EducationEvent",
        "name": "LaTeX ile Tez",
        "description": w["description"],
        "startDate": "2026-11-28T10:00:00+03:00",
        "endDate": "2026-11-28T13:00:00+03:00",
        "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
        "eventStatus": "https://schema.org/EventScheduled",
        "inLanguage": "tr",
        "location": {"@type": "VirtualLocation", "url": url(w["path"])},
        "organizer": {"@type": "Organization", "name": "YUXA Consultancy",
                      "url": url("")},
        "offers": {"@type": "Offer", "price": "600", "priceCurrency": "TRY",
                   "url": url(w["path"]), "availability": "https://schema.org/InStock"},
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
        f'<p><a href="{prefix}">← {t(w["back"])}</a></p>',
        "</div></section>",
        "</main>",
        footer(t(page["footer"])),
    ])
    return document(lang="tr", prefix=prefix, title=w["title"],
                    description=w["description"], canonical=url(w["path"]),
                    locale="tr_TR", body=body, jsonld=event)


def not_found_page():
    page = C.PAGES["tr"]
    body = "\n".join([
        header(lang="tr", prefix="/", current=None),
        '<main id="main"><div class="hero"><div class="wrap">',
        "<h1>Sayfa bulunamadı.</h1>",
        '<p class="lead">Page not found · Page introuvable</p>',
        '<div class="buttons"><a class="btn primary" href="/">Ana sayfa</a>'
        '<a class="btn" href="/en/">Home</a><a class="btn" href="/fr/">Accueil</a></div>',
        "</div></div></main>",
        footer(typo("tr", page["footer"])),
    ])
    return document(lang="tr", prefix="/", title="Sayfa bulunamadı · YUXA Consultancy",
                    description=page["description"], canonical=None,
                    locale="tr_TR", body=body)


def sitemap():
    paths = [C.PAGES[code]["path"] for code in C.LANGS]
    paths += [page_path(key, code) for key in C.WORK_PAGES for code in C.LANGS]
    paths.append(C.WORKSHOP["path"])
    urls = "".join(f"<url><loc>{url(p)}</loc></url>\n" for p in paths)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}</urlset>\n")


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    print(f"wrote {path}")


def main() -> None:
    for lang in C.LANGS:
        write(f"{C.PAGES[lang]['path']}index.html", home_page(lang))
    for key in C.WORK_PAGES:
        for lang in C.LANGS:
            write(f"{page_path(key, lang)}index.html", work_page(key, lang))
    write(f"{C.WORKSHOP['path']}index.html", workshop_page())
    write("404.html", not_found_page())
    write("sitemap.xml", sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {url('sitemap.xml')}\n")


if __name__ == "__main__":
    main()
