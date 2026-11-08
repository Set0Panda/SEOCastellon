#!/usr/bin/env python3
"""Generates the share-preview cards (og-es/va/en.png), the Apple touch icon and
the SVG favicon. Text and colour only; no stock imagery.

Run:  python3 src/make_images.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

BG = (250, 248, 244)
INK = (29, 35, 48)
MUTED = (88, 96, 114)
ACCENT = (194, 65, 12)
OK = (22, 101, 52)
LINE = (227, 223, 214)

CARDS = {
    "es": ("NEGOCIOS DE CASTELLÓN", "Tu ficha de Google, bien hecha.",
           "Test gratuito de 2 minutos y arreglo en 48 horas.",
           ["Precio cerrado", "Sin permanencia", "Sin darme tu contraseña"]),
    "va": ("NEGOCIS DE CASTELLÓ", "La teua fitxa de Google, ben feta.",
           "Test gratuït de 2 minuts i arranjament en 48 hores.",
           ["Preu tancat", "Sense permanència", "Sense donar contrasenya"]),
    "en": ("CASTELLÓN BUSINESSES", "Your Google profile, done properly.",
           "Free 2-minute test and a 48-hour fix.",
           ["Fixed price", "No lock-in", "No password needed"]),
}


def wrap(draw, text, font, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def spaced(draw, xy, text, font, fill, spacing):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + spacing


def card(code):
    eyebrow, headline, sub, facts = CARDS[code]
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 22, H], fill=ACCENT)

    left = 90
    spaced(d, (left, 70), eyebrow, ImageFont.truetype(SANS_B, 26), ACCENT, 4)

    f_head = ImageFont.truetype(SERIF_B, 84)
    lines = wrap(d, headline, f_head, W - left - 80)
    y = 150
    for ln in lines:
        d.text((left, y), ln, font=f_head, fill=INK)
        y += 104

    d.text((left, y + 14), sub, font=ImageFont.truetype(SANS, 36), fill=MUTED)

    d.line([left, H - 130, W - 80, H - 130], fill=LINE, width=2)
    f_fact = ImageFont.truetype(SANS_B, 28)
    x = left
    for fact in facts:
        d.text((x, H - 95), "✓", font=f_fact, fill=OK)
        d.text((x + 38, H - 95), fact, font=ImageFont.truetype(SANS, 28), fill=INK)
        x += 38 + d.textlength(fact, font=ImageFont.truetype(SANS, 28)) + 36
    im.save(os.path.join(ROOT, f"og-{code}.png"), optimize=True)


def apple_icon():
    S = 180
    im = Image.new("RGB", (S, S), ACCENT)
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(SANS_B, 120)
    w = d.textlength("✓", font=f)
    d.text(((S - w) / 2, 18), "✓", font=f, fill=(255, 255, 255))
    im.save(os.path.join(ROOT, "apple-touch-icon.png"), optimize=True)


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="14" fill="#c2410c"/>
  <path d="M17 33l10 10 20-22" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""

if __name__ == "__main__":
    for c in CARDS:
        card(c)
    apple_icon()
    with open(os.path.join(ROOT, "favicon.svg"), "w", encoding="utf-8") as fh:
        fh.write(FAVICON)
    print("images written")
