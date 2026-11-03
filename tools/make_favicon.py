#!/usr/bin/env python3
"""Draw the site icon: a white Go Medium "Y" on the accent colour.

Writes assets/favicon.svg. Needs fontTools and the Go fonts from TeX Live:

    python3 tools/make_favicon.py [path/to/Go-Medium.ttf]

The PNG touch icon is rendered from the SVG (see README.md).
"""
import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

GO_MEDIUM = "/usr/share/texmf-dist/fonts/truetype/bh/gofonts/Go-Medium.ttf"
ACCENT = "#00601F"
SIZE = 64          # viewBox side
GLYPH_HEIGHT = 40  # cap height of the drawn letter, in viewBox units


def main() -> None:
    font = TTFont(sys.argv[1] if len(sys.argv) > 1 else GO_MEDIUM)
    glyph_set = font.getGlyphSet()
    name = font.getBestCmap()[ord("Y")]
    glyph = glyph_set[name]

    # Bounding box of the outline, in font units.
    from fontTools.pens.boundsPen import BoundsPen
    bounds = BoundsPen(glyph_set)
    glyph.draw(bounds)
    x_min, y_min, x_max, y_max = bounds.bounds

    scale = GLYPH_HEIGHT / (y_max - y_min)
    width = (x_max - x_min) * scale
    dx = (SIZE - width) / 2 - x_min * scale
    dy = (SIZE + GLYPH_HEIGHT) / 2 + y_min * scale  # flip y: font y grows up

    pen = SVGPathPen(glyph_set, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    glyph.draw(TransformPen(pen, (scale, 0, 0, -scale, dx, dy)))

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}">'
        f'<rect width="{SIZE}" height="{SIZE}" rx="12" fill="{ACCENT}"/>'
        f'<path fill="#fff" d="{pen.getCommands()}"/></svg>\n'
    )
    out = Path(__file__).resolve().parent.parent / "assets" / "favicon.svg"
    out.write_text(svg)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
