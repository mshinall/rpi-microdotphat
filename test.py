#!/usr/bin/python
import time
import os
from microdotphat import scroll, fill, write_string, set_pixel, clear, show, WIDTH, HEIGHT, set_decimal

clear()


#myip = os.popen('echo `ifconfig | grep -A1 wlan0` | awk \'{print $6}\'').read()
#myip = "10.0.0.109          ";
#write_string(myip, kerning=False)
#i = 0
#while i < len(myip):
#	i += 1
#	scroll()
#	show()
#	time.sleep(1)

clear()
while True:
	now = time.localtime()
	tim = time.strftime("%H%M", now)
	sec = time.strftime("%S", now)
	str = tim + sec
	if int(sec) % 2 == 0:
		set_decimal(2, 1)
		set_decimal(4, 1)
	else:
		set_decimal(2, 0)
		set_decimal(4, 0)
	write_string(str, kerning=False)
	
	show()
	time.sleep(0.1)

