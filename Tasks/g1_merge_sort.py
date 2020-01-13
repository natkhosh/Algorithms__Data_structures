from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	if len(container) <= 1:
		return container
	else:
		middle = len(container) // 2
		print('=====')
		print('Common split')
		print('Left container: ', container[:middle])
		print('Right container: ', container[middle:])
		print('Split Left container')
		left_container = sort(container[:middle])
		print('Split Right container')
		right_container = sort(container[middle:])

	print("Merge ", left_container, right_container)
	print('---')
	return merge(left_container, right_container)


def merge(left_container, right_container):
	sorted_ = []
	left_container_index = 0
	right_container_index = 0

	left_container_lenght = len(left_container)
	right_container_lenght = len(right_container)

	for _ in range(left_container_lenght + right_container_lenght):
		if (left_container_index < left_container_lenght) and (right_container_index < right_container_lenght):
			if left_container[left_container_index] <= right_container[right_container_index]:
				sorted_.append(left_container[left_container_index])
				left_container_index += 1
			else:
				sorted_.append(right_container[right_container_index])
				right_container_index += 1
		elif left_container_index == left_container_lenght:
			sorted_.append(right_container[right_container_index])
			right_container_index += 1
		elif right_container_index == right_container_lenght:
			sorted_.append(left_container[left_container_index])
			left_container_index += 1

	print("Merge ", sorted_)
	return sorted_


if __name__ == "__main__":
	array = [6, 5, 12, 10, 9, 1]

	print(sort(array))