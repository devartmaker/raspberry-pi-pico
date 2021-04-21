from machine import Pin
from sound import DFPlayer
from utime import sleep

df = DFPlayer(0, Pin(0), Pin(1), volume=50)
while True:
    df.SetVolume(60)
    df.PlayNext()
    sleep(3)
    df.Stop()
    sleep(1)
    df.PlayFolder(1)
    sleep(2)
