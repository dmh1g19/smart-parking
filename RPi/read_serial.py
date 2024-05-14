import serial
import time

serial_port = '/dev/ttyACM0'
baud_rate = 9600

try:
    ser = serial.Serial(serial_port, baud_rate)
    print(f"Connected to {serial_port}")
except:
    print(f"Error connection to serial port: {e}")
    exit(1)

while True:
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
    except KeyboardInterrupt:
        print("Exiting...")
        break
    except Exception as e:
        print(f"Error reading from serial port: {e}")

ser.close()

