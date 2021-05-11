from machine import Pin
from speech_recognition import SpeechRecognition

speech = SpeechRecognition(0, rxPin=Pin(17), txPin=Pin(16))

speech.common_mode()
speech.delete(1)
speech.record(1)

while True:
    speech.readData()
