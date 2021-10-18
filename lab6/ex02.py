from math import *

try:

	#r = float(input("Input R: "))
	r = 10

	x = 0
	y = 0
	with open('res02', 'r') as f:
		x = float(f.readline())
		y = float(f.readline())

	if x >= 0 and y >= 0 and sqrt(x*x + y*y) <= r:
		res = ("[{};{}] belongs to the region".format(x , y))
	elif x <= 0 and y <= 0 and -x - r <= y:
		res = ("[{};{}] belongs to the region".format(x , y))
	else:
		res = ("[{};{}] not belongs to the region".format(x , y))
	with open('res02', 'w') as f:
		f.write(res)
except:
	print("Value error")
