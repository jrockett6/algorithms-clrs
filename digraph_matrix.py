import numpy as np 

class DigraphMatrix:
	def __init__(self, size):
		self.matrix = np.zeros((size, size), dtype = int)
		self.size = size

	def add_edge(self, vertex1, vertex2):
		try:
			if self.matrix[vertex1, vertex2] != 1:
				self.matrix[vertex1, vertex2] = 1

		except IndexError:
			if vertex1 >= self.size:
				print('Cannot add edge (' + str(vertex1) + ', ' + str(vertex2) + '), vertex ' + str(vertex1) + ' does not exist in graph')
			if vertex2 >= self.size:
				print('Cannot add edge (' + str(vertex1) + ', ' + str(vertex2) + '), vertex ' + str(vertex2) + ' does not exist in graph')

	def add_vertex(self):
		self.matrix.resize((self.size + 1, self.size + 1))
		self.size += 1

	def __str__(self):
		print(self.matrix)
		return ''