from typing import Hashable, List
import networkx as nx


def dfs_find(graph, src, dst, visied):
	visied[src] = True
	if src == dst:  # src - откуда начинаем смотреть, dst - куда мы хотим дойти
		return True

	for node in graph.adj[src]:
		if not visied[node]:
			if dfs_find(graph, node, dst, visited):
				return True
	return False


def dfs_new(graph, src, visied):
	visied[src] = True
	# if src == dst:  # src - откуда начинаем смотреть, dst - куда мы хотим дойти
	# 	return True

	for node in graph.adj[src]:
		if not visied[node]:
			if dfs_find(graph, node, visited):
				return True
	return False


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""
	print(g, start_node)
	return list(g.nodes)



if __name__ == "__main__":
	graph = nx. Graph()
	graph.add_nodes_from("ABCDEFG")
	graph.add_edges_from(
		[
			("A", "B"),
			("A", "C"),
			("B", "D"),
			("B", "E"),
			("C", "F"),
			("E", "G")
		]
	)

	graph.add_node('Z')
	graph.add_node('Y')
	graph.add_node('X')
	src = "A"
	dst = "X"

	visited = {node: False for node in graph.nodes}
	print(graph.nodes())
	for node in graph.adj:
		print(node, graph.adj[node])

	print(dfs_find(graph, src, dst, visited))
	print(visited)


	# if any visited.values() :
	# 	dfs_find(graph, src, dst, visited)