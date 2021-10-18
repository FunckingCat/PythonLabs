from math import *

try:
	x = 0
	with open('res01', 'r') as f:
		x = float(f.readline())

	if x <= -2:
		y = -x - 2
	if x > -2 and x < -1:
		y = sqrt(1 - pow(x + 1, 2))
	if x >= -1 and x <= 1:
		y = 1
	if x > 1 and x < 2:
		y = -2 * (x - 2) - 1
	if x >= 2:
		y = -1
	with open('res01', 'w') as f:
		f.write("X: {}  Y: {}".format(x, float(y)))	
except:
	print("Value error")


