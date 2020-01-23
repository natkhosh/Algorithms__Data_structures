from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
	"""
	Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

	:param stairway: list of ints, where each int is a cost of appropriate step
	:return: minimal cost of getting to the top
	"""
	stairway_sum = [0] * len(stairway)
	stairway_sum[0] = stairway[0]
	stairway_sum[1] = stairway[1]

	for i in range(2, len(stairway)):
		stairway_sum[i] = stairway[i] + min(stairway_sum[i - 1], stairway_sum[i - 2])

	# for i in range(len(stairway)):
	# 	if i + 1 < len(stairway) and stairway_sum[i + 1] > stairway_sum[i] + stairway[i + 1]:
	# 		stairway_sum[i + 1] = stairway_sum[i] + stairway[i + 1]
	# 	if i + 2 < len(stairway) and stairway_sum[i + 2] > stairway_sum[i] + stairway[i + 2]:
	# 		stairway_sum[i + 2] = stairway_sum[i] + stairway[i + 2]

	min_cost =stairway_sum[-1]
	print(stairway_sum)
	return min_cost


if __name__ == "__main__":
	stairway = [3, 5, 2, 0, 2, 8, 4, 10, 3]
	print(stairway)
	stairway_sum = [999] * len(stairway)
	print(stairway_path(stairway))