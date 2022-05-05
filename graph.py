#import numpy as np

import json
from pprint import pprint
from edge import Edge

class Graph:
	def __init__(self, path: str):
		self.edges = list()
		self.path = path
		self._create_edges()
		self._get_uniques()

	def _create_edges(self)->None:
		with open(self.path) as json_file:
			data = json.load(json_file)
			#pprint(data)
		for edge in data["Routes"]:
			#print(edge)
			self.edges.append(Edge(edge))
		self.starting_point = data["Start Point"]

	def _get_uniques(self):
		self.uniques = list()
		for e in self.edges:
			if e.from_node not in self.uniques:
				self.uniques.append(e.from_node)
