import utime
from machine import Pin

class Button:
    """
    Debounced pin handler
    usage e.g.:
    def button_callback(pin):
        print("Button (%s) changed to: %r" % (pin, pin.value()))
    button_handler = Button(Pin(32, mode=Pin.IN, pull=Pin.PULL_DOWN), button_callback)
    """

    def __init__(self, pin: Pin, callback, trigger: int=Pin.IRQ_FALLING, min_ago: int=300):
        self.callback = callback
        self.min_ago = min_ago

        self._blocked = False
        self._next_call = utime.ticks_ms() + self.min_ago

        pin.irq(self.debounce_handler, trigger)

    def call_callback(self, pin: Pin):
        self.callback(pin)

    def debounce_handler(self, pin):
        if utime.ticks_ms() > self._next_call:
            self._next_call = utime.ticks_ms() + self.min_ago
            self.call_callback(pin)
