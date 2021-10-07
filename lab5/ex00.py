from random import *
from math import *
import numpy as np

def gen_array(m: int, n: int):
	rng = np.random.default_rng(11)
	arr = np.array([(rng.integers(low=0, high=2, size=n)) for i in range(m)])
	return arr

def check_triangle(arr: np.ndarray) -> bool:
	i = 0
	for a in arr:
		for x in range(i):
			if a[x] != 0:
				return False
		i += 1
	return True

def swap_rows(arr, a, b):
	arr = list(arr)
	temp = arr[a]
	arr[a] = arr[b]
	arr[b] = temp
	arr = np.array(arr)
	return arr

def sum_rows(a ,b, weight):
	temp_a = [x for x in a]
	temp_b = [x * weight for x in b]
	a = [temp_a[i] + temp_b[i] for i in range(len(b))]
	return a

def go_triangle(arr: np.ndarray) -> np.ndarray:
	try:
		swaps = 0
		depth = 0
		for x in range(n - 1):
			print(x)
			main = arr[depth][depth]
			if (main == 0):
				toswap = depth + 1
				while (toswap < n):
					if (arr[toswap][depth] != 0):
						arr = swap_rows(arr, depth, toswap)
						swaps += 1
						break
					toswap += 1
				main = arr[depth][depth]
			for i in range (depth + 1, n):
				devisor = -arr[i][depth] / main
				arr[i] = sum_rows(arr[i], arr[depth], devisor)
			depth += 1
		if swaps % 2 == 1:
			return arr * -1
		return arr
	except:
		print("Данная матрица не может быть преведена к треугольной")
		return None

try:
	print("Треугольной может быть только квадратная матрица")
	#n = int(input("Input N: "))
	n = 4
except:
	print("Value Error")
	exit()

arr = gen_array(n, n)
print(arr)

arr = go_triangle(arr)
print(arr)
