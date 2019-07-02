#!/bin/bash

# Makes the folder we need
mkdir USB_IMAGE
# And extracts the huge image file
7z e image.7z -o~/P4wnP1/USB_STORAGE * -r
