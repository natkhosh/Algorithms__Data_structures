"""
My little Stack
"""
from typing import Any

stack = []  # переменная

def push(elem: Any) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	print("Добавили элемент {} в стек".format(elem))

	global stack
	temp_stack = []

	temp_stack.append(elem)
	temp_stack.extend(stack)

	stack = temp_stack

	return None


def pop() -> Any:
	"""
	Pop element from the top of the stack. If not elements - should return None.

	:return: popped element
	"""
	global stack
	if len(stack) > 0:
		elem_pop = stack.pop(0)
		return elem_pop
	else:
		return None


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it.

	:param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
	:return: peeked element or None if no element in this place
	"""

	if len(stack) > ind >= 0:
		peek_elem = stack[ind]
	else:
		peek_elem = None

	print(ind)
	return peek_elem


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	stack.clear()

	return None



if __name__ == "__main__":
	push(7)
	push(3)
	push(5)
	print(stack)


	print("---")
	print(peek(2))
	print("---")
	clear()
	print(stack)
