from re import S
from graph import Graph
from math import inf as INFINITY
from pprint import pprint

class Dijkstra:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.current = graph.starting_point
        self.visited = [self.current]
        self.table = [
            [e , INFINITY, None]for e in self.graph.uniques
        ]
        self._reassing_value("S", 0, "S")
        self.last = self.current

    def _find_neighbour(self):
        self.neighbour = []
        for edge in self.graph.edges:
            if edge.from_node == self.current:
                self.neighbour.append(edge)
        print(self.neighbour)

    def _find_shortest_distance(self):
        self.next_neighbour = None
        minimum = INFINITY
        for edge in self.neighbour:
            distance = self._find_min_total(edge.from_node) + edge.distance
            if distance < minimum and edge.to_node not in self.visited:
                self.next_neighbour, minimum = edge.from_node,  distance
                 
    def _reassing_value(self, node, new_cost, new_previous):
        counter = 0
        for e in self.table:
            if e[0] == node:
                break
            counter += 1

        self.table[counter] = [node, new_cost, new_previous]

    def _find_min_total(self, node):
        for e in self.table:
            if e[0] == node:
                return e[1]

    def solve(self):
        self.table.append([self.current, 0, self.current])
        while self.visited + [self.current] != self.graph.uniques:
            self._find_neighbour()
            self._find_shortest_distance()
            print(self.visited)
            print(self.next_neighbour)
            break

    

g = Graph("properties.json")
dijk = Dijkstra(g)
pprint(dijk.table)
dijk.solve()