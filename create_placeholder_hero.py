from pathlib import Path
from PIL import Image, ImageDraw

img_dir = Path(r'c:/Users/vidhi/coding/githubprojects/AirlineReservationSystemProject/dashboard/static/dashboard/img')
img_dir.mkdir(parents=True, exist_ok=True)
img_path = img_dir / 'hero.png'
width, height = 1600, 800
img = Image.new('RGB', (width, height), '#1d4ed8')
draw = ImageDraw.Draw(img)
for y in range(height):
    ratio = y / (height - 1)
    r = int(29 + ratio * (248 - 29))
    g = int(78 + ratio * (113 - 78))
    b = int(216 + ratio * (148 - 216))
    draw.line([(0, y), (width, y)], fill=(r, g, b))
plane = [
    (width * 0.2, height * 0.5),
    (width * 0.35, height * 0.44),
    (width * 0.8, height * 0.42),
    (width * 0.75, height * 0.5),
    (width * 0.8, height * 0.58),
    (width * 0.35, height * 0.56)
]
draw.polygon(plane, fill='white')
img.save(img_path, 'PNG')
print('Created', img_path)
