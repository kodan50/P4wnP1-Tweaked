#!/usr/bin/python

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import os
import pwd
import grp


GPIO.setmode(GPIO.BCM)

filepath = "/tmp/blink_count"
DELAY_PAUSE = 0.5
DELAY_BLINK = 0.2
uid="pi"
gid="pi"
LEDRed = 21
LEDGreen = 20
LEDBlue = 16
count=0

# We set all the LED's to off.
GPIO.setup(LEDRed, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LEDGreen, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LEDBlue, GPIO.OUT, initial=GPIO.LOW)

def prepare():
	# create control file if necessary
	if not os.path.exists(filepath):
		f = file(filepath, "w")
		f.write("255") # continous lit
		f.close()

		# fix ownership
		os.chown(filepath, pwd.getpwnam(uid).pw_uid, grp.getgrnam(gid).gr_gid)
		os.chmod(filepath, 0o666)


def blink(count, delay_off, delay_on):
	print "Count should still be ",count,"."
	# if count is greater than 20, green LED should be turned on continuosly
	if count > 20:
		GPIO.output(LEDRed, GPIO.LOW)
		GPIO.output(LEDGreen, GPIO.HIGH)
		GPIO.output(LEDBlue, GPIO.LOW)
	# If count is 0, LED should be turn off completely.
	elif count == 0:
		GPIO.output(LEDRed, GPIO.LOW)
		GPIO.output(LEDGreen, GPIO.LOW)
		GPIO.output(LEDBlue, GPIO.LOW)
	# This will blink green led x number of times. We want to change else to elseif with specific conditions.
	elif count > 10:
		count-=10
		for i in range(count):
			GPIO.output(LEDRed, GPIO.HIGH)
			GPIO.output(LEDGreen, GPIO.LOW)
			GPIO.output(LEDBlue, GPIO.LOW)
			time.sleep(delay_on)
			GPIO.output(LEDRed, GPIO.LOW)
			time.sleep(delay_off)

	else:
		for i in range(count):
			GPIO.output(LEDRed, GPIO.LOW)
			GPIO.output(LEDGreen, GPIO.LOW)
			GPIO.output(LEDBlue, GPIO.HIGH)
			time.sleep(delay_on)
			GPIO.output(LEDBlue, GPIO.LOW)
			time.sleep(delay_off)

# prepare()

with open(filepath, "r") as f:
	while True:
		value = f.read().split("\n")[0] # we read the whole file to prevent caching and split the needed value
		f.seek(0)
		count = 0
		try:
			count = int(value)
		except ValueError:
			count = 255 # failover if integer conversion not possible.

#		print "Blink count is set to",count,"."
#		count+=1
#		print "Blink count is set to",count,"."

		blink(count, DELAY_BLINK, DELAY_BLINK)
		time.sleep(DELAY_PAUSE)
