import smbus
import time
import requests
import sys
import struct

bus = smbus.SMBus(1)

SLAVE_ADDRESS = 0x04

def get_data():
    return bus.read_i2c_block_data(SLAVE_ADDRESS, 0);

def get_float(data, index):
    bytes = data[4*index:(index+1)*4]
    return struct.unpack('f', "".join(map(chr, bytes)))[0]

def request_reading():
    data = get_data()
    return get_float(data, 0)

while True:

    reading = request_reading()
    print(reading)
    sys.stdout.flush()

    #url = "https://api.thingspeak.com/update?api_key=REQ34H0DMYV3WYPV&field1=" + str(reading)
    #response = requests.request("GET", url)
    
    reading = 0.0
    
    time.sleep(0.5);
