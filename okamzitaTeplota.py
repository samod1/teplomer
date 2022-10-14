import requests
import RPi.GPIO as GPIO
import time
from datetime import datetime
temps=open('home/pi/tmp/acttemp.txt' ,'w+')

while True:

        sensorids = ["28-00000883f6c2","28-00000884cf74"]
        temperatures=[]
        now=datetime.now()

        temps.seek(0)
        lines=[]
        lines.append(str(now))
        for sens in sensorids:
		temperatures = []
		text = '';
		while text.split("\n")[0].find("YES") == -1 :
			# Open the file that we viewed earlier so that python can see what is in it. Replace the serial number as before.
			tfilename = "/sys/bus/w1/devices/" + sens +"/w1_slave"
			tfile = open(tfilename)
			# Read all of the text in the file.
			text = tfile.read()
			# Close the file now that the text has been read.
			tfile.close()
			time.sleep(0.1)
			# Split the text with new lines (\n) and select the second line.
			secondline = text.split("\n")[1]
			# Split the line into words, referring to the spaces, and select the 10th word (counting from 0).
			temperaturedata = secondline.split(" ")[9]
			# The first two characters are "t=", so get rid of those and convert the temperature from a string to a number.
			temperature = float(temperaturedata[2:])
			print("okamzita teplota zo senzora "+ sens+"je:",temperature/1000)
			lines.append(sens+ " "+str(temperature/1000))


	temps.write(lines[0])
	temps.write("\n")
	temps.write(lines[1])
	temps.write("\n")
	temps.write(lines[2])

	time.sleep(20)
	
	



temps.close()

