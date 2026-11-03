#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>

#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"

const int MAGNET_PINS[4] = {4, 5, 6, 7};
const int COIL_SENSOR_PINS[4] = {11, 12, 13, 14};

class MatHardwareController {
public:
    void init() {
        for(int i=0; i<4; i++) {
            pinMode(MAGNET_PINS[i], OUTPUT);
            digitalWrite(MAGNET_PINS[i], LOW);
            pinMode(COIL_SENSOR_PINS[i], INPUT);
        }
    }
    void setMagnetState(int zoneIndex, int state) {
        if(zoneIndex >= 0 && zoneIndex < 4) {
            digitalWrite(MAGNET_PINS[zoneIndex], state ? HIGH : LOW);
        }
    }
};

MatHardwareController matControl;

class WirelessCommandCallbacks: public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *pCharacteristic) {
        std::string value = pCharacteristic->getValue();
        if (value.length() == 3 && value[0] == 0xAA) {
            matControl.setMagnetState(value[1] - 1, value[2]);
        }
    }
};

void setup() {
    matControl.init();
    BLEDevice::init("Smart_Playing_Mat_Array");
    BLEServer *pServer = BLEDevice::createServer();
    BLEService *pService = pServer->createService(SERVICE_UUID);
    BLECharacteristic *pCharacteristic = pService->createCharacteristic(CHARACTERISTIC_UUID, BLECharacteristic::PROPERTY_WRITE);
    pCharacteristic->setCallbacks(new WirelessCommandCallbacks());
    pService->start();
    BLEDevice::getAdvertising()->start();
}

void loop() {
    delay(100);
}
