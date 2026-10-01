import os
import json
from builder_part3 import generate_rich_article_content

BASE_DIR = r"c:\Users\USER\Desktop\博客\jccesu.homes"

with open(os.path.join(BASE_DIR, "data", "providers.json"), "r", encoding="utf-8") as f:
    PROVIDERS = json.load(f)

with open(os.path.join(BASE_DIR, "data", "faqs.json"), "r", encoding="utf-8") as f:
    FAQS = json.load(f)

def write_md(file_path, title, description, content, date_str="2026-09-30"):
    summary_clean = description.replace('"', '\\"')
    fm = f"""---
title: "{title}"
description: "{description}"
summary: "{summary_clean}"
date: {date_str}
draft: false
---

{content}
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(fm)

# 1. SPEED TEST (15 Articles)
speed_test_titles = [
    "2026晚高峰机场跑分测速排行榜：谁是真正的 IPLC 专线之王",
    "4K与8K视频秒开体验评测：主流科学上网梯子下载吞吐量对比",
    "低延迟外服游戏加速测速：英雄联盟与 Steam 联机节点丢包率实测",
    "IPLC 点对点专线 vs IEPL 专线测速：晚高峰网络延迟对比分析",
    "BGP 多线入口节点解析：电信、联通与移动三网测速差异测试",
    "香港节点 vs 日本节点 vs 美区节点：延迟与网速跑分横向评测",
    "Hysteria2 协议极速跑分测试：劣质网络环境下的抗封锁加速表现",
    "Trojan 协议 TLS 握手延迟测试：网页加载速度与防封锁实测",
    "机场节点倍率（1x, 2x, 0.5x）真实速率测试：高倍率节点真的更快吗",
    "单线程与多线程下载速度测速：哪家机场能够跑满千兆家用宽带",
    "奈飞 Netflix 4K 与 Disney+ 高清流媒体解锁速度专项测试",
    "ChatGPT 与 Claude 3.5 原生住宅 IP 节点访问速度与风控检测",
    "移动 5G 手机网络科学上网测速：不同客户端连接稳定性对比",
    "免费与付费机场跑分差距有多大：节点超时率与带宽对比",
    "2026上半年机场稳定性综合跑分大盘点：防跑路选购指南"
]

for idx, t in enumerate(speed_test_titles, 1):
    fp = os.path.join(BASE_DIR, "content", "speed-test", f"speed-test-{idx}.md")
    cnt = generate_rich_article_content(t, "speed-test", "机场测速跑分")
    write_md(fp, t, f"针对【{t}】开展全方位的晚高峰真实测速与详细数据分析指南。", cnt)

print("Updated 15 Speed Test articles with clean summaries.")

# 2. RECOMMENDATIONS (20 Articles)
recommendations_titles = [
    "2026稳定机场推荐指南：新手小白避坑与高性价比梯子选购",
    "便宜稳定梯子推荐排行榜：年付 84 元起的高速科学上网服务",
    "Clash Verge 最强兼容机场推荐：一键导入与自动化规则分流",
    "Sing-box 极速节点机场推荐：支持 Hysteria2 与低耗电协议",
    "iOS 小火箭 (Shadowrocket) 专属机场推荐：扫描二维码极速上手",
    "外贸跨境电商与企业协同办公机场推荐：独享 IP 与全天候稳定",
    "AI 大模型开发者专属机场推荐：完美解锁 ChatGPT / Claude 3.5",
    "外服游戏玩家低延迟加速梯子推荐：延迟 30ms 以内 IPLC 专线",
    "8K 超高清流媒体观影机场推荐：晚高峰不卡顿大流量套餐",
    "按量付费（不限时长流量包）机场推荐：适合轻度出海用户",
    "月付 15 元以内平价科学上网机场推荐：学生党与新手首选",
    "备用梯子机场挑选建议：主线路维护时的双保险方案",
    "多设备家庭共享机场推荐：支持 5 台以上设备同时在线",
    "Windows 与 macOS 跨平台办公机场推荐：全客户端一键配置",
    "防封锁防跑路专线机场推荐：运营多年口碑老牌大厂大盘点",
    "顶级 IPLC/IEPL 专线机场对比推荐：灵动云 vs 暮光网络实测",
    "追剧党必看：全网主流 4K 解锁流媒体机场推荐与测试",
    "免费试用与退款保障机场推荐：零风险购买避坑指南",
    "全球多地区出口节点机场推荐：涵盖港台日韩美英欧节点",
    "2026终极科学上网梯子选购清单：按预算与需求精准匹配"
]

for idx, t in enumerate(recommendations_titles, 1):
    fp = os.path.join(BASE_DIR, "content", "recommendations", f"recommendation-{idx}.md")
    cnt = generate_rich_article_content(t, "recommendations", "机场推荐")
    write_md(fp, t, f"【{t}】全面剖析性价比、节点延迟与优质服务商选购建议。", cnt)

print("Updated 20 Recommendation articles with clean summaries.")

# 3. TUTORIALS (20 Articles)
tutorials_titles = [
    "Clash Verge Rev 新手小白零基础教程：从订阅导入到系统代理配置",
    "Sing-box 全平台配置指南：支持 Hysteria2 协议极速科学上网",
    "iOS Shadowrocket (小火箭) 节点导入教程：扫码配置与策略组切换",
    "v2rayN 最新版使用教程：手动添加节点与一键更新订阅步骤",
    "Android 手机 Clash for Android 配置教程：开启悬浮窗与 Tun 模式",
    "macOS 苹果电脑科学上网教程：Clash Verge macOS 版安装与授权",
    "OpenWrt 路由器安装 OpenClash 教程：实现全家设备自动翻墙",
    "Sub-Store 订阅转换工具使用教程：组合多个机场与节点去重",
    "Clash 策略组与分流规则配置教程：实现国内直连与海外代理分离",
    "解决 Clash 节点全部 Timeout 超时报错的 5 个排查步骤",
    "Clash 开启 Tun 模式后电脑无法联网解决教程与网络重置",
    "如何使用浏览器 SwitchyOmega 插件配合代理客户端灵活翻墙",
    "Shadowsocks / Trojan 手动配置教程：服务器地址与加密参数填写",
    "如何获取美区 Apple ID 并下载 Shadowrocket / Quantumult X",
    "智能电视 (Android TV / 小米电视) 安装科学上网软件看 4K 教程",
    "Linux 服务器环境下命令行配置 Clash / Sing-box 代理教程",
    "Clash Verge 自定义 DNS 防污染设置教程：开启 Fake-IP 模式",
    "新手购买机场后第一步操作清单：从发卡网到成功连通全过程",
    "如何使用 MTR 和 PingPlotter 测试自己节点的真实丢包率",
    "科学上网客户端防止 DNS 泄露与 WebRTC 隐私泄露全攻略"
]

for idx, t in enumerate(tutorials_titles, 1):
    fp = os.path.join(BASE_DIR, "content", "tutorials", f"tutorial-{idx}.md")
    cnt = generate_rich_article_content(t, "tutorials", "客户端教程")
    write_md(fp, t, f"【{t}】详细手把手图文操作指南与报错排查。", cnt)

print("Updated 20 Tutorial articles with clean summaries.")

# 4. KNOWLEDGE (15 Articles)
knowledge_titles = [
    "IPLC 专线与 IEPL 专线原理详解：为什么它们能做到不过 GFW",
    "BGP 多线中继工作原理：如何解决电信/联通/移动跨网卡顿问题",
    "Trojan 协议原理剖析：如何通过伪装 HTTPS 流量实现高抗封锁",
    "Hysteria2 协议技术优势：UDP 协议重构与劣质网络加速原理",
    "Shadowsocks (SS) 协议进化史：从socks5到 AEAD 加密与 SS 2022",
    "什么是原生住宅 IP (Residential IP)？对 AI 与流媒体有何影响",
    "节点倍率（1x, 2x, 0.5x）概念解析：如何计算实际扣除的流量",
    "DNS 污染与 GFW 封锁原理：Fake-IP 与 DOH 技术是如何应对的",
    "为什么晚高峰时期骨干网会拥堵？国际出口带宽分配原理解析",
    "自建 VPS 梯子与商业专线机场对比：成本、维护与抗封锁分析",
    "GFW 深度包检测 (DPI) 机制探讨：代理流量是如何被特征识别的",
    "单播、组播与多播节点架构差异：机场后端调度技术全景",
    "TCP 拥塞控制算法 (BBR vs Cubic) 对科学上网下载速率的影响",
    "网络安全与隐私保护：SSL/TLS 证书加解密全流程科普",
    "科学上网合规与网络安全知识汇总：合法出海与隐私边界"
]

for idx, t in enumerate(knowledge_titles, 1):
    fp = os.path.join(BASE_DIR, "content", "knowledge", f"knowledge-{idx}.md")
    cnt = generate_rich_article_content(t, "knowledge", "线路知识库")
    write_md(fp, t, f"【{t}】深入科普底层网络原理与架构知识。", cnt)

print("Updated 15 Knowledge articles with clean summaries.")

# 5. FAQ (30 Summary Articles + 100 Individual FAQ pages)
for idx in range(1, 31):
    fp = os.path.join(BASE_DIR, "content", "faq", f"faq-article-{idx}.md")
    t = f"魔法上网与机场选购常见疑问解答 (专题第 {idx} 期)"
    cnt = generate_rich_article_content(t, "faq", "常见疑问答疑")
    write_md(fp, t, f"【{t}】搜集并针对小白最常遇到的科学上网难题进行解答。", cnt)

# Individual 100 FAQ pages
for item in FAQS:
    fp = os.path.join(BASE_DIR, "content", "faq", f"{item['slug']}.md")
    cnt = f"""
## {item['question']}

### 📌 权威解答

{item['answer']}

---

### 💡 推荐搭配的高速稳定机场：
- **首选主力专线**：[灵动云官网注册](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J) (使用优惠码 `lingdong88` 享 8 折优惠)
- **大流量观影**：[暮光网络官网注册](https://varnexa.twilightaff.com/#/?code=X6iVG1Zb) (优惠码 `twilight2026`)
- **新手年付性价比**：[飞猫云官网注册](https://flycat1.flycatvipaff.cc/#/?code=KRjsCIZV) (年付折合每月 7 元)
- **稳健办公**：[微风网络官网注册](https://edp01.breezenetaff.com/#/?code=txKNNHZc) (月付 15 元起)

更多全站 28 家机场注册链接请参阅：[28 家全机场注册链接大全](/all-airports/)。
"""
    write_md(fp, item['question'], f"{item['question']} - 专业排查与解答。", cnt)

print("Updated 30 FAQ summary articles and 100 individual FAQ pages with clean summaries.")
