# Weather Display using Cyntech's WeatherHAT
#  by LeRoy Miller, (C) April 2018
# updated for Open Weather API Sep, 28 2020 LeRoy Miller (c) copywrite 2020
# required libraries:
# install the WeatherHAT library following this guide
# https://github.com/CyntechUK/WeatherHAT
#
# The Open Weather Map API example was found here:
# https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
# This code is based on the above work.
#
# This is still being tested, but appears to work.
# You need to change your location below either by City name, or Zip Code
# more information can be found on the weather-api site
#
# Most conditions are displayed - but not all (not sure how to display things like Haze and Fog
# For a list of Open Weather Map conditions:
# https://openweathermap.org/weather-conditions

from weatherhat import WeatherHat
from time import sleep
from neopixel import *
import requests, json 

# Enter your Open Weather Map API key here 
api_key = ""
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Dayton" 
#Examples of other citys (near me of course)
#city_name = "Dayton, OH, US" 
#city_name = "Cincinnati"
#city_name = "Middletown, OH, US"
#city_name = "Wilmington, OH, US"

#Below is the part of the URL you would change (if needed)
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

#By city ID
#complete_url = base_url + "appid=" + api_key + "&id=" + city_name

#By Zip code
#complete_url = base_url + "appid=" + api_key + "&zip=" + city_name

#By Latitude/Longitude (geographic coordinates)
#note two new variables are used lat and lon
#lat = "39.5352433"
#lon = "-84.3816072"
#complete_url = base_url + "appid=" + api_key + "&lat=" + lat + "&lon=" + lon



wh = WeatherHat()
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
sleep(.5)

while True:
	
	response = requests.get(complete_url)
	x = response.json()
	if x["cod"] != "404":
		y = x["main"]
		z = x["weather"]
		#test = z[0]["description"]
		test = z[0]["main"]
		print(test)

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

	if "Thunderstorm" in test:	
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

	if "Clouds" in test:
		wh.cloud("start")

	if "Not" in test:
		wh.rainbow("start")

	if "Clear" in test:
		wh.sun("start")

	sleep(60 * 5)

	wh.raining("stop")
	wh.cloud("stop")
	wh.storm("stop")
	wh.sun("stop")
	wh.rainbow("stop")
	sleep(2)
	panel.setPixelColor(0,Color(0,0,0))
	panel.setPixelColor(2,Color(0,0,0))
	panel.setPixelColor(4,Color(0,0,0))
	panel.setPixelColor(6,Color(0,0,0))
	panel.show()
