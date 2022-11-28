class AdjacentList:
    length = 0

    def __init__(self):
        length = 0


class Graph:
    number_of_nodes = 0
    adjacent_list = AdjacentList()

    def __init__(self):
        self.number_of_nodes = 0,
        self.adjacent_list = AdjacentList()

    # Example adjacent list
    # {
    # 0: [1,2],
    # 1: [3,4,5]
    # }

    def add_vertex(self, value: str):
        if hasattr(self.adjacent_list, str(value)):
            return
        setattr(self.adjacent_list, str(value), [])

    def add_edge(self, edge: []):
        if (hasattr(self.adjacent_list, str(edge[0])) and hasattr(self.adjacent_list, str(edge[1]))) is False:
            return False
        getattr(self.adjacent_list, str(edge[0])).append(edge[1])
        getattr(self.adjacent_list, str(edge[1])).append(edge[0])
        print(self.adjacent_list.__dict__)

    def show_connections(self):
        pass
