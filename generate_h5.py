import os
import re
import html

BASE = r"C:\Users\user\Desktop\H5"

# --- Product Data ---
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

PRODUCT_SUBTITLES = {
    "包包": "轻奢质感 · 大容量通勤首选",
    "口红": "一抹显色 · 高级丝绒妆感",
    "天然蜜蜡DIY可调节国风项链": "东方雅韵 · 蜜蜡温润国风",
    "香槟金印花改良长款气质旗袍": "改良剪裁 · 香槟金印花气质",
    "云锦序深墨底真丝刺绣长款旗袍": "深墨底色 · 真丝刺绣高定",
    "运动上衣": "轻量速干 · 运动更自在",
    "棕色菱格链条托特包女大容量": "菱格经典 · 链条托特大容量",
    "AEREN Airflow轻量缓震跑鞋": "Airflow透气 · 轻量缓震科技",
    "1.法式慵懒纯色套装": "慵懒法式 · 纯色简约通勤",
    "14.粉底液无痕无钢圈内衣": "粉底液色 · 无痕零感体验",
    "15.回力粉色老爹鞋": "经典回力 · 粉色复古潮流",
    "3.萌趣元气儿童长袖卫衣卫裤两件套": "萌趣印花 · 亲肤舒适两件套",
    "4.金色花纹短袖立领旗袍": "金色暗纹 · 短袖立领气质款",
    "7.高筒运动压缩袜护腿袜": "专业压缩 · 运动防护高筒款",
    "9.YSL小金条皮革哑光口红": "经典小金条 · 皮革哑光高级感",
    "连体运动服": "弹力亲肤 · 运动塑形一体式",
    "2025新款耳夹式无线蓝牙耳机": "不入耳黑科技 · 开放式舒适听感",
    "Apple_苹果iPhone17 国行全新正品手机": "全新国行 · 苹果旗舰级体验",
    "乌木沉香持久香薰 室内除异味香氛": "沉稳乌木 · 室内持久香薰体验",
    "海洋龙涎香盘香 家用持久留香赠香炉": "深海之息 · 家用持久留香赠香炉",
    "经典方扣漆皮细高跟通勤单鞋": "经典方扣 · 漆皮高跟通勤利器",
}

PRODUCT_PRICES = {
    "包包": "299",
    "口红": "159",
    "天然蜜蜡DIY可调节国风项链": "688",
    "香槟金印花改良长款气质旗袍": "1,280",
    "云锦序深墨底真丝刺绣长款旗袍": "2,680",
    "运动上衣": "199",
    "棕色菱格链条托特包女大容量": "359",
    "AEREN Airflow轻量缓震跑鞋": "599",
    "1.法式慵懒纯色套装": "259",
    "14.粉底液无痕无钢圈内衣": "129",
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
    "14.粉底液无痕无钢圈内衣": ["无痕", "无钢圈", "舒适", "内衣"],
    "15.回力粉色老爹鞋": ["回力", "粉色", "老爹鞋", "复古"],
    "3.萌趣元气儿童长袖卫衣卫裤两件套": ["儿童", "卫衣", "卫裤", "两件套"],
    "4.金色花纹短袖立领旗袍": ["旗袍", "金色花纹", "立领", "短袖"],
    "7.高筒运动压缩袜护腿袜": ["运动", "压缩", "高筒", "护腿"],
    "9.YSL小金条皮革哑光口红": ["YSL", "小金条", "哑光", "口红"],
    "连体运动服": ["连体", "运动", "弹力", "塑形"],
    "2025新款耳夹式无线蓝牙耳机": ["蓝牙耳机", "耳夹式", "无线", "降噪"],
    "Apple_苹果iPhone17 国行全新正品手机": ["iPhone17", "国行", "正品", "5G"],
    "乌木沉香持久香薰 室内除异味香氛": ["乌木", "沉香", "香薰", "除异味"],
    "海洋龙涎香盘香 家用持久留香赠香炉": ["盘香", "龙涎香", "留香", "赠香炉"],
    "经典方扣漆皮细高跟通勤单鞋": ["方扣", "漆皮", "高跟", "通勤"],
}

# Categories for index page grouping
PRODUCT_CATEGORIES = {
    "包包": "鞋包", "棕色菱格链条托特包女大容量": "鞋包",
    "口红": "美妆", "9.YSL小金条皮革哑光口红": "美妆",
    "天然蜜蜡DIY可调节国风项链": "配饰",
    "香槟金印花改良长款气质旗袍": "服饰", "云锦序深墨底真丝刺绣长款旗袍": "服饰",
    "运动上衣": "运动", "AEREN Airflow轻量缓震跑鞋": "运动",
    "1.法式慵懒纯色套装": "服饰", "4.金色花纹短袖立领旗袍": "服饰",
    "14.粉底液无痕无钢圈内衣": "配饰", "15.回力粉色老爹鞋": "鞋包",
    "3.萌趣元气儿童长袖卫衣卫裤两件套": "服饰",
    "7.高筒运动压缩袜护腿袜": "运动", "连体运动服": "运动",
    "2025新款耳夹式无线蓝牙耳机": "数码",
    "Apple_苹果iPhone17 国行全新正品手机": "数码",
    "乌木沉香持久香薰 室内除异味香氛": "生活",
    "海洋龙涎香盘香 家用持久留香赠香炉": "生活",
    "经典方扣漆皮细高跟通勤单鞋": "鞋包",
}

# New products (flagged with NEW badge on index)
NEW_PRODUCTS = [
    "2025新款耳夹式无线蓝牙耳机",
    "Apple_苹果iPhone17 国行全新正品手机",
    "乌木沉香持久香薰 室内除异味香氛",
    "海洋龙涎香盘香 家用持久留香赠香炉",
    "经典方扣漆皮细高跟通勤单鞋",
]

# Banner image mapping (banner index -> product folder name)
BANNER_PRODUCTS = {
    0: "Apple_苹果iPhone17 国行全新正品手机",
    1: "乌木沉香持久香薰 室内除异味香氛",
    2: "海洋龙涎香盘香 家用持久留香赠香炉",
    3: "经典方扣漆皮细高跟通勤单鞋",
}

NEW_PRODUCT_NAMES = set(NEW_PRODUCTS)

def get_sorted_images(folder, subfolder):
    path = os.path.join(folder, subfolder)
    if not os.path.exists(path):
        return []
    files = []
    for f in os.listdir(path):
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            if f.startswith("备") or f.startswith("预备"):
                continue
            files.append(f)
    def sort_key(fname):
        m = re.match(r'(\d+)', fname)
        return int(m.group(1)) if m else 999
    files.sort(key=sort_key)
    return files


def generate_h5(product_folder):
    product_name = os.path.basename(product_folder)
    title = PRODUCT_TITLES.get(product_name, product_name)
    subtitle = PRODUCT_SUBTITLES.get(product_name, "")
    price = PRODUCT_PRICES.get(product_name, "")
    tags = PRODUCT_TAGS.get(product_name, [])
    is_new = product_name in NEW_PRODUCT_NAMES

    main_images = get_sorted_images(product_folder, "主图")
    detail_images = get_sorted_images(product_folder, "详情图")

    # Find long image
    has_long_image = False
    long_image_name = None
    for name in ["详情页长图.png", "长图.jpg", "长图.png", "详情页长图.jpg"]:
        if os.path.exists(os.path.join(product_folder, name)):
            has_long_image = True
            long_image_name = name
            break

    main_paths = [f"主图/{html.escape(f)}" for f in main_images]
    detail_paths = [f"详情图/{html.escape(f)}" for f in detail_images]
    long_path = long_image_name if has_long_image else None

    dots_html = ""
    for i in range(len(main_paths)):
        active = "active" if i == 0 else ""
        dots_html += f'<span class="dot {active}" data-index="{i}"></span>'

    slides_html = ""
    for i, p in enumerate(main_paths):
        slides_html += f'<div class="slide"><img src="{p}" alt="主图{i+1}"></div>'

    detail_html = ""
    for p in detail_paths:
        detail_html += f'<div class="detail-img-wrap"><img src="{p}" alt="详情图" loading="lazy"></div>'

    tags_html = "".join([f'<span class="tag">{t}</span>' for t in tags])

    new_badge = '<span class="new-badge">NEW</span>' if is_new else ''

    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>{title}</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    background: #f5f5f5;
    color: #333;
    -webkit-tap-highlight-color: transparent;
    overflow-x: hidden;
}}
.container {{
    max-width: 430px;
    margin: 0 auto;
    background: #fff;
    min-height: 100vh;
    position: relative;
    padding-bottom: 80px;
}}

/* Header */
.header {{
    position: sticky;
    top: 0;
    z-index: 100;
    background: #fff;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid #f0f0f0;
}}
.header-title {{
    font-size: 16px;
    font-weight: 600;
    color: #1a1a1a;
}}
.header-back {{
    width: 32px; height: 32px;
    border-radius: 50%;
    background: #f5f5f5;
    display: flex; align-items: center; justify-content: center;
    color: #666; font-size: 16px; cursor: pointer; border: none;
}}
.header-share {{
    width: 32px; height: 32px;
    border-radius: 50%;
    background: #f5f5f5;
    display: flex; align-items: center; justify-content: center;
    color: #999; font-size: 14px; cursor: pointer; border: none;
}}

/* Carousel */
.carousel-wrap {{
    position: relative; width: 100%; overflow: hidden;
    background: #fafafa;
}}
.carousel {{
    display: flex;
    transition: transform 0.4s ease;
    touch-action: pan-y;
}}
.slide {{
    min-width: 100%; display: flex;
    align-items: center; justify-content: center;
}}
.slide img {{
    width: 100%; height: auto;
    display: block;
}}
.carousel-dots {{
    display: flex; justify-content: center; gap: 6px;
    padding: 10px 0;
    background: #fafafa;
}}
.dot {{
    width: 6px; height: 6px; border-radius: 50%;
    background: #ddd;
    transition: all 0.3s; cursor: pointer;
}}
.dot.active {{
    width: 18px; border-radius: 3px;
    background: #e60012;
}}

/* Product Info */
.info-section {{
    padding: 16px;
    background: #fff;
}}
.new-badge {{
    display: inline-block;
    font-size: 11px; font-weight: 600; color: #fff; background: #e60012;
    padding: 2px 8px; border-radius: 3px; margin-bottom: 10px;
    letter-spacing: 0.5px;
}}
.product-title {{
    font-size: 20px; font-weight: 600; color: #1a1a1a;
    line-height: 1.4; margin-bottom: 6px;
}}
.product-subtitle {{
    font-size: 13px; color: #999;
    line-height: 1.4; margin-bottom: 14px;
}}
.price-row {{
    display: flex; align-items: baseline; gap: 6px; margin-bottom: 12px;
}}
.price-symbol {{ font-size: 14px; color: #e60012; font-weight: 600; }}
.price {{
    font-size: 28px; font-weight: 700; color: #e60012;
    letter-spacing: -1px;
}}
.tags {{
    display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;
}}
.tag {{
    padding: 5px 12px;
    background: #fff5f5;
    border: 1px solid #ffd6d6;
    border-radius: 12px; font-size: 12px; color: #e60012;
}}

/* Divider */
.section-gap {{
    height: 10px; background: #f5f5f5;
}}

/* Trust Badges */
.trust-section {{
    padding: 16px;
    background: #fff;
    display: flex; justify-content: space-around;
    border-top: 1px solid #f5f5f5;
    border-bottom: 1px solid #f5f5f5;
}}
.trust-item {{ text-align: center; }}
.trust-icon {{ font-size: 20px; margin-bottom: 4px; }}
.trust-text {{ font-size: 11px; color: #999; }}

/* Detail Section */
.detail-section {{ padding: 0; }}
.detail-header {{
    text-align: center; padding: 20px 16px 12px;
}}
.detail-header-title {{
    font-size: 16px; font-weight: 600; color: #1a1a1a;
    position: relative; display: inline-block;
}}
.detail-header-title::before,
.detail-header-title::after {{
    content: "";
    position: absolute; top: 50%;
    width: 30px; height: 1px; background: #ddd;
}}
.detail-header-title::before {{ left: -40px; }}
.detail-header-title::after {{ right: -40px; }}
.detail-img-wrap {{ width: 100%; }}
.detail-img-wrap img {{ width: 100%; display: block; }}

/* Long Image */
.long-image-section {{ padding: 0; }}
.long-image-section img {{ width: 100%; display: block; }}

/* Bottom CTA Bar */
.cta-bar {{
    position: fixed; bottom: 0; left: 50%; transform: translateX(-50%);
    width: 100%; max-width: 430px;
    background: #fff;
    border-top: 1px solid #f0f0f0;
    padding: 8px 16px calc(8px + env(safe-area-inset-bottom));
    display: flex; gap: 10px; align-items: center;
    z-index: 200;
    box-shadow: 0 -2px 8px rgba(0,0,0,0.04);
}}
.btn-icon {{
    display: flex; flex-direction: column; align-items: center; gap: 3px;
    background: none; border: none; color: #999; cursor: pointer;
    padding: 4px 6px; font-family: inherit;
}}
.btn-icon .bi {{ font-size: 20px; line-height: 1; }}
.btn-icon span:last-child {{ font-size: 10px; }}
.btn-cart {{
    flex: 1; height: 42px; border-radius: 21px;
    border: 1px solid #e60012;
    background: #fff; color: #e60012;
    font-size: 14px; font-weight: 500;
    cursor: pointer; font-family: inherit;
}}
.btn-buy {{
    flex: 1.5; height: 42px; border-radius: 21px; border: none;
    background: linear-gradient(135deg, #ff4757, #e60012);
    color: #fff; font-size: 14px; font-weight: 600;
    cursor: pointer; font-family: inherit;
}}
</style>
</head>
<body>
<div class="container">

    <div class="header">
        <button class="header-back" onclick="history.back()">&larr;</button>
        <div class="header-title">商品详情</div>
        <div class="header-share">&#10247;</div>
    </div>

    <div class="carousel-wrap">
        <div class="carousel" id="carousel">
            {slides_html}
        </div>
        <div class="carousel-dots" id="dots">
            {dots_html}
        </div>
    </div>

    <div class="info-section">
        {new_badge}
        <h1 class="product-title">{title}</h1>
        <p class="product-subtitle">{subtitle}</p>
        <div class="price-row">
            <span class="price-symbol">&yen;</span>
            <span class="price">{price}</span>
        </div>
        <div class="tags">
            {tags_html}
        </div>
    </div>

    <div class="trust-section">
        <div class="trust-item">
            <div class="trust-icon">&#9992;</div>
            <div class="trust-text">极速发货</div>
        </div>
        <div class="trust-item">
            <div class="trust-icon">&#10003;</div>
            <div class="trust-text">正品保障</div>
        </div>
        <div class="trust-item">
            <div class="trust-icon">&#8635;</div>
            <div class="trust-text">七天退换</div>
        </div>
        <div class="trust-item">
            <div class="trust-icon">&#9829;</div>
            <div class="trust-text">品质严选</div>
        </div>
    </div>

    <div class="section-gap"></div>

    <div class="detail-section">
        <div class="detail-header">
            <span class="detail-header-title">商品详情</span>
        </div>
        {detail_html}
    </div>

    {f'<div class="long-image-section"><img src="{long_path}" alt="详情页长图" loading="lazy"></div>' if long_path else ''}

    <div style="height: 20px;"></div>

</div>

<div class="cta-bar">
    <button class="btn-icon">
        <span class="bi">&#9993;</span>
        <span>客服</span>
    </button>
    <button class="btn-icon">
        <span class="bi">&#9825;</span>
        <span>收藏</span>
    </button>
    <button class="btn-cart">加入购物车</button>
    <button class="btn-buy">立即购买</button>
</div>

<script>
(function() {{
    var carousel = document.getElementById('carousel');
    var dots = document.querySelectorAll('.dot');
    var slides = document.querySelectorAll('.slide');
    var current = 0;
    var startX = 0;
    var timer = null;

    function goTo(index) {{
        if (index < 0) index = slides.length - 1;
        if (index >= slides.length) index = 0;
        current = index;
        carousel.style.transform = 'translateX(-' + (current * 100) + '%)';
        dots.forEach(function(d, i) {{ d.classList.toggle('active', i === current); }});
    }}

    dots.forEach(function(dot, i) {{
        dot.addEventListener('click', function() {{ goTo(i); resetTimer(); }});
    }});

    carousel.addEventListener('touchstart', function(e) {{
        startX = e.touches[0].clientX;
        clearInterval(timer);
    }}, {{passive: true}});

    carousel.addEventListener('touchend', function(e) {{
        var diff = startX - e.changedTouches[0].clientX;
        if (Math.abs(diff) > 50) {{
            if (diff > 0) goTo(current + 1); else goTo(current - 1);
        }}
        resetTimer();
    }}, {{passive: true}});

    function resetTimer() {{
        clearInterval(timer);
        timer = setInterval(function() {{ goTo(current + 1); }}, 4000);
    }}
    resetTimer();
}})();
</script>

</body>
</html>'''

    output_path = os.path.join(product_folder, "h5-poster.html")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated: {output_path}")
    return output_path


if __name__ == "__main__":
    product_folders = []
    for item in os.listdir(BASE):
        item_path = os.path.join(BASE, item)
        if os.path.isdir(item_path) and item not in ['.workbuddy', 'banner图', 'deploy']:
            if os.path.exists(os.path.join(item_path, "主图")):
                product_folders.append(item_path)

    print(f"Found {len(product_folders)} product folders")
    for pf in sorted(product_folders):
        generate_h5(pf)
    print("\nAll H5 posters generated successfully!")
