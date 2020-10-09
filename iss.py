# ISS Display using Cyntech's WeatherHAT
#  by LeRoy Miller, (C) April 2020
# 
# required libraries:
# install the WeatherHAT library following this guide
# https://github.com/CyntechUK/WeatherHAT
#
# Change the latitude and longitude to your location
# Does not need to be excate, close will work
# This uses the open-notify.org api to get the ISS current location.
# it then calculates how far it is from you, and displays when it is close on the rainbow display.
# red is on the horizon, yellow you maybe able to hear it with the right radio.
# Green (3 top leds) it is close overhead or near overhead
# calculated in Miles
# Based on the EricISSnotification sketch from
# https://github.com/kd8bxp/Simple-ISS-Notification-System

from weatherhat import WeatherHat
from time import sleep
from neopixel import *
import requests, json 
import math

complete_url = "http://api.open-notify.org/iss-now.json"

mylat = 39.5352433
mylon = -84.3816072

def deg2rad(n):
    return (n*71)/4068

def rad2deg(n):
    return (n*4068)/71

def clearPixels():
    panel.setPixelColor(0,Color(0,0,0))
    panel.setPixelColor(1,Color(0,0,0))
    panel.setPixelColor(2,Color(0,0,0))
    panel.setPixelColor(3,Color(0,0,0))
    panel.setPixelColor(4,Color(0,0,0))
    panel.setPixelColor(5,Color(0,0,0))
    panel.setPixelColor(6,Color(0,0,0))
    panel.show()

wh = WeatherHat()
panel = Adafruit_NeoPixel(64,18,800000, 5, False, 50)
panel.begin()

wh.sun("start")
wh.sun("stop")
wh.cloud("start")
sleep(.05)
wh.cloud("stop")
wh.raining("start")
sleep(.05)
wh.raining("stop")
wh.storm("start")
sleep(.05)
wh.storm("stop")
wh.rainbow("start")
wh.rainbow("stop")
sleep(.5)

while True:
	
	response = requests.get(complete_url)
	x = response.json()
	isslat = float(x["iss_position"]["latitude"])
	isslon = float(x["iss_position"]["longitude"])
	theta = mylon - isslon
	dist = math.sin(deg2rad(mylat)) * math.sin(deg2rad(isslat)) + math.cos(deg2rad(mylat)) * math.cos(deg2rad(isslat)) * math.cos(deg2rad(theta))
	dist = math.acos(dist)
	dist = rad2deg(dist)
	miles = dist * 60 * 1.1515
	distance = int(miles)
	print(distance)

if distance <= 1350 and distance >= 1201:
	clearPixels()
	panel.setPixelColor(0,Color(255,255,255))
	panel.setPixelColor(6,Color(255,255,255))
	panel.show()

if distance <=1200 and distance >=1151:
	clearPixels()
	panel.setPixelColor(1,Color(255,153,0))
	panel.setPixelColor(5,Color(255,153,0))
	panel.show()

if distance <=1150 and distance >= 951:
	clearPixels()
	panel.setPixelColor(2,Color(0,255,0))
	panel.setPixelColor(4,Color(0,255,0))
	panel.show()

if distance <= 950:
	clearPixels()
	panel.setPixelColor(3,Color(0,255,0))
	panel.show()

if distance >= 1351:
	clearPixels()

sleep(1)
