import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)         #Read output from PIR motion sensor

while True:
	i=GPIO.input(12)
	if i==0:                 #When output from motion sensor is LOW
		print "No intruders",i
	else:
		print("gottcha")