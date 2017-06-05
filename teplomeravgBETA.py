#AVG temp
#subor avgtemp.txt
#priecinok /pi/home/tmp
#update kazych 5 minut

#import requests
#import RPi.GPIO as GPIO
import time

from datetime import datetime

i=0

while True:
    sensorids=["28-00000883f6c2","28-00000884cf74"]
    sens='28-00000884cf74'
    if sens == '28-00000884cf74' :
        print('ok')

