from PIL import Image, ImageDraw, ImageFont
import math

def gen_icon(size, path):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx, cy = size / 2, size / 2
    r = size * 0.45

    # Background circle with gradient effect
    for i in range(int(r), 0, -1):
        ratio = i / r
        cr = int(12 + (16 - 12) * ratio)
        cg = int(18 + (32 - 18) * ratio)
        cb = int(34 + (50 - 34) * ratio)
        d.ellipse([cx - i, cy - i, cx + i, cy + i], fill=(cr, cg, cb, 255))

    # Green ring
    ring_w = size * 0.06
    for angle in range(0, 300):
        rad = math.radians(angle - 90)
        for t in range(int(ring_w)):
            rr = r - size * 0.08 - t
            x = cx + rr * math.cos(rad)
            y = cy + rr * math.sin(rad)
            g = int(181 + (100 - 181) * (angle / 300))
            if 0 <= x < size and 0 <= y < size:
                img.putpixel((int(x), int(y)), (16, g, 129, 255))

    # Leaf / checkmark shape
    leaf_size = size * 0.22
    pts = [
        (cx - leaf_size * 0.4, cy + leaf_size * 0.1),
        (cx - leaf_size * 0.05, cy + leaf_size * 0.45),
        (cx + leaf_size * 0.5, cy - leaf_size * 0.4),
    ]
    d.line(pts, fill=(16, 185, 129, 255), width=max(3, size // 40))

    # Days text
    try:
        fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size // 8)
    except:
        fnt = ImageFont.load_default()
    d.text((cx, cy + r * 0.45), "QUIT", fill=(148, 163, 184, 255), font=fnt, anchor="mm")

    img.save(path, 'PNG')
    print(f"Generated {path}")

gen_icon(192, 'icon-192.png')
gen_icon(512, 'icon-512.png')
