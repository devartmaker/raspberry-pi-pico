from utime import sleep
from servo import Servo

motor = Servo(26)

while True:
    motor.move(0)
    sleep(1)
    motor.move(180)
    sleep(1)