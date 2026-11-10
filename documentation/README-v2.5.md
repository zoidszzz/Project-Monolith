# 🎴 Project Monolith: Advanced Modular Tabletop Ecosystem (v3.0)

Project Monolith is a premium, open-source tabletop hardware and software ecosystem designed to bring the anime "Duel Arena" fantasy into reality. It delegates operations across a mobile desktop launcher console, a passive rollable smart mat substrate, and an active docking cap. 

---

## 🚀 System Architecture Pass v3.0 (The Interconnected Power Update)

This update integrates an independent, hot-swappable battery cartridge system for the launcher alongside a plug-and-play cross-table power tethering link to pool all tabletop resources.

+------------------------------------+             +------------------------------------+
| UNIT 1: THE LAUNCHER (Machine A)   |             | UNIT 2: THE CAP DOCK SYSTEM        |
| [1x Hot-Swap Battery Cartridge]    |             | [2x Parallel Stacked Phone Bats]   |
|                                    |             |                                    |
|     (Magnetic Interconnect Port)   |             |     (Magnetic Interconnect Port)   |
+-----------------+------------------+             +-----------------+------------------+
|                                                  |
+================== [2-WIRE TETHER] ===============+
(Shared 5V Rail + Common GND)
### 1. Advanced Component Specifications

*   **The Monolith Module (The Launcher):** Milled from 5-axis CNC 6061-T6 Anodized Aluminum with a Synthetic Sapphire Crystal scanning window. Driven by an internal Raspberry Pi Pico W hub. Features a rear mechanical guide channel with a spring-loaded thumb lock to accept hot-swappable battery cartridges for continuous operation.
*   **The Smart Mat Substrate:** A lightweight, passive 3mm neoprene playmat carrying zero integrated batteries. It carries flexible printed circuit (FPC) trace routing, 4 independent MFRC522 RFID tracking grids, and local electromagnets terminating at a top-edge 8-pin pogo interface strip.
*   **The Case Cap & Dock:** Houses the master **ESP32-S3 wireless node** and two parallel-stacked flat phone batteries (**10,000 mAh**). When snapped onto the top edge of the smart mat, it "piggybacks" onto the FPC lines via spring pins to power the scanning grid.

### 2. Power Topology & Dual-State Runtimes

*   **State A: Pure Wireless Isolation (6–8 Hours Launcher / 42.5 Hours Mat):** The launcher and mat run on independent battery reservoirs. They communicate over ultra-low-latency Bluetooth Low Energy (BLE) signals. Best for zero-cord setups.
*   **State B: Tethered Interconnect (37.4 Hours Combined System Life):** A 2-pin magnetic breakaway cable links the Cap Dock directly to the Launcher. This bridges the 5V VCC power rails and unifies the system ground, pooling all three batteries into a massive **13,000 mAh mega-grid** to clear full multi-day convention events.

---

## 🛠️ Complete Electrical Component Mapping
+-------------------------------------------------+
|          TOTAL 13,000 mAh UNIFIED BUS           |
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
CROSS-TABLE POWER INTERCONNECT ROUTING

• Interface Port Type: 2-Pin Magnetic Breakaway Connector
• Trace Array: Parallel 5V VCC / System Ground Bridging Link
• Pin 1 (Shared 5V VCC Rail): Tethers Cap Dock Boost Output directly to Launcher Bus
• Pin 2 (System Common Ground): Establishes static electrical zero-reference baseline

======================================================================================
UNIT 1: LAUNCHER SUBSYSTEM (RASPBERRY PI PICO W)

[3-Pin Cartridge Power Receiving Bay Contacts]
• Terminal 1 (BAT+) ============> Inputs raw battery voltage (3.7V - 4.2V LiPo)
• Terminal 2 (GND) =============> Core System Ground Return
• Terminal 3 (NTC) =============> Relays thermal data to TP4056 safety loops
[TTL Optical Barcode Module]
• RX Pin <======================== GPIO 0 (TX)
• TX Pin ========================> GPIO 1 (RX)
[MX1508 Ballistic Engine Driver]
• IN1 (Feed Roller PWM Control) <= GPIO 14 (PWM)
• IN2 (Flywheel Trigger Signal) <= GPIO 15 (Digital OUT)

======================================================================================
UNIT 2: CAP-DOCK BRIDGED CAPTURE GRID (ESP32-S3 PIGGYBACK INTERFACE)

[Table State Tracking Grid (Shared High-Speed SPI Pogo-Pin Topology)]
• GPIO 11 (SCK) ================> Mat Pogo Header Line 1 ===> Linked to all 4 MFRC522 SCK
• GPIO 12 (MISO) ===============> Mat Pogo Header Line 2 ===> Linked to all 4 MFRC522 MISO
• GPIO 13 (MOSI) ===============> Mat Pogo Header Line 3 ===> Linked to all 4 MFRC522 MOSI
• GPIO 9 (RST) =================> Mat Pogo Header Line 4 ===> Tied globally to all 4 Reset Pins
• GPIO 18 (SS/CS Zone 1) =======> Mat Pogo Header Line 5 ===> Dedicated Chip Select Panel #1
• GPIO 19 (SS/CS Zone 2) =======> Mat Pogo Header Line 6 ===> Dedicated Chip Select Panel #2
• GPIO 20 (SS/CS Zone 3) =======> Mat Pogo Header Line 7 ===> Dedicated Chip Select Panel #3
• GPIO 21 (SS/CS Zone 4) =======> Mat Pogo Header Line 8 ===> Dedicated Chip Select Panel #4
