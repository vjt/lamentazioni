#!/usr/bin/env python3
"""Make site/static/og-default.jpg: 1200x630 link-preview image (WhatsApp/Telegram), < 300KB.
Host-run, needs Pillow + DejaVu fonts. Output is committed; rerun only to change the design."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADER = ROOT + '/site/themes/gloriousfuture/static/wp-content/themes/gloriousfuture/img/header.jpg'
OUT = ROOT + '/site/static/og-default.jpg'
FONTS = '/usr/share/fonts/truetype/dejavu/'
W, H = 1200, 630

src = Image.open(HEADER).convert('RGB')
# cover: scale the 900x180 header to full height, crop the middle (forest + light rays)
bg = src.resize((int(src.width * H / src.height), H), Image.LANCZOS)
x = (bg.width - W) // 2 + 250
bg = bg.crop((x, 0, x + W, H)).filter(ImageFilter.GaussianBlur(2))
bg = ImageEnhance.Brightness(bg).enhance(0.55)
# the sharp original header as a band across the middle
band = src.resize((W, int(src.height * W / src.width)), Image.LANCZOS)
bg.paste(band, (0, (H - band.height) // 2 - 40))

d = ImageDraw.Draw(bg)
title = ImageFont.truetype(FONTS + 'DejaVuSerif-Bold.ttf', 110)
sub = ImageFont.truetype(FONTS + 'DejaVuSerif.ttf', 34)
small = ImageFont.truetype(FONTS + 'DejaVuSans.ttf', 30)


def centered(y, text, font, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2 + 3, y + 3), text, font=font, fill=(0, 0, 0))
    d.text(((W - w) / 2, y), text, font=font, fill=fill)


centered(40, 'LAMENTAZIONI', title, (255, 255, 255))
centered(470, "Ci lamentiamo di tutto perche' AMIAMO NIENTE", sub, (240, 230, 140))
centered(515, "siamo PAZZI, non fateci CAZO", sub, (240, 230, 140))
centered(575, 'lamentazioni.diomaiale.com  ·  2005–2009', small, (220, 220, 220))
bg.save(OUT, 'JPEG', quality=82, optimize=True, progressive=True)
print(OUT, os.path.getsize(OUT))
