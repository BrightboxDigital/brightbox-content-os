#!/usr/bin/env python3
"""Composite Brightbox branding onto an AI-generated background image.

Deterministic branding layer. The AI model generates the artwork; this adds the
logo, a category label, a short headline, and a readability scrim programmatically,
so text is always crisp and correct and the logo is the real file (never AI-rendered).

USAGE
  ./scripts/brand-overlay --background master.png \
      --headline "Does a small Google Ads budget work?" \
      --category "Google Ads and PPC" --out /tmp/branded.png

Output is 1200x675 by default (the WordPress featured ratio). Feed the result to
generate-image --source to produce all the derivatives and wire it in.

Requires ImageMagick. Uses shared/brand/logo-reversed.png (white logo) on the dark
scrim by default; pass --logo to override.
"""

import argparse
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
LOGO_DEFAULT = REPO / "shared" / "brand" / "logo.png"  # the purple-blue logo, on a white chip

# brand palette (matches the blog template)
NAVY = "#0A1530"
AMBER = "#FFC163"


def die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def main():
    ap = argparse.ArgumentParser(description="Composite Brightbox branding onto a background image")
    ap.add_argument("--background", required=True, help="AI-generated background image")
    ap.add_argument("--headline", required=True, help="short headline text (kept crisp, not AI text)")
    ap.add_argument("--category", default="", help="category eyebrow label")
    ap.add_argument("--logo", default=str(LOGO_DEFAULT), help="logo PNG (placed on a white chip)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--width", type=int, default=1200)
    ap.add_argument("--height", type=int, default=675)
    args = ap.parse_args()

    for p in (args.background, args.logo, FONT):
        if not Path(p).exists():
            die(f"not found: {p}")
    if not shutil_which("magick"):
        die("ImageMagick (magick) not found")

    W, H = args.width, args.height
    tmp = Path(subprocess.run(["mktemp", "-d"], capture_output=True, text=True).stdout.strip())
    try:
        bg = tmp / "bg.png"
        # 1. cover-crop the background to the target size
        subprocess.run(["magick", args.background, "-resize", f"{W}x{H}^",
                        "-gravity", "Center", "-extent", f"{W}x{H}", str(bg)], check=True)

        # 2. Smooth horizontal scrim: opaque navy at the far left fading to transparent
        #    toward the middle, so white text is readable and the right-side art shows.
        scrim = tmp / "scrim.png"
        subprocess.run(["magick", "-size", f"{H}x{W}",
                        "gradient:#0A1530F2-#0A153000",
                        "-rotate", "90", "-flop",
                        str(scrim)], check=True)
        composed = tmp / "composed.png"
        subprocess.run(["magick", str(bg), str(scrim), "-compose", "over", "-composite",
                        str(composed)], check=True)

        # 3. logo on a clean white rounded chip, top-left (so the colour logo always reads)
        chip = tmp / "chip.png"
        lw = 250
        subprocess.run(["magick", args.logo, "-trim", "+repage", "-resize", f"{lw}x",
                        "-bordercolor", "white", "-border", "22x22",
                        "(", "+clone", "-alpha", "extract",
                        "-draw", "fill black polygon 0,0 0,14 14,0 fill white circle 14,14 14,0",
                        "(", "+clone", "-flip", ")", "-compose", "Multiply", "-composite",
                        "(", "+clone", "-flop", ")", "-compose", "Multiply", "-composite",
                        ")", "-alpha", "off", "-compose", "CopyOpacity", "-composite",
                        str(chip)], check=False)
        if not chip.exists():
            subprocess.run(["magick", args.logo, "-trim", "+repage", "-resize", f"{lw}x",
                            "-bordercolor", "white", "-border", "22x22", str(chip)], check=True)

        # 4. stacked text block: eyebrow over a large headline, left column, no overlap.
        #    The headline caption fills a fixed box so it renders large and readable.
        text = tmp / "text.png"
        col_w = int(W * 0.58)
        headline_img = tmp / "hl.png"
        subprocess.run(["magick", "-background", "none", "-fill", "white", "-font", FONT,
                        "-size", f"{col_w}x260", "-gravity", "West",
                        f"caption:{args.headline}", "-trim", "+repage", str(headline_img)], check=True)
        stack = ["magick", "-background", "none"]
        if args.category:
            eyebrow = tmp / "eb.png"
            subprocess.run(["magick", "-background", "none", "-fill", AMBER, "-font", FONT,
                            "-pointsize", "27", "-kerning", "3",
                            f"label:{args.category.upper()}", str(eyebrow)], check=True)
            stack += [str(eyebrow), "-splice", "0x18"]  # transparent gap below eyebrow
        stack += [str(headline_img), "-gravity", "West", "-append", str(text)]
        subprocess.run(stack, check=True)

        # 5. compose: scrimmed bg + logo chip (top-left) + text block (left, vertically centred lower)
        parts = ["magick", str(composed),
                 str(chip), "-gravity", "NorthWest", "-geometry", "+52+48", "-composite",
                 str(text), "-gravity", "West", "-geometry", "+56+40", "-composite",
                 "-quality", "92", args.out]
        subprocess.run(parts, check=True)
        print(f"branded image written: {args.out}")
        subprocess.run(["magick", "identify", "-format", "  %wx%h  %b\n", args.out])
    finally:
        subprocess.run(["rm", "-rf", str(tmp)])


def shutil_which(name):
    from shutil import which
    return which(name)


if __name__ == "__main__":
    main()
