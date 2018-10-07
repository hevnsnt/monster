#!/usr/bin/python
#
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

import RPi.GPIO as GPIO
import time

SleepTimeL = 2

def disclaimer():
  print("[-] Monster in a box test program ")
  print("")
  print("[-] It is expected that you have a RaspberryPi connected to a 4 Channel Relay via the following pins: ")
  print("    *  5v to VCC")
  print("    * GND to GND")
  print("    * GPIO14 to IN1")
  print("    * GPIO15 to IN2")
  print("    * GPIO18 to IN3")
  print("    * GPIO23 to IN4")
  print("")
  print("    --> Do not have anything connected to Relay Output <--")
  print("")
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
  


def testone():
  try:
    gpiosetup()
    print("")
    print("Test One: Turning each relay on, then turning all off ")
    GPIO.output(14, GPIO.LOW)
    print "Testing Relay : ONE"
    time.sleep(SleepTimeL); 
    GPIO.output(15, GPIO.LOW)
    print "Testing Relay : TWO"
    time.sleep(SleepTimeL);  
    GPIO.output(18, GPIO.LOW)
    print "Testing Relay : THREE"
    time.sleep(SleepTimeL);
    GPIO.output(23, GPIO.LOW)
    print "Testing Relay : FOUR"
    time.sleep(SleepTimeL);
    print "Turning all off"
    GPIO.cleanup()
    time.sleep(SleepTimeL);
    print "Test One completed."
    testtwo()

  # End program cleanly with keyboard
  except KeyboardInterrupt:
    print "  Quit"


def testtwo():
  try:
    gpiosetup()
    print("")
    print("Test Two: Turning each relay on then off")
    GPIO.output(14, GPIO.LOW)
    print "Testing Relay : ONE"
    time.sleep(SleepTimeL); 
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(15, GPIO.LOW)
    print "Testing Relay : TWO"
    time.sleep(SleepTimeL);  
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    print "Testing Relay : THREE"
    time.sleep(SleepTimeL);
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    print "Testing Relay : FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(23, GPIO.HIGH)
    GPIO.cleanup()
    print "Test completed."

  # End program cleanly with keyboard
  except KeyboardInterrupt:
    print "  Quit"


if __name__ == "__main__": # execute only if run as a script
  disclaimer()
