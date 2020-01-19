def fib_recursive(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using recursive algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	if n < 0:
		raise ValueError
	if n == 0:
		return 0
	if n == 1:
		return 1
	if n == 2:
		return 1
	fib_number = fib_recursive(n-1) + fib_recursive(n-2)
	return fib_number


def fib_iterative(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using iterative algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	# fib1 = fib2 = 1
	# i = 2
	# while i < n:
	# 	fib_sum = fib2 + fib1
	# 	fib1 = fib2
	# 	fib2 = fib_sum
	# 	i += 1
	# return fib_sum

	fib1 = fib2 = 1
	if n == 0:
		return 0
	if n == 1:
		return 1
	if n == 2:
		return 1
	if n < 0:
		raise ValueError
	else:
		for i in range(2, n):
			fib1, fib2 = fib2, fib1 + fib2
		fib_number = fib2
	return fib_number


if __name__ == '__main__':
	print(fib_recursive(-1))
	print(fib_recursive(6))
	print(fib_recursive(7))
	print('---')
	print(fib_iterative(-1))
	# print(fib_iterative(6))
	# print(fib_iterative(7))