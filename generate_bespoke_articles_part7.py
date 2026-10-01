import os
import json
from generate_bespoke_articles import BASE_DIR, write_md, build_bespoke_article

print("Generating 20 bespoke Tutorial articles & 15 Knowledge articles with 1500-2000 word depth...")

# 1. TUTORIALS (20 Bespoke Articles)
tuts_data = [
    ("tutorial-1.md", "Clash Verge Rev 新手小白零基础教程：从订阅导入到系统代理配置", "Clash Verge 教程", "Clash Verge Rev 是新一代开源 GUI 客户端，支持一键导入、规则分流与 Meta 内核。", "在客户端填入灵动云或暮光网络的订阅链接，一键更新即可加载节点。", "开启系统代理开关，并将模式设置为规则模式（Rule）。", "首选灵动云与暮光网络配合 Clash Verge。"),
    ("tutorial-2.md", "Sing-box 全平台配置指南：支持 Hysteria2 协议极速科学上网", "Sing-box 配置", "Sing-box 采用全新架构，性能强劲，内存占用低，完美支持 Hysteria2 协议。", "导入支持 Sing-box 订阅的机场链接，开启 TUN 网卡接管全站流量。", "在设置中放行本地局域网连接，允许其他设备共享代理。", "搭配支持 Hysteria2 的灵动云或暮光网络使用。"),
    ("tutorial-3.md", "iOS Shadowrocket (小火箭) 节点导入教程：扫码配置与策略组切换", "iOS 小火箭导入", "Shadowrocket 是 iOS 上最受欢迎的代理客户端，支持一键扫码与规则切替。", "登录灵动云后台，使用小火箭扫描专属订阅二维码快速导入。", "勾选所需节点，开启首页开关即可完成全局代理。", "搭配灵动云或飞猫云使用小火箭体验极佳。"),
    ("tutorial-4.md", "v2rayN 最新版使用教程：手动添加节点与一键更新订阅步骤", "v2rayN 教程", "v2rayN 是 Windows 经典客户端，支持 VLESS、Trojan、Shadowsocks 多协议。", "复制订阅链接至 v2rayN 订阅设置中，按 Ctrl+O 一键更新。", "自动选择延迟最低节点，勾选自动清除日志优化性能。", "推荐搭配微风网络与灵动云。"),
    ("tutorial-5.md", "Android 手机 Clash for Android 配置教程：开启悬浮窗与 Tun 模式", "Android Clash 教程", "Clash for Android 在安卓端功能强大，支持悬浮窗实时查看网速。", "导入订阅文件，开启 TUN 虚拟网卡模式接管系统流量。", "在应用分流中排除微信、支付宝等国内应用。", "推荐搭配飞猫云与灵动云。"),
    ("tutorial-6.md", "macOS 苹果电脑科学上网教程：Clash Verge macOS 版安装与授权", "macOS 科学上网", "macOS 用户推荐使用 Clash Verge macOS 版，支持 Intel 与 M 系列芯片。", "下载 dmg 安装包拖入 Applications，在系统偏好设置中授权辅助程序。", "导入订阅并开启系统代理或 TUN 模式。", "macOS 用户首选灵动云。"),
    ("tutorial-7.md", "OpenWrt 路由器安装 OpenClash 教程：实现全家设备自动翻墙", "OpenClash 路由器教程", "OpenClash 能在路由器层面接管流量，实现全家电视、手机、游戏机无感出海。", "在 OpenWrt 部署 OpenClash 插件，导入订阅后启用 TUN 模式。", "配置 fake-ip 解决本地 DNS 污染问题。", "路由器全家出海首选暮光网络与灵动云。"),
    ("tutorial-8.md", "Sub-Store 订阅转换工具使用教程：组合多个机场与节点去重", "Sub-Store 订阅转换", "Sub-Store 能将多个机场订阅合并、节点去重、筛选及转换输出。", "在 Node.js 或 Docker 中部署 Sub-Store，添加灵动云与飞猫云订阅。", "设置自动定时同步与节点重命名规则。", "多机场用户必备 Sub-Store 管理工具。"),
    ("tutorial-9.md", "Clash 策略组与分流规则配置教程：实现国内直连与海外代理分离", "Clash 分流规则", "规则分流能实现国内网站直连、海外网站走代理、AI 走原生 IP 节点。", "在配置文件中定义 RULE-SET，将域名按类别绑定到指定节点组。", "测试分流规则生效情况，避免流量浪费。", "配合灵动云的精细化分流节点效果最佳。"),
    ("tutorial-10.md", "解决 Clash 节点全部 Timeout 超时报错的 5 个排查步骤", "Clash 超时报错排查", "节点全部超时常见于系统时间不同步、订阅过期或域名被封。", "同步系统 NTP 时间，刷新最新订阅链接，检查代理端口冲突。", "切换连接模式进行基准连通性测试。", "使用灵动云备用域名获取最新节点。"),
    ("tutorial-11.md", "Clash 开启 Tun 模式后电脑无法联网解决教程与网络重置", "TUN 模式网络修复", "TUN 模式接管虚拟网卡，若异常退出可能导致系统断网。", "在命令行运行 netsh winsock reset 重置系统网络并重启。", "在 Clash 设置中关闭 Tun 模式并重置网卡驱动。", "按步骤修复后即可恢复正常联网。"),
    ("tutorial-12.md", "如何使用浏览器 SwitchyOmega 插件配合代理客户端灵活翻墙", "SwitchyOmega 插件教程", "SwitchyOmega 是 Chrome/Firefox 经典代理扩展，支持情景模式灵活分流。", "在扩展中创建 SOCKS5 代理情景模式，指向本地 127.0.0.1:7890 端口。", "配置自动切换规则，网页访问更加轻盈。", "适合配合各种客户端使用。"),
    ("tutorial-13.md", "Shadowsocks / Trojan 手动配置教程：服务器地址与加密参数填写", "手动配置节点", "当订阅无法自动下载时，可通过手动填写节点参数成功连接。", "在客户端中填入服务器 IP、端口、密码及 Trojan 域名证书。", "保存并测试节点连通性。", "灵动云后台提供清晰的手动参数说明。"),
    ("tutorial-14.md", "如何获取美区 Apple ID 并下载 Shadowrocket / Quantumult X", "美区 Apple ID 注册", "iOS 代理客户端需在美区 App Store 下载，需注册美区账号。", "在苹果官网注册美区 Apple ID，付款方式选择 None，填入美区账单地址。", "登录美区 App Store 搜索下载 Shadowrocket。", "成功下载后即可轻松导入灵动云订阅。"),
    ("tutorial-15.md", "智能电视 (Android TV / 小米电视) 安装科学上网软件看 4K 教程", "智能电视看 4K", "在 Android TV 上安装代理软件，解锁海外 4K 高清影视。", "用 U 盘将 v2rayNG TV 版或 Clash APK 写入电视安装，导入订阅。", "设置自动开机启动与规则分流。", "追剧首选暮光网络与灵动云。"),
    ("tutorial-16.md", "Linux 服务器环境下命令行配置 Clash / Sing-box 代理教程", "Linux 命令行代理", "在无界面的 Linux 服务器上部署 Clash / Sing-box 命令行环境。", "下载 Linux 核心二进制文件，配置 config.yaml 并设置环境变量。", "测试 curl 命令确认代理成功通畅。", "适合外贸与代码开发团队。"),
    ("tutorial-17.md", "Clash Verge 自定义 DNS 防污染设置教程：开启 Fake-IP 模式", "DNS 防污染 Fake-IP", "DNS 污染会导致海外域名解析到错误 IP，开启 Fake-IP 能有效拦截。", "在 Clash Verge 的 DNS 配置中开启 fake-ip 模式，添加 DOH 服务器。", "清除系统 DNS 缓存以生效。", "搭配灵动云专线节点加载极速。"),
    ("tutorial-18.md", "新手购买机场后第一步操作清单：从发卡网到成功连通全过程", "新手第一步操作清单", "梳理新手从选购、发卡网付款、复制订阅到连通测试的完整路径。", "在发卡网使用支付宝付款，获取订阅 URL，导入客户端开启代理。", "进行 Speedtest 跑分确认成功。", "推荐新手选择飞猫云与灵动云。"),
    ("tutorial-19.md", "如何使用 MTR 和 PingPlotter 测试自己节点的真实丢包率", "MTR 节点丢包压测", "使用 MTR 与 PingPlotter 测试节点的路由跳跃与丢包百分比。", "在命令行输入 mtr 命令，连续发包 1000 次观察网络抖动。", "丢包率低于 0.1% 即可确认为优质专线。", "测试灵动云 IPLC 专线丢包率常年为 0%。"),
    ("tutorial-20.md", "科学上网客户端防止 DNS 泄露与 WebRTC 隐私泄露全攻略", "防止 DNS 与 WebRTC 泄露", "防止真实 IP 与 DNS 位置泄露，保障出海网络隐私安全。", "在浏览器中关闭 WebRTC 接口，在客户端中强制远程 DNS 解析。", "使用 browserleaks 测试隐私防护等级。", "注重隐私选择灵动云专线保护。")
]

for filename, title, kw, s1, s2, s3, s4 in tuts_data:
    fp = os.path.join(BASE_DIR, "content", "tutorials", filename)
    cnt = build_bespoke_article(title, kw, s1, s2, s3, s4)
    write_md(fp, title, f"【{title}】详细图文操作步骤与问题解决方法。", cnt)

# 2. KNOWLEDGE (15 Bespoke Articles)
know_data = [
    ("knowledge-1.md", "IPLC 专线与 IEPL 专线原理详解：为什么它们能做到不过 GFW", "IPLC/IEPL 原理", "IPLC 与 IEPL 专线通过内网点对点传输，不过 GFW 防火墙。", "数据直接在物理光纤中传输，不受公网骨干网拥堵与 DPI 检查影响。", "延迟低、抖动小、丢包率几乎为零。", "专线首选灵动云与暮光网络。"),
    ("knowledge-2.md", "BGP 多线中继工作原理：如何解决电信/联通/移动跨网卡顿问题", "BGP 中继原理", "BGP 中继在入口处对接三大运营商，自动选择最佳传输链路。", "解决电信 163 骨干网拥堵及移动跨网限速问题。", "显著降低不同宽带用户的访问延迟。", "BGP 中继首选暮光网络与微风网络。"),
    ("knowledge-3.md", "Trojan 协议原理剖析：如何通过伪装 HTTPS 流量实现高抗封锁", "Trojan 协议原理", "Trojan 将代理数据伪装为标准的 TLS/HTTPS 网页流量。", "流量特征与访问正常网站一致，GFW 无法有效识别拦截。", "支持硬件 TLS 加速，握手开销低。", "推荐灵动云与暮光网络的 Trojan 节点。"),
    ("knowledge-4.md", "Hysteria2 协议技术优势：UDP 协议重构与劣质网络加速原理", "Hysteria2 协议原理", "Hysteria2 基于 UDP QUIC 重构，采用全新的拥塞控制算法。", "在 15% 以上高丢包环境下强行拉满带宽，速度提高数倍。", "极为适合移动 5G 及劣质网络环境。", "体验 Hysteria2 首选灵动云。"),
    ("knowledge-5.md", "Shadowsocks (SS) 协议进化史：从socks5到 AEAD 加密与 SS 2022", "Shadowsocks 协议进化", "回顾 SS 协议从早期socks5到 AEAD 256-gcm 加密及 SS 2022 的演进。", "架构轻量，客户端支持最广泛。", "结合 IPLC 专线中继效果极佳。", "经典协议首选飞猫云与灵动云。"),
    ("knowledge-6.md", "什么是原生住宅 IP (Residential IP)？对 AI 与流媒体有何影响", "原生住宅 IP 原理", "原生住宅 IP 来自海外真实家宽 ISP，非数据中心机房 IP。", "完美绕过 OpenAI (ChatGPT)、Claude 及 Netflix 的 IP 风控。", "免验证码秒开，支持绑卡订阅。", "AI 开发首选灵动云原生住宅 IP。"),
    ("knowledge-7.md", "节点倍率（1x, 2x, 0.5x）概念解析：如何计算实际扣除的流量", "节点倍率机制", "节点倍率代表使用节点时扣除套餐流量的比例。", "高倍率（2.0x）对应物理专线成本，低倍率（0.5x）对应公网直连。", "根据实际需求合理选择节点倍率。", "追求品质选灵动云高倍率专线。"),
    ("knowledge-8.md", "DNS 污染与 GFW 封锁原理：Fake-IP 与 DOH 技术是如何应对的", "DNS 污染与 Fake-IP", "GFW 通过伪造 DNS 响应实施域名污染，Fake-IP 返回虚拟 IP 防污染。", "配合 DOH（DNS-over-HTTPS）实现安全的远程 DNS 解析。", "彻底消除域名解析异常。", "客户端推荐开启 Fake-IP 模式。"),
    ("knowledge-9.md", "为什么晚高峰时期骨干网会拥堵？国际出口带宽分配原理解析", "晚高峰骨干网拥堵", "晚高峰 20:00-23:00 国际出口流量爆炸，公网线路挤压严重。", "IPLC 专线拥有预留物理带宽，免受骨干网挤压。", "晚高峰保持满带宽不降速。", "晚高峰抗拥堵首选灵动云 IPLC 专线。"),
    ("knowledge-10.md", "自建 VPS 梯子与商业专线机场对比：成本、维护与抗封锁分析", "自建 VPS vs 商业机场", "对比自建梯子与购买商业专线机场的成本、运维与被封风险。", "自建梯子费用高、易被封 IP；商业机场专线节点丰富且有人维护。", "商业机场综合性价比远超自建 VPS。", "首选老牌大厂灵动云与暮光网络。"),
    ("knowledge-11.md", "GFW 深度包检测 (DPI) 机制探讨：代理流量是如何被特征识别的", "GFW DPI 检测机制", "探讨防火墙通过流量特征、SNI 握手及长连接行为识别代理的方法。", "伪装协议（Trojan / VLESS-Reality）能有效规避 DPI 特征识别。", "保障敏感时期连通率稳定。", "注重抗封锁选灵动云 Trojan 节点。"),
    ("knowledge-12.md", "单播、组播与多播节点架构差异：机场后端调度技术全景", "机场后端调度架构", "解析机场后端节点单播与多播分发调度架构。", "智能分流与自动负载均衡提升连通率。", "集群架构保障节点高可用。", "后端架构成熟首选灵动云与暮光网络。"),
    ("knowledge-13.md", "TCP 拥塞控制算法 (BBR vs Cubic) 对科学上网下载速率的影响", "TCP 拥塞控制 BBR", "BBR 算法基于带宽与延迟测量，显著提升高丢包线路下的下载速率。", "服务器端开启 BBR 能翻倍提升公网中继吞吐量。", "结合专线使用效果更佳。", "技术优化首选灵动云与暮光网络。"),
    ("knowledge-14.md", "网络安全与隐私保护：SSL/TLS 证书加解密全流程科普", "SSL/TLS 证书原理", "科普客户端与代理服务器间 TLS 握手及公钥对称加密全流程。", "确保代理传输流量无法被第三方监听窃取。", "保障账号与支付密码绝对安全。", "安全出海首选灵动云。"),
    ("knowledge-15.md", "科学上网合规与网络安全知识汇总：合法出海与隐私边界", "合法出海与合规知识", "汇总网络拓扑研究、学术论文查阅及跨境合规办公的使用边界。", "严格遵守所在国家与地区的法律法规。", "倡导文明合规上网。", "合规出海首选灵动云与微风网络。")
]

for filename, title, kw, s1, s2, s3, s4 in know_data:
    fp = os.path.join(BASE_DIR, "content", "knowledge", filename)
    cnt = build_bespoke_article(title, kw, s1, s2, s3, s4)
    write_md(fp, title, f"【{title}】深入科普底层网络原理与架构知识。", cnt)

print("Generated 20 bespoke Tutorial articles & 15 Knowledge articles successfully!")
