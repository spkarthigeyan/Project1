import pyowm
import os,sys
import subprocess
import glob
from os import path
from subprocess import call

owm = pyowm.OWM('f4eacf887c75c2e4416c02101b1800f1')

place1 = owm.weather_at_id(2063523)  #perth
place2 = owm.weather_at_id(2147714)  #Sydney
place3 = owm.weather_at_id(4317656)  #Boston
place4 = owm.weather_at_id(2078025)  #Adelaide
place5 = owm.weather_at_id(7839805)  #Melbourne
cord1 = place1.get_location()
weat1 = place1.get_weather()
cord2 = place2.get_location()
weat2 = place2.get_weather()
cord3 = place3.get_location()
weat3 = place3.get_weather()
cord4 = place4.get_location()
weat4 = place4.get_weather()
cord5 = place5.get_location()
weat5 = place5.get_weather()

orig_stdout = sys.stdout
f = open('output.txt', 'w')
sys.stdout = f
	
t1=place1.get_reception_time(timeformat='iso')

print(cord1.get_name(),"|",cord1.get_lat(),",",cord1.get_lon(),"|",t1,"|",weat1.get_status(),"|",weat1.get_temperature('celsius'),"|",weat1.get_pressure(),"|",weat1.get_humidity(),"|","\n",cord2.get_name(),"|",cord2.get_lat(),",",cord2.get_lon(),"|",t1,"|",weat2.get_status(),"|",weat2.get_temperature('celsius'),"|",weat2.get_pressure(),"|",weat2.get_humidity(),"|","\n",cord3.get_name(),"|",cord3.get_lat(),",",cord3.get_lon(),"|",t1,"|",weat3.get_status(),"|",weat3.get_temperature('celsius'),"|",weat3.get_pressure(),"|",weat3.get_humidity(),"|","\n",cord4.get_name(),"|",cord4.get_lat(),",",cord4.get_lon(),"|",t1,"|",weat4.get_status(),"|",weat4.get_temperature('celsius'),"|",weat4.get_pressure(),"|",weat4.get_humidity(),"|","\n",cord5.get_name(),"|",cord5.get_lat(),",",cord5.get_lon(),"|",t1,"|",weat5.get_status(),"|",weat5.get_temperature('celsius'),"|",weat5.get_pressure(),"|",weat5.get_humidity(),"|","\n")

f.close()
sys.stdout = orig_stdout
