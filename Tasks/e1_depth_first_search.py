from typing import Hashable, List
import networkx as nx


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

visited = {node: False for node in graph.nodes}
list_vis = []


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""
	visited[start_node] = True
	if start_node not in list_vis:
		list_vis.append(start_node)
	for w in g.adj[start_node]:
		if not visited[w]:  # посещён ли текущий сосед?
			list_vis.append(w)
			dfs(g, w)
	print(visited)
	return list_vis


if __name__ == "__main__":

	print('Граф: ', graph.nodes())
	# for node in graph.adj:
	# 	print(node, graph.adj[node])

	print('Связанные ноды: ', dfs(graph, "A"))
	print('---')


	num_components = 0
	for key, value in visited.items():
		if value == False:
			dfs(graph, key)
			num_components += 1

	print('Число компонент связанности:= ', num_components)

