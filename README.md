# P4wnP1

WIP. Will likely destroy your flash drive, Raspberry Pi, computer, network, ISP switch, and a few satellites. Do not use this.

I don't feel as if any of these tweaks are necessary for the official P4wnP1 project, so I created my own stub for some random
stuff I've wanted to see included. I am also hoping this means I can restore my custom settings back if I have to reimage P4wnP1.

Speaking of included:

A payload mixing duckout and hidout to call a batch file stored on the USB_STORAGE, as well as a few random tests.
- I stashed all the test and example payloads into "example" subfolder for organization purposes.

A python script that will allow you to reset and power down your Raspberry Pi by installing a switch. see /GPIO/GPIO_button.py

A python script that can blink a multicolor LED depending on status. You will need to set ledstatus. see /GPIO/GPIO_led.py
 - Red can be used when we are running ducky like features, either duckhid or outhid.
 - Solid Red can be an error, check log for details.
 - Green should be idle, ready-for-a-command state.
- Blue can be used when we are running some internal operation, such as JohnTheRipper. Should also be used to tell what stage a payload is in, like what the onboard LED does, but can be seen from outside the case.
- Still in progress.
-If all LED's are off, then the Pi can be unplugged.
* I am hijacking the existing led_status to do this and reverting LEDACT so I can push this to another LED that is outside the Pi.

A tweak to the boot script that allows you to change the hostname of your Pi, so it won't come up as P4wnP1. See setup.cfg
 - Still in progress.

A RAMDrive was added so Ducky batch can send and execute duckyscripts without spamming writes to the SD card. If you change the default password to SSH into the Pi, you will need to update the batch file to include the new password.

And probably a few more things I forgot about.

Before using:

Please make sure you've updated Linux.
Please make sure you've updated P4wnP1.
! Actually, don't. I need to test and see if the update to P4wnP1 is what broke john, or if updating Linux broke John. Or why John is upset.

Run setup.sh to replace and configure what needs to be done.
