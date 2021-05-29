from machine import Pin
from dfplayer import DFPlayer
from utime import sleep

df = DFPlayer(0, txPin=Pin(16), rxPin=Pin(17), volume=50)

while True:
    df.SetVolume(60)
    df.PlayNext()
    sleep(3)
    df.Stop()
    sleep(1)
    df.PlayMp3Folder(1) # play mp3/0001.mp3
    sleep(5)
    df.PlayFolder(1, 2) # play 01/002.mp3
    sleep(5)
