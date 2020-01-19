"""
My little Queue
"""
from typing import Any

queue = []

def enqueue(elem: Any) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global queue

	queue.append(elem)

	# print(elem)
	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue. Should return None if no elements.

	:return: dequeued element
	"""
	global queue
	if len(queue) > 0:
		deq_element = queue.pop(0)
		return deq_element
	else:
		return None


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	if len(queue) > ind >= 0:
		peek_elem = queue[ind]
	else:
		peek_elem = None

	print(ind)
	return peek_elem



def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	queue.clear()

	return None


if __name__ == "__main__":
	enqueue(3)
	enqueue(5)
	enqueue(7)
	print(queue)

	# dequeue()
	# print(queue)

	print("---")
	print(peek(1))

	clear()
	print(queue)