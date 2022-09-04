#!/usr/bin/python
import time
from microdotphat import scroll, fill, write_string, set_pixel, clear, show, WIDTH, HEIGHT

clear()

a = [
'11110',
'00101',
'11110'
]

m = [
'11111',
'00110',
'11111'
]

p = [
'11111',
'00101',
'00111'
]

no = [[
'11111',
'10001',
'11111'
],[
'00000',
'11111',
'00000'
],[
'11101',
'10101',
'10111'
],[
'10101',
'10101',
'11111'
],[
'00111',
'00100',
'11111'
],[
'10111',
'10101',
'11101'
],[
'11111',
'10101',
'11101'
],[
'00001',
'11101',
'00011'
],[
'11111',
'10101',
'11111'
],[
'10111',
'10101',
'11111'
]]

def draw(x, y, c):
	for i in range(0, len(c)):
		for j in range(0, len(c[i])):
			p = c[i][j]
			set_pixel(x+j, y+i, int(p))

while True:
	clear()
	now = time.localtime()
	str = time.strftime("%I%M", now)
	write_string(str, kerning=False)

	amp = time.strftime("%p", now)
	if amp == "AM":
		draw(40, 0, a)
	else:
		draw(40, 0, p)
	draw(40, 4, m)

	sec = time.strftime("%S", now)
	i = int(sec[0])
	j = int(sec[1])
	draw(32, 0, no[i])
	draw(32, 4, no[j])

	show()
	time.sleep(0.1)

