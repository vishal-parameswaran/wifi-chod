from pythonping import ping
import os
import platform
if platform.system() == "Windows":
  os.add_dll_directory("C:\\Program Files\\VideoLAN\\VLC")
import vlc
from time import sleep
def internet_on():
      response_list = ping('8.8.8.8', size=10, count=1)
      if response_list.rtt_avg_ms > 1999:
        return False
      else:
        return True
repeat_counter = 0
while True:
  if repeat_counter>2:
    sleep(600)
  internet_check = internet_on()
  if not internet_check:
    p = vlc.MediaPlayer(os.getcwd() + "/song.mp3")
    p.play()
    sleep(12.330)
    repeat_counter+=1
  else:
    repeat_counter = 0
