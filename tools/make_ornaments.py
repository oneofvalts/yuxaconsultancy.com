#!/usr/bin/env python3
"""Draw the ornaments behind the headings of the work pages.

    python3 tools/make_ornaments.py

Writes two line drawings, used by style.css as masks, so that they take the
accent colour of either colour scheme:

- assets/cardioid.svg, for the maths pages and the workshop: N points on a
  circle, each joined to the point at twice its angle. The chords envelop a
  cardioid, the curve traced by a point of a circle rolling on another.
- assets/rings.svg, for the woodwork pages: growth rings as an end-grain cut
  shows them, closed curves around the pith that wander a little more with
  every year, and a few rays crossing them.

Both are computed, so the same script always draws the same figures.
"""
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SIZE = 600


def number(x: float) -> str:
    return f"{x:.1f}".rstrip("0").rstrip(".")


def svg(paths: list[str], width: float) -> str:
    body = "".join(f'<path d="{d}"/>' for d in paths)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}" '
            f'width="{SIZE}" height="{SIZE}"><g fill="none" stroke="#000" '
            f'stroke-width="{width}" stroke-linecap="round">{body}</g></svg>\n')


def cardioid(n: int = 144) -> str:
    """Chord from point k to point 2k of n on a circle, and the circle."""
    c, r = SIZE / 2, SIZE / 2 - 6
    point = [(c + r * math.cos(2 * math.pi * k / n + math.pi),
              c + r * math.sin(2 * math.pi * k / n + math.pi)) for k in range(n)]
    chords = []
    for k in range(1, n):
        (x1, y1), (x2, y2) = point[k], point[2 * k % n]
        if k != 2 * k % n:
            chords.append(f"M{number(x1)} {number(y1)}L{number(x2)} {number(y2)}")
    circle = (f"M{number(c - r)} {number(c)}a{number(r)} {number(r)} 0 1 0 "
              f"{number(2 * r)} 0a{number(r)} {number(r)} 0 1 0 {number(-2 * r)} 0")
    return svg([circle, "".join(chords)], 1)


def rings(years: int = 26) -> str:
    """Growth rings around an off-centre pith, and a few radial checks."""
    pith = (SIZE * 0.46, SIZE * 0.52)
    steps = 120
    paths = []
    base = 6.0
    for year in range(1, years + 1):
        # Good years and lean ones: the rings grow apart unevenly, and wander
        # more the further they are from the pith.
        base += 9 + 4 * math.sin(year * 2.3) + 2 * math.sin(year * 0.7)
        wobble = 0.4 + 0.08 * year
        points = []
        for i in range(steps):
            a = 2 * math.pi * i / steps
            r = (base
                 + wobble * (2.2 * math.sin(2 * a + 0.6) + 1.4 * math.sin(3 * a + year * 0.21)
                             + 0.8 * math.sin(5 * a + 1.3)))
            r *= 1 + 0.08 * math.cos(a - 0.5)  # the tree leaned: wider rings one side
            points.append((pith[0] + r * math.cos(a), pith[1] + r * math.sin(a)))
        d = "M" + "L".join(f"{number(x)} {number(y)}" for x, y in points) + "Z"
        paths.append(d)
    for a, inner, outer in ((0.35, 60, 205), (2.4, 90, 200), (4.1, 40, 215),
                            (5.3, 120, 195)):
        x1, y1 = pith[0] + inner * math.cos(a), pith[1] + inner * math.sin(a)
        x2, y2 = pith[0] + outer * math.cos(a), pith[1] + outer * math.sin(a)
        paths.append(f"M{number(x1)} {number(y1)}L{number(x2)} {number(y2)}")
    return svg(paths, 1.8)


def main() -> None:
    for name, drawing in (("cardioid", cardioid()), ("rings", rings())):
        path = ROOT / "assets" / f"{name}.svg"
        path.write_text(drawing)
        print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
