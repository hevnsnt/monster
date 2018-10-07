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

GPIO.setmode(GPIO.BCM)

# init list with GPIO numbers

pinList = [14, 15, 18, 23]

# loop through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 2

# main loop

try:
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
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

#if __name__ == "__main__": # execute only if run as a script
#  domains, lnames, female, male = loadArray()
#  for x in range(int(argv[1])):
#    print getName()

