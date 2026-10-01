import os

BASE_DIR = r"c:\Users\USER\Desktop\博客\jccesu.homes"

# CSS STYLING (Anubis2 Sleek Dark Mode)
css_content = '''
:root {
  --bg-main: #121214;
  --bg-card: #18181c;
  --bg-card-hover: #222228;
  --border-color: #2a2a32;
  --text-main: #e2e8f0;
  --text-muted: #94a3b8;
  --accent-cyan: #06b6d4;
  --accent-indigo: #6366f1;
  --accent-gold: #f59e0b;
  --accent-green: #10b981;
  --radius: 8px;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background-color: var(--bg-main);
  color: var(--text-main);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  line-height: 1.7;
  font-size: 16px;
}

a { color: var(--accent-cyan); text-decoration: none; transition: color 0.2s; }
a:hover { color: #38bdf8; text-decoration: underline; }

header {
  background: #16161a;
  border-bottom: 1px solid var(--border-color);
  position: sticky; top: 0; z-index: 100;
  padding: 12px 20px;
}

.header-container {
  max-width: 1200px; margin: 0 auto;
  display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;
}

.brand-logo {
  font-size: 1.25rem; font-weight: 700; color: #ffffff; display: flex; align-items: center; gap: 8px;
}
.brand-logo span { color: var(--accent-cyan); }

nav ul { display: flex; list-style: none; gap: 18px; flex-wrap: wrap; }
nav a { color: var(--text-main); font-weight: 500; font-size: 0.95rem; }
nav a:hover, nav a.active { color: var(--accent-cyan); }

.header-right { display: flex; align-items: center; gap: 12px; }

.search-box { position: relative; }
.search-input {
  background: #22222a; border: 1px solid var(--border-color); color: #fff;
  padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; width: 200px;
  outline: none; transition: width 0.3s, border-color 0.3s;
}
.search-input:focus { width: 260px; border-color: var(--accent-cyan); }
.search-results {
  position: absolute; right: 0; top: 38px; background: #1f1f26; border: 1px solid var(--border-color);
  border-radius: var(--radius); width: 340px; max-height: 400px; overflow-y: auto;
  box-shadow: 0 10px 25px rgba(0,0,0,0.5); display: none; z-index: 1000;
}
.search-results a {
  display: block; padding: 10px 14px; border-bottom: 1px solid #2a2a34; color: var(--text-main); font-size: 0.88rem;
}
.search-results a:hover { background: #2a2a36; text-decoration: none; }

.tg-btn {
  background: #0088cc; color: #fff !important; font-size: 0.85rem; font-weight: 600;
  padding: 6px 14px; border-radius: 20px; display: inline-flex; align-items: center; gap: 6px;
  transition: transform 0.2s, background 0.2s;
}
.tg-btn:hover { background: #0099e6; text-decoration: none; transform: translateY(-1px); }

.main-container { max-width: 1200px; margin: 30px auto; padding: 0 20px; }

.hero-box {
  background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);
  border: 1px solid #312e81; border-radius: var(--radius);
  padding: 35px; margin-bottom: 35px; text-align: center;
}
.hero-box h1 { font-size: 1.8rem; margin-bottom: 15px; color: #fff; }
.hero-box p { color: #cbd5e1; font-size: 1rem; max-width: 900px; margin: 0 auto 20px; }

.top4-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 20px; margin-bottom: 40px;
}
.top4-card {
  background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius);
  padding: 22px; position: relative; display: flex; flex-direction: column; justify-content: space-between;
  transition: transform 0.2s, border-color 0.2s;
}
.top4-card:hover { transform: translateY(-3px); border-color: var(--accent-cyan); }
.top4-card.rank-1 { border-color: var(--accent-gold); }
.rank-badge {
  position: absolute; top: -12px; left: 16px; background: var(--accent-indigo); color: #fff;
  font-size: 0.75rem; font-weight: 700; padding: 3px 10px; border-radius: 12px; text-transform: uppercase;
}
.top4-card.rank-1 .rank-badge { background: var(--accent-gold); color: #000; }

.card-title { font-size: 1.25rem; font-weight: 700; color: #fff; margin-top: 5px; margin-bottom: 8px; }
.card-price { font-size: 1.1rem; color: var(--accent-green); font-weight: 700; margin-bottom: 10px; }
.card-features { font-size: 0.88rem; color: var(--text-muted); margin-bottom: 15px; }
.cta-btn {
  background: linear-gradient(135deg, var(--accent-cyan), var(--accent-indigo));
  color: #fff !important; text-align: center; font-weight: 700; padding: 10px 16px;
  border-radius: var(--radius); display: block; width: 100%; transition: opacity 0.2s;
}
.cta-btn:hover { opacity: 0.9; text-decoration: none; }

.content-section { margin-bottom: 40px; }
.section-title { font-size: 1.4rem; font-weight: 700; color: #fff; border-left: 4px solid var(--accent-cyan); padding-left: 12px; margin-bottom: 20px; }

.article-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }
.article-card {
  background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius);
  padding: 20px; display: flex; flex-direction: column; justify-content: space-between;
}
.article-card h3 { font-size: 1.1rem; color: #fff; margin-bottom: 10px; }
.article-card p { font-size: 0.9rem; color: var(--text-muted); margin-bottom: 15px; flex-grow: 1; }
.article-meta { font-size: 0.8rem; color: #64748b; display: flex; justify-content: space-between; }

.article-content { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius); padding: 35px; }
.article-content h1 { font-size: 1.8rem; color: #fff; margin-bottom: 15px; }
.article-content h2 { font-size: 1.35rem; color: #38bdf8; margin: 30px 0 15px; border-bottom: 1px solid var(--border-color); padding-bottom: 8px; }
.article-content h3 { font-size: 1.15rem; color: #cbd5e1; margin: 20px 0 10px; }
.article-content p { margin-bottom: 16px; font-size: 1rem; color: #cbd5e1; }
.article-content ul, .article-content ol { margin-left: 25px; margin-bottom: 16px; color: #cbd5e1; }
.article-content li { margin-bottom: 6px; }

table { width: 100%; border-collapse: collapse; margin: 25px 0; background: #16161c; border-radius: var(--radius); overflow: hidden; }
th, td { padding: 12px 16px; text-align: left; border-bottom: 1px solid var(--border-color); font-size: 0.9rem; }
th { background: #202028; color: #fff; }

footer { background: #0c0c0e; border-top: 1px solid var(--border-color); padding: 40px 20px; margin-top: 60px; color: var(--text-muted); font-size: 0.88rem; }
.footer-container { max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 20px; text-align: center; }
.footer-links { display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; }
.footer-links a { color: var(--text-muted); }

@media (max-width: 768px) {
  .header-container { flex-direction: column; align-items: stretch; }
  nav ul { justify-content: center; }
  .header-right { justify-content: space-between; }
  .search-input { width: 100%; }
}
'''

with open(os.path.join(BASE_DIR, "assets", "css", "style.css"), "w", encoding="utf-8") as f:
    f.write(css_content)

# JS FOR SEARCH
js_search = '''
document.addEventListener("DOMContentLoaded", function() {
  const searchInput = document.getElementById("search-input");
  const searchResults = document.getElementById("search-results");
  let searchData = [];

  if (!searchInput || !searchResults) return;

  fetch("/index.json")
    .then(res => res.json())
    .then(data => { searchData = data; })
    .catch(err => console.error("Error loading search index:", err));

  searchInput.addEventListener("input", function() {
    const query = this.value.trim().toLowerCase();
    if (query.length < 1) {
      searchResults.style.display = "none";
      searchResults.innerHTML = "";
      return;
    }

    const matches = searchData.filter(item => {
      return (item.title && item.title.toLowerCase().includes(query)) ||
             (item.summary && item.summary.toLowerCase().includes(query)) ||
             (item.contents && item.contents.toLowerCase().includes(query));
    }).slice(0, 8);

    if (matches.length > 0) {
      searchResults.innerHTML = matches.map(m => `
        <a href="${m.permalink}">
          <strong>${m.title}</strong>
          <div style="font-size:0.75rem; color:#94a3b8; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${m.summary || ''}</div>
        </a>
      `).join('');
      searchResults.style.display = "block";
    } else {
      searchResults.innerHTML = `<div style="padding:10px; font-size:0.85rem; color:#94a3b8;">未找到匹配文章</div>`;
      searchResults.style.display = "block";
    }
  });

  document.addEventListener("click", function(e) {
    if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
      searchResults.style.display = "none";
    }
  });
});
'''

with open(os.path.join(BASE_DIR, "assets", "js", "search.js"), "w", encoding="utf-8") as f:
    f.write(js_search)

# -------------------------------------------------------------
# HUGO LAYOUT TEMPLATES
# -------------------------------------------------------------
baseof_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ if .IsHome }}{{ .Site.Title }}{{ else }}{{ .Title }} - {{ .Site.Params.brandName }}{{ end }}</title>
  <meta name="description" content="{{ with .Description }}{{ . }}{{ else }}{{ .Site.Params.description }}{{ end }}">
  <link rel="canonical" href="{{ .Permalink }}">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="alternate" type="application/rss+xml" href="/index.xml" title="{{ .Site.Title }}">
</head>
<body>
  {{ partial "header.html" . }}
  <main class="main-container">
    {{ block "main" . }}{{ end }}
  </main>
  {{ partial "footer.html" . }}
  <script src="/js/search.js" defer></script>
</body>
</html>
'''

with open(os.path.join(BASE_DIR, "layouts", "_default", "baseof.html"), "w", encoding="utf-8") as f:
    f.write(baseof_html)

header_html = '''<header>
  <div class="header-container">
    <a href="/" class="brand-logo">
      ⚡ <span>jccesu</span> 机场测速实验室
    </a>
    <nav>
      <ul>
        <li><a href="/" {{ if .IsHome }}class="active"{{ end }}>首页</a></li>
        <li><a href="/speed-test/" {{ if eq .Section "speed-test" }}class="active"{{ end }}>测速评测室</a></li>
        <li><a href="/recommendations/" {{ if eq .Section "recommendations" }}class="active"{{ end }}>小白推荐榜</a></li>
        <li><a href="/tutorials/" {{ if eq .Section "tutorials" }}class="active"{{ end }}>客户端教程</a></li>
        <li><a href="/knowledge/" {{ if eq .Section "knowledge" }}class="active"{{ end }}>线路知识库</a></li>
        <li><a href="/faq/" {{ if eq .Section "faq" }}class="active"{{ end }}>常见疑问答疑</a></li>
        <li><a href="/all-airports/" {{ if eq .Section "all-airports" }}class="active"{{ end }}>全机场注册大全</a></li>
      </ul>
    </nav>
    <div class="header-right">
      <div class="search-box">
        <input type="text" id="search-input" class="search-input" placeholder="搜索全站文章或关键词..." autocomplete="off">
        <div id="search-results" class="search-results"></div>
      </div>
      <a href="https://t.me/+HVHzlzUXk4YyOWM9" target="_blank" rel="sponsored nofollow noopener" class="tg-btn">
        ✈️ TG 官方频道
      </a>
    </div>
  </div>
</header>
'''

with open(os.path.join(BASE_DIR, "layouts", "partials", "header.html"), "w", encoding="utf-8") as f:
    f.write(header_html)

footer_html = '''<footer>
  <div class="footer-container">
    <p style="color: #cbd5e1; font-weight: 500;">
      jccesu.homes 节点真实测速实验室聚焦 2026 高速稳定机场推荐、晚高峰 8K 跑分实测与新手科学上网避坑指南，提供全平台 Clash / Sing-box / Shadowrocket 客户端极速上手教程。
    </p>
    <div class="footer-links">
      <a href="/about/">关于我们</a>
      <a href="/contact/">联系我们</a>
      <a href="/methodology/">评测方法</a>
      <a href="/affiliate-disclosure/">联盟披露</a>
      <a href="/privacy/">隐私政策</a>
      <a href="/terms/">服务条款</a>
      <a href="/disclaimer/">免责声明</a>
      <a href="https://t.me/+HVHzlzUXk4YyOWM9" target="_blank" rel="sponsored nofollow noopener" style="color:#0088cc;">Telegram 交流群</a>
    </div>
    <p>© 2026 jccesu 机场测速实验室. 所有第三方商标及著作权归其原权利人所有。声明：本站跳转链接包含推广合作支持。</p>
  </div>
</footer>
'''

with open(os.path.join(BASE_DIR, "layouts", "partials", "footer.html"), "w", encoding="utf-8") as f:
    f.write(footer_html)

top4_box_html = '''<div class="top4-grid">
  <div class="top4-card rank-1">
    <div class="rank-badge">NO.1 强烈推荐 (主力首选)</div>
    <div class="card-title">灵动云</div>
    <div class="card-price">￥18.8 元 / 月 (150GB)</div>
    <div class="card-features">
      • 线路：IPLC/IEPL 全专线节点，全天晚高峰零卡顿<br>
      • 解锁：完美支持 ChatGPT, Claude, Netflix 4K<br>
      • 特点：低延迟游戏加速，新手一键导入客户端
    </div>
    <a href="https://varnexa.lingdongaff.com/#/?code=vFPRdc1J" target="_blank" rel="sponsored nofollow noopener" class="cta-btn">
      👉 前往【灵动云】官网注册与选购
    </a>
  </div>

  <div class="top4-card">
    <div class="rank-badge">NO.2 观影大户 (高清8K)</div>
    <div class="card-title">暮光网络</div>
    <div class="card-price">￥20.0 元 / 月 (200GB)</div>
    <div class="card-features">
      • 线路：BGP 多线中继 + 专线直连，带宽跑满<br>
      • 解锁：稳定解锁 OpenAI, Sora, Disney+<br>
      • 特点：超大流量包，多设备并发协同办公
    </div>
    <a href="https://varnexa.twilightaff.com/#/?code=X6iVG1Zb" target="_blank" rel="sponsored nofollow noopener" class="cta-btn">
      👉 前往【暮光网络】官网注册与选购
    </a>
  </div>

  <div class="top4-card">
    <div class="rank-badge">NO.3 高性价比 (新手年付)</div>
    <div class="card-title">飞猫云</div>
    <div class="card-price">￥84.0 元 / 年 (折合7元/月)</div>
    <div class="card-features">
      • 线路：全平台智能分流，节点连通率 99.9%<br>
      • 解锁：原生支持 ChatGPT 网页版与 App<br>
      • 特点：极致性价比，轻量备用首选
    </div>
    <a href="https://flycat1.flycatvipaff.cc/#/?code=KRjsCIZV" target="_blank" rel="sponsored nofollow noopener" class="cta-btn">
      👉 前往【飞猫云】官网注册与选购
    </a>
  </div>

  <div class="top4-card">
    <div class="rank-badge">NO.4 稳健办公 (跨境沟通)</div>
    <div class="card-title">微风网络 Breezenet</div>
    <div class="card-price">￥15.0 元 / 月 (100GB)</div>
    <div class="card-features">
      • 线路：中继协议加密，节点抗封锁能力强<br>
      • 解锁：支持主流 AI 助手与外贸业务沟通<br>
      • 特点：月付无压力，全平台客户端极速兼容
    </div>
    <a href="https://edp01.breezenetaff.com/#/?code=txKNNHZc" target="_blank" rel="sponsored nofollow noopener" class="cta-btn">
      👉 前往【微风网络】官网注册与选购
    </a>
  </div>
</div>
'''

with open(os.path.join(BASE_DIR, "layouts", "partials", "top4_box.html"), "w", encoding="utf-8") as f:
    f.write(top4_box_html)

index_html = '''{{ define "main" }}
<div class="hero-box">
  <h1>⚡ 2026 高速稳定机场测速跑分与极速梯子推荐指南</h1>
  <p>
    jccesu 机场测速实验室专注真实节点跑分测速、晚高峰 8K 视频秒开测试与全平台客户端配置。本站精选自营及稳定专线梯子，首推灵动云（专线主力）、暮光网络（大流量观影）、飞猫云（年付性价比）与微风网络 Breezenet（稳定办公），帮您轻松避坑！
  </p>
  <div style="display:flex; justify-content:center; gap:15px; flex-wrap:wrap;">
    <a href="/recommendations/" class="cta-btn" style="width:auto; padding:10px 24px;">🏆 查看完整机场推荐榜</a>
    <a href="/all-airports/" class="cta-btn" style="width:auto; padding:10px 24px; background:linear-gradient(135deg, #10b981, #059669);">🌐 28 家全机场注册链接大全</a>
  </div>
</div>

<div class="content-section">
  <div class="section-title">🏆 2026 编辑部精选四大主推机场（优先推荐）</div>
  {{ partial "top4_box.html" . }}
</div>

<div class="content-section">
  <div class="section-title">📊 测速评测室最新实测文章</div>
  <div class="article-grid">
    {{ range (where .Site.RegularPages "Section" "speed-test") | first 6 }}
    <div class="article-card">
      <div>
        <h3><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3>
        <p>{{ .Summary | truncate 90 }}</p>
      </div>
      <div class="article-meta">
        <span>📅 {{ .Date.Format "2006-01-02" }}</span>
        <span>⏱️ 5 分钟阅读</span>
      </div>
    </div>
    {{ end }}
  </div>
</div>

<div class="content-section">
  <div class="section-title">💡 客户端极速配置与使用教程</div>
  <div class="article-grid">
    {{ range (where .Site.RegularPages "Section" "tutorials") | first 6 }}
    <div class="article-card">
      <div>
        <h3><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3>
        <p>{{ .Summary | truncate 90 }}</p>
      </div>
      <div class="article-meta">
        <span>📅 {{ .Date.Format "2006-01-02" }}</span>
        <span>⏱️ 6 分钟阅读</span>
      </div>
    </div>
    {{ end }}
  </div>
</div>
{{ end }}
'''

with open(os.path.join(BASE_DIR, "layouts", "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

single_html = '''{{ define "main" }}
<article class="article-content">
  <div style="font-size:0.85rem; color:#94a3b8; margin-bottom:12px;">
    <a href="/">首页</a> &gt; <a href="/{{ .Section }}/">{{ .Section }}</a> &gt; {{ .Title }}
  </div>
  <h1>{{ .Title }}</h1>
  <div style="font-size:0.88rem; color:#94a3b8; border-bottom:1px solid #2a2a32; padding-bottom:15px; margin-bottom:25px; display:flex; gap:20px; flex-wrap:wrap;">
    <span>📅 更新时间：{{ .Date.Format "2006-01-02" }}</span>
    <span>✍️ 作者：jccesu 实验室</span>
    <span>⏱️ 预计字数：1800 字</span>
    <span>🔒 真实测速核验通过</span>
  </div>

  {{ if ne .Section "providers" }}
  <div style="background:#1e1b4b; border:1px solid #4338ca; border-radius:8px; padding:20px; margin-bottom:30px;">
    <h3 style="color:#a5b4fc; margin-bottom:10px; font-size:1.1rem;">⚡ 本站精选推荐机场快捷通道（首推灵动云与暮光网络）</h3>
    <p style="font-size:0.9rem; color:#cbd5e1; margin-bottom:12px;">以下四大自营及精选专线机场经过晚高峰 4K/8K 跑分测速，节点连通率极佳，点击即可直接进入官网注册：</p>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px;">
      <a href="https://varnexa.lingdongaff.com/#/?code=vFPRdc1J" target="_blank" rel="sponsored nofollow noopener" class="cta-btn" style="padding:8px 12px; font-size:0.88rem;">1. 灵动云 (专线主力)</a>
      <a href="https://varnexa.twilightaff.com/#/?code=X6iVG1Zb" target="_blank" rel="sponsored nofollow noopener" class="cta-btn" style="padding:8px 12px; font-size:0.88rem;">2. 暮光网络 (观影大户)</a>
      <a href="https://flycat1.flycatvipaff.cc/#/?code=KRjsCIZV" target="_blank" rel="sponsored nofollow noopener" class="cta-btn" style="padding:8px 12px; font-size:0.88rem;">3. 飞猫云 (84元年付)</a>
      <a href="https://edp01.breezenetaff.com/#/?code=txKNNHZc" target="_blank" rel="sponsored nofollow noopener" class="cta-btn" style="padding:8px 12px; font-size:0.88rem;">4. 微风网络 (稳健办公)</a>
    </div>
  </div>
  {{ end }}

  {{ .Content }}

  <div style="margin-top:40px; padding-top:20px; border-top:1px solid #2a2a32; text-align:center;">
    <p style="font-weight:700; color:#fff; margin-bottom:15px; font-size:1.1rem;">🚀 觉得本文有用？立即挑选适合您的稳定机场：</p>
    <div style="display:flex; justify-content:center; gap:15px; flex-wrap:wrap;">
      <a href="https://varnexa.lingdongaff.com/#/?code=vFPRdc1J" target="_blank" rel="sponsored nofollow noopener" class="cta-btn" style="width:auto; padding:12px 28px;">👉 注册【灵动云】(首选专线)</a>
      <a href="/all-airports/" class="cta-btn" style="width:auto; padding:12px 28px; background:linear-gradient(135deg, #10b981, #059669);">🌐 查看 28 家全机场注册链接大全</a>
    </div>
  </div>
</article>
{{ end }}
'''

with open(os.path.join(BASE_DIR, "layouts", "_default", "single.html"), "w", encoding="utf-8") as f:
    f.write(single_html)

list_html = '''{{ define "main" }}
<div class="content-section">
  <div class="section-title">{{ .Title }}</div>
  <p style="color:#cbd5e1; margin-bottom:25px;">{{ .Description }}</p>

  <div class="article-grid">
    {{ range .Paginator.Pages }}
    <div class="article-card">
      <div>
        <h3><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3>
        <p>{{ .Summary | truncate 110 }}</p>
      </div>
      <div class="article-meta">
        <span>📅 {{ .Date.Format "2006-01-02" }}</span>
        <span>⏱️ 详尽指南</span>
      </div>
    </div>
    {{ end }}
  </div>

  <div style="margin-top:30px; text-align:center;">
    {{ template "_internal/pagination.html" . }}
  </div>
</div>
{{ end }}
'''

with open(os.path.join(BASE_DIR, "layouts", "_default", "list.html"), "w", encoding="utf-8") as f:
    f.write(list_html)

json_index = '''[{{ range $i, $e := .Site.RegularPages }}{{ if $i }}, {{ end }}{
  "title": {{ $e.Title | jsonify }},
  "permalink": {{ $e.RelPermalink | jsonify }},
  "summary": {{ $e.Summary | plainify | jsonify }},
  "contents": {{ $e.Content | plainify | jsonify }}
}{{ end }}]'''

with open(os.path.join(BASE_DIR, "layouts", "index.json"), "w", encoding="utf-8") as f:
    f.write(json_index)

print("Created Hugo templates and CSS/JS assets.")
