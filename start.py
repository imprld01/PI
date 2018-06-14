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

url = "https://api.thingspeak.com/update?api_key=REQ34H0DMYV3WYPV&field1=" + str(reading)
response = requests.request("GET", url)
print(response.text)
