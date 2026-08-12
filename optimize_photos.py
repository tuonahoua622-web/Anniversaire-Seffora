import os
from PIL import Image

dst = r"C:\Users\DELL\OneDrive\Desktop\Anniversaire\photos"
for i in range(1, 7):
    p = os.path.join(dst, f"photo{i}.jpg")
    im = Image.open(p)
    im = im.convert("RGB")
    w, h = im.size
    if w > 900:
        ratio = 900 / w
        im = im.resize((900, int(h * ratio)), Image.LANCZOS)
    im.save(p, "JPEG", quality=82, optimize=True)
    print(f"photo{i}.jpg -> {im.size} {os.path.getsize(p)//1024} KB")
