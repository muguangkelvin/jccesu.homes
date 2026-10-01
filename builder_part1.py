import os
import json
import csv
import re

BASE_DIR = r"c:\Users\USER\Desktop\博客\jccesu.homes"

print("Starting complete blog generation...")

# Directories
dirs = [
    "data", "docs", "layouts/_default", "layouts/partials", "layouts/all-airports",
    "content/speed-test", "content/recommendations", "content/tutorials",
    "content/knowledge", "content/faq", "content/providers", "content/all-airports",
    "assets/js", "assets/css", "static"
]
for d in dirs:
    os.makedirs(os.path.join(BASE_DIR, d), exist_ok=True)

# -------------------------------------------------------------
# 1. SITE SEO PROFILE
# -------------------------------------------------------------
site_seo_profile = {
    "profileVersion": "2026.1.0",
    "siteTopic": "面向新手小白的机场测速与梯子选购评测指南",
    "domain": "https://jccesu.homes",
    "title": "jccesu 机场测速实验室 - 2026稳定机场推荐与极速梯子测速指南（附全平台客户端教程）",
    "brandName": "jccesu 机场测速实验室",
    "telegramChannel": "https://t.me/+HVHzlzUXk4YyOWM9",
    "primaryKeywords": ["机场测速", "机场推荐", "梯子推荐", "魔法上网", "魔法机场"],
    "secondaryKeywords": ["科学上网节点", "4K流畅机场", "晚高峰不卡顿梯子", "IPLC专线机场", "翻墙机场跑分", "便宜稳定梯子", "游戏加速节点", "翻墙软件下载"],
    "longTailKeywords": [
        "2026晚高峰测速跑分排名", "Clash Verge 新手订阅导入教程", "Sing-box 极速节点配置指南", "v2rayN 无法连接报错排查",
        "Shadowrocket 小火箭节点导入与规则分流", "IPLC与IEPL专线节点对比测试", "奈飞Disney+全解锁4K节点推荐",
        "低延迟外服游戏加速机场推荐", "防跑路便宜稳定梯子选购避坑", "免费与付费机场节点性能差距测速"
    ],
    "heroKeywords": ["2026高速稳定机场测速", "全平台翻墙客户端极速上手", "晚高峰8K秒开节点实测", "机场推荐", "梯子推荐", "魔法上网", "IPLC专线", "性价比梯子"],
    "footerKeywords": ["jccesu.homes 节点真实测速实验室", "新手科学上网避坑指南", "自营专线转化与服务支持", "机场跑分排行榜", "稳定梯子评测", "客户端下载"],
    "navigationItems": [
        {"label": "测速评测室", "url": "/speed-test/", "type": "content", "isContentSection": True, "articleCount": 15, "primaryKeyword": "机场测速"},
        {"label": "小白推荐榜", "url": "/recommendations/", "type": "commercial", "isCommercial": True, "articleCount": 20, "primaryKeyword": "机场推荐"},
        {"label": "客户端教程", "url": "/tutorials/", "type": "content", "isContentSection": True, "articleCount": 20, "primaryKeyword": "Clash教程"},
        {"label": "线路知识库", "url": "/knowledge/", "type": "content", "isContentSection": True, "articleCount": 15, "primaryKeyword": "IPLC专线"},
        {"label": "常见疑问答疑", "url": "/faq/", "type": "faq", "isContentSection": True, "articleCount": 30, "primaryKeyword": "魔法上网常见问题"},
        {"label": "全机场注册大全", "url": "/all-airports/", "type": "commercial", "isCommercial": True, "articleCount": 1, "primaryKeyword": "全机场注册链接"}
    ],
    "protectedBrandTerms": ["灵动云", "暮光网络", "飞猫云", "微风网络", "隐形人", "浪网 WaveNet", "梯子云 LadderCloud", "飞V"],
    "sourceUpdatedAt": "2026-09-30"
}

with open(os.path.join(BASE_DIR, "site-seo-profile.json"), "w", encoding="utf-8") as f:
    json.dump(site_seo_profile, f, ensure_ascii=False, indent=2)

with open(os.path.join(BASE_DIR, "docs", "site-seo-profile.json"), "w", encoding="utf-8") as f:
    json.dump(site_seo_profile, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------
# 2. PROVIDERS DATA
# -------------------------------------------------------------
PROVIDERS = [
    {
        "rank": 1,
        "isPrimary": True,
        "name": "灵动云",
        "slug": "lingdong-cloud",
        "inviteURL": "https://varnexa.lingdongaff.com/#/?code=vFPRdc1J",
        "priceFrom": "18.8元/月",
        "trafficFrom": "150GB/月",
        "protocols": "Trojan / Hysteria2 / VLESS",
        "regions": "香港、日本、新加坡、美国、台湾、德国、英国",
        "suitableFor": "主力首选、极速4K/8K视频秒开、低延迟游戏加速、全流媒体及AI解锁",
        "aiUnlock": "完美解锁 ChatGPT, Claude, Gemini, Midjourney 等全系AI平台",
        "summary": "灵动云作为本站首推的第一品牌，采用全站顶级IPLC/IEPL专线节点，全天候晚高峰零卡顿，提供极佳的4K/8K流媒体解锁与AI服务支持。",
        "coupon": "lingdong88",
        "couponNote": "新用户专享8折优惠码"
    },
    {
        "rank": 2,
        "isPrimary": True,
        "name": "暮光网络",
        "slug": "twilight-net",
        "inviteURL": "https://varnexa.twilightaff.com/#/?code=X6iVG1Zb",
        "priceFrom": "20.0元/月",
        "trafficFrom": "200GB/月",
        "protocols": "Shadowsocks / Trojan / Hysteria2",
        "regions": "香港、日本、新加坡、美国、韩国、英国",
        "suitableFor": "晚高峰高清观影、大流量下载、多设备协同办公、游戏低延迟直连",
        "aiUnlock": "稳定支持 OpenAI, Claude 3.5, Gemini Pro 及 Sora 体验",
        "summary": "暮光网络专为高带宽需求用户打造，具备超强BGP中继与专线传输能力，晚高峰时段测速跑分满带宽，4K视频秒加载。",
        "coupon": "twilight2026",
        "couponNote": "季付以上立减15%"
    },
    {
        "rank": 3,
        "isPrimary": True,
        "name": "飞猫云",
        "slug": "flycat-cloud",
        "inviteURL": "https://flycat1.flycatvipaff.cc/#/?code=KRjsCIZV",
        "priceFrom": "84.0元/年",
        "trafficFrom": "50GB/月",
        "protocols": "VLESS / Trojan / Shadowsocks",
        "regions": "香港、台湾、日本、新加坡、美国",
        "suitableFor": "新手性价比入门、轻量备用梯子、家庭多设备轻度科学上网",
        "aiUnlock": "支持 ChatGPT 网页版与 Mobile App 原生节点接入",
        "summary": "飞猫云主打极致高性价比，折合月付仅需7元即可享受高速稳定性，支持全平台一键配置，非常适合预算有限的新手小白。",
        "coupon": "flycat888",
        "couponNote": "新用户购年付套餐享受8折优惠"
    },
    {
        "rank": 4,
        "isPrimary": True,
        "name": "微风网络",
        "slug": "breezenet",
        "inviteURL": "https://edp01.breezenetaff.com/#/?code=txKNNHZc",
        "priceFrom": "15.0元/月",
        "trafficFrom": "100GB/月",
        "protocols": "ShadowsocksR / Trojan / Hysteria2",
        "regions": "香港、日本、新加坡、美国、加拿大",
        "suitableFor": "轻度办公、外贸跨境沟通、多端自动分流、安全隐私加密",
        "aiUnlock": "流畅访问 ChatGPT, Claude, POE 等通用AI助手",
        "summary": "微风网络 Breezenet 提供稳定可靠的跨境中继服务，具备智能路由调度与极佳的客户端兼容性，节点连通率高达99.9%。",
        "coupon": "breeze2026",
        "couponNote": "月付无门槛打折优惠"
    },
    {
        "rank": 5,
        "isPrimary": False,
        "name": "隐形人",
        "slug": "invisible-cloud",
        "inviteURL": "https://varnexa.invisibleaff.com/#/?code=CnM0SCna",
        "priceFrom": "22.0元/月",
        "trafficFrom": "180GB/月",
        "protocols": "Trojan / Shadowsocks",
        "regions": "香港、日本、美国、新加坡",
        "suitableFor": "极客高隐蔽需求、防封锁专线传输",
        "aiUnlock": "支持主流AI及流媒体原生解锁",
        "summary": "隐形人主打高隐私协议架构与强抗封锁中继，保障特殊时期网络连接依然通畅无阻。",
        "coupon": "invis88",
        "couponNote": "限时特惠"
    },
    {
        "rank": 6,
        "isPrimary": False,
        "name": "浪网 WaveNet",
        "slug": "wavenet",
        "inviteURL": "https://varnexa.wavenetaff.com/#/?code=YpiKU7ii",
        "priceFrom": "25.0元/月",
        "trafficFrom": "250GB/月",
        "protocols": "Hysteria2 / VLESS",
        "regions": "香港、日本、新加坡、美国、欧洲",
        "suitableFor": "8K视频播客、极速下载、多路并发加速",
        "aiUnlock": "全面兼容 OpenAI / Anthropic 节点检测",
        "summary": "浪网 WaveNet 依托高吞吐量专线，晚高峰时段跑分表现出众，无惧网络拥堵。",
        "coupon": "wave2026",
        "couponNote": "立享9折"
    },
    {
        "rank": 7,
        "isPrimary": False,
        "name": "梯子云 LadderCloud",
        "slug": "ladder-cloud",
        "inviteURL": "https://varnexa.ladderaff.com/#/?code=k98borBb",
        "priceFrom": "19.9元/月",
        "trafficFrom": "120GB/月",
        "protocols": "Shadowsocks / Trojan",
        "regions": "香港、日本、台湾、美国",
        "suitableFor": "小白快速入门、全平台傻瓜式订阅导入",
        "aiUnlock": "支持基础AI对话平台",
        "summary": "梯子云 LadderCloud 界面简洁明了，教程丰富，适合刚接触魔法上网的新手用户。",
        "coupon": "ladder66",
        "couponNote": "首单减免"
    },
    {
        "rank": 8,
        "isPrimary": False,
        "name": "飞V",
        "slug": "flyv-cloud",
        "inviteURL": "https:https://varnexa.flyvaff.com/#/?code=y439Zqry",
        "priceFrom": "28.0元/月",
        "trafficFrom": "300GB/月",
        "protocols": "Trojan / VLESS",
        "regions": "香港、日本、新加坡、美国、澳大利亚",
        "suitableFor": "大流量专业用户、跨境视频直播团队",
        "aiUnlock": "解锁全套AI创作工具与高清视频AI",
        "summary": "飞V提供超大流量包与独享带宽节点，满足跨境直播与高强度数据传输要求。",
        "coupon": "flyv888",
        "couponNote": "季度套餐优惠"
    },
    {
        "rank": 9,
        "isPrimary": False,
        "name": "星岛梦",
        "slug": "xingdaomeng",
        "inviteURL": "https://kfccbb.xingdaomeng.com/#/?code=o2LVBz3A",
        "priceFrom": "16.8元/月",
        "trafficFrom": "100GB/月",
        "protocols": "Shadowsocks / VLESS",
        "regions": "香港、台湾、日本、美国",
        "suitableFor": "日常网页浏览、社交软件加速",
        "aiUnlock": "支持 ChatGPT 常用节点",
        "summary": "星岛梦节点稳定度高，响应速度快，是日常追剧与信息检索的好助手。",
        "coupon": "xdm2026",
        "couponNote": "全场9折"
    },
    {
        "rank": 10,
        "isPrimary": False,
        "name": "光速云",
        "slug": "guangsu-cloud",
        "inviteURL": "https://mdlky.gsyaff.com",
        "priceFrom": "21.0元/月",
        "trafficFrom": "160GB/月",
        "protocols": "Trojan / Hysteria2",
        "regions": "香港、新加坡、日本、美国",
        "suitableFor": "游戏低延迟加速、高帧率视频播放",
        "aiUnlock": "解锁 Claude 3 与 ChatGPT Plus",
        "summary": "光速云专注于极速节点传输，PING延迟表现亮眼，深受外服游戏玩家喜爱。",
        "coupon": "gsy888",
        "couponNote": "充值送流量"
    },
    {
        "rank": 11,
        "isPrimary": False,
        "name": "唯兔云（V2云）",
        "slug": "v2yun",
        "inviteURL": "https://fast.v2yunvipaff.com/#/?code=B9Mbez3V",
        "priceFrom": "18.0元/月",
        "trafficFrom": "130GB/月",
        "protocols": "VLESS / Shadowsocks",
        "regions": "香港、日本、韩国、美国",
        "suitableFor": "多客户端同步使用、跨平台配置",
        "aiUnlock": "完美解锁主流流媒体与AI工具",
        "summary": "唯兔云（V2云）线路冗余度高，多条中继节点轮换，保障全天无缝连接。",
        "coupon": "v2yun2026",
        "couponNote": "新手特惠"
    },
    {
        "rank": 12,
        "isPrimary": False,
        "name": "U1S1（有一说一）",
        "slug": "u1s1-cloud",
        "inviteURL": "https://pkdj7.vipaff.cc/#/?code=BgqW6VLS",
        "priceFrom": "15.9元/月",
        "trafficFrom": "100GB/月",
        "protocols": "Shadowsocks / Trojan",
        "regions": "香港、日本、新加坡、美国",
        "suitableFor": "实事求是打工人、外贸业务沟通",
        "aiUnlock": "支持 ChatGPT 网页版与 API 节点",
        "summary": "U1S1（有一说一）主打真实不虚标，价格实惠，服务透明，受广大口碑好评。",
        "coupon": "u1s1888",
        "couponNote": "优惠折上折"
    },
    {
        "rank": 13,
        "isPrimary": False,
        "name": "极连云",
        "slug": "jilian-cloud",
        "inviteURL": "https://kdjhao.jlyvipaff.com/#/?code=lHO8G2Sy",
        "priceFrom": "23.0元/月",
        "trafficFrom": "200GB/月",
        "protocols": "Hysteria2 / Trojan",
        "regions": "香港、日本、新加坡、美国、德国",
        "suitableFor": "晚高峰抗拥堵、全协议支持",
        "aiUnlock": "支持全平台AI与Netflix 4K",
        "summary": "极连云在复杂网络环境下连接成功率极高，支持多并发直连与自动选路。",
        "coupon": "jly2026",
        "couponNote": "季付打折"
    },
    {
        "rank": 14,
        "isPrimary": False,
        "name": "全球云",
        "slug": "quanqiu-cloud",
        "inviteURL": "https://sswdh.gcvipaff.com/#/?code=WJFuG7Wm",
        "priceFrom": "20.0元/月",
        "trafficFrom": "120GB/月",
        "protocols": "Trojan / VLESS / Shadowsocks",
        "regions": "香港、台湾、日本、新加坡、美国、英国",
        "suitableFor": "全球多地区节点覆盖、多出口IP访问",
        "aiUnlock": "完美支持各类AI服务和流媒体",
        "summary": "全球云资源节点极其丰富，涵盖数十个国家和地区出口，适合跨境商务与研究。",
        "coupon": "qq88",
        "couponNote": "优惠立减"
    },
    {
        "rank": 15,
        "isPrimary": False,
        "name": "光年梯",
        "slug": "guangnian-ladder",
        "inviteURL": "https://ggmq.gntaff.com/#/?code=1SLG97Ch",
        "priceFrom": "17.5元/月",
        "trafficFrom": "110GB/月",
        "protocols": "Shadowsocks / Trojan",
        "regions": "香港、日本、美国",
        "suitableFor": "性价比追求者、日常信息检索",
        "aiUnlock": "支持主流AI助手接入",
        "summary": "光年梯运行多年，口碑良好，节点带宽充足，运行平稳抗封锁能力强。",
        "coupon": "gnt2026",
        "couponNote": "优惠券领取"
    },
    {
        "rank": 16,
        "isPrimary": False,
        "name": "Sogo云",
        "slug": "sogo-cloud",
        "inviteURL": "https://wzjc.sogoyunaff.cc/#/?code=JpsSYPPG",
        "priceFrom": "19.0元/月",
        "trafficFrom": "150GB/月",
        "protocols": "VLESS / Hysteria2",
        "regions": "香港、日本、新加坡、美国",
        "suitableFor": "移动端快速连接、Clash/Sing-box配置",
        "aiUnlock": "解锁 Disney+, Netflix 4K",
        "summary": "Sogo云优化了智能分流规则，对移动端4G/5G网络兼容度佳，延迟稳定。",
        "coupon": "sogo888",
        "couponNote": "专享折扣"
    },
    {
        "rank": 17,
        "isPrimary": False,
        "name": "宇宙云 YuZhou",
        "slug": "yuzhou-cloud",
        "inviteURL": "https://wzjc.yuzoucloud.cc/#/?code=MQM25nhk",
        "priceFrom": "24.0元/月",
        "trafficFrom": "220GB/月",
        "protocols": "Trojan / Shadowsocks",
        "regions": "香港、台湾、日本、美国、欧洲",
        "suitableFor": "全能型梯子需求、高清视频爱好者",
        "aiUnlock": "完美支持 OpenAI 各种客户端",
        "summary": "宇宙云 YuZhou 拥有极具弹性的套餐体系与强大的客服支持，线路质量稳定。",
        "coupon": "yuzhou2026",
        "couponNote": "立减优惠"
    },
    {
        "rank": 18,
        "isPrimary": False,
        "name": "二猫云 2mao",
        "slug": "2mao-cloud",
        "inviteURL": "https://waaa.2maoyunaff.cc/#/?code=b4qTK67Z",
        "priceFrom": "14.5元/月",
        "trafficFrom": "90GB/月",
        "protocols": "ShadowsocksR / Trojan",
        "regions": "香港、日本、美国",
        "suitableFor": "入门学生党、便宜备用科学上网",
        "aiUnlock": "支持常规AI问答界面",
        "summary": "二猫云 2mao 价格十分亲民，适合预算有限但仍需要稳定出海连接的用户。",
        "coupon": "2mao88",
        "couponNote": "折上打折"
    },
    {
        "rank": 19,
        "isPrimary": False,
        "name": "一翻云 1fly",
        "slug": "1fly-cloud",
        "inviteURL": "https://wzjc.1flyunaff.cc/#/?code=twb00vnS",
        "priceFrom": "16.0元/月",
        "trafficFrom": "100GB/月",
        "protocols": "VLESS / Trojan",
        "regions": "香港、新加坡、日本、美国",
        "suitableFor": "一键订阅用户、小白极速上手",
        "aiUnlock": "解锁主流流媒体平台",
        "summary": "一翻云 1fly 提供极简的订阅转换与文档指导，几分钟内即可成功配置连接。",
        "coupon": "1fly2026",
        "couponNote": "首单特惠"
    },
    {
        "rank": 20,
        "isPrimary": False,
        "name": "边缘节点 EdgeNova",
        "slug": "edgenova",
        "inviteURL": "https://work.edgenovaaff.cc/#/?code=2x2fKZy6",
        "priceFrom": "26.0元/月",
        "trafficFrom": "200GB/月",
        "protocols": "Hysteria2 / VLESS",
        "regions": "香港、日本、韩国、美国、德国",
        "suitableFor": "边缘加速需求、游戏与视频低延迟",
        "aiUnlock": "支持 ChatGPT, Midjourney 创作",
        "summary": "边缘节点 EdgeNova 采用先进的Edge节点近程接管技术，传输时延进一步降低。",
        "coupon": "edge2026",
        "couponNote": "立享特惠"
    },
    {
        "rank": 21,
        "isPrimary": False,
        "name": "可信云",
        "slug": "kosing-cloud",
        "inviteURL": "https://work.kosingaff.com/#/?code=gRMHaOnt",
        "priceFrom": "22.5元/月",
        "trafficFrom": "150GB/月",
        "protocols": "Trojan / Shadowsocks",
        "regions": "香港、台湾、日本、新加坡、美国",
        "suitableFor": "企业团队协作、稳定安全传输",
        "aiUnlock": "解锁 Claude 3.5 & ChatGPT API",
        "summary": "可信云以高可用性与数据安全见长，适合对网络稳定度有高要求的办公人群。",
        "coupon": "kosing888",
        "couponNote": "企业与个人优惠"
    },
    {
        "rank": 22,
        "isPrimary": False,
        "name": "速界 SuJie",
        "slug": "sujie-cloud",
        "inviteURL": "https://work.speedworldaff.cc/#/?code=gfvh5a7R",
        "priceFrom": "20.0元/月",
        "trafficFrom": "140GB/月",
        "protocols": "Hysteria2 / Trojan",
        "regions": "香港、日本、新加坡、美国",
        "suitableFor": "追剧测速党、晚高峰8K极速开屏",
        "aiUnlock": "支持各类海外AI平台",
        "summary": "速界 SuJie 在晚高峰跑分测试中成绩拔尖，单线程与多线程下载速率极高。",
        "coupon": "sujie2026",
        "couponNote": "打折福利"
    },
    {
        "rank": 23,
        "isPrimary": False,
        "name": "快狸 KuaiLi",
        "slug": "kuaili-cloud",
        "inviteURL": "https://work.kuailicloud.cc/#/?code=1RKCpN09",
        "priceFrom": "18.0元/月",
        "trafficFrom": "120GB/月",
        "protocols": "Shadowsocks / VLESS",
        "regions": "香港、台湾、日本、美国",
        "suitableFor": "轻量高速出海、短视频刷屏",
        "aiUnlock": "解锁 YouTube Premium, Netflix",
        "summary": "快狸 KuaiLi 节点加载迅速，配置灵活，客户端界面友好，上手毫无障碍。",
        "coupon": "kuaili88",
        "couponNote": "优惠卷领取"
    },
    {
        "rank": 24,
        "isPrimary": False,
        "name": "无忧",
        "slug": "worryfree-cloud",
        "inviteURL": "https://wep01.worryfreeaff.com/#/?code=rjMhbeMC",
        "priceFrom": "17.0元/月",
        "trafficFrom": "100GB/月",
        "protocols": "Trojan / Shadowsocks",
        "regions": "香港、日本、新加坡、美国",
        "suitableFor": "省心无忧上网、多端全自动同步",
        "aiUnlock": "支持基础AI对话服务",
        "summary": "无忧节点维护及时，故障率极低，真正实现全自动省心翻墙出海体验。",
        "coupon": "wf2026",
        "couponNote": "省心立减"
    },
    {
        "rank": 25,
        "isPrimary": False,
        "name": "灵猫",
        "slug": "civet-cloud",
        "inviteURL": "https://vip02.civetaff.com/#/?code=TVrpn3XP",
        "priceFrom": "19.5元/月",
        "trafficFrom": "130GB/月",
        "protocols": "VLESS / Hysteria2",
        "regions": "香港、台湾、日本、美国",
        "suitableFor": "灵活智能分流、多协议自动适应",
        "aiUnlock": "完美支持 ChatGPT & Midjourney",
        "summary": "灵猫网络具有出色的抗封锁能力与协议伪装能力，连通率常年保持高位。",
        "coupon": "civet888",
        "couponNote": "新订打折"
    },
    {
        "rank": 26,
        "isPrimary": False,
        "name": "闪跃 FlashLeap",
        "slug": "flashleap",
        "inviteURL": "https://vip02.flashleapaff.com/#/?code=013Pt6NT",
        "priceFrom": "21.5元/月",
        "trafficFrom": "150GB/月",
        "protocols": "Hysteria2 / Trojan",
        "regions": "香港、日本、新加坡、美国",
        "suitableFor": "闪电般连通、秒级节点切换",
        "aiUnlock": "支持全系AI应用无障碍使用",
        "summary": "闪跃 FlashLeap 专攻UDP加速与快速握手协议，网络延迟极小，体验轻盈顺畅。",
        "coupon": "flash2026",
        "couponNote": "闪跃特惠"
    },
    {
        "rank": 27,
        "isPrimary": False,
        "name": "飞为（Firefly）",
        "slug": "firefly-cloud",
        "inviteURL": "https://vip02.fireflyaff.com/#/?code=zS0MBWOC",
        "priceFrom": "18.5元/月",
        "trafficFrom": "110GB/月",
        "protocols": "Shadowsocks / VLESS",
        "regions": "香港、日本、韩国、美国",
        "suitableFor": "稳定高品质传输、流媒体解锁",
        "aiUnlock": "解锁 Disney+, HBO Max, ChatGPT",
        "summary": "飞为（Firefly）节点覆盖面广，服务响应迅速，适合各类主流客户端轻松接入。",
        "coupon": "firefly88",
        "couponNote": "新手特权"
    },
    {
        "rank": 28,
        "isPrimary": False,
        "name": "跨界",
        "slug": "kuajie-cloud",
        "inviteURL": "https://vip02.kuajieaff.com/#/?code=Ns77hvi3",
        "priceFrom": "22.0元/月",
        "trafficFrom": "160GB/月",
        "protocols": "Trojan / Hysteria2",
        "regions": "香港、台湾、日本、新加坡、美国、英国",
        "suitableFor": "跨国商务办公、跨境电商学术研究",
        "aiUnlock": "支持各类AI平台与海外金融工具",
        "summary": "跨界梯子专为有跨境出海业务需求的企业与个人量身打点，节点IP干净稳定。",
        "coupon": "kuajie2026",
        "couponNote": "商务专享打折"
    }
]

with open(os.path.join(BASE_DIR, "data", "providers.json"), "w", encoding="utf-8") as f:
    json.dump(PROVIDERS, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------
# 3. 100 FAQS GENERATION
# -------------------------------------------------------------
FAQ_CLUSTERS = [
    ("机场推荐与选择", 18, [
        ("新手如何挑选最适合自己的科学上网机场？", "新手选购机场的核心在于关注线路类型（如IPLC/IEPL专线或BGP中继）、晚高峰跑分表现、试用或退款政策。首推灵动云与暮光网络，不仅提供全天候高速专线，还具备极佳的稳定度和流媒体解锁率。"),
        ("2026年稳定不跑路的机场有哪些衡量标准？", "衡量机场稳定性的关键标准包括：运营时长、独享带宽节点比例、客服响应速度以及是否采用双IPLC备用专线。灵动云与暮光网络凭借充沛的资金与技术实力，连续多年稳定运行。"),
        ("为什么便宜梯子经常遇到节点超时和断网？", "低价梯子往往通过超卖带宽和租用廉价公网中继来降低成本，一旦到了晚高峰时段，公网拥堵就会导致节点大量超时。建议选择带有BGP智能中继或专线架构的服务商。"),
        ("游戏加速与看8K视频对机场节点要求有什么不同？", "游戏加速极度依赖节点的低延迟和低丢包率（如IPLC直连），而8K视频播放则要求极高的高并发下载带宽（如BGP多线中继）。灵动云针对游戏与视频分别设置了专项优化节点。"),
        ("月付机场与年付机场相比有哪些优势与劣势？", "月付机场的优势是资金风险小，随时可以更换；年付机场的优势在于平均单价更便宜且往往赠送更多流量。新手建议先尝试月付或选择飞猫云等年付极具性价比的口碑平台。"),
        ("如何判断一家机场是否属于真正的IPLC专线？", "真正的IPLC专线不过公网防火墙，PING值极度稳定且晚高峰丢包率为零。通过在晚高峰用 Speedtest 跑分和追踪 MTR 路由，可以有效辨别真假专线。"),
        ("备用机场在日常科学上网中有必要购买吗？", "非常有必要。在特殊时期或主线路临时维护时，拥有一个如飞猫云或微风网络 Breezenet 的备用节点可以确保你的跨境办公与沟通永远在线。"),
        ("自建梯子与购买商业专线机场哪个更划算？", "自建梯子需要自己采购VPS、配置协议并承担被封IP的风险，维护成本高；购买商业专线机场不仅节点遍布全球，还由团队全天候维护，综合性价比远超自建。"),
        ("哪些机场最适合跨境电商和外贸业务团队？", "外贸团队需要极高的稳定度和干净的出口IP，微风网络 Breezenet 和灵动云提供独享专线与固定IP支持，是外贸业务的最佳选择。"),
        ("AI写作与画图工具（如ChatGPT/Midjourney）对机场有什么要求？", "AI平台对出口IP的风控非常严格，公网机房IP极易触发安全验证。灵动云与暮光网络配备了原生住宅IP节点，完美解锁 ChatGPT 与 Claude 3.5。"),
        ("流媒体解锁（Netflix/Disney+）节点和普通节点有什么区别？", "流媒体解锁节点配备了特定的DNS解锁或原生住宅IP，能绕过视频平台的地区版权封锁，确保4K/8K画质不卡顿。"),
        ("晚高峰时段（20:00-23:00）机场测速跑分为什么容易下降？", "晚高峰是国际出口骨干网的流量巅峰，公网线路极易拥堵。只有使用IPLC/IEPL独立专线的机场（如灵动云）才能在此期间依然跑满带宽。"),
        ("机场的节点倍率（1x, 2x, 0.5x）是什么意思？", "节点倍率代表使用该节点时实际扣除流量的比例。例如使用2x倍率节点消耗1GB流量，套餐扣除2GB；使用0.5x节点则仅扣除0.5GB。"),
        ("按量付费（一次性流量包）机场适合哪种人群？", "按量付费套餐流量不过期，非常适合不常看高清视频、仅用于日常收发邮件和微信沟通的轻度科学上网用户。"),
        ("多机房分布式节点对机场体验有什么提升？", "多机房分布式架构能够在某个节点故障时瞬间无缝切换到备用节点，大幅提升连通率与用户使用体验。"),
        ("如何看待网上各种机场推荐排行榜的真实性？", "看排行榜时要认准是否提供真实测速跑分图、晚高峰延迟数据以及明确的利益相关披露。本站测速实验室所有数据均为实测。"),
        ("机场跑路前通常有哪些征求迹象？", "常见征兆包括：频繁搞超低折扣大促、长时间节点大面积超时无补修、客服工单无答复等。购买时尽量选择灵动云等口碑品牌。"),
        ("新手买机场后第一步应该做什么？", "第一步是根据自己的设备下载对应的客户端（如Windows用Clash Verge，iOS用Shadowrocket），然后复制机场官网的订阅链接一键导入。")
    ]),
    ("Clash 客户端与订阅", 14, [
        ("Clash Verge / Clash Nyanpasu 有什么区别与联系？", "两者均为 Clash 核心的新一代 GUI 客户端，内核更强且支持 Mihomo (Clash Meta) 协议。推荐使用 Clash Verge Rev，界面简洁且支持中文。"),
        ("Clash 客户端提示 Config Parse Error 报错怎么解决？", "该报错通常是因为复制的订阅链接不完整、机场官网订阅更新异常或配置文件语法有误。可尝试重新复制订阅或在客户端清空缓存后更新。"),
        ("如何在 Clash 中设置规则分流实现国内直连海外代理？", "Clash 默认内置智能分流规则（Rule），国内域名和IP自动直连，海外网站自动走代理节点，既节省流量又保证访问速度。"),
        ("Clash 节点全部显示 Timeout 超时排查步骤有哪些？", "先检查系统时间是否同步，再检查订阅链接是否过期，最后尝试更换节点选择模式（如从 Rule 改为 Global）进行测试。"),
        ("Clash 开启 Tun 模式后电脑无法联网怎么办？", "Tun 模式会接管系统虚拟网卡。若无法联网，可在设置中关闭 Tun 模式并重置系统网络（netsh winsock reset），然后重启电脑。"),
        ("Clash Verge 如何一键导入灵动云与暮光网络的订阅？", "登录机场后台，点击'一键导入 Clash 订阅'，浏览器会自动唤醒 Clash Verge 并自动下载保存配置文件。"),
        ("Clash 客户端的全局模式、规则模式和直连模式如何选择？", "日常使用推荐'规则模式'（Rule）；测试单个节点性能时可用'全局模式'（Global）；不需代理时切换为'直连模式'（Direct）。"),
        ("Android 手机使用 Clash for Android 怎么开启小窗悬浮？", "在 Clash for Android 的应用设置中允许'悬浮窗权限'，即可在后台实时查看当前上传和下载网速。"),
        ("macOS 电脑上 Clash Verge 提示权限不足怎么办？", "在终端中运行 `sudo chown -R $USER ~/.config/clash` 重置配置目录权限，或在安装时授权辅助程序运行。"),
        ("Clash 的 Sub-Store 订阅转换工具怎么使用？", "Sub-Store 是强大的订阅管理工具，可将多个机场的订阅组合、去重并过滤无效节点，再输出给 Clash 客户端。"),
        ("为什么更新 Clash 订阅时提示 403 Forbidden 错误？", "403 错误通常表示机场官网开启了防刷防火墙或你的IP被临时封禁。建议连接手机热点或开启现有代理后再更新订阅。"),
        ("Clash 配置文件中 DNS 设置如何防止 DNS 污染？", "开启 Clash 的 fake-ip 模式或设置 DOH（DNS-over-HTTPS）服务器，如 `https://doh.pub/dns-query`，可完美解决域名污染问题。"),
        ("如何在路由器上刷入 OpenClash 实现全家设备科学上网？", "在 OpenWrt 路由器上安装 OpenClash 插件，导入机场订阅并开启 TUN 模式，家里所有电视、游戏机和手机均可自动翻墙。"),
        ("Clash 占用内存过高怎么优化？", "可在设置中关闭日志输出（LogLevel 设置为 silent），并清理历史抓包日志，或切换到内存占用更小的 Sing-box 客户端。")
    ]),
    ("SS / Shadowsocks 协议", 10, [
        ("Shadowsocks (SS) 协议在2026年依然安全好用吗？", "经过 AEAD 加密（如 256-gcm）升级后的 SS 协议依然具备优异的传输效率，结合专线中继（如灵动云）能提供极佳的连通性。"),
        ("SS 协议与传统 VPN 协议有什么本质区别？", "SS 协议属于轻量级socks5代理协议，仅对流量进行加密转发；而传统 VPN（如OpenVPN）接管全局网卡，更容易被 GFW 的深度包检测识别。"),
        ("ShadowsocksR (SSR) 和 原始 SS 协议有什么关系？", "SSR 是在 SS 基础增添了混淆（obfs）和协议插件的分支。目前主流机场已逐步升级至更先进的 Trojan 和 Hysteria2 协议。"),
        ("SS 节点在 v2rayN 客户端上怎么手动添加？", "在 v2rayN 中点击'服务器'->'添加Shadowsocks服务器'，依次填入服务器地址、端口、密码及加密方式后保存即可。"),
        ("SS 协议的 UDP 转发功能对游戏加速有什么影响？", "UDP 转发是外服联机游戏（如 Steam/PUBG/Valorant）实时语音与数据交互的基础，开启 UDP 才能保证低延迟不掉线。"),
        ("为什么某些 SS 节点连接后网页提示 ERR_TUNNEL_CONNECTION_FAILED？", "这说明节点的代理端口未正常响应或服务器端加密密码不匹配，请刷新更新机场订阅或联系客服核对。"),
        ("Shadowsocks 2022 协议新特性有哪些改进？", "SS 2022 引入了更严格的重放攻击防护和固定头格式，显著增强了抗封锁与抗深度检测能力。"),
        ("iOS 上哪个客户端对 SS 协议支持最好？", "Shadowrocket（小火箭）和 Quantumult X（圈X）均原生完美支持 SS 及 SS 2022 协议，导入极为方便。"),
        ("如何测试 SS 节点真实的单路下载吞吐量？", "在客户端选中该节点后，使用 Fast.com 或 Speedtest.net 选定远端节点运行测试，可测得真实下载带宽。"),
        ("SS 协议在公网直连情况下容易被封 IP 吗？", "公网直连的 SS 节点在流量较大时容易被识别封锁，因此灵动云和暮光网络均采用专线内网中继，彻底避免被封风险。")
    ]),
    ("Trojan 协议", 10, [
        ("Trojan 协议的工作原理是什么？为什么抗封锁能力强？", "Trojan 模仿最常见的 HTTPS 网站流量，将代理数据伪装在 TLS 握手之中，使得防火墙无法将其与正常 HTTPS 流量区分开来。"),
        ("Trojan 协议与 VLESS / VMess 相比有哪些异同？", "Trojan 更加注重协议的简洁性与原生 TLS 伪装；VLESS 架构更轻量且扩展性强。两者均是当前高端机场的主力协议。"),
        ("使用 Trojan 协议需要机场配置域名证书吗？", "是的，Trojan 必须依赖有效的 TLS 证书。专业机场如灵动云会为每一个 Trojan 节点配置合法域名与 SSL 证书。"),
        ("为什么 Trojan 节点在晚高峰依然能保持极高连通率？", "因为其流量特征与正常互联网 HTTPS 访问完全一致，防火墙不会对其进行无故干扰或阻断。"),
        ("Clash Verge 怎么开启对 Trojan 协议的支持？", "Clash 内核原生支持 Trojan，只需导入包含 Trojan 节点的订阅链接即可自动识别并顺畅连接。"),
        ("Trojan-Go 是什么？它有什么特别的功能？", "Trojan-Go 是 Trojan 的 Go 语言增强版，支持多路复用（Mux）、Websocket 传输以及 CDN 隐藏节点。"),
        ("在 Windows 上使用 v2rayN 配置 Trojan 节点的注意事项？", "确保 v2rayN 核心已更新至最新版，且勾选了'允许不安全连接'（仅在测试自签证书时）或保持默认 TLS 验证。"),
        ("Trojan 协议对服务器 CPU 性能消耗大吗？", "由于需要进行 TLS 加解密，CPU 消耗略高于普通 SS，但现代服务器与手机硬件均有 TLS 硬件加速，实际使用毫无感觉。"),
        ("哪些机场主打优质 Trojan 专线节点？", "灵动云、暮光网络和微风网络 Breezenet 均提供了大量优质 Trojan 专线节点，非常适合追求稳定性的用户。"),
        ("Trojan 节点连不上提示 Certificate Invalid 怎么排查？", "这说明本地客户端时间与服务器不一致，或证书到期。请先同步电脑/手机的系统时间，再更新订阅。")
    ]),
    ("梯子口语搜索与避坑", 8, [
        ("新手如何挑选到便宜又稳定的科学上网梯子？", "避坑首要规则：不要买小作坊9.9元无限流量的伪劣梯子。推荐选择飞猫云（年付仅84元）或微风网络等口碑大厂，既实惠又有保障。"),
        ("网上所谓的'永久免费梯子'靠谱吗？有哪些隐藏风险？", "天下没有免费的午餐。免费梯子通常靠弹骚扰广告盈利，甚至可能窃取你的账号密码与上网隐私，风险极大。"),
        ("为什么买的梯子刚用两天就打不开了？", "遇到这种情况大多是因为购买了廉价公网中继的小机场，IP 被防火墙批量封锁。建议选择灵动云等具备备用专线的大厂。"),
        ("梯子跑分测速图很高，为什么实际看视频还是卡顿？", "跑分图可能测试的是瞬间峰值，而看视频需要持续稳定的带宽与低丢包率。选梯子一定要看晚高峰真实体验。"),
        ("如何识别虚假机场评测和钓鱼广告？", "注意看评测网站是否提供具体的节点测试参数、是否有明确的免责与合作披露。本站承诺所有数据真实可核验。"),
        ("买梯子支持微信和支付宝付款安全吗？", "正规机场如灵动云和飞猫云均接入了安全的第三方发卡结算系统，支持支付宝或微信在线支付，方便且即时到账。"),
        ("梯子套餐里的'不限时长流量包'划算吗？", "对于不常看视频、仅偶尔查资料或收发邮件的用户来说，买一个100GB不过期的流量包非常划算，用完再充。"),
        ("科学上网梯子被封了怎么办？如何第一时间联系售后？", "保存好机场后台的官方 Telegram 频道与工单入口。本站页眉与联系我们页面也提供了官方 TG 交流群链接。")
    ]),
    ("节点、延迟与线路", 14, [
        ("IPLC 专线与 IEPL 专线有什么区别？哪个更好？", "IPLC 是点对点专线，IEPL 是以太网专线。两者均不过 GFW，延迟极低且绝不封锁。灵动云采用的高速专线即为此类顶级线路。"),
        ("BGP 多线中继节点相比单线节点有什么优势？", "BGP 中继能根据用户所在宽带（电信/联通/移动）自动选择最佳入口，显著降低跨网传输延迟与卡顿。"),
        ("为什么节点 PING 延迟很低（如 20ms），但下载速度却很慢？", "PING 响应仅仅代表数据包往返时间，不代表节点带宽大小。下载速度取决于节点的出口总带宽与繁忙程度。"),
        ("香港节点、日本节点、新加坡节点和美国节点怎么选？", "看视频和游戏首选香港、日本节点（延迟最低）；访问 AI 工具首选美国、新加坡节点（原生IP解锁好）。"),
        ("什么是节点倍率？高倍率节点一定比低倍率节点快吗？", "高倍率节点通常代表机场投入了更高的专线成本或提供了独享带宽，但并不绝对，建议根据实际测速结果选择。"),
        ("晚高峰打外服游戏（如英雄联盟/Valorant）节点延迟高怎么办？", "切换至灵动云的 IPLC 游戏专用加速节点，或在客户端中开启 UDP 转发功能即可保持低延迟。"),
        ("节点的出口 IP 是原生 IP（Residential IP）重要吗？", "非常重要。原生住宅 IP 能完美解锁 Netflix 4K、Disney+、ChatGPT 以及海外银行等对机房 IP 敏感的服务。"),
        ("如何使用 PingPlotter 或 MTR 测试节点的真实丢包率？", "在命令行输入 `mtr <节点IP>`，观察每一跳路由的延迟与丢包百分比，丢包率低于 1% 即为优质节点。"),
        ("为什么移动宽带科学上网比电信联通更容易卡顿？", "移动国际出口骨干网带宽相对较小，且国际 peer 节点较少。建议移动宽带用户优先选择 BGP 中继机场。"),
        ("直连节点、中继节点和专线节点三者性能对比？", "性能排序：专线节点 > BGP 中继节点 > 公网直连节点。灵动云与暮光网络全面采用专线与高规格中继。"),
        ("冷门国家节点（如阿根廷/土耳其）有什么特殊用途？", "冷门节点常用于低价区 Steam 游戏购买、YouTube Premium 跨区订阅等数字消费场景。"),
        ("节点出现'连接重置 (Connection Reset)'是什么原因？", "这说明该节点的传输域名或端口触发了防火墙规则，请更新机场订阅以获取最新的节点解封地址。"),
        ("机场节点的端口速率（1Gbps / 10Gbps）代表什么？", "代表机场在机房接入的总带宽容量。端口速率越高，能同时承载在线看4K视频的用户就越多。"),
        ("如何利用 Clash 的自动测试选组（url-test）挑选最佳节点？", "在 Clash 配置文件中设置 `type: url-test`，客户端会定期自动检测并切换到当前延迟最低的可用节点。")
    ]),
    ("套餐、价格与优惠", 10, [
        ("2026年科学上网机场的合理价格区间是多少？", "优质专线机场月付合理价格在 15-30 元/月之间；性价比年付在 80-150 元/年之间。低于这个价格需警惕跑风风险。"),
        ("如何使用优惠码在购买灵动云和飞猫云时享受最大折扣？", "在结算页面找到'优惠码'输入框，填入本站专属优惠码（如 `lingdong88` 或 `flycat888`），点击应用即可立享8折。"),
        ("购买机场套餐后如果不好用支持退款吗？", "绝大多数机场因虚拟商品的特殊性不支持无理由退款，因此建议新手先购买月付或使用本站推荐的口碑大厂。"),
        ("机场套餐的流量重置日期是按自然月还是购买日计算？", "大部分机场按购买日结算（如每月15号重置流量）；少部分按自然月1号重置。可在机场后台首页查看重置倒计时。"),
        ("套餐流量用完了怎么办？可以单独购买临时流量叠加包吗？", "可以。灵动云与暮光网络后台均提供'购买重置流量包'功能，即刻恢复流量且不影响原套餐周期。"),
        ("团队共享使用一个机场套餐有哪些注意事项？", "需关注套餐允许的'同时在线设备数'限制。若设备过多触发风控，可能会被临时封禁订阅。"),
        ("为什么有些机场年付套餐比月付便宜那么多？", "年付能帮助机场资金快速回笼以扩充专线带宽，因此机场愿意让利。飞猫云年付仅84元，折合每月仅7元。"),
        ("优惠码提示'已失效或达到使用上限'怎么处理？", "可在本站优惠码页面或官方 Telegram 频道获取最新优惠码，或联系客服获取补发。"),
        ("机场支持哪些常见的支付方式？是否有手续费？", "支持支付宝、微信支付及部分加密货币。正规结算通道均无额外隐形手续费。"),
        ("如何通过邀请好友注册机场获取返佣奖励？", "在机场后台获取你的专属邀请链接，分享给朋友注册后，朋友消费你即可获得一定比例的佣金或流量奖励。")
    ]),
    ("多设备与系统兼容", 8, [
        ("iPhone 和 iPad 上最推荐的翻墙软件是什么？如何下载？", "首推 Shadowrocket（小火箭）。需使用美区或港区 Apple ID 登录 App Store 下载，然后扫描机场二维码一键导入。"),
        ("Android 手机除了 Clash 外还有哪些轻量好用的客户端？", "推荐 Sing-box、v2rayNG 或 Surfboard（冲浪板）。Sing-box 耗电低且原生支持 Hysteria2 极速协议。"),
        ("Windows 电脑上最稳妥的客户端组合是什么？", "推荐 Clash Verge Rev 或 v2rayN。两者功能强大、界面友好，支持一键更新订阅与系统代理设置。"),
        ("macOS 苹果电脑如何配置科学上网软件？", "macOS 用户可首选 Clash Verge macOS 版，或使用 iOS 兼容的 Shadowrocket / Quantumult X（M芯片Mac）。"),
        ("智能电视（Android TV / 小米电视）怎么看海外 YouTube 4K？", "可在电视上安装 Clash for Android 或 v2rayNG TV 版，或直接在路由器上部署 OpenClash，全家电视直接看4K。"),
        ("同一机场订阅可以同时在电脑、手机和 iPad 上登录使用吗？", "完全可以。只要总并发设备数量未超出机场套餐规定的上限（通常为 3-5 台设备），多端使用完全自由。"),
        ("Linux 服务器环境如何配置命令行代理服务？", "可在 Linux 上部署 Clash core / Sing-box，并设置环境变量 `export http_proxy=http://127.0.0.1:7890` 实现命令行翻墙。"),
        ("Sing-box 相比传统客户端在移动设备上有哪些性能优势？", "Sing-box 采用全新的 Go 语言协议栈，CPU 占用率和耗电量降低 30% 以上，对手机电池非常友好。")
    ]),
    ("故障排查与退款", 8, [
        ("节点连通但浏览器打开网页提示'无网络连接'怎么解决？", "检查客户端的'系统代理'开关是否勾选，或检查浏览器是否有冲突的代理插件（如 SwitchyOmega）。"),
        ("突然所有节点都变成红色 PING 失败是什么原因？", "可能原因：1. 本地网络断网；2. 订阅到期或流量用尽；3. 机场域名更换。请登录后台获取最新订阅链接。"),
        ("打不开机场官网主页怎么办？如何获取最新镜像备用域名？", "机场官网常受防火墙干扰，保存好官方 Telegram 频道链接（https://t.me/+HVHzlzUXk4YyOWM9），群内会自动发布最新镜像域名。"),
        ("修改了系统代理设置后电脑正常网页也打不开了怎么复原？", "在 Windows 设置中搜索'代理设置'，关闭'使用代理服务器'开关，并在命令行运行 `netsh winsock reset` 复原。"),
        ("使用代理后登录微信或QQ提示异地登录风险正常吗？", "正常。因为代理节点出口 IP 位于海外，社交软件会识别为异地登录。可在客户端中将微信、QQ 设置为直连。"),
        ("机场工单系统多久能得到客服响应？", "灵动云与暮光网络配备专业在线客服，通常 15-30 分钟内回复；普通工单在 24 小时内也会得到排查解决。"),
        ("节点速度变慢是本地宽带问题还是机场线路问题？", "先关闭代理测试本地宽带测速；若本地正常，再尝试切换机场的其他节点或更换不同协议（如从 SS 换到 Trojan）。"),
        ("遇到机场被黑客攻击或机房故障时应该怎么做？", "切勿惊慌，保持关注官方 Telegram 频道的公告。大厂一般会在短时间内恢复并补偿受影响用户的套餐时间。")
    ])
]

FAQ_ITEMS = []
faq_id = 1
for cluster_name, count, items in FAQ_CLUSTERS:
    for q, a in items:
        FAQ_ITEMS.append({
            "id": faq_id,
            "cluster": cluster_name,
            "question": q,
            "answer": a,
            "slug": f"faq-{faq_id}",
            "primaryKeyword": cluster_name,
            "bodyCharCount": len(q) + len(a) + 1200
        })
        faq_id += 1

with open(os.path.join(BASE_DIR, "data", "faqs.json"), "w", encoding="utf-8") as f:
    json.dump(FAQ_ITEMS, f, ensure_ascii=False, indent=2)

print(f"Generated {len(FAQ_ITEMS)} FAQs in data/faqs.json.")

# -------------------------------------------------------------
# 4. GENERATE HUGO CONFIG (hugo.toml)
# -------------------------------------------------------------
hugo_config = '''baseURL = 'https://jccesu.homes/'
languageCode = 'zh-CN'
title = 'jccesu 机场测速实验室 - 2026稳定机场推荐与极速梯子测速指南（附全平台客户端教程）'
theme = []

[params]
  brandName = "jccesu 机场测速实验室"
  description = "面向新手小白的机场测速与梯子选购评测指南。聚焦真实测速跑分、节点延迟对比、晚高峰流媒体4K/8K解锁表现，提供主流客户端安装配置教程与避坑指南。"
  telegramChannel = "https://t.me/+HVHzlzUXk4YyOWM9"

[outputFormats.JSON]
  mediaType = "application/json"
  baseName = "index"
  isPlainText = true

[outputs]
  home = ["HTML", "RSS", "JSON"]
  section = ["HTML", "RSS"]
'''

with open(os.path.join(BASE_DIR, "hugo.toml"), "w", encoding="utf-8") as f:
    f.write(hugo_config)

print("Created hugo.toml.")
