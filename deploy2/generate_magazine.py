# -*- coding: utf-8 -*-
"""Generate magazine-style flip-book H5 for each product."""

import os
import re
import html

BASE = r"C:\Users\user\Desktop\H5"

PRODUCT_TITLES = {
    "包包": "复古菱格棕托特包",
    "口红": "丝绒哑光高定口红",
    "天然蜜蜡DIY可调节国风项链": "天然蜜蜡国风项链",
    "香槟金印花改良长款气质旗袍": "香槟金印花改良旗袍",
    "云锦序深墨底真丝刺绣长款旗袍": "云锦序真丝刺绣旗袍",
    "运动上衣": "速干透气运动上衣",
    "棕色菱格链条托特包女大容量": "棕色菱格链条托特包",
    "AEREN Airflow轻量缓震跑鞋": "AEREN Airflow轻量跑鞋",
    "1.法式慵懒纯色套装": "法式慵懒纯色套装",
    "14.粉底液无痕无钢圈内衣": "无痕无钢圈舒适内衣",
    "15.回力粉色老爹鞋": "回力粉色老爹鞋",
    "3.萌趣元气儿童长袖卫衣卫裤两件套": "萌趣元气儿童卫衣卫裤套装",
    "4.金色花纹短袖立领旗袍": "金色花纹短袖立领旗袍",
    "7.高筒运动压缩袜护腿袜": "高筒运动压缩护腿袜",
    "9.YSL小金条皮革哑光口红": "YSL小金条皮革哑光口红",
    "连体运动服": "修身连体运动服",
    "2025新款耳夹式无线蓝牙耳机": "2025新款耳夹式蓝牙耳机",
    "Apple_苹果iPhone17 国行全新正品手机": "Apple iPhone17 国行正品",
    "乌木沉香持久香薰 室内除异味香氛": "乌木沉香持久香薰",
    "海洋龙涎香盘香 家用持久留香赠香炉": "海洋龙涎香盘香 赠香炉",
    "经典方扣漆皮细高跟通勤单鞋": "经典方扣漆皮细高跟单鞋",
}

PRODUCT_PRICES = {
    "包包": "299", "口红": "159",
    "天然蜜蜡DIY可调节国风项链": "688",
    "香槟金印花改良长款气质旗袍": "1,280",
    "云锦序深墨底真丝刺绣长款旗袍": "2,680",
    "运动上衣": "199", "棕色菱格链条托特包女大容量": "359",
    "AEREN Airflow轻量缓震跑鞋": "599",
    "1.法式慵懒纯色套装": "259", "14.粉底液无痕无钢圈内衣": "129",
    "15.回力粉色老爹鞋": "269",
    "3.萌趣元气儿童长袖卫衣卫裤两件套": "159",
    "4.金色花纹短袖立领旗袍": "980",
    "7.高筒运动压缩袜护腿袜": "79",
    "9.YSL小金条皮革哑光口红": "329",
    "连体运动服": "239",
    "2025新款耳夹式无线蓝牙耳机": "199",
    "Apple_苹果iPhone17 国行全新正品手机": "5,999",
    "乌木沉香持久香薰 室内除异味香氛": "99",
    "海洋龙涎香盘香 家用持久留香赠香炉": "69",
    "经典方扣漆皮细高跟通勤单鞋": "299",
}

PRODUCT_TAGS = {
    "包包": ["大容量", "轻奢", "通勤", "菱格"],
    "口红": ["丝绒", "哑光", "显白", "高定"],
    "天然蜜蜡DIY可调节国风项链": ["国风", "蜜蜡", "DIY", "可调节"],
    "香槟金印花改良长款气质旗袍": ["改良旗袍", "印花", "气质", "长款"],
    "云锦序深墨底真丝刺绣长款旗袍": ["真丝", "刺绣", "高定", "云锦"],
    "运动上衣": ["速干", "透气", "轻量", "运动"],
    "棕色菱格链条托特包女大容量": ["菱格", "链条", "托特包", "大容量"],
    "AEREN Airflow轻量缓震跑鞋": ["轻量", "缓震", "透气", "跑鞋"],
    "1.法式慵懒纯色套装": ["法式", "慵懒", "纯色", "套装"],
    "14.粉底液无痕无钢圈内衣": ["无痕", "零感", "舒适", "内衣"],
    "15.回力粉色老爹鞋": ["回力", "粉色", "复古", "老爹鞋"],
    "3.萌趣元气儿童长袖卫衣卫裤两件套": ["萌趣", "卫衣", "儿童", "两件套"],
    "4.金色花纹短袖立领旗袍": ["旗袍", "金色", "立领", "短袖"],
    "7.高筒运动压缩袜护腿袜": ["压缩袜", "运动", "高筒", "护腿"],
    "9.YSL小金条皮革哑光口红": ["YSL", "小金条", "皮革", "哑光"],
    "连体运动服": ["运动", "塑形", "弹力", "连体"],
    "2025新款耳夹式无线蓝牙耳机": ["蓝牙", "耳夹式", "无线", "不入耳"],
    "Apple_苹果iPhone17 国行全新正品手机": ["iPhone17", "国行", "正品", "旗舰"],
    "乌木沉香持久香薰 室内除异味香氛": ["乌木", "沉香", "香薰", "持久"],
    "海洋龙涎香盘香 家用持久留香赠香炉": ["龙涎香", "盘香", "持久", "赠香炉"],
    "经典方扣漆皮细高跟通勤单鞋": ["方扣", "漆皮", "高跟", "通勤"],
}


def get_sorted_images(folder, subfolder):
    path = os.path.join(folder, subfolder)
    if not os.path.exists(path):
        return []
    files = []
    for f in os.listdir(path):
        low = f.lower()
        if not low.endswith(('.png', '.jpg', '.jpeg')):
            continue
        # skip backup images
        if '备' in f:
            continue
        files.append(f)

    def sort_key(fname):
        m = re.match(r'(\d+)', fname)
        return int(m.group(1)) if m else 9999

    files.sort(key=sort_key)
    return files


def find_long_image(folder):
    for fname in ["长图.jpg", "长图.png", "详情页长图.png", "详情页长图.jpg"]:
        fp = os.path.join(folder, fname)
        if os.path.exists(fp):
            return fname
    return None


def generate_magazine(product_folder_name):
    folder = os.path.join(BASE, product_folder_name)
    title = PRODUCT_TITLES.get(product_folder_name, product_folder_name)
    price = PRODUCT_PRICES.get(product_folder_name, "---")
    tags = PRODUCT_TAGS.get(product_folder_name, [])
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in tags)

    main_imgs = get_sorted_images(folder, "主图")
    detail_imgs = get_sorted_images(folder, "详情图")
    long_img = find_long_image(folder)

    # Build pages
    pages = []

    # Page 0: Cover - first main image
    cover_img = f"主图/{main_imgs[0]}" if main_imgs else None
    pages.append({
        "type": "cover",
        "img": cover_img,
        "title": title,
        "price": price,
        "tags": tags_html,
    })

    # Pages 1..N: remaining main images
    for i, img in enumerate(main_imgs[1:], 1):
        pages.append({
            "type": "main",
            "img": f"主图/{img}",
            "label": f"主图 {i+1}/{len(main_imgs)}",
        })

    # Detail pages: one per image
    for i, img in enumerate(detail_imgs):
        pages.append({
            "type": "detail",
            "img": f"详情图/{img}",
            "label": f"详情 {i+1}/{len(detail_imgs)}",
        })

    # Long image page (if exists)
    if long_img:
        pages.append({
            "type": "long",
            "img": long_img,
            "label": "详情总览",
        })

    # End page
    pages.append({"type": "end", "img": None, "label": ""})

    total = len(pages)

    # Generate HTML
    pages_html = ""
    dots_html = ""

    for idx, page in enumerate(pages):
        t = page["type"]
        cls = "page" if idx == 0 else "page"
        img_path = page["img"]
        rel_path = f"{product_folder_name}/{img_path}" if img_path else ""

        if t == "cover":
            pages_html += f'''<div class="page cover-page" data-idx="{idx}">
  <div class="cover-bg">
    <img src="{rel_path}" alt="{title}" class="cover-img">
  </div>
  <div class="cover-overlay">
    <div class="cover-tags">{tags_html}</div>
    <h1 class="cover-title">{title}</h1>
    <div class="cover-price">\u00a5{price}</div>
  </div>
</div>
'''
        elif t in ("main", "detail", "long"):
            pages_html += f'''<div class="page image-page" data-idx="{idx}">
  <img src="{rel_path}" alt="" class="full-img">
  <div class="page-label">{page["label"]}</div>
</div>
'''

        elif t == "end":
            pages_html += f'''<div class="page end-page" data-idx="{idx}">
  <div class="end-content">
    <div class="end-logo">{title}</div>
    <div class="end-line"></div>
    <div class="end-thanks">Thank You</div>
    <div class="end-sub">感谢浏览 \u00b7 期待与您相遇</div>
  </div>
</div>
'''

        dots_html += f'<span class="dot{" active" if idx==0 else ""}" data-idx="{idx}"></span>\n'

    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>{title}</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html,body {{
  width:100%; height:100%;
  overflow:hidden;
  font-family: -apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  background:#fff;
  -webkit-tap-highlight-color: transparent;
  touch-action: pan-y;
}}

.container {{
  width:100%; height:100%;
  max-width:430px;
  margin:0 auto;
  position:relative;
  overflow:hidden;
}}

.topper {{
  position:fixed; top:0; left:50%; transform:translateX(-50%);
  width:100%; max-width:430px;
  z-index:100;
  padding:12px 16px;
  display:flex; align-items:center; justify-content:space-between;
  background: rgba(255,255,255,0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom:0.5px solid rgba(0,0,0,0.06);
}}
.topper-back {{
  width:32px; height:32px; border-radius:50%;
  border:0.5px solid #e0e0e0;
  background:#fff;
  display:flex; align-items:center; justify-content:center;
  font-size:16px; color:#333; cursor:pointer;
}}
.topper-title {{
  font-size:14px; font-weight:500; color:#222;
  letter-spacing:0.5px;
}}
.topper-dots {{
  display:flex; gap:6px; align-items:center;
}}
.top-dot {{
  width:5px; height:5px; border-radius:50%;
  background:#d0d0d0;
  transition:all 0.3s;
}}
.top-dot.on {{ background:#4A94FF; width:7px; height:7px; }}

.pages-wrapper {{
  width:100%; height:100%;
  transition: transform 0.55s cubic-bezier(0.25,0.46,0.45,0.94);
  will-change:transform;
}}
.page {{
  width:100%; height:100%;
  position:relative;
  overflow:hidden;
  display:flex; align-items:center; justify-content:center;
  background:#fff;
}}

.cover-page {{ background:#f8f8f8; }}
.cover-bg {{
  width:100%; height:100%;
  display:flex; align-items:center; justify-content:center;
  position:relative;
}}
.cover-img {{
  width:100%; height:100%;
  object-fit:cover;
}}
.cover-overlay {{
  position:absolute; bottom:0; left:0; right:0;
  padding: 60px 24px 40px;
  background: linear-gradient(transparent 0%, rgba(255,255,255,0.7) 30%, rgba(255,255,255,0.95) 60%, #fff 100%);
}}
.cover-tags {{
  display:flex; flex-wrap:wrap; gap:8px; margin-bottom:12px;
}}
.tag {{
  padding:4px 10px;
  background:rgba(74,148,255,0.08);
  border:0.5px solid rgba(74,148,255,0.25);
  border-radius:12px;
  font-size:11px; color:#4A94FF;
  letter-spacing:0.5px;
}}
.cover-title {{
  font-size:24px; font-weight:600; color:#1a1a1a;
  line-height:1.3; margin-bottom:8px; letter-spacing:0.5px;
}}
.cover-price {{
  font-size:32px; font-weight:600; color:#4A94FF;
  letter-spacing:-0.5px;
}}

.image-page {{ background:#fafafa; }}
.full-img {{
  width:100%; height:100%;
  object-fit:contain;
  display:block;
}}
.page-label {{
  position:absolute; bottom:24px; left:50%; transform:translateX(-50%);
  padding:4px 14px;
  background:rgba(0,0,0,0.45);
  border-radius:20px;
  font-size:11px; color:#fff;
  letter-spacing:1px;
}}

.end-page {{
  background:linear-gradient(135deg, #f0f5ff 0%, #e8f0fe 50%, #f5f8ff 100%);
  display:flex; align-items:center; justify-content:center;
}}
.end-content {{ text-align:center; }}
.end-logo {{
  font-size:22px; font-weight:600; color:#1a1a1a;
  letter-spacing:1px; margin-bottom:16px;
}}
.end-line {{
  width:32px; height:1px; background:#4A94FF;
  margin:0 auto 16px;
}}
.end-thanks {{
  font-size:28px; font-weight:300; color:#4A94FF;
  letter-spacing:3px; margin-bottom:8px;
}}
.end-sub {{
  font-size:13px; color:#999;
  letter-spacing:1px;
}}

.side-dots {{
  position:fixed; right:8px; top:50%; transform:translateY(-50%);
  z-index:90;
  display:flex; flex-direction:column; gap:8px;
  align-items:center;
}}
.dot {{
  width:6px; height:6px; border-radius:50%;
  background:rgba(0,0,0,0.18);
  transition:all 0.35s;
  cursor:pointer;
}}
.dot.active {{
  width:8px; height:8px;
  background:#4A94FF;
  box-shadow: 0 0 0 2px rgba(74,148,255,0.2);
}}
</style>
</head>
<body>
<div class="container" id="container">

  <div class="topper" id="topper">
    <button class="topper-back" onclick="history.back()">&#8592;</button>
    <div class="topper-title">{title}</div>
    <div class="topper-dots" id="topDots">
      {''.join(f'<span class="top-dot{" on" if i==0 else ""}" id="td{i}"></span>' for i in range(min(total, 5)))}
    </div>
  </div>

  <div class="pages-wrapper" id="pagesWrapper" style="transform:translateY(0)">
{pages_html}  </div>

  <div class="side-dots" id="sideDots">
{dots_html}  </div>

</div>

<script>
(function() {{
  var total = {total};
  var current = 0;
  var wrapper = document.getElementById('pagesWrapper');
  var sideDots = document.querySelectorAll('#sideDots .dot');
  var topDots = document.querySelectorAll('.top-dot');
  var startY = 0;
  var isAnimating = false;
  var autoTimer = null;

  function updateIndicators(idx) {{
    sideDots.forEach(function(d, i) {{ d.classList.toggle('active', i === idx); }});
    // top mini dots
    var groupSize = topDots.length;
    if (total <= groupSize) {{
      topDots.forEach(function(d, i) {{ d.classList.toggle('on', i === idx); }});
    }} else {{
      var seg = total / groupSize;
      var segIdx = Math.floor(idx / seg);
      topDots.forEach(function(d, i) {{ d.classList.toggle('on', i === segIdx); }});
    }}
  }}

  function goTo(idx) {{
    if (isAnimating) return;
    if (idx < 0) idx = 0;
    if (idx >= total) idx = total - 1;
    if (idx === current) return;
    isAnimating = true;
    current = idx;
    wrapper.style.transform = 'translateY(-' + (current * 100) + '%)';
    updateIndicators(current);
    setTimeout(function() {{ isAnimating = false; }}, 560);
    resetAuto();
  }}

  function resetAuto() {{
    clearTimeout(autoTimer);
    autoTimer = setTimeout(function() {{
      if (current < total - 1) goTo(current + 1);
      else goTo(0);
    }}, 5000);
  }}

  // Touch
  function isAtTop() {{ return current === 0; }}
  function isAtBottom() {{ return current === total - 1; }}

  wrapper.parentElement.addEventListener('touchstart', function(e) {{
    startY = e.touches[0].clientY;
  }}, {{passive:true}});

  wrapper.parentElement.addEventListener('touchend', function(e) {{
    var diff = startY - e.changedTouches[0].clientY;
    if (Math.abs(diff) > 40) {{
      if (diff > 0) goTo(current + 1);
      else goTo(current - 1);
    }}
  }}, {{passive:true}});

  // Mouse wheel (desktop)
  wrapper.parentElement.addEventListener('wheel', function(e) {{
    e.preventDefault();
    if (e.deltaY > 20) goTo(current + 1);
    else if (e.deltaY < -20) goTo(current - 1);
  }}, {{passive:false}});

  // Side dot clicks
  sideDots.forEach(function(dot) {{
    dot.addEventListener('click', function() {{
      goTo(parseInt(dot.dataset.idx));
    }});
  }});

  // Keyboard
  document.addEventListener('keydown', function(e) {{
    if (e.key === 'ArrowDown' || e.key === 'ArrowRight') goTo(current + 1);
    if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') goTo(current - 1);
  }});

  resetAuto();
}})();
</script>
</body>
</html>'''

    out_path = os.path.join(folder, "magazine.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"  OK [{total} pages] {product_folder_name} -> magazine.html")
    return total


def main():
    print("Generating magazine H5 for each product...\n")
    grand_total = 0

    for item in sorted(os.listdir(BASE)):
        path = os.path.join(BASE, item)
        if not os.path.isdir(path):
            continue
        if item.startswith(".") or item in ("banner图", "deploy", "deploy2"):
            continue
        main_dir = os.path.join(path, "主图")
        if not os.path.exists(main_dir):
            continue

        try:
            pages = generate_magazine(item)
            grand_total += pages
        except Exception as e:
            print(f"  FAIL {item}: {e}")

    print(f"\nDone. Total pages across all magazines: {grand_total}")


if __name__ == "__main__":
    main()
