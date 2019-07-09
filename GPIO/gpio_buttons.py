#!/usr/bin/python

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time # Allows the use of delays to avoid output spamming and wasted CPU cycles
import os # This code will allow us to run terminal commands
GPIO.setmode(GPIO.BCM) #  Setting this to board and doing a pin count was my preferred stance, but it did not work and this did. So score a point for this method.

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set GPIO12 to be an input pin and set initial value to be pulled high (on?)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set GPIO14 same as above.

while True:
	if GPIO.input(14) == 0:
		print('Raspberry Pi is going for a power down now!')
		os.system("sudo shutdown -h now")
	if GPIO.input(12) == 0:
		print('Raspberry Pi is going for a reboot now!')
		os.system("sudo reboot")
	time.sleep(0.05) # You may want to tweak this setting to suit your needs. A lower value increases sensitivity to button presses at the cost of CPU cycles.
