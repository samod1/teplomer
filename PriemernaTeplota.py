import requests
import RPi.GPIO as GPIO
import time
from datetime import datetime

avgtemps=open('/home/pi/tmp/avgtemp.txt' , 'w+')
i=0

while True:
    sensorids=["28-00000883f6c2","28-00000884cf74"]
    temperatures = []
    now=datetime.now()
    avgtemperatures1=0
    avgtemperatures2=0
    temperatures1 = [5]
    temperatures2 = [5]

    avgtemps.seek(0)
    lines = []
    lines.append(str(now))
    i=i+1
    
    for sens in sensorids:
        text = '';
        while text.split("\n")[0].find("YES") == -1 :
            # Open the file that we viewed earlier so that python can see what is in it. Replace the serial number as before.
            tfilename = "/sys/bus/w1/devices/" + sens +"/w1_slave"
            tfile = open(tfilename)
            # Read all of the text in the file.
            text = tfile.read()
            # Close the file now that the text has been read.
            tfile.close()
            # Split the text with new lines (\n) and select the second line.
            secondline = text.split("\n")[1]
            # Split the line into words, referring to the spaces, and select the 10th word (counting from 0).
            temperaturedata = secondline.split(" ")[9]
            # The first two characters are "t=", so get rid of those and convert the temperature from a string to a number.
            temperature = float(temperaturedata[2:]) 
            if sens == '28-00000883f6c2':
               ##priradime teploty k senzoru 1
               temperatures1[i]=temperature/1000
               #count avg temperature
               avgtemperatures1= sum(temperatures1)/float((len(temperatures1)))
               #write avg value to the file
               avgtemps.write("28-00000883f6c2 " + str(avgtemperatures1))
            avgtemps.write("\n")
	    if sens == '28-00000884cf74':
                #priradime teplotu k senzoru 2
                temperatures2[i]=temperature/1000
                #vypocitame priemernu
                avgtemperatures2= sum(temperatures2)/float(len(temperatures2))
                #urobime vypis
                avgtemps.write("28-00000884cf74 " + str(avgtemperatures2))
    if i>4:
     i=0

    time.sleep(3)
    
avgtemps.close()
