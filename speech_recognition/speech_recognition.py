from machine import Timer, UART, Pin
from utime   import sleep_ms

class SpeechRecognition :
    WAIT = (0xAA, 0x00)
    COMMON_MODE = (0xAA, 0x36)
    COMPACT_MODE = (0xAA, 0x37)
    RECORD1 = (0xAA, 0x11)
    RECORD2 = (0xAA, 0x12)
    RECORD3 = (0xAA, 0x13)
    IMPORT1 = (0xAA, 0x21)
    IMPORT2 = (0xAA, 0x22)
    IMPORT3 = (0xAA, 0x23)
    DELETE1 = (0xAA, 0x01)
    DELETE2 = (0xAA, 0x02)
    DELETE3 = (0xAA, 0x03)
    DELETE_ALL = (0xAA, 0x04)

    def __init__( self,
                  uartBus,
                  txPin: Pin,
                  rxPin: Pin,
                  callback= None) :

        self._uart = UART(uartBus, baudrate = 9600, tx=txPin, rx=rxPin)
        self._timer = Timer()
        self.isCommonMode = True
        self.callback = callback

        self.wait()

    def _tx_data(self, command):
        print("[Send]", command)
        self._uart.write(bytearray(command))
        sleep_ms(1000)

    def _rx_data(self):
        while self._uart.any() :
            if self.isCommonMode:
                c = self._uart.read()
                print(c.decode())
            else:
                c = self._uart.read(1)
                if c == b'\xcc':
                    print("Success")
                elif c == b'\xe0' or c == b'\xe1':
                    print("Error")
                elif c == b'\x11' or c == b'\x12' or c == b'\x13' or c == b'\x14' or c == b'\x15':
                    if self.callback != None:
                        self.callback(int.from_bytes(c, "big") - 6)
                elif c == b'\x21' or c == b'\x22' or c == b'\x23' or c == b'\x24' or c == b'\x25':
                    if self.callback != None:
                        self.callback(int.from_bytes(c, "big") - 6)
                elif c == b'\x31' or c == b'\x32' or c == b'\x33' or c == b'\x34' or c == b'\x35':
                    if self.callback != None:
                        self.callback(int.from_bytes(c, "big") - 6)
                else:
                    print(c)

    def wait(self):
        self._tx_data(SpeechRecognition.WAIT)

    def common_mode(self):
        self.isCommonMode = True
        self._tx_data(SpeechRecognition.COMMON_MODE)

    def compact_mode(self):
        self.isCommonMode = False
        self._tx_data(SpeechRecognition.COMPACT_MODE)

    def record(self, group):
        if group == 1:
            self._tx_data(SpeechRecognition.RECORD1)
        elif group == 2:
            self._tx_data(SpeechRecognition.RECORD2)
        elif group == 3:
            self._tx_data(SpeechRecognition.RECORD3)

    def listen(self, group):
        if group == 1:
            self._tx_data(SpeechRecognition.IMPORT1)
        elif group == 2:
            self._tx_data(SpeechRecognition.IMPORT2)
        elif group == 3:
            self._tx_data(SpeechRecognition.IMPORT3)
        
    
    def delete(self, group):
        if group == 1:
            self._tx_data(SpeechRecognition.DELETE1)
        elif group == 2:
            self._tx_data(SpeechRecognition.DELETE2)
        elif group == 3:
            self._tx_data(SpeechRecognition.DELETE3)

    def readData(self):
        self._rx_data()