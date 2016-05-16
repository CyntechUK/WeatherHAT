# WeatherHAT

Turn your Raspberry Pi in to a handy weather display, perfect for showing weather at the moment, a day in advance or on an upcoming holiday!

The HAT comes with 7 super bright RGB LEDs, a large yellow sun, blue rain drops, white clouds/stars and a perfect yellow thunderstorm.Each LED can be dimmed or brightened giving some nice effects to the current weather. The HAT can also be used to create interactive games to provide an extra dimension of play.

The orientation of the HAT to look at means the Pi can be stood up on its side to be displayed nicely on a shelf or desk perfect for a quick glance at the forecast - Place next to the door so you know if you should grab the umbrella or the sun hat!


## Installation

At the moment the library is borrowing the ws2812 library from Pimoroni's UnicornHAT to drive the WS2812 RGB LEDs.

Ensure that i2c is enabled in raspi-config

    sudo raspi-config

Go down to Advanced Options, i2c and Enable, enable for boot also. Finish and reboot.

Install UnicornHAT library:

    sudo pip install unicornhat
    sudo apt-get install python-smbus

Get the current files:

    git clone https://github.com/CyntechUK/WeatherHAT.git
    cd WeatherHAT
    sudo python cycle.py

Run the cycle.py to enable a short demo of the LEDs

A friendlier Python library is current under construction and will be released soon!