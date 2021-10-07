from random import *
from math import *

try:
	n = int(input("Input N: "))
except:
	print("Value Error")
	exit()
arr = [randrange(-50000, 50000)/10000 for i in range(n)]
print(arr)
print("Min num index ", arr.index(min(arr)))
try:
	fst_neg = arr.index([x for x in arr if x < 0][0])
	summ = sum([abs(x) for x in arr if arr.index(x) > fst_neg])
	print("Absolute summ after first negative ", summ)
except:
	print("No negative elements")
try:
	a = int(input("Input A: "))
	b = int(input("Input B: "))
except:
	print("Value Error")
	exit()
for x in arr:
	if x >= a and x <= b:
		arr.remove(x)
		arr.append(0)
print(arr)
