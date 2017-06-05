import requests
import RPi.GPIO as GPIO
import time

from datetime import datetime

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

while True:
	time.strftime("%H:%M:%S:")
	now = datetime.now()
	sensorids = ["28-00000883f6c2","28-00000884cf74"]
	temperatures = [] 
	#avgtemperatures = []
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
			# Put the decimal point in the right place and display it.
			#temperatures.append(temperature / 1000)
			#avgtemperatures.append(sum(temperatures) / float(len(temperatures)))
			subor=open('test.txt', 'w+')
			subor.write(print ("okamzita teplota zo senzora " + sens + " je: ",temperature/1000))
            subor.close()




