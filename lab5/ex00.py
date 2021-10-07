from random import *
from math import *
import numpy as np

def gen_array(m: int, n: int):
	rng = np.random.default_rng(145)
	arr = np.array([(rng.integers(low=0, high=2, size=n)) for i in range(m)])
	return arr

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

def go_triangle(arr_src: np.ndarray, n) -> np.ndarray:
	arr = np.eye(n)
	np.copyto(arr, arr_src)
	try:
		swaps = 0
		depth = 0
		for x in range(n - 1):
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
		if arr[n-1][n-1] == 0:
			print("Данная матрица не может быть преведена к треугольной")
			return None
		if swaps % 2 == 1:
			return arr * -1
		return arr
	except:
		print("Данная матрица не может быть преведена к треугольной")
		return None

try:
	print("Треугольной может быть только квадратная матрица")
	#n = int(input("Input N: "))
	n = 6
except:
	print("Value Error")
	exit()

arr = gen_array(n, n)
arr_tri = go_triangle(arr, n)

print(arr)
print(arr_tri)
