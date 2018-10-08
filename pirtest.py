import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN)         #Read output from PIR motion sensor

while True:
	i=GPIO.input(18)
	if i==0:                 #When output from motion sensor is LOW
		print "No intruders",i
		GPIO.output(3, 0)  #Turn OFF 
	else:
		print("gottcha")