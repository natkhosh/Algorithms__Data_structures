"""
This module implements some functions based on linear search algo
"""
from typing import Sequence

import numpy as np


def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array
	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	min_elem = min(arr)
	print('Array:', arr)
	print('Min:', min_elem)
	index = None
	for i, elem in enumerate(arr):
		if elem == min_elem:
			index = i
			return index
	return index


if __name__ == "__main__":
	n = 10
	arr = np.arange(n)
	find_elem = np.random.choice(arr)
	np.random.shuffle(arr)
	print('Index:', min_search(arr))