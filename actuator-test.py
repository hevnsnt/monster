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
# version 0.01

import RPi.GPIO as GPIO
import time
import os
import sys
import random

SleepTimeL = 2

def disclaimer():
  print("[/////////] Monster in a box test program ")
  print("")
  print("[-] It is expected that you have a RaspberryPi connected to a 4 Channel Relay via the following pins: ")
  print("    *  5v to VCC")
  print("    * GND to GND")
  print("    * GPIO14 to IN1")
  print("    * GPIO15 to IN2")
  print("    * GPIO18 to IN3")
  print("    * GPIO23 to IN4")
  print("")
  print("    !!--> Do not have anything connected to Relay Output <--!!")
  print("")
  print("            Audio testing will require speakers connected to audio jack or hdmi")
  print("                 and your output preferences properly set in raspi-config.")
  print ("")
  print(".                  WARNING -- DO NOT PROCEED IF NOT WIRED AS DESCRIBED")
  print(".                  YOU COULD DAMAGE YOUR RASPBERRYPI OR OTHER EQUIPMENT")
  print("")
  if raw_input("Please type 'I agree' to continue: ").upper() == "I AGREE":
    testone()
  else:
    print("Cancelling")
    return

def gpiosetup():
  GPIO.setmode(GPIO.BCM)

  # init list with GPIO numbers
  pinList = [14, 15, 18, 23]

  # loop through pins and set mode and state to 'high'
  for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

def randTime():
  timeDelay = random.uniform(0.01, 0.5)
  return(timeDelay)


def testone():
  try:
    gpiosetup()
    print("")
    time.sleep(2)
    print("Test One: Jumping relay one.")
    print("  [+] Up and Down")
    GPIO.output(14, GPIO.LOW)
    GPIO.output(14, GPIO.HIGH)
    print("  [+] Jumping relay one.")

    for i in range(30):
      GPIO.output(14, GPIO.LOW)
      time.sleep(randTime())

      GPIO.output(14, GPIO.HIGH)
      time.sleep(randTime())

  # End program cleanly with keyboard
  except KeyboardInterrupt:
    print "  Quit"


def testtwo():
  try:
    gpiosetup()
    print("")
    print("Test One: Jumping relay two.")
    for i in range(10):
      GPIO.output(15, GPIO.LOW)
      time.sleep(randTime())
      GPIO.output(15, GPIO.HIGH)
      time.sleep(randTime())

  # End program cleanly with keyboard
  except KeyboardInterrupt:
    print "  Quit"



if __name__ == "__main__": # execute only if run as a script
  try:
    if sys.argv[1] == "-s":
      testone()
    else:
      disclaimer()
    
    GPIO.cleanup()
    print("\n[--EXIT--] Testing complete")
    print("    Find more information about this project at")
    print("    https://github.com/hevnsnt/monster")
    print("")
  except KeyboardInterrupt:
    print "  Quit"
