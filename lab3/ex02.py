from math import *

try:
	xs = float(input("Input x start : "))
	xe = float(input("Input x end   : "))
	st = float(input("Input dx      : "))
	es = float(input("Input eps     : "))
except:
	print("Value Error")
	exit()

print("+--------------+--------------+-----------------+")
print("I     X        I      Y       I         N       I")
print("+--------------+--------------+-----------------+")
while xs <= xe:
	if abs(xs) < 1:
		xs += st
		continue
	y = 0
	n = 1
	m = 0
	while True:
		de = 1 / (n * xs ** n)
		y += de
		n += 2
		m += 1
		if abs(de) < es:
			break
	print("I {:10.3f}   I {:10.3f}   I    {:7}      I".format(xs, y, m))
	xs += st
print("+--------------+--------------+-----------------+")






