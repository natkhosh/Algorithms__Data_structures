import networkx as nx
import  matplotlib.pyplot as plt

orders = [
    (9, 12),
    (10, 12)
]

def plot(graph):
    pos = nx.spring_layout(graph)
    labels = {n: n for n in graph.nodes()}

    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    plt.show()


if __name__ == "__main__":

    graph = nx.MultiDiGraph()
    graph.add_nodes_from(range(0, 23))
    graph.add_edge(9, 10)
    for order in orders:
        for i in range(order[0], order[1]):
            graph.add_edge(i, i + 1)

    for d in graph.out_degree:
        print(d)
