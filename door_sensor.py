import urllib2
import time
import RPi.GPIO as io
io.setmode(io.BCM)
from subprocess import call
import shutil

door_sensor = 18
trigger = True
io.setup(door_Sensor, io.IM, pull_up_down=io.PUD_UP)

#function for door opening
def door_open():
  print("Door is open. Wasn't expected. Trying to capture a picture..")
  # wait for a second before prompting the camera to take a picture
  time.sleep(1)
  call[("gphoto2","--capture-image-and-download","--filename","/home/pi/intruder_photos_img-%H%M%s.jpg")]
  photo = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/intruder_photos/ /"
  call ([photo], shell=True)
  # call shutil.rmtree to remove the folder once the picture is taken, to prevent all photos in intruder_photos from be uploaded into Dropbox 
  shutil.rmtree('/home/pi/intruder_photos')

#function for door closing
def door_close():
  print("Door closed, all good!")

while True:
  if io.input(door_sensor):
    door_open()
    trigger = False
  if not io.input(door_sensor):
    door_close()
    trigger = True

