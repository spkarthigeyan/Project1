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
place6 = owm.weather_at_id(3094325)  #Kuchary,Poland
place7 = owm.weather_at_id(1850147)  #Tokyo,Japan
place8 = owm.weather_at_id(2207349)  #Bellara,AU
place9 = owm.weather_at_id(5332921)  #California, US
place10 = owm.weather_at_id(5202009) #Moscow,US
place11 = owm.weather_at_id(2643743) #London
place12 = owm.weather_at_id(2655603) #Birmingham
place13 = owm.weather_at_id(4736286) #Texas,US
place14 = owm.weather_at_id(3054643) #Budapest,HU
place15 = owm.weather_at_id(6455259) #Paris,FR

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
cord6 = place6.get_location()
weat6 = place6.get_weather()
cord7 = place7.get_location()
weat7 = place7.get_weather()
cord8 = place8.get_location()
weat8 = place8.get_weather()
cord9 = place9.get_location()
weat9 = place9.get_weather()
cord10 = place10.get_location()
weat10 = place10.get_weather()
cord11 = place11.get_location()
weat11 = place11.get_weather()
cord12 = place12.get_location()
weat12 = place12.get_weather()
cord13 = place13.get_location()
weat13 = place13.get_weather()
cord14 = place14.get_location()
weat14 = place14.get_weather()
cord15 = place15.get_location()
weat15 = place15.get_weather()

orig_stdout = sys.stdout
f = open('output.txt', 'w')
sys.stdout = f
	
#t1=place1.get_reception_time(timeformat='iso')
#now=datetime.datetime.now().isoformat()
now = datetime.datetime.now()
per = now + datetime.timedelta(hours=8)
syd = now + datetime.timedelta(hours=11)
bos = now - datetime.timedelta(hours=5)
ade = now + datetime.timedelta(hours=10,minutes=30)
mel = now + datetime.timedelta(hours=11)
kuc = now + datetime.timedelta(hours=1)
tok = now + datetime.timedelta(hours=9)
bel = now + datetime.timedelta(hours=10)
cal = now - datetime.timedelta(hours=8)
mos = now - datetime.timedelta(hours=3)
lon = now + datetime.timedelta(hours=0)
bir = now + datetime.timedelta(hours=0)
tex = now - datetime.timedelta(hours=6)
bud = now + datetime.timedelta(hours=1)
par = now + datetime.timedelta(hours=1)

perth = per.isoformat()
sydney = syd.isoformat()
boston = bos.isoformat()
adelaide = ade.isoformat()
melbourne = mel.isoformat()
kuchary = kuc.isoformat()
tokyo = tok.isoformat()
bellara = bel.isoformat()
california = cal.isoformat()
moscow = mos.isoformat()
london = lon.isoformat()
birmin = bir.isoformat()
texas = tex.isoformat()
budap = bud.isoformat()
paris = par.isoformat()

print(cord1.get_name(),"|",cord1.get_lat(),",",cord1.get_lon(),"|",perth,"|",weat1.get_status(),"|",weat1.get_temperature('celsius'),"|",weat1.get_pressure(),"|",weat1.get_humidity(),"|","\n",cord2.get_name(),"|",cord2.get_lat(),",",cord2.get_lon(),"|",sydney,"|",weat2.get_status(),"|",weat2.get_temperature('celsius'),"|",weat2.get_pressure(),"|",weat2.get_humidity(),"|","\n",cord3.get_name(),"|",cord3.get_lat(),",",cord3.get_lon(),"|",boston,"|",weat3.get_status(),"|",weat3.get_temperature('celsius'),"|",weat3.get_pressure(),"|",weat3.get_humidity(),"|","\n",cord4.get_name(),"|",cord4.get_lat(),",",cord4.get_lon(),"|",adelaide,"|",weat4.get_status(),"|",weat4.get_temperature('celsius'),"|",weat4.get_pressure(),"|",weat4.get_humidity(),"|","\n",cord5.get_name(),"|",cord5.get_lat(),",",cord5.get_lon(),"|",melbourne,"|",weat5.get_status(),"|",weat5.get_temperature('celsius'),"|",weat5.get_pressure(),"|",weat5.get_humidity(),"|","\n",cord6.get_name(),"|",cord6.get_lat(),",",cord6.get_lon(),"|",kuchary,"|",weat6.get_status(),"|",weat6.get_temperature('celsius'),"|",weat6.get_pressure(),"|",weat6.get_humidity(),"|","\n",cord7.get_name(),"|",cord7.get_lat(),",",cord7.get_lon(),"|",tokyo,"|",weat7.get_status(),"|",weat7.get_temperature('celsius'),"|",weat7.get_pressure(),"|",weat7.get_humidity(),"|","\n",cord8.get_name(),"|",cord8.get_lat(),",",cord8.get_lon(),"|",bellara,"|",weat8.get_status(),"|",weat8.get_temperature('celsius'),"|",weat8.get_pressure(),"|",weat8.get_humidity(),"|","\n",cord9.get_name(),"|",cord9.get_lat(),",",cord9.get_lon(),"|",california,"|",weat9.get_status(),"|",weat9.get_temperature('celsius'),"|",weat9.get_pressure(),"|",weat9.get_humidity(),"|","\n",cord10.get_name(),"|",cord10.get_lat(),",",cord10.get_lon(),"|",moscow,"|",weat10.get_status(),"|",weat10.get_temperature('celsius'),"|",weat10.get_pressure(),"|",weat10.get_humidity(),"|","\n",cord11.get_name(),"|",cord11.get_lat(),",",cord11.get_lon(),"|",london,"|",weat11.get_status(),"|",weat11.get_temperature('celsius'),"|",weat11.get_pressure(),"|",weat11.get_humidity(),"|","\n",cord12.get_name(),"|",cord12.get_lat(),",",cord12.get_lon(),"|",birmin,"|",weat12.get_status(),"|",weat12.get_temperature('celsius'),"|",weat12.get_pressure(),"|",weat12.get_humidity(),"|","\n",cord13.get_name(),"|",cord13.get_lat(),",",cord13.get_lon(),"|",texas,"|",weat13.get_status(),"|",weat13.get_temperature('celsius'),"|",weat13.get_pressure(),"|",weat13.get_humidity(),"|","\n",cord14.get_name(),"|",cord14.get_lat(),",",cord14.get_lon(),"|",budap,"|",weat14.get_status(),"|",weat14.get_temperature('celsius'),"|",weat14.get_pressure(),"|",weat14.get_humidity(),"|","\n",cord15.get_name(),"|",cord15.get_lat(),",",cord15.get_lon(),"|",paris,"|",weat15.get_status(),"|",weat15.get_temperature('celsius'),"|",weat15.get_pressure(),"|",weat15.get_humidity(),"|","\n")

f.close()
sys.stdout = orig_stdout
