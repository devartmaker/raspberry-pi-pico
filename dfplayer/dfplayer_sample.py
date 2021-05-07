from machine import Pin
from sound import DFPlayer
from utime import sleep

df = DFPlayer(0, txPin=Pin(12), rxPin=Pin(13), volume=50)
while True:
    df.SetVolume(60)
    df.PlayNext()
    sleep(3)
    df.Stop()
    sleep(1)
    df.PlaySpecific(1) # play mp3/0001.mp3
    sleep(2)
