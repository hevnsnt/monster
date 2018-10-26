#!/usr/bin/python

# _   .-')                     .-') _   .-')    .-') _     ('-.  _  .-')   
#( '.( OO )_       v1.0      ( OO ) ) ( OO ). (  OO) )  _(  OO)( \( -O )  
# ,--.   ,--.).-'),-----. ,--./ ,--,' (_)---\_)/     '._(,------.,------.  
# |   `.'   |( OO'  .-.  '|   \ |  |\ /    _ | |'--...__)|  .---'|   /`. ' 
# |         |/   |  | |  ||    \|  | )\  :` `. '--.  .--'|  |    |  /  | | 
# |  |'.'|  |\_) |  |\|  ||  .     |/  '..`''.)   |  |  (|  '--. |  |_.' | 
# |  |   |  |  \ |  | |  ||  |\    |  .-._)   \   |  |   |  .--' |  .  '.' 
# |  |   |  |   `'  '-'  '|  | \   |  \       /   |  |   |  `---.|  |\  \  
# `--'   `--'     `-----' `--'  `--'   `-----'    `--'   `------'`--' '--' 
#                                                                 IN A BOX          
#
# Find more information about this project at
# https://github.com/hevnsnt/monster
# 
import pygame
import random
import RPi.GPIO as GPIO
import time
import os


def gpiosetup():
  '''Setup the GPIO pins, note this is written to support 4 relays on pins 14, 15, 18, and 23 of Raspi.
  However, you do not need to have a 4 relay board. If you only want to lift lid, connect just pin 14,
  if you want two 14 and 15 and so on. '''
  GPIO.setmode(GPIO.BCM)
  pinList = [14, 15, 18, 23] # These are Raspi GPIO numbers, Edit this if your setup is different.

  # loop through pins and set mode and state to 'HIGH' as Relays move from NC to NO when moved 'LOW' 
  for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)


def openLid():
  try:
    gpiosetup()
    print("")
    print("Jumping the Lid (Relay 1)")
    print("     [+] Up and Down")
    GPIO.output(14, GPIO.LOW)
    GPIO.output(14, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(14, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(14, GPIO.HIGH)
    time.sleep(2)
    print("     [+] Jumping Lid")

    for i in range(60):
      GPIO.output(14, GPIO.LOW)
      time.sleep(randTime())

      GPIO.output(14, GPIO.HIGH)
      time.sleep(randTime())
  # End program cleanly with keyboard
  except KeyboardInterrupt:
    print "  Quit"

def smoke():
  try:
    print("")
    print("Adding some smoke to the box:")
    print("     [+] Fog on")
    GPIO.output(15, GPIO.LOW)
    time.sleep(15)
    GPIO.output(15, GPIO.HIGH)
    print("     [+] Fog off")
  # End program cleanly with keyboard
  except KeyboardInterrupt:
    print "  Quit"


def monsterscream():
	smoke()
	print("     [+] Monster is ANGRY")
	pygame.mixer.music.stop()
	pygame.mixer.music.load("audio/Monster-scream.mp3")
	pygame.mixer.music.play(1)
	openLid()
	startmusic()

def randTime():
  '''This function returns a random time'''
  timeDelay = random.uniform(0.01, 0.5)
  return(timeDelay)

def minwait(min):
	time.sleep(min*30)


def startmusic():
	print("     [+] Playing monster sleeping sound")
	pygame.mixer.music.load("audio/monster-sleeping.mp3")
	pygame.mixer.music.play(-1)
	minwait(1)
  	monsterscream()


if __name__ == "__main__": # execute only if run as a script
	try:
		os.system("cat monster.txt") # This is the easist way I know how to do this. CHANGE MY MIND
		print("[+] Adjusting RaspberryPi Audio volume to 100%\n") #Set Raspi Audio Output all the way up
		os.system("amixer sset PCM,0 200%") #Set Raspi Audio Output all the way up
		gpiosetup() #Setup the GPIO pins
		pygame.mixer.init()
		print("Everything appears correct!")
		print("\n[+] Monster in a box is online")
		print("     [+] Waking up Monster...")
		startmusic()
		# End program cleanly with keyboard

	except KeyboardInterrupt: 
		GPIO.cleanup()
		print("\n[--EXIT--] Monster in a box complete")
		print("    Find more information about this project at")
		print("     [[ https://github.com/hevnsnt/monster ]]")
		print("")
