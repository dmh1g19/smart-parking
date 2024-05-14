from bluepy.btle import Scanner, DefaultDelegate
from mkr_wan_1300_connect import Sender 
import json

'''
    Detects the broadcast from the nRF52840 feather board (acting as an iBeacon)
    Data is sent to the MKR WAN 1300 as a JSON
'''

# For now only detect one bluetooth beacon (single parking spot)

PORT = "/dev/ttyACM0"
RATE = 9600
TIME_OUT = 1
ADTYPE = 255
SCAN_RATE = 10.0
PARKING_01_UUID = "4c000215e2c56db5dffb48d2b060d0f5a71096e0"

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

sender = Sender(PORT, RATE, TIME_OUT)

scanner = Scanner().withDelegate(ScanDelegate())
found = False
while found == False:
    print("Scanning...")
    devices = scanner.scan(SCAN_RATE)

    for dev in devices:
        #print(f"Device {dev.addr} ({dev.addrType}), RSSI={dev.rssi} dB")
    
        for (adtype, desc, value) in dev.getScanData():
            #print(f"{desc}: {value}")
            if adtype == ADTYPE:
                if value.startswith(PARKING_01_UUID):
                    print(f"Beacon found! Device {dev.addr} ({dev.addrType})")
                    print(f"SSI={dev.rssi} dB")
                    print(f"Name: {dev.getValueText(9)}")

                    db = int(f"{dev.rssi}"[1:])
                    name = str(f"{dev.getValueText(9)}")
                    state = "0"

                    sender.connect()

                    if db <= 55:
                        state = "0"
                    else:
                        state = "1"
                        
                    data = {
                        "name": name,
                        "ssi": db,
                        "state": state

                    }
                    json_string = json.dumps(data)
                    sender.send(json_string)

                    found = True
