import json
import serial
import time
import tkinter as tk
from threading import Thread

# Configured to interface with the PC serial footprint
SERIAL_PORT = "COM3"  # Adjust target identifier based on device management assignment
BAUD_RATE = 115200

# Simulated Local Database Card Matching Registry
CARD_DATABASE = {
    "04A2B9C8": {"name": "Blue-Eyes White Dragon", "type": "Monster", "atk": 3000},
    "15E3F0A1": {"name": "Black Luster Soldier", "type": "Monster", "atk": 3000},
    "88C4D2F9": {"name": "Pot of Greed", "type": "Spell", "atk": "N/A"}
}

class MonolithOverlayApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Project Monolith Remote Overlay System")
        self.window.geometry("450x200")
        self.window.configure(bg="#111111")
        
        # Transparent UI Anchor for Overlay Capture Pipelines
        self.zone_labels = []
        for i in range(4):
            lbl = tk.Label(window, text=f"Zone {i+1}: Empty Table State", 
                           fg="#777777", bg="#111111", font=("Arial", 12, "bold"))
            lbl.pack(pady=5)
            self.zone_labels.append(lbl)

    def update_zone(self, zone_idx, card_id):
        if card_id in CARD_DATABASE:
            card_info = CARD_DATABASE[card_id]
            display_text = f"Zone {zone_idx}: {card_info['name']} [ATK: {card_info['atk']}]"
            color = "#00FF66" # Neon green execution marker for active play tracking
        else:
            display_text = f"Zone {zone_idx}: Unknown Card Scan [{card_id}]"
            color = "#FFCC00"
            
        self.zone_labels[zone_idx - 1].config(text=display_text, fg=color)

def serial_reader_worker(app):
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Tracking Data Stream on {SERIAL_PORT}...")
        while True:
            if ser.in_waiting:
                raw_line = ser.readline().decode('utf-8').strip()
                try:
                    data = json.loads(raw_line)
                    if data.get("status") == "IN_PLAY":
                        zone = int(data.get("zone"))
                        card_id = data.get("card_id")
                        # Push cross-thread telemetry block directly to UI update frame
                        app.window.after(0, app.update_zone, zone, card_id)
                except ValueError:
                    pass # Suppress incomplete line artifacts
            time.sleep(0.01)
    except Exception as e:
        print(f"Serial Interface Network Disconnected: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    overlay_app = MonolithOverlayApp(root)
    
    # Fire off background worker to parse the incoming USB streams asynchronously
    comm_thread = Thread(target=serial_reader_worker, args=(overlay_app,), daemon=True)
    comm_thread.start()
    
    root.mainloop()
