---
title: 'How to install Gemma 4 on your phone (iPhone & Android)'
description: 'Step-by-step guide to download and run Gemma 4 locally on your iPhone or Android device using Google AI Edge Gallery.'
pubDate: '2026-04-06T15:33:00.000Z'
heroImage: 'https://images.unsplash.com/photo-1523475472560-d2df97ec485c?auto=format&fit=crop&w=1600&q=80'
categories: ["ai", "mobile"]
tags: ["gemma", "edge-ai", "guide"]
author: '["gndx"]'
---

# Gemma 4 in your pocket: fast install for iPhone and Android

Gemma 4 now runs **offline** on modern phones thanks to the official **Google AI Edge Gallery** app. This guide walks you through the setup on both **iPhone** and **Android** with zero cables or complicated steps.

> 🧠 Why it matters: Running models locally gives you **full privacy**, no per-token fees, and the freedom to use AI even when you have no signal.

---

## Quick requirements

- **iPhone** on iOS 17 or newer, ideally with an A16 chip or Apple Silicon for best performance.
- **Android** on Android 14, powered by a Tensor, Snapdragon 8 Gen 2, or similar flagship SoC.
- 6 GB of free storage and Wi-Fi for the initial download.

---

## iPhone: Gemma 4 inside Google AI Edge Gallery

1. Open the **App Store** on your iPhone.
2. Search for **Google AI Edge Gallery** and tap **Get**.
3. Launch the app, grant local permissions, and open the **AI Chat** tab.
4. Locate **Gemma 4** ("Edge Optimized" build).
5. Tap **Download** and wait for completion, then select **Run locally**.

> 📲 On iPhone you’ll see a "Thinking" mode to visualize reasoning steps and a "Battery Saver" toggle to trade speed for longer sessions.

**Direct link:** [Google AI Edge Gallery – App Store](https://apps.apple.com/us/app/google-ai-edge-gallery/id6749645337?utm_source=gndx.dev)

---

## Android: enable Gemma 4 in minutes

1. Head to **Google Play** and install **Google AI Edge Gallery** (requires up-to-date Play Services).
2. Allow storage permissions so models can be stored locally.
3. In the **Model Hub** tab, search **Gemma 4** → tap **Download**.
4. When finished, press **Set as default** inside **AI Chat**.
5. Craft your first prompt. Example: *"Brainstorm productivity app ideas in Spanish."*

> 🤖 On Android you can toggle **GPU Acceleration** under *Settings → Performance*. If the phone heats up, switch the profile to **Balanced**.

**Direct link:** [Google AI Edge Gallery – Google Play](https://play.google.com/store/apps/details?id=com.google.ai.edgegallery&hl=en&gl=US)

---

## Useful features on both platforms

| Feature | iPhone | Android |
| --- | --- | --- |
| Thinking Mode | ✅ | ✅ |
| Agent Skills (Wikipedia, Docs) | ✅ | ✅ |
| Ask Image (photo analysis) | ✅ | ✅ |
| Audio Scribe (speech to text) | ✅ | ✅ |
| Battery Saver / Thermal guard | ✅ | ✅ |

---

## Tips to get the best experience

- **Update** the app whenever new Gemma 4 optimizations drop.
- Use Bluetooth headphones for long audio interactions (Audio Scribe).
- Keep battery above 40% before running extended sessions.
- Disable **Low Power Mode** (iPhone) or **Battery Saver** (Android) to avoid throttling.

---

## Common issues and quick fixes

- **Slow downloads:** switch to Wi-Fi 5/6 and keep the screen awake.
- **Android app crashes:** clear cache via App Info → Storage & cache.
- **Short replies on iPhone:** enable *Extended Context* in Settings → Labs.

---

## Next steps for power users

1. Enable **Agent Skills** and connect Google Drive to query documents.
2. Create **Shortcuts** (iOS) or **Assistant Routines** (Android) to launch prompts by voice.
3. Integrate Gemma 4 with your stack (for example Next.js + Supabase) via the local API exposed by Edge Gallery at `http://localhost:8288`.

---

### TL;DR

- Install **Google AI Edge Gallery** on iPhone or Android.
- Download the **Gemma 4** model inside the app and mark it as local.
- Start chatting offline while keeping your data private.

Your phone is now a **mini AI server** ready to run Gemma 4 anytime.
