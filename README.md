# Project Monolith: The Open-Source "Duel Arena" Ecosystem 🎴⚡

An ultra-premium, open-source hardware and software ecosystem that bridges physical trading card games (TCGs) with local peer-to-peer digital animations. Inspired by the tactical fantasy of anime "Duel Disks," Project Monolith reimagines tabletop gaming by transforming the physical table into a smart, interactive digital battleground without sacrificing the tactile satisfaction of real cards.

---

## 🌌 The Vision
For decades, fans have tried to build wearable, mechanical "Duel Disks." They always fail because strapped wrist mechanisms are heavy, prone to jamming, and ruin expensive cards. 

**Project Monolith shifts the paradigm.** Instead of a clunky plastic toy, we have engineered a smartphone-grade, desktop-anchored ecosystem:
1. **The Core Module:** A pocket-sized, CNC-milled aluminum machine that automatically searches, sorts, and ballistically deals cards.
2. **The Smart Mat:** A flexible neoprene playmat embedded with hidden micro-electromagnets that act as a "magnetic net" to catch and lock flying cards flat onto the table.
3. **The Twin-Phone Arena:** Two smartphones placed side-by-side in the center of the table act as a local, split-screen "Digivice-style" visual rendering matrix for 2D/3D combat animations.

---

## 🛠️ Hardware & Architecture Specifications

### 1. The Monolith Unibody Module (The Launcher)
* **Form Factor:** 4.0" x 3.0" x 2.25" (The footprint of a premium deck box).
* **Chassis Material:** 5-axis CNC-machined **6061-T6 Anodized Aluminum** outer shell with a lightweight **Magnesium-Lithium Alloy** internal component skeleton.
* **Drop Protection:** Floating internal mechanical tray suspended inside the unibody via **60-Durometer Nitrile Rubber (NBR) shock-gaskets** to survive a 2-meter drop onto concrete.
* **Optical Window:** Diamond-wheel ground **Synthetic Sapphire Crystal** scanning plate to prevent lifetime card-sleeve abrasion from clouding the internal laser scanners.
* **Brain:** Raspberry Pi Pico W executing an asynchronous MicroPython firmware loop.

### 2. The Smart Mat Array (The Battlefield)
* **Surface:** 3mm soft neoprene lamination with an integrated flexible printed circuit (FPC) substrate layer.
* **The Magnetic Catch:** Low-profile **5V 25N flat-face micro-electromagnets** embedded in each player zone. 
* **The Sleeve Modifier:** Standard card sleeves retrofitted with an ultra-thin **0.5mm passive mu-metal or iron foil border strip**. 
* **The Capture:** When a card is flung from the Monolith, the mat opens a localized magnetic field in milliseconds, snapping the metallic-edged card flat to the table to eliminate sliding or flipping.
* **Brain:** ESP32-S3 microcontroller managing high-speed N-Channel MOSFET switching and localized SPI communication.

---

## 📡 Software & Local Network Streaming

Project Monolith acts as a **universal card gaming platform**—entirely independent of any single game's ruleset. The hardware reads generic barcodes printed along the margins of the custom sleeves, while the app manages the rule configuration profiles (e.g., *Yu-Gi-Oh!*, *Magic: The Gathering*, *Pokémon*, or custom Indie tabletop games).

* **Zero-Camera Table Tracking:** No overhead webcams. An embedded sensor array beneath the mat continuously tracks table states, broadcasting real-time frame packets over a local Wi-Fi WebSocket network without cloud latency.
* **The Split-Screen Phone Engine:** Connected local smartphones capture the mat's telemetry data to automatically animate combats, manage life-point calculations, track hidden card sequences inside the deck, and trigger virtual visual effects when a player commands an attack.

---

## 📄 License
This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**. Feel free to fork, build, hack, and modify this machine—but all derivatives must remain open-source, and commercial distribution without project authorization is prohibited.
