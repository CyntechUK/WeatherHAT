from weatherhat import WeatherHat
from time import sleep

wh = WeatherHat()

while True:
  wh.sun("start")
  sleep(5)
  wh.cloud("start")
  sleep(5)
  wh.raining("start")
  wh.sun("stop")
  sleep(10)
  wh.storm("start")
  sleep(10)
  wh.storm("stop")
  sleep(5)
  wh.raining("stop")
  sleep(3)
  wh.sun("start")
  wh.cloud("stop")
  wh.rainbow()
  
  sleep(10)