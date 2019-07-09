#!/usr/bin/env python
import RPi.GPIO as GPIO

# We may have to change this to BCM to make it consistent with our reset buttons.
GPIO.setmode(GPIO.BCM)

# three pins for 8 payloads.
pins = [15,18,23]

#Looks like we are going for the "Run these to ground" method.
for pin in pins:
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

output = ''

# I can't test this right now, but I suspect this will only add enabled pins, so up to three options.
# This will probably need to be rewritten.
for pin in pins:

	if not GPIO.input(pin):
		output+= '1'
	else:
		output += '0'

output = output[::-1]
print(output)
