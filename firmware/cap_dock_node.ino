#include <WiFi.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include <SPI.h>
#include <MFRC522.h>

// Hardware Pin Framework
#define SPI_SCK      11
#define SPI_MISO     12
#define SPI_MOSI     13
#define RST_PIN      9

const int ZONE_COUNT = 4;
const int chipSelectPins[ZONE_COUNT] = {18, 19, 20, 21};
MFRC522 mfrc522[ZONE_COUNT];

// Local System Network Identifiers
const char* ssid = "Project_Monolith_Net";
const char* password = "BallisticCapture2026";

AsyncWebServer server(80);
AsyncWebSocket ws("/arena");

void onWsEvent(AsyncWebSocket *server, AsyncWebSocketClient *client, AwsEventType type, void *arg, uint8_t *data, size_t len) {
    // Captures structural feedback loops from the twin-screen controllers if necessary
}

void setup() {
    Serial.begin(115200);
    SPI.begin(SPI_SCK, SPI_MISO, SPI_MOSI, -1);

    // Structural Init for RFID Array Tracking Grid
    for (int i = 0; i < ZONE_COUNT; i++) {
        mfrc522[i].PCD_Init(chipSelectPins[i], RST_PIN);
    }

    // Provision Standalone Soft Access Point Topology
    WiFi.softAP(ssid, password);
    Serial.println("");
    Serial.print("Local Battle Arena Hotspot Active at IP: ");
    Serial.println(WiFi.softAPIP());

    // Register Network Telemetry Layer
    ws.onEvent(onWsEvent);
    server.addHandler(&ws);
    server.begin();
}

void loop() {
    ws.cleanupClients();

    for (int i = 0; i < ZONE_COUNT; i++) {
        if (mfrc522[i].PICC_IsNewCardPresent() && mfrc522[i].PICC_ReadCardSerial()) {
            String cardUID = "";
            for (byte b = 0; b < mfrc522[i].uid.size; b++) {
                cardUID += String(mfrc522[i].uid.uidByte[b] < 0x10 ? "0" : "");
                cardUID += String(mfrc522[i].uid.uidByte[b], HEX);
            }
            cardUID.toUpperCase();

            // Construct telemetry JSON payload
            String telemetryFrame = "{\"status\":\"IN_PLAY\",\"zone\":" + String(i + 1) + ",\"card_id\":\"" + cardUID + "\"}";

            // TARGET 1: Pipe Frame directly to PC via USB Serial Wire Link
            Serial.println(telemetryFrame);

            // TARGET 2: Broadcast Frame dynamically to Twin Phone App over Local Wi-Fi WebSocket
            ws.textAll(telemetryFrame);

            mfrc522[i].PICC_HaltA();
        }
    }
    delay(20); // Maintain rigid 50Hz polling cycle limit
}
