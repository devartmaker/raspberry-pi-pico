from utime import sleep
from lcd_i2c import LCD
from machine import I2C, Pin

i2c = I2C(0, sda=Pin(16), scl=Pin(17))
lcd = LCD(i2c, 0x3f, 2, 16)

while True:
    lcd.putstr("Hello world")
    lcd.move_to(0, 1)
    lcd.putstr("My name is Pico")

    sleep(1)
    lcd.clear()
    sleep(1)