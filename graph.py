from digraph import Digraph, Node

class Graph(Digraph):
	def __init__(self):
		Digraph.__init__(self)

	def add_edge(self, vertex1, vertex2):
		try:
			#Test if vertices exist
			if not vertex1 in self.vertices or not vertex2 in self.vertices:
				raise IndexError

			#Else, add edges
			for edges in self.vertices[vertex1]:
				if edges == vertex2:
					print('Edge "' + vertex1 + ', ' + vertex2 + '" already exists in graph')
					return

			self.vertices[vertex1].append(vertex2)
			self.vertices[vertex2].append(vertex1)

		except IndexError:
			if vertex1 not in self.vertices:
				print('Cannot add edge (' + str(vertex1) + ', ' + str(vertex2) + '), vertex ' + str(vertex1) + ' does not exist in graph')
			if vertex2 not in self.vertices:
				print('Cannot add edge (' + str(vertex1) + ', ' + str(vertex2) + '), vertex ' + str(vertex2) + ' does not exist in graph')