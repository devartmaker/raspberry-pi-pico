from utime import sleep
from machine import Pin
from tm1637 import TM1637

tm = TM1637(clk=Pin(17), dio=Pin(16))
count = 0

while True:
    # tm.number(count)
    tm.numbers(count, count, True)
    count += 1
    sleep(0.1)
