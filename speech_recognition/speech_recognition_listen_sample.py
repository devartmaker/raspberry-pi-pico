from machine import Pin
from speech_recognition import SpeechRecognition

def onReceivce(index):
    print(index)

speech = SpeechRecognition(0, rxPin=Pin(17), txPin=Pin(16), callback=onReceivce)

speech.compact_mode()
speech.listen(1)

while True:
    speech.readData()
