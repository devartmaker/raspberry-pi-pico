from utime import sleep
from neopixel import Neopixel

pixels = Neopixel(10, 0, 16, "GRB")

while True:
    pixels.fill((0, 0, 0))
    pixels.show()
    sleep(0.25)
    pixels.set_pixel(0, (255, 0, 0))
    pixels.show()
    sleep(0.25)
    pixels.set_pixel(1, (0, 255, 0))
    pixels.show()
    sleep(0.25)
    pixels.set_pixel(2, (0, 0, 255))
    pixels.show()
    sleep(1)
    pixels.set_pixel_line(3, 9, (255, 0, 255))
    pixels.show()
    sleep(1)
    pixels.set_pixel_line_gradient(0, 9, (255, 0, 0), (0, 0, 255))
    pixels.show()
    sleep(1)
    for i in range(20):
        pixels.rotate_left(1)
        pixels.show()
        sleep(0.05)
    for i in range(20):
        pixels.rotate_right(2)
        pixels.show()
        sleep(0.05)