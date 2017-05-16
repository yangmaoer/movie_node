#!/usr/bin/python
# -*- coding:utf-8 -*-
import smbus
import time

address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)
while True:
    bus.write_byte(address, A0)
    value0 = bus.read_byte(address)
    print(value0 * 3.3 / 255)
    time.sleep(0.1)
    bus.write_byte(address, A1)
    value1 = bus.read_byte(address)
    print(value1 * 3.3 / 255)
    time.sleep(0.1)
