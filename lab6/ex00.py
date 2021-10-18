from math import *

def tg(a):
	return sin(a) / cos(a)

try:
	a = float(input("Input   number: "))
	res1 = (cos(2 * a)) / (1 + sin(2 * a))
	res2 = (1 - tg(a)) / (1 + tg(a))
	with open('res00', 'w') as f:
		f.write("First  formula: {}\n".format(res1))
		f.write("Second formula: {}\n".format(res2))
except:
	print("Value error")
