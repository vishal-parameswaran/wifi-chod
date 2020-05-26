
import os
os.add_dll_directory("C:\\Program Files\\VideoLAN\\VLC")
import vlc
from time import sleep
import socket
def internet_on():
      hostname = socket.gethostname()
      ip_address = socket.gethostbyname(hostname)
      if ip_address == "127.0.0.1":
        return False
      else:
        return True
repeat_counter = 0
while True:
  if repeat_counter>2:
    sleep(600)
  internet_check = internet_on()
  if not internet_check:
    print("hi")
    p = vlc.MediaPlayer("song.mp3")
    p.play()
    sleep(12.330)
    repeat_counter+=1

