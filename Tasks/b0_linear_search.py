"""
This module implements some functions based on linear search algo
"""
from typing import Sequence
import numpy as np
import random


def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""

	min_ = arr[0]
	for i in range(len(arr)):
		if min_ > arr[i]:
			min_ = arr[i]
			index = i

	return index

def finding_element(find_element, array):
	index = None
	for i, elem in enumerate(array):
		if elem == find_element:
			index = i
			return index
		else:
			index = None


if __name__== "__main__":
	n = 1000
	array = np.arange(n)
	find_element = np.random.choice(array)
	np.random.shuffle(array)
	print(finding_element(find_element, array))
	print(min_search(array))
