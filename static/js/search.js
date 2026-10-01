document.addEventListener("DOMContentLoaded", function() {
  const searchInput = document.getElementById("search-input");
  const searchResults = document.getElementById("search-results");
  let searchData = [];

  if (!searchInput || !searchResults) return;

  // Keyword association dictionary to expand query terms
  const ASSOCIATIONS = {
    "机场": ["机场", "梯子", "节点", "科学上网", "翻墙", "推荐", "IPLC", "BGP", "灵动云", "暮光网络", "飞猫云", "微风网络"],
    "梯子": ["梯子", "机场", "科学上网", "翻墙", "节点", "推荐", "选购"],
    "节点": ["节点", "测速", "延迟", "丢包率", "IPLC", "IEPL", "Hysteria2", "Trojan", "全节点"],
    "翻墙": ["科学上网", "梯子", "机场", "教程", "客户端"],
    "苹果": ["iOS", "Shadowrocket", "小火箭", "macOS", "Apple ID", "iPhone", "iPad"],
    "安卓": ["Android", "Clash for Android", "Sing-box", "APK", "悬浮窗"],
    "电脑": ["Windows", "macOS", "Clash Verge", "v2rayN", "系统代理"],
    "ai": ["chatgpt", "claude", "gemini", "midjourney", "sora", "原生住宅 ip", "风控", "人工智能"],
    "流媒体": ["netflix", "disney+", "8k", "观影", "youtube", "4k秒开", "解锁"],
    "优惠": ["优惠码", "8折", "年付", "性价比", "折扣", "充值"],
    "小白": ["新手", "入门", "推荐", "教程", "一键"],
    "教程": ["配置", "设置", "导入", "客户端", "教程"]
  };

  fetch("/index.json")
    .then(res => res.json())
    .then(data => { searchData = data; })
    .catch(err => console.error("Error loading search index:", err));

  function getSectionTag(permalink) {
    if (permalink.includes("/speed-test/")) return '<span class="search-tag" style="background:#0284c7; color:#e0f2fe;">📊 测速</span>';
    if (permalink.includes("/recommendations/")) return '<span class="search-tag" style="background:#7c3aed; color:#ede9fe;">🏆 推荐</span>';
    if (permalink.includes("/tutorials/")) return '<span class="search-tag" style="background:#059669; color:#d1fae5;">💡 教程</span>';
    if (permalink.includes("/knowledge/")) return '<span class="search-tag" style="background:#d97706; color:#fef3c7;">📚 知识</span>';
    if (permalink.includes("/faq/")) return '<span class="search-tag" style="background:#db2777; color:#fce7f3;">❓ FAQ</span>';
    if (permalink.includes("/all-airports/")) return '<span class="search-tag" style="background:#2563eb; color:#dbeafe;">🌐 28家机场</span>';
    return '<span class="search-tag">📄 文章</span>';
  }

  function highlight(text, queries) {
    if (!text) return "";
    let clean = text.replace(/<[^>]*>?/gm, '');
    let lower = clean.toLowerCase();

    for (let q of queries) {
      if (!q || q.length === 0) continue;
      let idx = lower.indexOf(q);
      if (idx !== -1) {
        let start = Math.max(0, idx - 20);
        let end = Math.min(clean.length, idx + q.length + 40);
        let snippet = (start > 0 ? "..." : "") + clean.substring(start, end) + (end < clean.length ? "..." : "");
        // Highlight query match
        let regex = new RegExp(`(${q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
        return snippet.replace(regex, '<mark style="background:#f59e0b; color:#000; padding:0 2px; border-radius:2px;">$1</mark>');
      }
    }
    return clean.length > 70 ? clean.substring(0, 70) + "..." : clean;
  }

  searchInput.addEventListener("input", function() {
    const rawQuery = this.value.trim().toLowerCase();
    if (rawQuery.length < 1) {
      searchResults.style.display = "none";
      searchResults.innerHTML = "";
      return;
    }

    // Split query by spaces
    const queryTokens = rawQuery.split(/\s+/).filter(t => t.length > 0);
    
    // Expand tokens with associations
    let expandedTokens = [...queryTokens];
    for (let t of queryTokens) {
      if (ASSOCIATIONS[t]) {
        expandedTokens.push(...ASSOCIATIONS[t].map(x => x.toLowerCase()));
      }
    }

    const matches = searchData.filter(item => {
      const titleLower = (item.title || "").toLowerCase();
      const summaryLower = (item.summary || "").toLowerCase();
      const contentsLower = (item.contents || "").toLowerCase();
      const fullText = titleLower + " " + summaryLower + " " + contentsLower;

      // Check if item contains any of the query tokens or associated terms
      return expandedTokens.some(tok => fullText.includes(tok));
    }).sort((a, b) => {
      // Prioritize title matches
      const aTitleMatch = queryTokens.some(tok => (a.title || "").toLowerCase().includes(tok));
      const bTitleMatch = queryTokens.some(tok => (b.title || "").toLowerCase().includes(tok));
      if (aTitleMatch && !bTitleMatch) return -1;
      if (!aTitleMatch && bTitleMatch) return 1;
      return 0;
    }).slice(0, 10);

    if (matches.length > 0) {
      searchResults.innerHTML = matches.map(m => `
        <a href="${m.permalink}">
          <div style="margin-bottom:4px; display:flex; align-items:center;">
            ${getSectionTag(m.permalink)}
            <strong style="color:#f8fafc; font-size:0.9rem;">${m.title}</strong>
          </div>
          <div style="font-size:0.78rem; color:#94a3b8; line-height:1.5;">
            ${highlight(m.summary || m.contents, queryTokens)}
          </div>
        </a>
      `).join('');
      searchResults.style.display = "block";
    } else {
      searchResults.innerHTML = `<div style="padding:14px; text-align:center; font-size:0.85rem; color:#94a3b8;">🔍 未找到与“<strong style="color:#38bdf8;">${rawQuery}</strong>”相关的文章或节点</div>`;
      searchResults.style.display = "block";
    }
  });

  document.addEventListener("click", function(e) {
    if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
      searchResults.style.display = "none";
    }
  });
});
