"""Quick compress - no rmtree, uses deploy2 folder"""
import os, shutil
from PIL import Image

BASE = r'C:\Users\user\Desktop\H5'
DEPLOY = os.path.join(BASE, 'deploy2')
EXCLUDE_DIRS = {'.git', '.edgeone', '.workbuddy', 'deploy', 'deploy2', '__pycache__'}
MAX_WIDTH, JPEG_QUALITY = 1500, 75

os.makedirs(DEPLOY, exist_ok=True)

total_orig, total_comp, img_count = 0, 0, 0

for item in os.listdir(BASE):
    if item in EXCLUDE_DIRS or item.startswith('.'):
        continue
    src = os.path.join(BASE, item)
    if os.path.isdir(src):
        for root, dirs, files in os.walk(src):
            rel = os.path.relpath(root, BASE)
            dstdir = os.path.join(DEPLOY, rel)
            os.makedirs(dstdir, exist_ok=True)
            for f in files:
                sf = os.path.join(root, f)
                df = os.path.join(dstdir, f)
                sz = os.path.getsize(sf)
                total_orig += sz
                ext = f.lower()
                if ext.endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        img = Image.open(sf)
                        w, h = img.size
                        if img.mode in ('RGBA', 'P'):
                            bg = Image.new('RGB', img.size, (255,255,255))
                            if img.mode == 'P': img = img.convert('RGBA')
                            bg.paste(img, mask=img.split()[-1] if img.mode=='RGBA' else None)
                            img = bg
                        elif img.mode != 'RGB':
                            img = img.convert('RGB')
                        if w > MAX_WIDTH:
                            img = img.resize((MAX_WIDTH, int(h*MAX_WIDTH/w)), Image.LANCZOS)
                        jn = os.path.splitext(f)[0] + '.jpg'
                        df = os.path.join(dstdir, jn)
                        img.save(df, 'JPEG', quality=JPEG_QUALITY, optimize=True)
                        total_comp += os.path.getsize(df)
                        img_count += 1
                    except Exception as e:
                        shutil.copy2(sf, df)
                        total_comp += sz
                else:
                    shutil.copy2(sf, df)
                    total_comp += sz
    else:
        dst = os.path.join(DEPLOY, item)
        shutil.copy2(src, dst)
        total_comp += os.path.getsize(src)

# Update HTML refs: .png -> .jpg
for root, dirs, files in os.walk(DEPLOY):
    for f in files:
        if f.endswith('.html'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8') as fh:
                c = fh.read()
            c = c.replace('.png"', '.jpg"')
            with open(fp, 'w', encoding='utf-8') as fh:
                fh.write(c)

print(f'Done: {total_orig/1024/1024:.0f}MB -> {total_comp/1024/1024:.0f}MB ({(1-total_comp/total_orig)*100:.1f}%), {img_count} images')
