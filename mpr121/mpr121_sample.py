from utime import sleep_ms
from machine import I2C, Pin
from mpr121 import MPR121

i2c = I2C(0, sda=Pin(16), scl=Pin(17))
sensor = MPR121(i2c)

while True:
    for i in range(12):
        if sensor.is_touched(i):
            print("Touched : ", i)
            sleep_ms(100)