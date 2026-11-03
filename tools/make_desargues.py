#!/usr/bin/env python3
"""Draw the figure of Abdullah Uyu's card on the home page: Desargues's
theorem, which his graduation project formalized in Lean.

Two triangles in perspective from a point have their three pairs of
corresponding sides meeting on one line, the axis. Writes
assets/desargues.svg (600 x 400, the aspect ratio of the photographs) in
the house colours of style.css, with their dark variants:

    python3 tools/make_desargues.py

The figure is computed, not traced: the second triangle is the first seen
from the centre, each vertex pushed out along its ray, and the three meeting
points come out collinear because the theorem says so; figure() checks it.
"""
from pathlib import Path

WIDTH, HEIGHT = 600, 400
# Panel, muted, ink and accent of style.css: light, then dark.
LIGHT = {"bg": "#e3e9d6", "muted": "#676470", "ink": "#221321", "accent": "#00601f"}
DARK = {"bg": "#303332", "muted": "#969faf", "ink": "#eaf2ef", "accent": "#7fca5a"}

# The centre, the first triangle and how far out along each ray the second
# triangle's vertices lie; chosen so that every point falls well inside.
CENTRE = (58, 192)
TRIANGLE = ((222, 277), (115, 253), (223, 197))
RATIOS = (1.85, 2.58, 1.42)


def meet(p, q, r, s):
    """The intersection of the line pq with the line rs."""
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p, q, r, s
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    a, b = x1 * y2 - y1 * x2, x3 * y4 - y3 * x4
    return ((a * (x3 - x4) - (x1 - x2) * b) / d, (a * (y3 - y4) - (y1 - y2) * b) / d)


def along(p, q, t):
    """The point p + t(q - p)."""
    return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))


def nearer(p, v, w):
    """Of v and w, the one nearer to p."""
    return min((v, w), key=lambda u: (u[0] - p[0]) ** 2 + (u[1] - p[1]) ** 2)


def num(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def line(p, q, cls):
    return (f'<line class="{cls}" x1="{num(p[0])}" y1="{num(p[1])}" '
            f'x2="{num(q[0])}" y2="{num(q[1])}"/>')


def dot(p, cls, r):
    return f'<circle class="{cls}" cx="{num(p[0])}" cy="{num(p[1])}" r="{r}"/>'


def rules(colours):
    return (f".bg{{fill:{colours['bg']}}}.ray,.ext{{stroke:{colours['muted']}}}"
            f".tri{{stroke:{colours['ink']}}}.pt{{fill:{colours['ink']}}}"
            f".axis{{stroke:{colours['accent']}}}.hit{{fill:{colours['accent']}}}")


def figure(centre, triangle, ratios):
    """The SVG of the configuration."""
    first = triangle
    second = tuple(along(centre, v, t) for v, t in zip(first, ratios))
    sides = ((0, 1), (1, 2), (2, 0))
    hits = [meet(first[i], first[j], second[i], second[j]) for i, j in sides]
    (x1, y1), (x2, y2), (x3, y3) = hits
    area = abs((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1))
    assert area < 1e-6 * WIDTH * HEIGHT, "the meeting points are not collinear"

    # The axis runs through the outermost meeting points, edge to edge.
    ends = max(((p, q) for p in hits for q in hits),
               key=lambda pq: (pq[0][0] - pq[1][0]) ** 2 + (pq[0][1] - pq[1][1]) ** 2)
    if abs(ends[1][1] - ends[0][1]) > abs(ends[1][0] - ends[0][0]):
        edges = ((0, 0), (WIDTH, 0)), ((0, HEIGHT), (WIDTH, HEIGHT))
    else:
        edges = ((0, 0), (0, HEIGHT)), ((WIDTH, 0), (WIDTH, HEIGHT))
    axis = [meet(*ends, *edge) for edge in edges]

    shapes = [f'<rect class="bg" width="{WIDTH}" height="{HEIGHT}"/>', line(*axis, "axis")]
    # Rays from the centre through each pair of vertices, a little beyond.
    shapes += [line(centre, along(centre, v, 1.06), "ray") for v in second]
    # Each pair of corresponding sides, extended from the side to the axis.
    for (i, j), hit in zip(sides, hits):
        for tri in (first, second):
            shapes.append(line(nearer(hit, tri[i], tri[j]), hit, "ext"))
    for tri in (first, second):
        points = " ".join(f"{num(x)},{num(y)}" for x, y in tri)
        shapes.append(f'<polygon class="tri" points="{points}"/>')
    shapes += [dot(v, "pt", 4) for v in first + second]
    shapes.append(dot(centre, "pt", 5))
    shapes += [dot(hit, "hit", 5.5) for hit in hits]

    style = ("line,polygon{fill:none;stroke-linecap:round;stroke-linejoin:round}"
             ".ray{stroke-width:1.25;opacity:.6}"
             ".ext{stroke-width:1.25;stroke-dasharray:3 5}"
             ".tri{stroke-width:2.25}.axis{stroke-width:2.5}"
             + rules(LIGHT) + "@media (prefers-color-scheme:dark){" + rules(DARK) + "}")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" '
            f'width="{WIDTH}" height="{HEIGHT}"><style>{style}</style>'
            + "".join(shapes) + "</svg>\n")


def main() -> None:
    out = Path(__file__).resolve().parent.parent / "assets" / "desargues.svg"
    out.write_text(figure(CENTRE, TRIANGLE, RATIOS))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
