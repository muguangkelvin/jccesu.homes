import os
import subprocess

BASE_DIR = r"c:\Users\USER\Desktop\博客\jccesu.homes"

index_html_content = '''{{ define "main" }}
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

<!-- 实验室核心测速介绍与内容规划 (放置在 HERO 与主推榜单之间) -->
<div class="content-section" style="background:#18181c; border:1px solid #2a2a32; border-radius:12px; padding:30px; margin-bottom:40px;">
  <div class="section-title" style="margin-bottom:15px;">🔬 机场测速实验室：用真实数据看清节点质量，告别虚标与断流</div>
  
  <div style="background:#1f1f26; border-left:4px solid #06b6d4; border-radius:6px; padding:18px 22px; margin-bottom:30px; color:#cbd5e1; font-size:0.95rem; line-height:1.8;">
    <p style="margin-bottom:10px;">在网络代理与跨境连接服务市场中，“千兆带宽”、“纯专线不卡顿”、“全节点4K秒开”等宣传口号屡见不鲜。然而，很多用户在实际付费后，常常遭遇晚高峰大面积飘红、严重丢包、测速跑满但网页打不开等现实问题。</p>
    <p style="margin:0;"><strong>机场测速实验室（SpeedTest Lab）</strong> 建立的初衷，就是消除营销宣传与实际体验之间的信息不对称。我们不依赖单次的片面跑分，而是通过多地运营商探针、全天候高频监测以及真实流媒体/AI服务交互测试，构建客观、量化的节点质量数据库。</p>
  </div>

  <!-- 1. 核心测速方法论 -->
  <h3 style="color:#38bdf8; font-size:1.2rem; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
    🎯 我们的核心测速方法论
  </h3>
  <p style="color:#94a3b8; font-size:0.9rem; margin-bottom:18px;">
    评测一个代理服务是否优质，单一的 Speedtest 峰值带宽早已失去参考价值。机场测速实验室采用多维度复合测试体系：
  </p>

  <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px; margin-bottom:35px;">
    <div style="background:#22222a; border:1px solid #333340; border-radius:8px; padding:18px;">
      <h4 style="color:#f59e0b; font-size:1rem; margin-bottom:8px;">🌙 晚高峰极限压力实测</h4>
      <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.6; margin:0;">重点监测每日 20:00 至 23:00 的网络表现，考察运营商骨干网拥塞时的丢包率、延迟抖动与速率下限。</p>
    </div>
    <div style="background:#22222a; border:1px solid #333340; border-radius:8px; padding:18px;">
      <h4 style="color:#10b981; font-size:1rem; margin-bottom:8px;">🌐 三网多节点并发探测</h4>
      <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.6; margin:0;">覆盖中国电信、中国联通、中国移动不同省份的主流入口，还原不同宽带环境下真实的访问延迟与协议穿透力。</p>
    </div>
    <div style="background:#22222a; border:1px solid #333340; border-radius:8px; padding:18px;">
      <h4 style="color:#6366f1; font-size:1rem; margin-bottom:8px;">🚀 真实业务场景吞吐</h4>
      <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.6; margin:0;">不仅看理论带宽，更注重 YouTube 4K/8K 缓冲速度、网页首屏渲染时间，以及 Fast.com / Cloudflare 节点拉流稳定性。</p>
    </div>
    <div style="background:#22222a; border:1px solid #333340; border-radius:8px; padding:18px;">
      <h4 style="color:#ec4899; font-size:1rem; margin-bottom:8px;">🛡️ IP 纯净度与服务风控评级</h4>
      <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.6; margin:0;">自动化检测各节点的流媒体（Netflix、Disney+）解锁状态，以及对 OpenAI（ChatGPT）、Claude 等严格风控平台的原生 IP 支持率。</p>
    </div>
  </div>

  <!-- 2. 核心专栏与内容规划 -->
  <h3 style="color:#38bdf8; font-size:1.2rem; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
    📚 核心专栏与内容规划
  </h3>
  <p style="color:#94a3b8; font-size:0.9rem; margin-bottom:18px;">
    为帮助不同需求的用户快速检索，实验室设有四个核心内容板块：
  </p>

  <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:18px; margin-bottom:35px;">
    <div style="background:#22222a; border:1px solid #333340; border-radius:8px; padding:20px;">
      <h4 style="color:#fff; font-size:1.02rem; margin-bottom:10px; border-bottom:1px solid #3a3a48; padding-bottom:6px;">📊 1. 周期性测速榜单与横向横评</h4>
      <ul style="color:#cbd5e1; font-size:0.86rem; padding-left:18px; line-height:1.7; margin:0;">
        <li><strong>月度/季度稳定性红黑榜</strong>：根据长期监控数据，汇总平均连通率最高与晚高峰劣化严重的平台。</li>
        <li><strong>线路架构分类横评</strong>：横向对比 IPLC/IEPL 纯内网专线、公网 BGP 中继与直连节点的性价比与抗封锁表现。</li>
        <li><strong>小众与新秀挖掘</strong>：针对市面新上线的特色服务进行小范围实测，评估其带宽冗余与技术实力。</li>
      </ul>
    </div>

    <div style="background:#22222a; border:1px solid #333340; border-radius:8px; padding:20px;">
      <h4 style="color:#fff; font-size:1.02rem; margin-bottom:10px; border-bottom:1px solid #3a3a48; padding-bottom:6px;">📈 2. 真实测速图谱与数据报告</h4>
      <ul style="color:#cbd5e1; font-size:0.86rem; padding-left:18px; line-height:1.7; margin:0;">
        <li><strong>全节点延迟热力图</strong>：直观展示香港、日本、新加坡、美国等主流地区节点的平均延迟分布。</li>
        <li><strong>24 小时丢包曲线</strong>：跟踪特定线路一整天的网络波动周期，帮助用户避开骨干网拥挤时段。</li>
        <li><strong>协议效能对比</strong>：在恶劣网络丢包环境下，对比 Shadowsocks、Trojan、VLESS 以及 Hysteria 2、TUIC 等协议的恢复速度与速率表现。</li>
      </ul>
    </div>

    <div style="background:#22222a; border:1px solid #333340; border-radius:8px; padding:20px;">
      <h4 style="color:#fff; font-size:1.02rem; margin-bottom:10px; border-bottom:1px solid #3a3a48; padding-bottom:6px;">🔓 3. 解锁能力与应用场景验证</h4>
      <ul style="color:#cbd5e1; font-size:0.86rem; padding-left:18px; line-height:1.7; margin:0;">
        <li><strong>AI 生产力专线库</strong>：持续跟踪各服务商对 ChatGPT / Claude / Midjourney 的 IP 风控规避能力，标注家宽与原生 IP 分布。</li>
        <li><strong>全球流媒体解锁状态表</strong>：按地区（日区、美区、港区、台区等）实时标记流媒体解锁方案，规避自制剧限制与代理阻断。</li>
        <li><strong>外服游戏低延迟专线测试</strong>：记录 Steam、Epic、外服竞技网游的 UDP 转发表现与 NAT 类型。</li>
      </ul>
    </div>

    <div style="background:#22222a; border:1px solid #333340; border-radius:8px; padding:20px;">
      <h4 style="color:#fff; font-size:1.02rem; margin-bottom:10px; border-bottom:1px solid #3a3a48; padding-bottom:6px;">🛠️ 4. 客户端与测速工具实操指南</h4>
      <ul style="color:#cbd5e1; font-size:0.86rem; padding-left:18px; line-height:1.7; margin:0;">
        <li><strong>自建测速环境教程</strong>：指导用户如何使用主流开源工具（如 StairSpeedTest、SSRSpeed 等）搭建自己的自动化测速脚本。</li>
        <li><strong>主流客户端内核优化</strong>：针对 Clash Verge Rev、Sing-box、Surge、Shadowrocket 等工具提供分流配置优化方案，避免本地 DNS 污染与分流冲突引起的测速偏差。</li>
      </ul>
    </div>
  </div>

  <!-- 3. 实验室量化评估指标 -->
  <h3 style="color:#38bdf8; font-size:1.2rem; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
    ⚖️ 实验室量化评估指标
  </h3>

  <div style="overflow-x:auto; margin-bottom:25px;">
    <table style="width:100%; border-collapse:collapse; background:#1e1b26; border-radius:8px; overflow:hidden;">
      <thead>
        <tr style="background:#2a2a38; color:#fff;">
          <th style="padding:12px 16px; border-bottom:1px solid #3a3a4a; text-align:left;">评估维度</th>
          <th style="padding:12px 16px; border-bottom:1px solid #3a3a4a; text-align:left;">测试指标</th>
          <th style="padding:12px 16px; border-bottom:1px solid #3a3a4a; text-align:left;">合格线标准</th>
          <th style="padding:12px 16px; border-bottom:1px solid #3a3a4a; text-align:left;">极佳标准</th>
        </tr>
      </thead>
      <tbody style="color:#cbd5e1; font-size:0.9rem;">
        <tr style="border-bottom:1px solid #2a2a36;">
          <td style="padding:12px 16px; font-weight:600; color:#fff;">晚高峰丢包率</td>
          <td style="padding:12px 16px;">20:00-23:00 平均丢包</td>
          <td style="padding:12px 16px; color:#f59e0b;">≤ 2.0%</td>
          <td style="padding:12px 16px; color:#10b981; font-weight:700;">≤ 0.1%</td>
        </tr>
        <tr style="border-bottom:1px solid #2a2a36;">
          <td style="padding:12px 16px; font-weight:600; color:#fff;">延迟抖动 (Jitter)</td>
          <td style="padding:12px 16px;">连续发包延迟标准差</td>
          <td style="padding:12px 16px; color:#f59e0b;">≤ 15 ms</td>
          <td style="padding:12px 16px; color:#10b981; font-weight:700;">≤ 3 ms</td>
        </tr>
        <tr style="border-bottom:1px solid #2a2a36;">
          <td style="padding:12px 16px; font-weight:600; color:#fff;">流媒体解锁</td>
          <td style="padding:12px 16px;">常见平台原生 IP 识别率</td>
          <td style="padding:12px 16px;">支持核心大区</td>
          <td style="padding:12px 16px; color:#10b981; font-weight:700;">全球主流全解</td>
        </tr>
        <tr>
          <td style="padding:12px 16px; font-weight:600; color:#fff;">AI 接口可用率</td>
          <td style="padding:12px 16px;">ChatGPT/Claude 网页连通</td>
          <td style="padding:12px 16px;">偶有验证码</td>
          <td style="padding:12px 16px; color:#10b981; font-weight:700;">免验证秒开</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- 4. 结语与免责声明 -->
  <div style="background:#16161f; border:1px solid #2d2d3d; border-radius:8px; padding:20px; margin-top:20px;">
    <p style="color:#e2e8f0; font-weight:600; margin-bottom:8px; font-size:0.96rem;">💡 结语与使用建议：</p>
    <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; margin-bottom:12px;">
      网络连接的质量始终是动态变化的，任何单一时间点的测速截图都不能代表永久的稳定性。建议将 <strong>机场测速实验室</strong> 设为常备参考站点，在订阅续费、节点挑选或排查网络异常时，对比最新发布的动态监控数据，以数据为依据做出最优选择。
    </p>
    <p style="color:#94a3b8; font-size:0.8rem; margin:0; line-height:1.6;">
      (免责声明：本实验室发布的所有技术测评、数据报告与工具使用教程，仅供计算机网络拓扑研究、网络性能测试及跨国合规办公技术交流使用，请严格遵守所在国家与地区的法律法规。)
    </p>
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
    f.write(index_html_content)

print("Updated layouts/index.html with the new Laboratory introduction section.")
