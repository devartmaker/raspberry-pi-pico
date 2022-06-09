from utime import sleep
from ds3231 import ds3231
rtc = ds3231()
rtc.set_time('13:45:50,Monday,2022-14-00')

while True:
    now = rtc.read_time()
    print(now)
    sleep(1)