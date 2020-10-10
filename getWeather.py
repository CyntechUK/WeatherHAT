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

#Set up the HAT hardware

wh = WeatherHat()
panel = Adafruit_NeoPixel(64,18,800000, 5, False, 50)
panel.begin()

# Set up the weather conditions, these are the ID values from https://openweathermap.org/weather-conditions
# Looking at the list of IDs is should be clear what is going on here.

#Rain
rainlo = 500
rainhi = 511

#Rain Shower
rainshowerlo = 520
rainshowerhi = 531

#Snow
snowlo = 600
snowhi = 611

#Snow Shower
snowshowerlo = 612
snowshowerhi = 622

#Thunderstorm
tstormlo = 200
tstormhi = 232

#Sunny or clear
sunlo = 800
sunhi = 800

#Drizzle
drizzlelo = 300
drizzlehi = 310

#Drizzle shower
drizzlesholo = 311
drizzleshohi = 321

#Scattered Clouds
cloudlo = 801
cloudhi = 802

#Overcast
overcastlo = 803
overcasthi = 804

#These conditions are unused at the moment but included for completeness.

#Mist
#mistlo = 701
#misthi = 701

#Smoke
#smokelo = 711
#smokehi = 711

#Haze
#hazelo = 721
#hazehi = 721

#Dust, sand/ dust whirls
#dust1lo = 731
#dust1hi = 731

#Fog
#foglo = 741
#foghi = 741

#Sand
#sandlo = 751
#sandhi = 751

#Dust
#dust2lo = 761
#dust2hi = 761

#Volcanic ash
#ashlo = 762
#ashhi = 762

#Squall - Showers ?
#squalllo = 771
#squallhi = 771

#Tornado
#tornadolo = 781
#tornadohi = 781

#Cycle the display at the start of the script

wh.sun("start")
sleep(.5)
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
sleep(.5)
wh.rainbow("stop")
sleep(1)

while True:
	
	response = requests.get(complete_url)
	x = response.json()
	if x["cod"] != "404":
		y = x["id"]
		z = x["weather"]
		test = z[0]["id"]
		print(test)

# Compare current weather to the rain list

	if test >= rainlo and test <= rainhi:
		wh.cloud("start")
		wh.raining("start")

# Compare current weather to the rain shower list

	if test >= rainshowerlo and test <= rainshowerhi:
		wh.cloud("start")
		wh.raining("start")
		wh.rainbow("start")
   
# Compare current weather to the snow list

	if test >= snowlo and test <= snowhi:
		wh.cloud("start")
		panel.setPixelColor(0,Color(255,255,255))
		panel.setPixelColor(2,Color(255,255,255))
		panel.setPixelColor(4,Color(255,255,255))
		panel.setPixelColor(6,Color(255,255,255))
		panel.show()
	
# Compare current weather to the snow shower list

	if test >= snowshowerlo and test <= snowshowerhi:
		wh.cloud("start")
		panel.setPixelColor(0,Color(255,255,255))
		panel.setPixelColor(2,Color(255,255,255))
		panel.setPixelColor(4,Color(255,255,255))
		panel.setPixelColor(6,Color(255,255,255))
		panel.show()
		wh.rainbow("start")
	
# Compare current weather to the thunderstorm list
		
	if test >= tstormlo and test <= tstormhi:
		wh.cloud("start")
		wh.raining("start")
		wh.storm("start")

# Compare current weather to the sunny list

	if test >= sunlo and test <= sunhi:
		wh.sun("start")

# Compare current weather to the drizzle list	
		
	if test >= drizzlelo and test <= drizzlehi:	
		wh.cloud("start")
		wh.raining("start")	
		
		# Compare current weather to the drizzle shower list	
		
	if test >= drizzlesholo and test <= drizzleshohi:	
		wh.cloud("start")
		wh.raining("start")	

# Compare current weather to the scattered clouds list	

	if test >= cloudlo and test <= cloudhi:	
		wh.cloud("start")
		wh.sun("start")

# Compare current weather to the overcast list	

	if test >= overcastlo and test <= overcasthi:	
		wh.cloud("start")


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