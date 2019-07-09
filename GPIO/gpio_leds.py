#!/usr/bin/python

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time # This will let us to blink the LEDs at different speeds.
import os # This code will allow us to run terminal commands

GPIO.setmode(GPIO.BCM)

LEDRed = 16
LEDGreen = 20
LEDBlue = 21

GPIO.setup(LEDRed, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LEDGreen, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(LEDBlue, GPIO.OUT, initial=GPIO.LOW)

# The red LED will light when the Raspberry Pi is ready to be powered down.
# The Green LED will light when the unit is running idle and, in theory, not currently processing anything.
# The Blue LED will light when we use led_blink instead of using the onboard LED to indicate this.

# Indentation is broken beyond repair.
# We need to decide on a blink patterns.
# I am thinking if blinkled is between 1 and 5, we can blink the blue LED.
# If blinkled is between 6 and 10, blink the red LED.
# Do we want to alternate blue and red if there is a problem?

blink = 11

try:
	while True:
		if blink > 10:
			GPIO.output(LEDRed, GPIO.HIGH)
			GPIO.output(LEDGreen, GPIO.LOW)
			GPIO.output(LEDBlue, GPIO.LOW)
			time.sleep(0.5)
			GPIO.output(LEDRed, GPIO.LOW)
			GPIO.output(LEDGreen, GPIO.LOW)
			GPIO.output(LEDBlue, GPIO.HIGH)
			time.sleep(0.5)
		elif blink > 5:
			GPIO.output(LEDRed, GPIO.HIGH)
			GPIO.output(LEDGreen, GPIO.LOW)
			GPIO.output(LEDBlue, GPIO.LOW)
			time.sleep(0.5)
			GPIO.output(LEDRed, GPIO.LOW)
			GPIO.output(LEDGreen, GPIO.LOW)
			GPIO.output(LEDBlue, GPIO.LOW)
			time.sleep(0.5)
		elif blink > 0:
			GPIO.output(LEDRed, GPIO.LOW)
			GPIO.output(LEDGreen, GPIO.LOW)
			GPIO.output(LEDBlue, GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(LEDRed, GPIO.LOW)
			GPIO.output(LEDGreen, GPIO.LOW)
			GPIO.output(LEDBlue, GPIO.LOW)
			time.sleep(0.5)
		elif blink == 0:
			GPIO.output(LEDRed, GPIO.LOW)
			GPIO.output(LEDGreen, GPIO.HIGH)
			GPIO.output(LEDBlue, GPIO.LOW)
except KeyboardInterrupt:
	print('interrupted!')
	GPIO.cleanup()
