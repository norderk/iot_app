#### ABOUT THE PROJECT
This project uses several different buildingblocks with a singe purpose, home automation. On a base level there is a raspberrypie running a docker container with a zigbee2mqtt client. This client relays commands wia an antenna(radio) allowing the user to control different endpoints. The user interface is a web application built in Django. In an effort to make the application asyncrones and to handle input from multiple sources the messegebroker RabbitMQ is used together with Celery(integrated with django). My aim is to make this an open source project I would love for others to copy share and use the code base.


#### BUILT WITH

* SW <br>
    - Python 3.10<br>
    - JavaScript<br>
    - HTML<br>
    - SCSS<br>
    - Docker<br>

* HW <br>
    - Raspberry Pi Zero 2<br>
    - Micro SSD-card   -->   Raspbian GNU/Linux 11 (bullseye)<br>
    - Sonoff, Zigbee-3.0-USB-Dongle-Plus<br>
    - Philips Hue light-strip<br>
    - Philips Hue lightbulbs<br>

#### GETTING STARTED
Setup a remote server

#### INSTALLATION
As always we start by standing on the shoulders of others! Or why invent the wheel! <br>
Here is a tutorial for getting started with Eclipse Mosquitto and Zigbee2mqtt with the help of Docker and docker-compose: https://github.com/docker/docker-install 
#### USAGE