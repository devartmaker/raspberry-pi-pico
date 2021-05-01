from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=40000)
oled = SSD1306_I2C(128, 32, i2c)

oled.fill(0)
oled.text("Hi~", 0, 0)
oled.text("Dev.Art", 10, 10)
oled.show()
