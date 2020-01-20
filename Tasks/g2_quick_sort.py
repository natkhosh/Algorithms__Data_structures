from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with quick sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	less = []
	equal = []
	greater = []

	if len(container) > 1:
		pivot = container[0]
		for x in container:
			if x < pivot:
				less.append(x)
			if x == pivot:
				equal.append(x)
			if x > pivot:
				greater.append(x)
		return sort(less) + equal + sort(greater)
	else:
		return container


if __name__ == '__main__':
	array = [12, 4, 5, 6, 7, 3, 1, 15]

	print(sort(array))