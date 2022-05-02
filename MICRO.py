import time
from machine import Pin, SPI

led=Pin(25,Pin.OUT)        #create LED object from pin13,Set Pin13 to output
spi = SPI(1, 100000)       # Default assignment: sck=Pin(10), mosi=Pin(11), miso=Pin(8)
ss = Pin(9, Pin.OUT) 

while True:
  led.value(1)            #Set led turn on
  time.sleep(0.5)
  ss.off()
  spi.write(b'62345')     # write 5 bytes on MOSI
  ss.on()
  led.value(0)            #Set led turn off
  time.sleep(0.5)
  ss.off()
  spi.write(b'62345')     # write 5 bytes on MOSI
  ss.on()



