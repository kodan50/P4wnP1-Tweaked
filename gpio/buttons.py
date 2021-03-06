#!/usr/bin/python

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time # Allows the use of delays to avoid output spamming and wasted CPU cycles
import os # This code will allow us to run terminal commands
GPIO.setmode(GPIO.BCM) # Just make sure this is set uniform to any other gpio scripts you run.

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set GPIO12 to be an input pin and set initial value to be pulled high.
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set GPIO14 same as above.

while True:
	if GPIO.input(4) == 0:
		print('Raspberry Pi is going for a power down now!')
		os.system("sudo shutdown -h now")
		time.sleep(2)
	if GPIO.input(12) == 0:
		print('Raspberry Pi is going for a reboot now!')
		os.system("sudo reboot")
		time.sleep(2)
	time.sleep(0.05) # This value represents how long the button has to be pressed to register. A lower value increases sensitivity to button presses at the cost of increased CPU usage.
