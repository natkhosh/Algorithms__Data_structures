from typing import Hashable, List
import networkx as nx

#
# def dfs_find(graph, src, dst, visited):
# 	visited[src] = True
# 	if src == dst:  # src - откуда начинаем смотреть, dst - куда мы хотим дойти
# 		return True
#
# 	for node in graph.adj[src]:
# 		if not visited[node]:
# 			if dfs_find(graph, node, dst, visited):
# 				return True
# 	return False
#
#
#
# def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
# 	"""
# 	Do an depth-first search and returns list of nodes in the visited order
#
# 	:param g: input graph
# 	:param start_node: starting node of search
# 	:return: list of nodes in the visited order
# 	"""
# 	print(g, start_node)
# 	return list(g.nodes)
#
# def find_connect(g: nx.Graph):
# 	count = 0
# 	visited = {node: False for node in g.nodes}
# 	for source in g.nodes:
# 		for dest in g.nodes:
# 			if dfs_find(g, source, dest, visited) == True:
# 				count += 1
#
# 	return print(count)

def dfs(v):
    visited[v] = True
    for w in graph.adj[v]:
        if visited[w] == False:  # посещён ли текущий сосед?
            dfs(w)


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
	# graph.add_edge("Z", "X")
	src = "A"
	dst = "X"

	visited = {node: False for node in graph.nodes}
	print(graph.nodes())
	for node in graph.adj:
		print(node, graph.adj[node])

	#print(dfs_find(graph, src, dst, visited))
	dfs(src)
	print(visited)
	print('-------------')
	#find_connect(graph)

	n = graph.number_of_nodes()
	# print(nx.number_connected_components(graph))

	num_components = 0
	for key, value in visited.items():
		if value == False:
			dfs(key)
			num_components += 1

	print('num:= ', num_components)

	# count = 0
	# node_not_connected = []
	# for key, value in visited.items():
	# 	if value == False:
	# 		node_not_connected.append(key)
	# print(node_not_connected)
	# for src in node_not_connected:
	# 	for dst in node_not_connected:
	# 		dfs_find(graph, src, dst, visited)
	# 		if visited.values():
	# 			count += 1
	# print(count)