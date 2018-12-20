from digraph_matrix import DigraphMatrix 

class GraphMatrix(DigraphMatrix):
	def __init__(self, size):
		DigraphMatrix.__init__(self, size)

	def add_edge(self, vertex1, vertex2):
		try:
			if self.matrix[vertex1, vertex2] != 1:
				self.matrix[vertex1, vertex2] = 1
				self.matrix[vertex2, vertex1] = 1

		except IndexError:
			if vertex1 >= self.size:
				print('Cannot add edge (' + str(vertex1) + ', ' + str(vertex2) + '), vertex ' + str(vertex1) + ' does not exist in graph')
			if vertex2 >= self.size:
				print('Cannot add edge (' + str(vertex1) + ', ' + str(vertex2) + '), vertex ' + str(vertex2) + ' does not exist in graph')