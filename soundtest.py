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


def seckc():
    pygame.mixer.music.stop()
    while True:
    	sounda.play()
    startmusic()


def getrandom():
	rand = random.randint(1,10111)
	return rand
	#

def randt():
	i = 1
	while True:
		i = getrandom()
		if i < 230:
			print(str(i) + " is lower than 230!")
			seckc()
		else:
			time.sleep(2)

def startmusic():
	pygame.mixer.music.load("audio/IDGAFOS3.0.mp3")
	pygame.mixer.music.play(-1)
  	randt()




if __name__ == "__main__": # execute only if run as a script
  pygame.mixer.init()
  sounda = pygame.mixer.Sound("audio/seckc.mp3")
  startmusic()

  print("\n[/////////] Testing complete")
  print("    Find more information about this project at")
  print("    https://github.com/hevnsnt/monster")
  print("")
