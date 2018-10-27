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


if __name__ == "__main__": # execute only if run as a script
	try:
		os.system('cls' if os.name == 'nt' else 'clear')
		os.system("cat monster.txt") # This is the easist way I know how to do this. CHANGE MY MIND
		monster.gpiosetup()
		mouth(.300)
		
		# End program cleanly with keyboard

	except KeyboardInterrupt: 
		GPIO.cleanup()
		print("\n[--EXIT--] Monster in a box complete")
		print("    Find more information about this project at")
		print("     [[ https://github.com/hevnsnt/monster ]]")
		print("")
