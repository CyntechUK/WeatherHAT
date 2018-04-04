# Weather Display using Cyntech's WeatherHAT
#  by LeRoy Miller, (C) April 2018
# required libraries:
# weather-api (current version) https://pypi.python.org/pypi/weather-api/0.0.5
# install the WeatherHAT library following this guide
# https://github.com/CyntechUK/WeatherHAT
#
# This is still being tested, but appears to work.
# You need to change your location below either by City name, or Zip Code
# more information can be found on the weather-api site
#
# Most conditions are displayed - but not all (not sure how to display things like Haze and Fog
# For a list of Yahoo conditions:
# https://developer.yahoo.com/weather/documentation.html#codes

from weather import Weather
from weatherhat import WeatherHat
from time import sleep
from neopixel import *

wh = WeatherHat()
weather = Weather()
panel = Adafruit_NeoPixel(64,18,800000, 5, False, 50)
panel.begin()

wh.sun("start")
wh.sun("stop")
wh.cloud("start")
sleep(.5)
wh.cloud("stop")
wh.raining("start")
sleep(.5)
wh.raining("stop")
wh.storm("start")
sleep(.5)
wh.storm("stop")
wh.rainbow("start")
wh.rainbow("stop")

while True:
	#location = weather.lookup_by_location('dayton')
	location = weather.lookup(45042)
	condition = location.condition()
	print(condition.text())
	test = condition.text()
	#print "Rain" in test

#while True:
 	
	if "Rain" in test:
  	  wh.cloud("start")
  	  wh.raining("start")

	if "Snow" in test:
	  wh.cloud("start")
	  panel.setPixelColor(0,Color(255,255,255))
	  panel.setPixelColor(2,Color(255,255,255))
	  panel.setPixelColor(4,Color(255,255,255))
	  panel.setPixelColor(6,Color(255,255,255))
	  panel.show()
	  #wh.rainbow("start")

	if "Thunderstorms" in test:	
	  wh.cloud("start")
	  wh.raining("start")
	  wh.storm("start")

	if "Storm" in test:
	  wh.cloud("start")
	  wh.raining("start")
	  wh.storm("start")

	if "Sunny" in test:
	  wh.sun("start")

	#if "Hurrican" in test:
	#if "Tornado" in test:
	#if "Sleet" in test:

	if "Drizzle" in test:
	  wh.cloud("start")
	  wh.raining("start")

	if "Showers" in test:
	  wh.cloud("start")
	  wh.raining("start")

	#if "Hail" in test:
	#if "Dust" in test:
	#if "Fog" in test:
	#if "Haze" in test:

	if "Cloudy" in test:
	  wh.cloud("start")

	if "Not" in test:
	  wh.rainbow("start")

	sleep(60 * 5)

	wh.raining("stop")
	wh.cloud("stop")
	wh.storm("stop")
	wh.sun("stop")
	wh.rainbow("stop")
	panel.setPixelColor(0,Color(0,0,0))
	panel.setPixelColor(2,Color(0,0,0))
	panel.setPixelColor(4,Color(0,0,0))
	panel.setPixelColor(6,Color(0,0,0))
	panel.show()
