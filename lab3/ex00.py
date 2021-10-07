from math import *

def func(x):
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
	return y

try:
	xs = float(input("Input x start: "))
	xe = float(input("Input x end  : "))
	st = float(input("Input step   : "))

	print("    Xbeg = {} Xend = {} \n        Dx = {}".format(xs, xe, st))
	print("+-----------+-----------+")
	print("+     X     +      Y    +")
	print("+-----------+-----------+")
	while (xs <= xe):
		y = func(xs)
		print("I{0:8.2f}   I{1:8.2f}   I".format(xs, y))
		xs += st
	print("+-----------+-----------+")
except:
	print("Value error")




