from lcd_i2c import LCD
from machine import I2C, Pin
from utime import sleep

i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=400000)
lcd = LCD(i2c, 0x3f, 2, 16)

customChar = [
  0x1F,
  0x05,
  0x00,
  0x1F,
  0x04,
  0x1F,
  0x11,
  0x1F
]
lcd.custom_char(0, bytearray(customChar))

while True:
    lcd.clear()
    for i in range(16):
        lcd.move_to(i, 0)
        lcd.putchar(chr(0))
        sleep(0.1)