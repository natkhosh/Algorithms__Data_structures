"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

queue = []
queue_0 = []
queue_1 = []
queue_2 = []
queue_3 = []
queue_4 = []
queue_5 = []

def enqueue(elem: Any, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global queue
	global queue_0
	global queue_1
	global queue_2
	global queue_3
	global queue_4
	global queue_5


	if priority == 0:
		queue_0.append(elem)
	elif priority == 1:
		queue_1.append(elem)
	elif priority == 2:
		queue_2.append(elem)
	elif priority == 3:
		queue_3.append(elem)
	elif priority == 4:
		queue_4.append(elem)
	elif priority == 5:
		queue_5.append(elem)

	queue = queue_0 + queue_1 + queue_2 + queue_3 + queue_4 + queue_5

def dequeue() -> Any:
	"""
	Return element from the beginning of the queue. Should return None if not elements.

	:return: dequeued element
	"""
	global queue
	global queue_0
	global queue_1
	global queue_2
	global queue_3
	global queue_4
	global queue_5



	if len(queue_0) > 0:
		queue_0.remove(queue[0])
	else:
		if len(queue_1) > 0:
			queue_1.remove(queue[0])
		else:
			if len(queue_2) > 0:
				queue_2.remove(queue[0])
			else:
				if len(queue_3) > 0:
					queue_3.remove(queue[0])
				else:
					if len(queue_4) > 0:
						queue_4.remove(queue[0])
					else:
						if len(queue_5) > 0:
							queue_5.remove(queue[0])

	if len(queue) > 0:
		deq_element = queue.pop(0)
		return deq_element
	else:
		return None

def peek(ind: int = 0, priority: int = 0) -> Any:
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
	queue_0.clear()
	queue_1.clear()
	queue_2.clear()
	queue_3.clear()
	queue_4.clear()
	queue_5.clear()
	return None


if __name__ == "__main__":
	enqueue(2)
	enqueue(1)
	enqueue(5)
	enqueue(23)
	enqueue('dh', 3)
	enqueue('sh', 1)
	print(queue)
	print('---')
	print('E_0: ', queue_0)
	print('E_1: ', queue_1)
	print('E_2: ', queue_2)
	print('E_3: ', queue_3)
	print('E_4: ', queue_4)
	print('E_5: ', queue_5)

	dequeue()
	dequeue()
	dequeue()
	dequeue()
	dequeue()
	dequeue()
	dequeue()

	print(queue)

	print('---')
	print('E_0: ', queue_0)
	print('E_1: ', queue_1)
	print('E_2: ', queue_2)
	print('E_3: ', queue_3)
	print('E_4: ', queue_4)
	print('E_5: ', queue_5)