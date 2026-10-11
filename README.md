# 👑 RBX Manager 2 — Modern Roblox Multi-Account Manager (RAM) for Windows

<div align="center">

<a href="https://github.com/toskaman/RBX-Manager-2/releases/download/v1.9.34.1/brag.mp4">
  <img src="https://github.com/toskaman/RBX-Manager-2/releases/download/v1.9.34.1/brag.jpg" alt="RBX Manager 2 Interface and Feature Showcase Video" width="100%" />
</a>

<p>
  <a href="https://toskaman.github.io/RBX-Manager-2/">
    <img src="https://img.shields.io/badge/%F0%9F%8C%90%20Official%20Showcase-GitHub%20Pages-00f2ff?style=for-the-badge" alt="Official Web Showcase" />
  </a>
  <a href="https://github.com/toskaman/RBX-Manager-2/releases/download/v1.9.34.1/brag.mp4">
    <img src="https://img.shields.io/badge/%E2%96%B6%20Watch%20Showcase-1080p%20%E2%80%A2%201m48s-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch Feature Video" />
  </a>
  <a href="https://discord.gg/zNpj8ctH9p">
    <img src="https://img.shields.io/badge/Discord-Join%2010%2C000%2B%20Community-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord Community" />
  </a>
</p>

[![Status](https://img.shields.io/badge/Status-Active%20%26%20Up--to--Date%20(2026)-00f2ff?style=for-the-badge&logo=roblox&logoColor=white)](https://toskaman.github.io/RBX-Manager-2/)
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%20%2F%2011%20(64--bit)-blueviolet?style=for-the-badge&logo=windows&logoColor=white)](https://toskaman.github.io/RBX-Manager-2/)
[![Version](https://img.shields.io/badge/Release-v1.9.36.25-00ff88?style=for-the-badge)](https://discord.gg/zNpj8ctH9p)
[![License](https://img.shields.io/badge/License-Free%20Core%20%26%20Optional%20Premium-FFD700?style=for-the-badge)](#-free-vs-premium-comparison)
[![VirusTotal](https://img.shields.io/badge/VirusTotal-0%2F72%20Clean%20(Official%20Build)-brightgreen?style=for-the-badge&logo=virustotal&logoColor=white)](#-security-transparency--anti-cheat-integrity)
[![Anticheat](https://img.shields.io/badge/Byfron%20%2F%20Hyperion-Safe%20(Native%20DuplicateHandle)-success?style=for-the-badge&logo=shield&logoColor=white)](#-how-multi-instance-works-technically)

### **High-performance Roblox Multi-Account Manager for Windows.**
*Run multiple Roblox instances simultaneously without mouse hijacking. Features 320x240 micro-windows, background Anti-AFK, independent FPS throttling, and local DPAPI encryption.*

[🌐 Official Website](https://toskaman.github.io/RBX-Manager-2/) • [✨ Key Innovations](#-key-innovations) • [⚙️ Feature Breakdown](#%EF%B8%8F-complete-feature-breakdown) • [📊 Comparison Matrix](#-comparison-rbx-manager-2-vs-legacy-managers) • [💎 Free vs Premium](#-free-vs-premium-comparison) • [🚀 Official Community & Downloads](#-official-community--downloads)

</div>

---

## 🌟 Key Innovations

Built specifically for high-efficiency multi-boxing, account farming (*Pet Simulator 99, Blox Fruits, Anime Vanguards, Blade Ball, Sol's RNG, etc.*), trading, and seamless multi-account management.

* 🛡️ **Native Mutex Management (Hyperion & Byfron Safe)** : Closes the singleton mutex via standard Windows API (`DuplicateHandle` with `DUPLICATE_CLOSE_SOURCE`). **Zero DLL injection and zero client memory modification**.
* 📐 **320x240 Micro-Window Mode** : Overrides the default 800x600 Roblox restriction, reducing rendering resolution and VRAM load by ~84% to easily tile dozens of accounts on a single monitor.
* ⚡ **Non-Intrusive Background Anti-AFK** : Custom virtual event dispatcher that prevents 20-minute disconnects without stealing physical mouse or keyboard focus. Keep working or playing while farming in the background.
* 🧠 **Granular FPS Limiting per Account** : Lock background farming instances to 15 FPS while running your primary active game at 144 FPS to prevent CPU overheating.
* 📱 **Remote Web Dashboard** : Built-in local web interface accessible via phone, tablet, or secondary PC on your LAN to monitor account statuses and launch sessions.
* 🔒 **Local Hardware-Bound Encryption** : Stored `.ROBLOSECURITY` session cookies and credentials are encrypted strictly on your local PC via Windows DPAPI and master password protection.
* ↩ **Instant Native Window Restore** : Switch between 320x240 micro-farming view and normal native Roblox window in 0ms with a single click.
* 🧹 **Automated Roblox Logs Cleaner** : Automatically purges leftover Roblox debug log files older than 24h or over 50MB, saving gigabytes of hidden SSD storage.

---

## ⚙️ Complete Feature Breakdown

### 🎮 1. Multi-Account Management & Quick Migration
* **Fast Account Migration** : Import existing accounts in seconds using 1-click cookie import, fully compatible with export lists from legacy account managers.
* **Tags, Nicknames & Instant Filter** : Group accounts with color tags, custom aliases, and instant search.
* **VIP & Private Server Hub** : Associate private VIP server links directly with specific accounts for 1-click automatic joining.
* **Independent FPS Selector** : Configure custom FPS targets per account (e.g., 15 FPS for background farming, 144 FPS for main gameplay).

### ⚡ 2. Resource Optimization & Efficiency Methodology
* **Resolution Scaling Savings** : Reducing render resolution from 800x600 (480,000 pixels) to 320x240 (76,800 pixels) cuts rasterization workload by ~84% per frame.
* **Background Frame Throttling** : Inactive background instances run at reduced frame rates to lower GPU and CPU power draw.
* **CPU Core Isolation & Affinity** : Balance instances across available physical CPU cores to eliminate frame pacing stutters.
* **Auto-Shutdown Timer** : Automatically shut down your computer after a specified farming duration or scheduled time.

### 🛡️ 3. Anti-AFK & Automation
* **Use PC While AFK** : Keeps accounts active indefinitely without hijacking your physical mouse cursor.
* **Automatic Client Update Handling** : Seamlessly adapts to weekly Roblox client updates.
* **Diagnostic Logging** : Built-in local error logging for rapid technical support.

### 🎨 4. Custom Themes & UI
* **Modern WPF Architecture** : High-DPI responsive design with hardware-accelerated rendering.
* **Themes** : Choose between *Default Dark Neon*, *🐱 Izu Kawaii (Pastel Pink)*, *Blocky Bricks*, and *SWAGNUB*.
* **Minimize on Launch** : Automatically tucks game windows to the background upon launch.
* **Panic Button** : Instantly close all active sessions with a single hotkey.

### 💬 5. Discord Webhook Notifications
* **Real-Time Webhook Alerts** : Receive Discord notifications on game launch, unexpected disconnects, or crashes.
* **Per-Account Filter** : Mute or enable Discord alerts for specific accounts.

---

## 📊 Comparison: RBX Manager 2 vs Legacy Managers

| Feature / Capability | 👑 **RBX Manager 2 (2026)** | 🐺 **IceWolf RAM (Legacy)** | 📦 **Basic Process Closers** |
|---|:---:|:---:|:---:|
| **Core Multi-Account Access** | ✅ **100% Free** | ✅ Free | ✅ Free |
| **User Interface Technology** | ✅ **Modern WPF + Themes** | ❌ 2018 WinForms | ❌ CLI / Basic |
| **Micro-Resizing (Down to 320x240)** | ✅ **Yes (WS_POPUP)** | ❌ No (800x600 Lock) | ❌ No |
| **Non-Intrusive Background Anti-AFK** | ✅ **Yes (Zero Mouse Hijack)** | ❌ Steals Mouse Focus | ❌ Steals Mouse Focus |
| **Independent FPS Limit per Account** | ✅ **Granular per Account** | ⚠️ Global Only | ❌ No |
| **Remote Web Dashboard (Mobile/LAN)** | ✅ **Yes** | ❌ No | ❌ No |
| **Safe Exit Protocol (`WM_CLOSE`)** | ✅ **Yes (Preserves Data)** | ❌ Force Kill Process | ❌ Force Kill Process |
| **Active Update Support** | ⚡ **< 24h Turnaround** | ❌ Archived | ❌ None |

---

## 💎 Free vs Premium Comparison

| Capability | 🆓 Free Edition | 💎 Premium / Unlimited |
|---|:---:|:---:|
| **Unlimited Accounts & Multi-Instance Launching** | ✅ Included | ✅ Included |
| **320x240 Micro-Window Scaling** | ✅ Included | ✅ Included |
| **Non-Intrusive Background Anti-AFK** | ✅ Included | ✅ Included |
| **Independent FPS Limit per Account** | ✅ Included | ✅ Included |
| **Remote Web Dashboard Access** | ✅ Included | ✅ Included |
| **Automatic Roblox Logs Cleaner** | ✅ Included | ✅ Included |
| **Dynamic 60 FPS Rainbow RGB Mode** | ❌ Locked | ✅ **Unlocked** |
| **Full 10+ Cyber Neon Theme Catalog** | ❌ 2 Base Themes | ✅ **Unlocked** |
| **Advanced Copper Memory Optimizer** | ❌ Locked | ✅ **Unlocked** |
| **VIP Discord Role & Priority Support** | ❌ Community Support | ✅ **Lifetime Access** |

---

## 🛡️ Security Transparency & Anti-Cheat Integrity

* 🔒 **Native Win32 DuplicateHandle (`DUPLICATE_CLOSE_SOURCE`)** : Roblox enforces single-instance sessions via a singleton mutex (`ROBLOX_singletonMutex`). RBX Manager 2 calls standard Windows APIs to close this handle without injecting DLLs, hooking game functions, or modifying Roblox client memory.
* 🔐 **Local DPAPI Encryption** : Stored passwords and `.ROBLOSECURITY` session cookies are encrypted locally on your Windows machine using DPAPI and master password protection. No cookies or personal data are transmitted to external servers.
* 🧪 **Independent Antivirus Verification** : Official binary releases are scanned on VirusTotal and accompanied by public scan reports showing 0 detections. Because the software is closed-source, users are always encouraged to independently scan downloaded files on [VirusTotal](https://www.virustotal.com) or Windows Defender.

---

## 🚀 Official Community & Downloads

> ⚠️ **NO EXECUTABLES OR BINARY FILES ARE HOSTED DIRECTLY ON GITHUB.**  
> Verified official releases, automatic update packages, and community support are distributed exclusively through our official Discord community hub.

<div align="center">

# 🌐 [JOIN THE OFFICIAL DISCORD COMMUNITY](https://discord.gg/zNpj8ctH9p)
### 👉 **https://discord.gg/zNpj8ctH9p** 👈

**Get verified access to the latest release of RBX Manager 2, fast technical support, license activation, and an active community of 10,000+ players.**

</div>

---

## ❓ Frequently Asked Questions (FAQ)

<details>
<summary><b>Q: How do I run multiple Roblox accounts at once on PC without lag?</b></summary>
Running multiple accounts without stutter requires reducing graphics overhead and limiting idle thread usage. RBX Manager 2 uses <b>320x240 Micro-Window scaling</b> (cutting rendering pixel area by ~84%) and independent background FPS caps (e.g., 15 FPS for farming clients, 144 FPS for your active game). This allows standard PCs to run multiple instances comfortably.
</details>

<details>
<summary><b>Q: Does RBX Manager 2 inject DLLs or trigger Byfron (Hyperion) anti-cheat?</b></summary>
<b>No.</b> RBX Manager 2 does not inject DLLs, hook game memory, or modify Roblox client binaries. It operates strictly outside game memory, closing the singleton mutex handle via the standard Windows API <code>DuplicateHandle</code> before launching subsequent instances.
</details>

<details>
<summary><b>Q: How does the background Anti-AFK work without moving the mouse?</b></summary>
Traditional tools use <code>SendInput</code> to hijack your physical mouse cursor, interrupting your workflow. RBX Manager 2 dispatches non-intrusive virtual keep-alive signals directly to target Roblox window message queues, keeping instances connected 24/7 while leaving your cursor completely free.
</details>

<details>
<summary><b>Q: Where are my login cookies and credentials stored?</b></summary>
All <code>.ROBLOSECURITY</code> cookies and configuration files are encrypted strictly on your local PC using Windows DPAPI and master password encryption. No account information is ever transmitted across the internet.
</details>

<details>
<summary><b>Q: How do I import my accounts from older account managers?</b></summary>
You can migrate accounts in seconds using the built-in <b>1-Click Cookie Import</b> feature by copying your existing account lists or cookies directly into the tool.
</details>

<details>
<summary><b>Q: Is RBX Manager 2 free or paid?</b></summary>
Core multi-Roblox farming, unlimited accounts, micro-windows, and background Anti-AFK are <b>100% free forever</b>. An optional Premium license is available for users who want extra cosmetic cyber themes, 60 FPS rainbow RGB mode, and priority support.
</details>

---

## 🌍 International Documentation & Localized Guides

Explore localized guides and terminology on the [official web showcase](https://toskaman.github.io/RBX-Manager-2/):

* 🇪🇸 **[Español](https://toskaman.github.io/RBX-Manager-2/es/)** : Administrador de cuentas de Roblox — Multi Roblox sin lag en Windows 10 y 11.
* 🇧🇷 **[Português (Brasil)](https://toskaman.github.io/RBX-Manager-2/pt-br/)** : Gerenciador de contas Roblox — Como abrir vários Roblox no PC ao mesmo tempo sem travar o mouse.
* 🇫🇷 **[Français](https://toskaman.github.io/RBX-Manager-2/fr/)** : Gestionnaire multi-comptes Roblox — Lancer plusieurs Roblox en même temps sans ralentissement.
* 🇩🇪 **[Deutsch](https://toskaman.github.io/RBX-Manager-2/de/)** : Roblox Multi-Account Manager — Mehrere Roblox-Konten gleichzeitig öffnen mit RAM-Optimierung.

---

## ⭐ Support the Project

If you find **RBX Manager 2** helpful for your farming and multi-boxing, please consider giving this repository a **Star (⭐)** at the top right of the page! It helps more players discover the project.

---

<div align="center">
<sub><b>Disclaimer:</b> RBX Manager 2 is an independent Windows utility program developed by toskaman and is not affiliated with, endorsed, sponsored, or supported by Roblox Corporation. Roblox is a registered trademark of Roblox Corporation. All executable releases are distributed via the official Discord community; users are always encouraged to independently verify downloaded files.</sub>
</div>
