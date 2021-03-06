'''
Simple tool to change images into byte.
https://javl.github.io/image2cpp/
'''

import framebuf
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from framebuf import FrameBuffer

i2c = I2C(0, sda=Pin(16), scl=Pin(17))
oled = SSD1306_I2C(128, 64, i2c)

smile = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf8\x00\x00\x00\x00\x00\x00\x7f\xff\x00\x00\x00\x00\x00\x01\xff\xff\xc0\x00\x00\x00\x00\x07\xe0\x03\xf0\x00\x00\x00\x00\x0f\x80\x00\xf8\x00\x00\x00\x00\x1e\x00\x00\x3c\x00\x00\x00\x00\x38\x01\xc0\x0e\x00\x00\x00\x00\x70\x1e\x3c\x07\x00\x00\x00\x00\xe0\x60\x03\x03\x80\x00\x00\x00\xc1\x80\x00\xc1\x80\x00\x00\x01\xc3\x00\x00\x61\xc0\x00\x00\x01\x84\x00\x00\x10\xc0\x00\x00\x03\x08\x00\x00\x08\x60\x00\x00\x03\x18\x00\x00\x0c\x60\x00\x00\x02\x10\x00\x00\x04\x20\x00\x00\x06\x20\x00\x00\x02\x30\x00\x00\x06\x20\x00\x00\x02\x30\x00\x00\x06\x60\x00\x00\x03\x30\x00\x00\x06\x40\x00\x00\x01\x30\x00\x00\x04\x40\x00\x00\x01\x10\x00\x00\x04\x40\x00\x00\x01\x10\x00\x00\x06\x43\xc0\x01\xe1\x30\x00\x00\x06\x43\xe0\x03\xe1\x30\x00\x00\x06\x46\x30\x06\x31\x30\x00\x00\x02\x44\x10\x04\x11\x20\x00\x00\x02\x40\x00\x00\x01\x20\x00\x00\x03\x20\x00\x00\x02\x60\x00\x00\x01\x20\x00\x00\x02\x40\x00\x00\x01\xa0\x00\x00\x02\xc0\x00\x00\x00\x90\x00\x00\x04\x80\x00\x00\x00\xd8\x00\x00\x0d\x80\x00\x00\x00\x6c\x00\x00\x1b\x00\x00\x00\x00\x36\x00\x00\x36\x00\x00\x00\x00\x1b\x00\x00\x6c\x00\x00\x00\x00\x0f\x80\x00\xf8\x00\x00\x00\x00\x1f\xf0\x07\xfc\x00\x00\x00\x00\x38\x7f\xff\x0e\x00\x00\x00\x00\x30\x38\x0e\x06\x00\x00\x00\x00\x60\x1f\xfc\x03\x00\x00\x00\x00\x60\x08\x08\x03\x00\x00\x00\x00\x60\x0c\x18\x03\x00\x00\x00\x00\x60\x04\x10\x03\x00\x00\x00\x00\x60\x04\x10\x03\x00\x00\x00\x00\x20\x06\x30\x02\x00\x00\x00\x00\x30\x02\x20\x06\x00\x00\x00\x00\x30\x02\x20\x06\x00\x00\x00\x00\x18\x02\x20\x0c\x00\x00\x00\x00\x0c\x03\xe0\x18\x00\x00\x00\x00\x0c\x06\x30\x10\x00\x00\x00\x00\x03\x04\x10\x60\x00\x00\x00\x00\x01\x8c\x18\xc0\x00\x00\x00\x00\x00\x78\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
fb = FrameBuffer(smile, 64, 64, framebuf.MONO_HLSB)

oled.fill(0)
oled.text("Dev.Art", 10, 27)
oled.blit(fb, 64, 0)
oled.show()
