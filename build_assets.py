from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parent
SCREENSHOTS = PROJECT / "Design" / "AppStore" / "Final"
OUT = ROOT / "assets"

for source in sorted(SCREENSHOTS.glob("0[1-4]-*.png")):
    image = Image.open(source).convert("RGB")
    image.thumbnail((760, 1652), Image.Resampling.LANCZOS)
    image.save(OUT / "screenshots" / f"{source.stem}.webp", "WEBP", quality=86, method=6)

hero = Image.open(PROJECT / "AuroraAlert" / "Assets.xcassets" / "PukekoheAurora.imageset" / "pukekohe-aurora.png").convert("RGB")
web_hero = hero.copy()
web_hero.thumbnail((1800, 1350), Image.Resampling.LANCZOS)
web_hero.save(OUT / "aurora-hero.webp", "WEBP", quality=85, method=6)
hero = hero.resize((1200, 900), Image.Resampling.LANCZOS).crop((0, 135, 1200, 765))
hero = hero.filter(ImageFilter.GaussianBlur(1.5))
overlay = Image.new("RGBA", hero.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)
for y in range(630):
    alpha = int(65 + 135 * y / 629)
    draw.line((0, y, 1200, y), fill=(12, 4, 18, alpha))
hero = Image.alpha_composite(hero.convert("RGBA"), overlay)

font_paths = [
    "/System/Library/Fonts/SFNSRounded.ttf",
    "/System/Library/Fonts/SFNS.ttf",
]
font_path = next(Path(path) for path in font_paths if Path(path).exists())
title = ImageFont.truetype(str(font_path), 84)
body = ImageFont.truetype(str(font_path), 35)
draw = ImageDraw.Draw(hero)
draw.text((70, 365), "Know when to look up.", font=title, fill="white")
draw.text((74, 475), "Aurora Heads Up", font=body, fill=(255, 157, 203))
draw.text((74, 525), "A calm, local answer for your sky tonight.", font=body, fill=(232, 224, 237))
hero.convert("RGB").save(OUT / "aurora-heads-up-social.jpg", quality=91, progressive=True)

icon = Image.open(OUT / "app-icon.png").convert("RGB")
icon.resize((192, 192), Image.Resampling.LANCZOS).save(OUT / "app-icon-192.png", quality=95)
icon.resize((512, 512), Image.Resampling.LANCZOS).save(OUT / "app-icon-512.png", quality=95)
