import smbus
import time
import requests
import sys

bus = smbus.SMBus(1)

SLAVE_ADDRESS = 0x04

def request_reading():
    reading = int(bus.read_byte(SLAVE_ADDRESS))
    return reading

reading = request_reading()
print(reading)
sys.stdout.flush()
"""
while True:
    command = raw_input("Enter command: ")
    if command == 'l':
        bus.write_byte(SLAVE_ADDRESS, ord('l'))
    if command == 'r':
        thingspeak_get = 0
        while True:
            reading = request_reading()
            if thingspeak_get == 15:
                url = "https://api.thingspeak.com/update?api_key=REQ34H0DMYV3WYPV&field1=0"
                response = requests.request("GET", url)
                print response.text,
                print '        '
                thingspeak_get = 0
            time.sleep(1)
            thingspeak_get += 1
"""
