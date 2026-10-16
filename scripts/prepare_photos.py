"""Create restrained, web-ready crops from Shivam's supplied photos.

Only crop, tonal balance, modest color correction, and output sizing are
applied. No face synthesis, retouching, or structural edits are performed.
"""

import argparse
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

def grade(image: Image.Image, *, brightness: float, contrast: float, color: float) -> Image.Image:
    image = ImageEnhance.Brightness(image).enhance(brightness)
    image = ImageEnhance.Contrast(image).enhance(contrast)
    image = ImageEnhance.Color(image).enhance(color)
    return ImageEnhance.Sharpness(image).enhance(1.04)


def save_webp(image: Image.Image, destination: Path, max_size: tuple[int, int]) -> None:
    image.thumbnail(max_size, Image.Resampling.LANCZOS)
    image.save(destination, "WEBP", quality=90, method=6)


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare the supplied natural photos for the portfolio.")
    parser.add_argument("--portrait", type=Path, required=True, help="Original seated portrait")
    parser.add_argument("--event", type=Path, required=True, help="Original hackathon/event photo")
    args = parser.parse_args()

    portrait = ImageOps.exif_transpose(Image.open(args.portrait)).convert("RGB")
    # 4:5 crop: removes the busy wall lettering while retaining the real setting,
    # clothing, expression, and natural face detail.
    portrait = portrait.crop((190, 285, 850, 1110))
    portrait = grade(portrait, brightness=1.05, contrast=1.04, color=0.94)
    save_webp(portrait, ASSETS / "shivam-portrait.webp", (900, 1125))

    event = ImageOps.exif_transpose(Image.open(args.event)).convert("RGB")
    # Keep the event venue, face, and held badge in the crop.
    width, height = event.size
    top, bottom = int(height * 0.12), int(height * 0.88)
    event = event.crop((0, top, width, bottom))
    event = grade(event, brightness=0.99, contrast=1.04, color=0.95)
    save_webp(event, ASSETS / "shivam-event.webp", (1100, 1700))


if __name__ == "__main__":
    main()
