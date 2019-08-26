# I am rewriting this file. Plese stand by.

#I want to make sure admin permission is given before we move on.
[ "$UID" -eq 0 ] || exec sudo bash "$0" "$@"

# Let's create a goto function just like batch files have!
# The colon must come after the label. Just Linux things.
function goto
{
    label=$1
    cmd=$(sed -n "/$label:/{:a;n;p;ba};" $0 | grep -v ':$')
    eval "$cmd"
    exit
}
start=${1:-"start"}
goto $start

start:
#Internet is needed. So, let's check for internet, and terminate if it isn't found.
echo "Checking for an active internet connection"
ping -c 5 www.google.com>>/dev/null

if [ $? -eq  0 ]
then
goto HaveInternet
else
echo "Internet may be down. Please reconnect and try again."
echo "Press any key to close."
read -n 1 -s
exit
fi

HaveInternet:

# In the line below this, we are going to start a block and see if we can get some unique information out of the current config before we nuke it.
# Hopefully, once we can test out this option, we can make the replaced configuration file contain the correct wifi and bluetooth settings so user can reconnect without reconfiguring P4wnP1.
# git wifi name
# git wifi password
# git bluetooth information

# Let's nuke P4wnP1, and reclone it.
cd ~/
rm -rf ~/P4wnP1
git clone https://github.com/mame82/P4wnP1.git

# Write wifi name
# write password
# write bluetooth

# We want to make a RAM drive to offset writing to temp. This should decrease flash drive writes and increase lifespan.

#We have a handful of files in the temp folder we use and don't want to lose. Let's move them to a directory, and have P4wnP1 copy them on boot.
mkdir $wdir/resource
mkdir $wdir/resource/tmp
cp /tmp/* $wdir/resource/tmp

#Now that these files are safe, let's nuke the contents of the tmp folder.
rm -rf /tmp/*

#We can also nuke the contents of /var/tmp, since it does not have anything we need to keep.
rm -rf /var/tmp/*

#We are going to write the entries we need into fstab. You can tweak the size of tmp if you plan to write larger files to P4wnP1 for processing.
echo "tmpfs			/tmp		tmpfs	defaults,noatime,nosuid,nodev,noexec,mode=0755,size=1M	0	0 " >> /etc/fstab
echo "tmpfs			/var/tmp	tmpfs	defaults,noatime,nosuid,nodev,noexec,mode=0755,size=1M	0	0 " >> /etc/fstab

# extracts the huge image file
rm ~/P4wnP1/USB_STORAGE/image.bin
7z e ~/P4wnP1-Tweaked/files/image.7z -o~/P4wnP1/USB_STORAGE * -r

# Copies the edited files into P4wnP1 directories.
rm ~/P4wnP1/boot_P4wnP1
cp ~/P4wnP1-Tweaked/files/boot_P4wnP1 ~/P4wnP1/boot/boot_P4wnP1
rm ~/P4wnP1/ledtool/ledtool.py
cp ~/P4wnP1-Tweaked/files/ledtool.py ~/P4wnP1/ledtool/

# Copies the newly created files into P4wnP1 directories.
mkdir ~/P4wnP1/gpio
cp ~/P4wnP1-Tweaked/gpio/gpio_buttons.py ~/P4wnP1/gpio/
cp ~/P4wnP1-Tweaked/files/callduckydrive.txt ~/P4wnP1/payloads

# Cleans up P4wnP1 payloads by moving them into /examples. You can easily call a payload from this folder, or move the payload out of /examples.
cd ~/P4wnP1/payloads/
mkdir examples
mv *.txt examples

# Copies our ducky payload into the payload folder.
cp ~/P4wnP1-Tweaked/files/callduckydrive.txt ~/P4wnP1/payloads/
