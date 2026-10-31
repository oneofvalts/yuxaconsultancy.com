#!/usr/bin/env python3
"""Build the static site for yuxaconsultancy.com.

    python3 build.py

Reads content.py and writes index.html, en/index.html, fr/index.html,
atolye/index.html, 404.html, sitemap.xml and robots.txt next to this file.
Standard library only; the output is committed and served by GitHub Pages.
"""

import html
import json
import re
from pathlib import Path
from urllib.parse import quote

import content as C

ROOT = Path(__file__).resolve().parent
NBSP, NNBSP = " ", " "

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


def document(*, lang, prefix, title, description, canonical, locale, body,
             jsonld=None, alternates=()):
    """A complete HTML page. prefix leads from the page to the site root."""
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
        f'<meta property="og:image" content="{url("assets/og.png")}">',
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


def header(*, page, prefix, current_lang, on_home):
    """Wordmark, section links and the language switch."""
    base = "" if on_home else f"{prefix}{page['path']}"
    sections = "".join(f'<a href="{base}#{page["ids"][key]}">{label}</a>'
                       for key, label in page["nav"])
    langs = []
    for code in C.LANGS:
        target = f"{prefix}{C.PAGES[code]['path']}" or "./"
        current = ' aria-current="page"' if code == current_lang and on_home else ""
        langs.append(f'<a href="{target}" hreflang="{code}" lang="{code}" '
                     f'title="{LANG_NAMES[code]}"{current}>{code.upper()}</a>')
    home = f"{prefix}{page['path']}" or "./"
    return (
        f'<a class="skip" href="#main">{page["skip"]}</a>\n'
        '<header class="site"><div class="wrap">\n'
        f'<a class="wordmark" href="{home}">YUXA</a>\n'
        f'<nav class="sections" aria-label="{page["nav_label"]}">{sections}</nav>\n'
        f'<nav class="langs" aria-label="Dil · Language · Langue">{"".join(langs)}</nav>\n'
        "</div></header>"
    )


def contact_buttons(page, *, email_label):
    buttons = []
    if C.WHATSAPP_LINK:
        buttons.append(f'<a class="btn primary" href="{C.WHATSAPP_LINK}" '
                       f'rel="noopener">{page["cta_whatsapp"]}</a>')
    booking = C.BOOKING_LINK or mailto(page["book_subject"])
    kind = "btn" if C.WHATSAPP_LINK else "btn primary"
    buttons.append(f'<a class="{kind}" href="{booking}">{page["cta_book"]}</a>')
    buttons.append(f'<a class="btn" href="{mailto(page["mail_subject"])}">'
                   f"{email_label}</a>")
    return '<div class="buttons">' + "".join(buttons) + "</div>"


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
    prefix = "../" if page["path"] else ""
    ids = page["ids"]

    cards = []
    for service in page["services"]:
        items = "".join(f"<li>{t(i)}</li>" for i in service["items"])
        cards.append(f'<article class="card"><h3>{t(service["title"])}</h3>'
                     f'<p>{t(service["body"])}</p><ul>{items}</ul></article>')
    steps = "".join(f"<li><strong>{t(a)}</strong> {t(b)}</li>" for a, b in page["how"])
    price_groups = []
    for name, rows in page["prices"]:
        body = "".join(f"<tr><td>{t(item)}</td><td>{t(price)}</td></tr>"
                       for item, price in rows)
        price_groups.append(f'<div><h3>{t(name)}</h3>'
                            f'<table class="price"><tbody>{body}</tbody></table></div>')
    team = "".join(
        f'<article class="person"><h3>{m["name"]}</h3>'
        f'<p class="role">{t(m["role"][lang])}</p>'
        + "".join(f"<p>{t(p)}</p>" for p in m["bio"][lang])
        + "</article>"
        for m in C.TEAM)
    faq = "".join(f"<details><summary>{t(q)}</summary><p>{t(a)}</p></details>"
                  for q, a in page["faq"])
    note = (f'<p class="note">{t(page["contact_note"])}</p>'
            if C.WHATSAPP_LINK else "")

    body = "\n".join([
        header(page=page, prefix=prefix, current_lang=lang, on_home=True),
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
        '<div class="teaser">',
        f'<h2>{t(page["workshop_title"])}</h2>',
        f'<p>{t(page["workshop_text"])}</p>',
        f'<p><a href="{prefix}{C.WORKSHOP["path"]}">{t(page["workshop_link"])} →</a></p>',
        "</div>",
        "</div></section>",
        f'<section id="{ids["team"]}"><div class="wrap">',
        f'<h2>{t(page["team_title"])}</h2>',
        f'<div class="team">{team}</div>',
        "</div></section>",
        f'<section id="{ids["faq"]}"><div class="wrap">',
        f'<h2>{t(page["faq_title"])}</h2>',
        faq,
        "</div></section>",
        f'<section id="{ids["contact"]}"><div class="wrap">',
        f'<h2>{t(page["contact_title"])}</h2>',
        f'<p>{t(page["contact_text"])}</p>',
        contact_buttons(page, email_label=C.EMAIL),
        note,
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


def workshop_page():
    w, page = C.WORKSHOP, C.PAGES["tr"]
    t = lambda s: typo("tr", s)  # noqa: E731
    prefix = "../"
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
        header(page=page, prefix=prefix, current_lang="tr", on_home=False),
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
        header(page=page, prefix="/", current_lang="tr", on_home=False),
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
    paths = [C.PAGES[code]["path"] for code in C.LANGS] + [C.WORKSHOP["path"]]
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
    write(f"{C.WORKSHOP['path']}index.html", workshop_page())
    write("404.html", not_found_page())
    write("sitemap.xml", sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {url('sitemap.xml')}\n")


if __name__ == "__main__":
    main()
