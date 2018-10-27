#!/usr/bin/python

# _   .-')                     .-') _   .-')    .-') _     ('-.  _  .-')   
#( '.( OO )_                 ( OO ) ) ( OO ). (  OO) )  _(  OO)( \( -O )  
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
import RPi.GPIO as GPIO
import time
import os, sys, monster

def mouth(opentime):
  '''This function moves the mouth up and down'''
  GPIO.output(14, GPIO.LOW)
  time.sleep(opentime)
  GPIO.output(14, GPIO.HIGH)
  time.sleep(0.1)


def halloween():
  mouth(.353)
  print("one")
  mouth(.286)
  print("one")
  mouth(.329)
  print("one")
  mouth(.351)
  print("one")
  mouth(.873)
  print("one")
  mouth(.290)
  print("one")
  mouth(.241)
  print("one")
  mouth(.291)
  print("one")
  mouth(.230)
  print("one")
  mouth(2.334)
  print("done")




if __name__ == "__main__": # execute only if run as a script
	try:
		os.system('cls' if os.name == 'nt' else 'clear')
		os.system("cat monster.txt") # This is the easist way I know how to do this. CHANGE MY MIND
		monster.gpiosetup()
		pygame.mixer.init()
		pygame.mixer.music.load("audio/Happy_Halloween.mp3")
		pygame.mixer.music.play(-1)
		time.sleep(1.286)
		halloween()
		GPIO.cleanup()
		# End program cleanly with keyboard

	except KeyboardInterrupt: 
		GPIO.cleanup()
		print("\n[--EXIT--] Monster in a box complete")
		print("    Find more information about this project at")
		print("     [[ https://github.com/hevnsnt/monster ]]")
		print("")
