# P4wnP1-Tweaked

WIP. Please use this modification with extreme care. This modification currently has no polish, and has no been tested outside of a very specific setup, and the installation will probably fail spectacularely.

I don't feel as if any of these tweaks are necessary for the official P4wnP1 project, so I created my own stub for some random
stuff I've wanted to see included. I am also hoping this means I can restore my custom settings back if I have to reimage P4wnP1.

Speaking of included:

A payload mixing duckout and hidout to call a batch file stored on the USB_STORAGE, as well as a few random tests.
* Windows 10 apparently treats DELAY as a keystroke and opens Office when DELAY is used. I changed the script so DUCKY won't use DELAY, so Office won't break DUCKY.
- I stashed all the test and example payloads into "example" subfolder for organization purposes.

A python script that will allow you to reset and power down your Raspberry Pi by installing a button. see /gpio/button.py

I've hijacked ledtool to use an external LED to show status. Please refer to ledtool.py in order to get new color setting information. Below will list how I am using these LED colors.
- When the LED is solid green, it means P4wnP1 is idle and ready for a job.
- When the LED is blinking red, Ducky is sending something out to control the computer.
- When the LED is blinking blue, it means P4wnP1 is processing something, or waiting on something else.
- Red and Blue LEDs can blink up to 10 times a loop, so you can see what stage a script is in.

A tweak to the boot script that allows you to change the hostname of your Pi, so it won't come up as P4wnP1. See setup.cfg
 - Still in progress.

A RAMDrive was added so Ducky batch can send and execute duckyscripts without spamming writes to the SD card. If you change the default password to SSH into the Pi, you will need to update the batch file to include the new password.

And probably a few more things I forgot about.

When you run setup, it will ask for root password and execute as root. Please check the code over before you execute to make sure you trust it!

* Setup will nuke the existing P4wnP1 directory and reclone the latest one. Make sure you save any of your own files before proceeding.

* Setup will add mount entries into fstab in order to make tmp a ramfs drive.
