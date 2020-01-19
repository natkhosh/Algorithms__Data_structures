from typing import Any, Sequence, Optional
import numpy as np



def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array (using recursive way)

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	def search_recursive(left, right):
		if left >= right:
			return None
		if arr[left] == elem:
			return left

		middle = left + (right - left) // 2
		if arr[middle] == elem:
			if middle == left + 1:
				return middle
			else:
				return search_recursive(left, middle + 1)
		if not (arr[middle] < elem):
			return search_recursive(left, middle)
		else:
			return search_recursive(middle + 1, right)

	return search_recursive(0, len(arr))

if __name__ == "__main__":
	n = 10
	array = np.arange(n)
	element = 9
	#element = np.random.choice(array)
	print(array, element)
	print(binary_search(element, array))