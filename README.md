# home-security-system

Hello everyone!
This branch contains the python code that does all of the following
1. Intercept the state of the reed switch (door sensor) indicating whether the door is open or closed
2. Accordingly prompt the camera to take a photo 
3. Store the photo in a specified folder intruder_photos in /home/pi/ directory on Raspberry Pi
4. Upload the photo to your Dropbox account using an open source program called Dropbox Uploader

How to install:
1. Simply download the python program and save it in home/pi directory on your Raspberry Pi
2. Connect your reed switch to pin 18 of the pi cobbler mounted on the breadboard
3. Connect your DSLR camera to the USB port of the Raspberry Pi
4. Make sure you have Dropbox account set up 
4. Run the program
5. Fiddle around with the states of the reed switch and watch the console to help guide you


