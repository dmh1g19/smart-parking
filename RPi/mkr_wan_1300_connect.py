import serial
import time

'''
    Connects to the MKR WAN 1300 via serial USB, and sends parking spot information to TTN (The things network)
'''

class Sender:
    def __init__(self, port, throughput, timeout):
        self.port = port
        self.throughput = throughput
        self.timeout = timeout
        self.ser = None

    def connect(self):
        self.ser = serial.Serial(self.port, self.throughput, timeout=self.timeout) # the 9600 is the throughput for the serial link
        self.ser.flush()
        print("Connection sequence complete.")

    def send(self, s):
        self.ser.flush()
        msg = s
        self.ser.write(f"{msg}\n".encode('utf-8'))
        print("Sending sequence completed.")

