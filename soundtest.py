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
	print("     [+] Playing Interrupt")
	pygame.mixer.music.stop()
	pygame.mixer.music.load("audio/seckc.mp3")
	pygame.mixer.music.play(1)
	minwait(1)
	startmusic()


def getrandom():
	rand = random.randint(1,10111)
	return rand

def randt():
	i = 1
	while True:
		i = getrandom()
		if i < 230:
			print(str(i) + " is lower than 230!")
			seckc()
		else:
			time.sleep(2)

def minwait(min):
	time.sleep(min*30)


def startmusic():
	print("     [+] Playing background sound")
	pygame.mixer.music.load("audio/IDGAFOS3.0.mp3")
	pygame.mixer.music.play(-1)
	minwait(1)
  	seckc()


if __name__ == "__main__": # execute only if run as a script
	try:
		pygame.mixer.init()
		print("Starting Sound Test:")
		print("     [+] Starting Music")
		startmusic()
		# End program cleanly with keyboard

	except KeyboardInterrupt: 
		print("\n[--EXIT--] Testing complete")
		print("    Find more information about this project at")
		print("    https://github.com/hevnsnt/monster")
		print("")
