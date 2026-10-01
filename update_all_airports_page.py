import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import json

BASE_DIR = r"c:\Users\USER\Desktop\博客\jccesu.homes"

with open(os.path.join(BASE_DIR, "data", "providers.json"), "r", encoding="utf-8") as f:
    PROVIDERS = json.load(f)

print(f"Loaded {len(PROVIDERS)} providers from providers.json.")

# Generate content for content/all-airports/index.md
md_lines = []
md_lines.append("---")
md_lines.append('title: "2026 全网 28 家稳定科学上网机场注册链接与选购大盘点"')
md_lines.append('description: "汇总全网 28 家主流科学上网机场的完整套餐价格、简介、热点亮点、覆盖地区、支持设备、专属优惠码及官方注册链接。"')
md_lines.append("date: 2026-09-30")
md_lines.append("draft: false")
md_lines.append("---")
md_lines.append("")
md_lines.append("# 🌐 2026 全网 28 家稳定科学上网机场注册链接与选购大盘点")
md_lines.append("")
md_lines.append("为方便广大新手小白与极客用户快速比价及寻找最适合自己的科学上网梯子，jccesu 机场测速实验室将本站整理的 28 家机场官方注册链接、全部套餐价格、简介描述、核心热点亮点、节点覆盖地区、支持设备与客户端以及专属优惠码汇总盘点如下：")
md_lines.append("")
md_lines.append('<div style="background:#181824; border:1px solid #2a2a38; border-radius:10px; padding:20px; margin:25px 0;">')
md_lines.append('  <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; margin:0; padding-left:18px;">')
md_lines.append('    <li><strong>付费策略建议</strong>：初次尝试任意机场，强烈建议先购买月付或试用套餐。实际测试高峰期（晚 8:00 - 11:00）的油管跑分与延迟表现满意后，再考虑长期订阅。</li>')
md_lines.append('    <li><strong>常备主力与备用</strong>：建议搭配“一主一副”双机场策略，避免单一服务商维护时影响工作与娱乐。</li>')
md_lines.append('  </ul>')
md_lines.append('</div>')
md_lines.append("")
md_lines.append('<div style="text-align:center; padding:16px 0; border-top:1px dashed #3a3a4c; margin:25px 0;">')
md_lines.append('  <h3 style="color:#60a5fa; font-size:1.3rem; font-weight:700; margin:0; display:inline-flex; align-items:center; gap:8px;">')
md_lines.append('    🧾 梯子优选与精选推荐文章合集')
md_lines.append('  </h3>')
md_lines.append('</div>')
md_lines.append("")
md_lines.append('<h2 style="color:#fff; font-size:1.35rem; font-weight:700; margin-bottom:8px;">📋 28款优质机场导航与直达汇总</h2>')
md_lines.append('<p style="color:#94a3b8; font-size:0.9rem; margin-bottom:20px;">为了方便查阅与选择，以下按照线路特性及适用场景分为四个梯队：</p>')
md_lines.append("")
md_lines.append("## 🏆 第一梯队：特色线路与隐蔽安全优选")
md_lines.append("提供高私密性、防审查协议与多地区冷门节点的定制化加速方案。")
md_lines.append("")
md_lines.append('<div style="overflow-x:auto; margin-bottom:30px;">')
md_lines.append('  <table style="width:100%; border-collapse:collapse; background:#181822; border-radius:8px; overflow:hidden; border:1px solid #2a2a38;">')
md_lines.append('    <thead>')
md_lines.append('      <tr style="background:#222230; color:#cbd5e1; font-size:0.92rem; text-align:left;">')
md_lines.append('        <th style="padding:12px 16px; border-bottom:1px solid #2d2d3e; width:22%;">节点名称</th>')
md_lines.append('        <th style="padding:12px 16px; border-bottom:1px solid #2d2d3e; width:56%;">特点与定位</th>')
md_lines.append('        <th style="padding:12px 16px; border-bottom:1px solid #2d2d3e; width:22%; text-align:center;">官网直达</th>')
md_lines.append('      </tr>')
md_lines.append('    </thead>')
md_lines.append('    <tbody style="color:#e2e8f0; font-size:0.9rem;">')
md_lines.append('      <tr style="border-bottom:1px solid #222230;">')
md_lines.append('        <td style="padding:12px 16px; font-weight:700; color:#60a5fa;">🥇 灵动云</td>')
md_lines.append('        <td style="padding:12px 16px; color:#cbd5e1;">动态调整最优节点，移动漫游无感切换</td>')
md_lines.append('        <td style="padding:12px 16px; text-align:center;"><a href="https://varnexa.lingdongaff.com/#/?code=vFPRdc1J" target="_blank" rel="sponsored nofollow noopener" style="display:inline-block; background:#10b981; color:#fff; padding:6px 14px; border-radius:6px; font-size:0.85rem; font-weight:600; text-decoration:none;">前往灵动云官网</a></td>')
md_lines.append('      </tr>')
md_lines.append('      <tr style="border-bottom:1px solid #222230;">')
md_lines.append('        <td style="padding:12px 16px; font-weight:700; color:#fff;">🥈 暮光网络</td>')
md_lines.append('        <td style="padding:12px 16px; color:#cbd5e1;">线路优化完善，流媒体原生 IP 解锁良好</td>')
md_lines.append('        <td style="padding:12px 16px; text-align:center;"><a href="https://varnexa.twilightaff.com/#/?code=X6iVG1Zb" target="_blank" rel="sponsored nofollow noopener" style="display:inline-block; background:#10b981; color:#fff; padding:6px 14px; border-radius:6px; font-size:0.85rem; font-weight:600; text-decoration:none;">前往暮光网络官网</a></td>')
md_lines.append('      </tr>')
md_lines.append('      <tr style="border-bottom:1px solid #222230;">')
md_lines.append('        <td style="padding:12px 16px; font-weight:700; color:#fff;">🥉 飞V</td>')
md_lines.append('        <td style="padding:12px 16px; color:#cbd5e1;">简洁高效，多客户端支持完备</td>')
md_lines.append('        <td style="padding:12px 16px; text-align:center;"><a href="https://varnexa.flyvaff.com/#/?code=y439Zqry" target="_blank" rel="sponsored nofollow noopener" style="display:inline-block; background:#10b981; color:#fff; padding:6px 14px; border-radius:6px; font-size:0.85rem; font-weight:600; text-decoration:none;">前往飞V官网</a></td>')
md_lines.append('      </tr>')
md_lines.append('      <tr style="border-bottom:1px solid #222230;">')
md_lines.append('        <td style="padding:12px 16px; font-weight:700; color:#fff;">梯子云 LadderCloud</td>')
md_lines.append('        <td style="padding:12px 16px; color:#cbd5e1;">老牌协议多通道支持，适合各类小众客户端</td>')
md_lines.append('        <td style="padding:12px 16px; text-align:center;"><a href="https://varnexa.ladderaff.com/#/?code=k98borBb" target="_blank" rel="sponsored nofollow noopener" style="display:inline-block; background:#10b981; color:#fff; padding:6px 14px; border-radius:6px; font-size:0.85rem; font-weight:600; text-decoration:none;">前往梯子云官网</a></td>')
md_lines.append('      </tr>')
md_lines.append('      <tr style="border-bottom:1px solid #222230;">')
md_lines.append('        <td style="padding:12px 16px; font-weight:700; color:#fff;">浪网 WaveNet</td>')
md_lines.append('        <td style="padding:12px 16px; color:#cbd5e1;">动态流量分发，大带宽不限速体验</td>')
md_lines.append('        <td style="padding:12px 16px; text-align:center;"><a href="https://varnexa.wavenetaff.com/#/?code=YpiKU7ii" target="_blank" rel="sponsored nofollow noopener" style="display:inline-block; background:#10b981; color:#fff; padding:6px 14px; border-radius:6px; font-size:0.85rem; font-weight:600; text-decoration:none;">前往浪网官网</a></td>')
md_lines.append('      </tr>')
md_lines.append('      <tr>')
md_lines.append('        <td style="padding:12px 16px; font-weight:700; color:#fff;">隐形人</td>')
md_lines.append('        <td style="padding:12px 16px; color:#cbd5e1;">主打深度混淆与抗封锁，敏感时期安全稳定</td>')
md_lines.append('        <td style="padding:12px 16px; text-align:center;"><a href="https://varnexa.invisibleaff.com/#/?code=CnM0SCna" target="_blank" rel="sponsored nofollow noopener" style="display:inline-block; background:#10b981; color:#fff; padding:6px 14px; border-radius:6px; font-size:0.85rem; font-weight:600; text-decoration:none;">前往隐形人官网</a></td>')
md_lines.append('      </tr>')
md_lines.append('    </tbody>')
md_lines.append('  </table>')
md_lines.append('</div>')
md_lines.append("")
md_lines.append("## 🏆 编辑部重点推荐四大主力机场 (精细参数大盘点)")
md_lines.append("")

# Top 4 Detailed Cards
primary_providers = [p for p in PROVIDERS if p.get("isPrimary", False)]
for p in primary_providers:
    rank = p["rank"]
    name = p["name"]
    url = p["inviteURL"]
    price = p.get("priceFrom", "")
    traffic = p.get("trafficFrom", "")
    summary = p.get("summary", "")
    suitable = p.get("suitableFor", "")
    ai_unlock = p.get("aiUnlock", "")
    regions = p.get("regions", "")
    coupon = p.get("coupon", "无")
    coupon_note = p.get("couponNote", "专享优惠")
    
    md_lines.append(f'<div style="background:#181824; border:1px solid #3b82f6; border-radius:10px; padding:20px; margin-bottom:25px;">')
    md_lines.append(f'  <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #2d2d3f; padding-bottom:12px; margin-bottom:15px;">')
    md_lines.append(f'    <h3 style="color:#60a5fa; margin:0; font-size:1.25rem;">NO.{rank} {name} (编辑部主力首选)</h3>')
    md_lines.append(f'    <a href="{url}" target="_blank" rel="sponsored nofollow noopener" class="cta-btn" style="padding:6px 14px; font-size:0.88rem;">👉 官网注册/登录</a>')
    md_lines.append(f'  </div>')
    md_lines.append(f'  <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:14px; font-size:0.92rem; color:#cbd5e1;">')
    md_lines.append(f'    <div><strong style="color:#f59e0b;">💰 套餐价格：</strong>{price}（基础流量 {traffic}，另有季付/年付高阶套餐）</div>')
    md_lines.append(f'    <div><strong style="color:#10b981;">🎫 优惠码：</strong><code style="background:#262636; padding:2px 6px; border-radius:4px; color:#34d399;">{coupon}</code> ({coupon_note})</div>')
    md_lines.append(f'    <div><strong style="color:#38bdf8;">🌐 覆盖地区：</strong>{regions}</div>')
    md_lines.append(f'    <div><strong style="color:#a78bfa;">📱 支持设备：</strong>Windows / macOS / iOS (小火箭/QuanX) / Android (Clash) / Linux / 路由器</div>')
    md_lines.append(f'  </div>')
    md_lines.append(f'  <div style="margin-top:14px; padding-top:12px; border-top:1px dashed #2d2d3f; font-size:0.9rem; color:#cbd5e1; line-height:1.7;">')
    md_lines.append(f'    <p style="margin-bottom:6px;"><strong style="color:#ec4899;">📝 简介：</strong>{summary}</p>')
    md_lines.append(f'    <p style="margin:0;"><strong style="color:#f43f5e;">🔥 热点与亮点：</strong>{suitable} | {ai_unlock}</p>')
    md_lines.append(f'  </div>')
    md_lines.append(f'</div>')
    md_lines.append("")

md_lines.append("---")
md_lines.append("")
md_lines.append("## 📊 全网更多精选机场完整大盘点表 (第 5 - 28 名)")
md_lines.append("")

# Table header with all required columns
md_lines.append("| 序号与名称 | 套餐价格 | 简介 | 核心热点 & AI解锁 | 覆盖地区 | 支持设备 | 优惠码 | 官方注册链接 |")
md_lines.append("| :---: | :---: | :--- | :--- | :--- | :--- | :---: | :---: |")

other_providers = [p for p in PROVIDERS if not p.get("isPrimary", False)]
for p in other_providers:
    rank = p["rank"]
    name = p["name"]
    url = p["inviteURL"]
    price = p.get("priceFrom", "暂无")
    traffic = p.get("trafficFrom", "")
    summary = p.get("summary", "")
    suitable = p.get("suitableFor", "")
    ai_unlock = p.get("aiUnlock", "")
    regions = p.get("regions", "港日新美台")
    coupon = p.get("coupon", "直达优惠")
    coupon_note = p.get("couponNote", "专享优惠")
    
    # Format table cells nicely
    price_str = f"<b>{price}</b><br><small style='color:#94a3b8;'>({traffic})</small>"
    hot_str = f"<b>{suitable}</b><br><small style='color:#cbd5e1;'>AI: {ai_unlock}</small>"
    devices_str = "Win / Mac / iOS / Android / 路由器"
    coupon_str = f"<code>{coupon}</code><br><small style='color:#34d399;'>{coupon_note}</small>" if coupon != "直达优惠" else "点击链接享优惠"
    link_str = f"<a href='{url}' target='_blank' rel='sponsored nofollow noopener' style='color:#38bdf8; font-weight:600;'>👉 注册 {name}</a>"
    
    md_lines.append(f"| **{rank}. {name}** | {price_str} | {summary} | {hot_str} | {regions} | {devices_str} | {coupon_str} | {link_str} |")

md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("### 💡 选购避坑总结与说明")
md_lines.append("1. **链接真实性**：本表格所有链接均为官方直达注册链接（包含专享优惠通道），请放心点击使用。")
md_lines.append("2. **优惠码使用**：在发卡网结算时，复制对应机场的优惠码在【优惠券/折扣码】输入框中粘贴即可享受额外折扣。")
md_lines.append("3. **售后交流**：官方 Telegram 频道与交流群：[Telegram 官方频道](https://t.me/+HVHzlzUXk4YyOWM9)。")
md_lines.append("")

output_path = os.path.join(BASE_DIR, "content", "all-airports", "index.md")
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Successfully wrote all 28 providers detailed data to {output_path}!")
