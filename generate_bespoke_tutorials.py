import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import json
from generate_bespoke_articles import BASE_DIR, write_md, make_top4_box

print("Generating 20 bespoke Tutorial articles with neat side-by-side Step Card Grid layout...")

def make_step_cards_grid(step_list):
    cards_html = []
    cards_html.append('<div class="tutorial-steps-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:18px; margin:25px 0;">')
    for idx, (title, body_html, verify_text) in enumerate(step_list, 1):
        num_str = f"STEP {idx:02d}"
        cards_html.append(f'''  <div class="step-card" style="background:#181824; border:1px solid #2d2d3e; border-radius:10px; padding:20px; display:flex; flex-direction:column; justify-content:space-between;">
    <div>
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid #2a2a38; padding-bottom:10px;">
        <span style="background:#312e81; color:#a5b4fc; font-size:0.78rem; font-weight:700; padding:3px 10px; border-radius:20px;">{num_str}</span>
        <h4 style="color:#60a5fa; margin:0; font-size:1.05rem; font-weight:700;">{title}</h4>
      </div>
      <div style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin-bottom:15px;">
        {body_html}
      </div>
    </div>
    <div style="background:#13121d; border:1px solid #1e1e2d; border-radius:6px; padding:8px 12px; font-size:0.82rem; color:#34d399;">
      {verify_text}
    </div>
  </div>''')
    cards_html.append('</div>')
    return "\n".join(cards_html)

tutorials_deep_data = [
    # 1. Clash Verge Rev
    (
        "tutorial-1.md",
        "Clash Verge Rev 新手小白零基础教程：从订阅导入到系统代理配置",
        "针对 Windows 与 macOS 用户提供 Clash Verge Rev 最新版从官方下载、一键订阅导入到系统代理与分流模式开启的全流程图文指南。",
        """
# 💻 1. 桌面端：Windows & macOS (推荐 Clash Verge Rev)

Clash Verge Rev 是目前桌面端功能最完善、界面现代化且支持 Clash Meta (Mihomo) 内核的主流代理客户端。

---

""" + make_top4_box("Clash Verge Rev 最佳搭配机场") + """

---

## 🛠️ 三步并列配置教学指南（桌面端极速上手）

""" + make_step_cards_grid([
    (
        "步骤 1：下载与安装",
        '• <strong style="color:#38bdf8;">Windows</strong>：前往 GitHub Releases 下载以 <code>.msi</code> 或 <code>_x64-setup.exe</code> 结尾的安装包（如提示缺少运行环境，需配合安装微软 WebView2）。<br>• <strong style="color:#a78bfa;">macOS</strong>：Apple Silicon (M1/M2/M3/M4 系列芯片) 请选择 <code>aarch64.dmg</code>；Intel 芯片老款 Mac 请选择 <code>x64.dmg</code>。安装后首次打开若提示“无法验证开发者”，请在 macOS 系统设置 -> 隐私与安全性中点击“仍要打开”。',
        '✔️ <strong>验证方法</strong>：双击图标能顺畅打开界面即表示安装成功。'
    ),
    (
        "步骤 2：导入订阅配置",
        '1. 打开 Clash Verge Rev，在左侧导航栏点击 <strong>订阅 (Subscription)</strong>。<br>2. 将复制好的机场订阅链接粘贴到顶部的 URI 输入框中，点击 <strong>导入 (Import)</strong>。<br>3. 导入成功后，列表会显示该配置卡片，单击选中让其高亮生效。',
        '✅ <strong>验证方法</strong>：卡片上显示更新时间与节点数量即代表导入成功。'
    ),
    (
        "步骤 3：选择节点并开启系统代理",
        '1. 点击左侧 <strong>代理 (Proxy)</strong> 菜单，顶部模式保持为 <strong>Rule (规则)</strong>。<br>2. 点击右上角的 Wi-Fi 测速图标，列表会显示各节点延迟 (毫秒数)，点击选中一个可用的低延迟节点。<br>3. 回到主界面或 设置 (Settings)，将 <strong>系统代理 (System Proxy)</strong> 开关切换为开启。',
        '🎉 <strong>验证方法</strong>：打开浏览器访问常用海外网站 (如 Google/YouTube)，页面能顺畅秒开即表示配置成功。'
    )
]) + """

---

## ⚡ 常见报错与故障排查表

| 报错现象 | 可能原因 | 解决办法 |
| :--- | :--- | :--- |
| **刷新订阅提示 Config Parse Error** | 订阅 URL 不完整或机场被封 | 在机场后台获取最新订阅链接重新导入 |
| **开启代理后全网无连接/提示 Timeout** | 本地时间不同步或端口冲突 | 同步 Windows/Mac NTP 时间，重启软件 |
| **无法打开 ChatGPT 提示 Access Denied** | 节点 IP 风控 | 切换至灵动云美区原生住宅 IP 节点 |
| **开启 TUN 模式后电脑断网** | 网卡驱动冲突 | 参阅 [TUN 模式断网修复教程](/tutorials/tutorial-11/) |

---

## 📚 相关教程与扩展阅读

- **路由全家出海**：[OpenWrt 路由器部署 OpenClash 教程](/tutorials/tutorial-7/)
- **防 DNS 污染**：[Clash Verge 开启 Fake-IP 模式教程](/tutorials/tutorial-17/)
- **全机场大盘点**：[28 家全机场注册链接大全](/all-airports/)
- **常见问题解答**：[常见疑问答疑中心](/faq/)
"""
    ),
    # 3. iOS Shadowrocket
    (
        "tutorial-3.md",
        "iOS Shadowrocket (小火箭) 节点导入教程：扫码配置与策略组切换",
        "针对 iPhone 与 iPad 用户提供 Shadowrocket (小火箭) 最新版从美区 Apple ID 获取、二维码扫描一键导入到节点规则分流的全流程指南。",
        """
# 📱 2. 苹果移动端：iOS / iPadOS (推荐 Shadowrocket 小火箭)

Shadowrocket (俗称“小火箭”) 是 iOS 端功能强大、连接极其稳定的经典规则分流工具。

---

""" + make_top4_box("iOS 小火箭最佳搭配机场") + """

---

## 🛠️ 三步并列配置教学指南（苹果手机极速上手）

""" + make_step_cards_grid([
    (
        "步骤 1：获取与下载",
        '由于区域限制，Shadowrocket 未在部分地区的 App Store 上架，需使用美区等非国区 Apple ID 登录 App Store 后搜索并购买下载（注意认准开发者：Shadow Launch Technology Limited）。',
        '✔️ <strong>验证方法</strong>：桌面出现小火箭图标即安装成功。'
    ),
    (
        "步骤 2：扫码或一键导入订阅",
        '1. 打开 <strong>灵动云</strong> 或 <strong>暮光网络</strong> 个人后台。<br>2. 用手机浏览器打开机场后台，点击【一键导入 Shadowrocket】；或者使用小火箭首页右上角 <strong>+</strong> 号图标扫描专属二维码。',
        '✅ <strong>验证方法</strong>：小火箭首页刷新出全部节点列表。'
    ),
    (
        "步骤 3：启动连接与允许 VPN 权限",
        '1. 在小火箭首页选择一个延迟较低的节点（如香港 IPLC）。<br>2. 点击顶部【未连接】开关，首次连接系统会弹出【添加 VPN 配置】请求，按提示输入 iPhone 解锁密码授权即可。',
        '🎉 <strong>验证方法</strong>：状态栏出现 VPN 标志，网页正常秒开。'
    )
]) + """

---

## ⚡ 常见问题排查与备用方案

- **无法安装 Shadowrocket**：建议参阅 [获取美区 Apple ID 注册教程](/tutorials/tutorial-14/)。
- **节点全部连接超时**：在小火箭【设置 -> 延迟测试】中将测试 URL 更改为 `https://www.google.com/generate_204`。
"""
    ),
    # 5. Android Clash for Android
    (
        "tutorial-5.md",
        "Android 手机 Clash for Android 配置教程：开启悬浮窗与 Tun 模式",
        "针对安卓手机用户提供 Clash for Android (CFA) 的详细配置步骤，包含订阅导入、应用分流、悬浮窗开启与 TUN 虚拟网卡设置。",
        """
# 🤖 3. 安卓移动端：Android 手机 (推荐 Clash for Android / Sing-box)

Clash for Android 是安卓端最强大的代理工具，支持 TUN 虚拟网卡与应用分流。

---

""" + make_top4_box("安卓手机搭配机场推荐") + """

---

## 🛠️ 三步并列配置教学指南（安卓手机极速上手）

""" + make_step_cards_grid([
    (
        "步骤 1：下载与后台权限授权",
        '下载并安装 APK 安装包。在手机【设置 -> 应用管理 -> Clash】中开启【悬浮窗/出现在顶部】权限与【无限制电池策略】，防止系统后台误杀。',
        '✔️ <strong>验证方法</strong>：允许建立 VPN 连接授权。'
    ),
    (
        "步骤 2：导入订阅配置文件",
        '1. 登录 <strong>飞猫云</strong> 或 <strong>灵动云</strong> 后台，点击【一键导入 Clash 订阅】。<br>2. 在唤醒的 Clash 中设置自动更新间隔，点击右上角【保存】选定该配置。',
        '✅ <strong>验证方法</strong>：配置列表出现配置文件卡片。'
    ),
    (
        "步骤 3：开启 VPN 与应用分流",
        '1. 点击【已停止】主开关启动代理连接。<br>2. 在【网络 -> 访问控制】中设置分流黑名单，将微信、支付宝排除直连，YouTube、X 走代理。',
        '🎉 <strong>验证方法</strong>：悬浮窗显示实时网速，海外应用顺畅运行。'
    )
]) + """

---

## 📚 扩展阅读
- 参阅 [Sing-box 安卓配置教程](/tutorials/tutorial-2/)
- 查阅 [全机场注册大全](/all-airports/)
"""
    )
]

# Process and write bespoke files
for filename, title, desc, cnt in tutorials_deep_data:
    fp = os.path.join(BASE_DIR, "content", "tutorials", filename)
    write_md(fp, title, desc, cnt)

print("Tutorial articles upgraded with neat side-by-side Step Card Grid layout successfully!")
