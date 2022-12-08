class Graph:
    number_of_nodes = 0
    adjacent_list = {}

    def __init__(self):
        self.number_of_nodes = 0,
        self.adjacent_list = {}

    # Example adjacent list
    # {
    # 0: [1,2],
    # 1: [3,4,5]
    # }

    def add_vertex(self, value: str):
        if self.adjacent_list[value] is not None:
            return
        self.adjacent_list[value] = []

    def add_edge(self, node1, node2):
        if self.adjacent_list[node1] is None and self.adjacent_list[node2]:
            return False
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)


# from graph_by_class import Graph
#
# graph = Graph()
# graph.add_vertex(10)
# graph.add_vertex(20)
# graph.add_vertex(30)
# graph.add_vertex(40)
# graph.add_vertex(10)
# graph.add_vertex(340)
#
# graph.add_edge([10, 20])
#
# print(graph.adjacent_list)

