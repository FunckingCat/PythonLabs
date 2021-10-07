from math import *

try:

	#r = float(input("Input R: "))
	r = 10

	x = float(input("Input x: "))
	y = float(input("Input y: "))

	if x >= 0 and y >= 0 and sqrt(x*x + y*y) <= r:
		print("[{};{}] belongs to the region".format(x , y))
	elif x <= 0 and y <= 0 and -x - r <= y:
		print("[{};{}] belongs to the region".format(x , y))
	else:
		print("[{};{}] not belongs to the region".format(x , y))
	
except:
	print("Value error")
