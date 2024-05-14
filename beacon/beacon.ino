#include <bluefruit.h>
#include <Adafruit_NeoPixel.h>

#define MANUFACTURER_ID   0x004C // 0x004C is Apple

#define LED_PIN    8 // Neopixel pin
#define LED_COUNT 1
Adafruit_NeoPixel pixel(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

// AirLocate UUID: E2C56DB5-DFFB-48D2-B060-D0F5A71096E0
uint8_t beaconUuid[16] = 
{ 
  0xE2, 0xC5, 0x6D, 0xB5, 0xDF, 0xFB, 0x48, 0xD2, 
  0xB0, 0x60, 0xD0, 0xF5, 0xA7, 0x10, 0x96, 0xE0, 
};

// A Beacon packet consists of the following information: UUID, Major, Minor, RSSI @ 1M
BLEBeacon beacon(beaconUuid, 0x0001, 0x0000, -54);

void setupAdv(void)
{  
  Bluefruit.Advertising.setBeacon(beacon);

  // char* adv = Bluefruit.Advertising.getData();

  // There is no room left for 'Name' in the advertising packet
  // Use the optinal secondary Scan Response packet for 'Name' instead
  Bluefruit.ScanResponse.addName();
}

void neoPixelGreen() {
  pixel.setPixelColor(0, pixel.Color(0, 255, 0));
  pixel.show();
}

void neoPixelRed() {
  pixel.setPixelColor(0, pixel.Color(255, 0, 0));
  pixel.show();
  delay(100);
}

void setup() 
{
  Serial.begin(115200);

  pixel.begin(); // Initialize the NeoPixel
  pixel.show();  // Initialize all pixels to 'off'
  
  Bluefruit.begin();
  Bluefruit.setName("Parking_spot_1");
  beacon.setManufacturer(MANUFACTURER_ID);
  
  setupAdv();  // Setup the advertising packet
  Bluefruit.Advertising.setInterval(32, 244); // The range is 20ms to 10.24s, values in units of 0.625ms
  Bluefruit.Advertising.start();
}

void loop() 
{
  neoPixelGreen();
  digitalToggle(LED_BUILTIN);
  delay(100);
}
