from machine import Pin
from button import Button

count = 0

def on_click(pin):
    global count
    count += 1
    print(pin, count)

button = Pin(16, Pin.IN, Pin.PULL_DOWN)
Button(button, on_click)
