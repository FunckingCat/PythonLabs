from math import *
from random import *

def shot(r, x, y):
	if x >= 0 and y >= 0 and sqrt(x*x + y*y) <= r:
		return [x, y, 1]
	elif x <= 0 and y <= 0 and -x - r <= y:
		return [x, y, 1]
	else:
		return [x, y, 0]

r = 10
print ("   X        Y      RES")
print ("--------------------------")
for i in range(10):
	x, y, res = shot(r, randrange(-r - 1, r + 1), randrange(-r - 1, r + 1))
	if res == 1: res = "YES" 
	else: res = "NO"
	print("   {:3}      {:3}   {}".format(x, y, res))





