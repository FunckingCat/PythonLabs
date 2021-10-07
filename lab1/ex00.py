from math import *

def tg(a):
	return sin(a) / cos(a)

try:
	a = float(input("Input   number: "))
	res1 = (cos(2 * a)) / (1 + sin(2 * a))
	res2 = (1 - tg(a)) / (1 + tg(a))
	print("First  formula: ", res1)
	print("Second formula: ", res2)
except:
	print("Value error")
