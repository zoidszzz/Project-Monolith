# 🎴 Project Monolith: Modular Hardware Ecosystem

Project Monolith is a premium, open-source tabletop hardware and software ecosystem designed to bring the anime "Duel Arena" fantasy into reality. Instead of relying on a heavy mechanical device strapped to a player's arm, it delegates operations across a highly portable desktop launcher console, a passive rollable smart mat substrate, and an active docking cap.

---

## 🚀 System Architecture Pass v2.0 (The Modular Update)

The ecosystem separates processing power and structural flexibility by using a "piggyback" hardware interface:

+-------------------------------------------------------------+
|  THE CAP DOCK (Detachable System Brain)                      |
|  [ESP32-S3] + [18650 Battery Hub] + Phone Stand Mount       |
+----------------------+--------------------------------------+
|  <-- (Sliding Pogo Pin Connector Bus)
+----------------------v--------------------------------------+
|  THE SMART MAT SUBSTRATE (Passive Sensor Grid)              |
|  [Zone 1 RFID]   [Zone 2 RFID]   [Zone 3 RFID]   [Zone 4 RFID] |
+-------------------------------------------------------------+
### 1. Component Specifications

*   **The Monolith Module (The Launcher):** A heavy, pocket-sized 4.0" x 3.0" x 2.25" unibody box. Milled from 5-axis CNC 6061-T6 Anodized Aluminum with a diamond-wheel ground Synthetic Sapphire Crystal optical scanning plate. Driven by an internal Raspberry Pi Pico W hub.
*   **The Smart Mat Substrate:** A lightweight, passive 3mm neoprene playmat. It contains zero integrated microcontrollers or rigid batteries. It carries only flexible printed circuit (FPC) trace routing, 4 independent RFID tracking grids, and local electromagnets terminating at a top-edge pogo pin interface strip. It can be rolled tightly into its carrying case without risk of breaking active components.
*   **The Case Cap & Dock:** The structural lid of the carrying case serves as a multi-functional system dock. It acts as an adjustable smartphone stand, holds the master rechargeable LiPo/18650 battery bank, and houses the **ESP32-S3 wireless node**. When snapped onto the top edge of the smart mat, it "piggybacks" onto the FPC lines to power the mat and read table data.

### 2. Dual-Target Gameplay Modes

*   **Local Twin-Phone Battle Arena:** The Cap Dock broadcasts asynchronous JSON telemetry frames over a local 50Hz Wi-Fi WebSocket network to two smartphones placed side-by-side, updating health pools, rules, and rendering real-time synchronized 3D battlefield animations.
*   **Remote Web-Cam PC Duels:** When connected to a computer via USB-C, the Cap Dock pipes real-time card positions directly to a PC client. Player actions are instantly translated into automated digital graphic overlays on Discord, Zoom, or OBS video streams during remote online matchups.

---

## 🛠️ Complete Electrical Component Mapping
+-------------------------------------------------+
|             5V 4A MAIN SWITCHING PSU            |
+---------+-----------------------------+---------+
| (+5V)                       | (GND)
v                             v
+----------------------------------------+   +---------------------------------------+
|          5V VCC SYSTEM RAIL            |   |         SYSTEM COMMON GND RAIL        |
|                                        |   |                                       |
|  +--> Pi Pico W [VBUS Pin]             |   |  +--> Pi Pico W [Any GND Pin]         |
|  +--> ESP32-S3 [5V / Vin Pin in Cap]   |   |  +--> ESP32-S3 [Any GND Pin]          |
|  +--> Barcode Scanner Module [VCC]     |   |  +--> Barcode Scanner Module [GND]    |
|  +--> MX1508 Dual DC Driver [VCC]      |   |  +--> MX1508 Dual DC Driver [GND]     |
|  +--> ULN2003 Driver Board [VCC]       |   |  +--> ULN2003 Driver Board [GND]      |
|  +--> Solenoid Plunger Coil (+)        |   |  +--> S8050 Transistor [Emitter]      |
|  +--> Electromagnets Z1-Z4 (+)         |   |  +--> IRL540 MOSFETs Z1-Z4 [Source]   |
+----------------------------------------+   +---------------------------------------+

======================================================================================
UNIT 1: LAUNCHER SUBSYSTEM (RASPBERRY PI PICO W)

[TTL Optical Barcode Module]
• RX Pin <======================== GPIO 0 (TX)
• TX Pin ========================> GPIO 1 (RX)
[MX1508 Ballistic Engine Driver]
• IN1 (Feed Roller PWM Control) <= GPIO 14 (PWM)
• IN2 (Flywheel Trigger Signal) <= GPIO 15 (Digital OUT)
• MOTOR A Terminals ============> [N20 Core DC Feed Roller Motor]
• MOTOR B Terminals ============> [High-RPM Brushless Flywheel Unit]
[ULN2003 360-Degree Azimuth Base Driver]
• IN1 / IN2 / IN3 / IN4 <======== GPIO 2, 3, 4, 5 (Digital Sequential Matrix)
• Output Wiring Bundle =========> [28BYJ-48 Stepper Internal Drive Harness]
[Secondary Mechanical Dump Gate Solenoid Circuit]
• GPIO 16 (Digital OUT) --------> [1kΩ Resistor] ----> Base of S8050 NPN Transistor
• Collector of S8050 -----------> Solenoid Plunger Coil (-) Terminal
• Flyback Protection Diode ------> 1N4007 across Solenoid [+ (Anode) / - (Cathode)]

======================================================================================
UNIT 2: CAP-DOCK BRIDGED CAPTURE GRID (ESP32-S3 PIGGYBACK INTERFACE)

[High-Frequency Active Magnetic Braking Cells (1 through 4)]
• GPIO 4, 5, 6, 7 <=============> [100Ω Gate Resistors] ----> Gate of IRL540 MOSFET
• Gate Protection Link =========> [10kΩ Pulldown to GND] tied to each individual Gate
• Drain of IRL540 MOSFET =======> Electromagnet Lead (-) for Target Zone Array
• Reverse-Surge Suppression =====> 1N4007 Diode pinned directly across each Coil
[Table State Tracking Grid (Shared High-Speed SPI Pogo-Pin Topology)]
• GPIO 11 (SCK) ================> Mat Pogo Header Line 1 ===> Linked to all 4 MFRC522 SCK
• GPIO 12 (MISO) ===============> Mat Pogo Header Line 2 ===> Linked to all 4 MFRC522 MISO
• GPIO 13 (MOSI) ===============> Mat Pogo Header Line 3 ===> Linked to all 4 MFRC522 MOSI
• GPIO 9 (RST) =================> Mat Pogo Header Line 4 ===> Tied globally to all 4 Reset Pins
• GPIO 18 (SS/CS Zone 1) =======> Mat Pogo Header Line 5 ===> Dedicated Chip Select Panel #1
• GPIO 19 (SS/CS Zone 2) =======> Mat Pogo Header Line 6 ===> Dedicated Chip Select Panel #2
• GPIO 20 (SS/CS Zone 3) =======> Mat Pogo Header Line 7 ===> Dedicated Chip Select Panel #3
• GPIO 21 (SS/CS Zone 4) =======> Mat Pogo Header Line 8 ===> Dedicated Chip Select Panel #4


## ⚙️ Repository Directory Structure

*   `/firmware/launcher_pico/` : MicroPython operational loops for ballistic flight execution.
*   `/firmware/cap_dock_node/` : C++ firmware bridging active mat SPI lines to WebSockets and PC Serial JSON channels.
*   `/schematics/` : Gerber files for the flexible printed circuit tracking layout.
*   `/cad/` : Industrial 3D printing and milling files for the launcher unibody shell and Cap Dock slider components.

---
*This is for informational purposes only. For medical advice or diagnosis, consult a professional. AI responses may include mistakes.*
