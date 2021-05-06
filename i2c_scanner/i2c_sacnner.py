from machine import Pin, I2C

i2c = I2C(0, sda=Pin(16), scl=Pin(17))
 
print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:', len(devices))
 
  for address in devices:  
    print("Decimal address: ", address, " | Hexa address: ", hex(address))
