from smbus import SMBus
import gpiozero
import RPi.GPIO as rpi
from time import sleep
import threading
import unicornhat as unicorn
import math, colorsys

bus = 0



def frange(start, stop, step):
  i = start

  if (start < stop):
    while i <= stop:
      yield i
      i += step
      # For some reason, += doesn't always add an exact decimal, so we have to round the value
      i = round(i, 1)
  else:
    while i >= stop:
      yield i
      i += step
      # For some reason, += doesn't always add an exact decimal, so we have to round the value
      i = round(i, 1)

class WeatherHat(threading.Thread):

  def __init__(self):
    if rpi.RPI_REVISION == 1:
      i2c_bus = 0
    else:
      i2c_bus = 1

    self.bus = SMBus(i2c_bus)
    self.bus.write_i2c_block_data(0x54, 0x00, [0x01])
    self.bus.write_byte_data(0x54, 0x13, 0xFF)
    self.bus.write_byte_data(0x54, 0x14, 0xFF)
    self.bus.write_byte_data(0x54, 0x15, 0xFF)

    self.sun1 = gpiozero.PWMLED(4)
    self.sun2 = gpiozero.PWMLED(17)
    self.sun3 = gpiozero.PWMLED(27)



  def update(self):
     self.bus.write_byte_data(0x54, 0x16, 0xFF)


  def cleanup(self):
    self.bus.write_i2c_block_data(0x54, 0x00, [0x00])


  def rain1(self, value):
    self.bus.write_byte_data(0x54, 0x12, value)
    self.update()

  def rain2(self, value):
    self.bus.write_byte_data(0x54, 0x11, value)
    self.update()

  def rain3(self, value):
    self.bus.write_byte_data(0x54, 0x10, value)
    self.update()

  def rain4(self, value):
    self.bus.write_byte_data(0x54, 0x04, value)
    self.update()

  def rain5(self, value):
    self.bus.write_byte_data(0x54, 0x02, value)
    self.update()

  def rain6(self, value):
    self.bus.write_byte_data(0x54, 0x01, value)
    self.update()

  def storm1(self, value):
    self.bus.write_byte_data(0x54, 0x05, value)
    self.update()

  def storm2(self, value):
    self.bus.write_byte_data(0x54, 0x08, value)
    self.update()

  def storm3(self, value):
    self.bus.write_byte_data(0x54, 0x0A, value)
    self.update()

  def storm4(self, value):
    self.bus.write_byte_data(0x54, 0x06, value)
    self.update()

  def storm5(self, value):
    self.bus.write_byte_data(0x54, 0x09, value)
    self.update()

  def storm6(self, value):
    self.bus.write_byte_data(0x54, 0x0B, value)
    self.update()

  def cloud1(self, value):
    self.bus.write_byte_data(0x54, 0x0F, value)
    self.update()

  def cloud2(self, value):
    self.bus.write_byte_data(0x54, 0x0D, value)
    self.update()

  def cloud3(self, value):
    self.bus.write_byte_data(0x54, 0x0E, value)
    self.update()

  def cloud4(self, value):
    self.bus.write_byte_data(0x54, 0x0C, value)
    self.update()

  def cloud5(self, value):
    self.bus.write_byte_data(0x54, 0x07, value)
    self.update()

  def cloud6(self, value):
    self.bus.write_byte_data(0x54, 0x03, value)
    self.update()

  def sunled(self, part, value):
    if ( part == 1 ):
      self.sun1.value = value
    elif ( part == 2 ):
      self.sun2.value = value
    else:
      self.sun3.value = value





  def rainrun(self):
    while self.rainrunning == 1:
      k = 70
      j = 20
      for i in range(100,1,-1):
        if j == 1:
          j = 80
        if k == 1:
          k = 90

        self.rain3(j)
        self.rain2(i)
        sleep(0.005)
        self.rain5(i)
        sleep(0.005)
        sleep(0.005)
        self.rain4(j)

        self.rain1(k)
        sleep(0.005)
        self.rain6(k)
        k = k-1
        j = j-1

      self.rain1(0)
      self.rain2(0)
      self.rain3(0)
      self.rain4(0)
      self.rain5(0)
      self.rain6(0)



  def raining(self,action):
    if action == "start":
      self.rainrunning = 1
      threading.Thread(target = self.rainrun).start()
    if action == "stop":
      self.rainrunning = 0






  def cloudrun(self):
    while self.cloudrunning == 1:
      k = 70
      j = 20
      for i in range(60,1,-1):
        if j == 1:
          j = 20
        if k == 1:
          k = 50

        self.cloud1(j)
        self.cloud2(i)
        sleep(0.005)
        self.cloud3(i)
        sleep(0.005)
        sleep(0.005)
        self.cloud4(j)

        self.cloud5(k)
        sleep(0.005)
        self.cloud6(k)
        k = k-1
        j = j-1
  
      self.cloud1(0)
      self.cloud2(0)
      self.cloud3(0)
      self.cloud4(0)
      self.cloud5(0)
      self.cloud6(0)



  def cloud(self,action):
    if action == "start":
      self.cloudrunning = 1
      threading.Thread(target = self.cloudrun).start()
    if action == "stop":
      self.cloudrunning = 0



  def stormrun(self):
    while self.stormrunning == 1:
      for i in range(255,1,-1):
        self.storm6(i)
        self.storm5(i-20)
        self.storm4(i-40)
        self.storm3(i-60)
        self.storm2(i-80)
        self.storm1(i-100)
        sleep(0.005)

      self.storm1(0)
      self.storm2(0)
      self.storm3(0)
      self.storm4(0)
      self.storm5(0)
      self.storm6(0)

  def storm(self,action):
    if action == "start":
      self.stormrunning = 1
      threading.Thread(target = self.stormrun).start()
    if action == "stop":
      self.stormrunning = 0




  def sunrun(self):
    while self.sunrunning == 1:

      for i in frange(0.4,0.2,-0.1):
        self.sunled(3,i)
        self.sunled(1,i*2)
        self.sunled(2,i*1.5)
        sleep(0.1)

      self.sunled(1,0.0)
      self.sunled(2,0.0)
      self.sunled(3,0.0)


  def sun(self,action):
    if action == "start":
      self.sunrunning = 1
      threading.Thread(target = self.sunrun).start()
    if action == "stop":
      self.sunrunning = 0



  def rainbow(self):
    i = 0.0
    offset = 30
    count = 0
    while count < 300:
      i = i + 0.3
      for y in range(8):
        for x in range(8):
          r = 0#x * 32
          g = 0#y * 32
          xy = x + y / 4
          r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
          g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
          b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
          r = max(0, min(255, r + offset))
          g = max(0, min(255, g + offset))
          b = max(0, min(255, b + offset))
          unicorn.set_pixel(x,y,int(r),int(g),int(b))    
      unicorn.show()
      sleep(0.01)
      count = count + 1

    unicorn.clear()
    unicorn.show()
    