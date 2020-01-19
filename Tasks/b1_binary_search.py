from typing import Any, Sequence, Optional
import numpy as np
import random


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	index = None
	left = 0
	right = len(arr) - 1

	while right > left + 1:
		middle = (left + right) // 2
		if arr[middle] == elem:
			index = middle
			break
		elif arr[middle] > elem:
			right = middle
		else:
			left = middle
	else:
		if elem == arr[right]:
			index = right
		elif elem == arr[left]:
			index = left
		else:
			index = None

	return index


if __name__ == "__main__":
	n = 10
	array = np.arange(n)
	element = 11
	#element = np.random.choice(array)
	print(array, element)
	print(binary_search(element, array))
