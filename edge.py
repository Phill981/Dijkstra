
class Edge:
    def __init__(self, edge: list)->None:
        self.from_node = edge[0]
        self.to_node = edge[1]
        self.distance = edge[2]