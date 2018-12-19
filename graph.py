import numpy as np

class Node:
	def __init__(self, data):
		self.value = data
		self.next = None

class Graph:
	def __init__(self, size):
		self.vertices = np.array([], dtype = object)

		for x in range(size):
			np.append(self.vertices, Node(x))
			print('hi')

		print(self.vertices.size)

	def add_edge(self, vertex):
		node_iterator = self.vertices[vertex]

		while node_iterator.next != None:
			if node_iterator.next.value == vertex:
				return
			node_iterator = node_iterator.next

		node_iterator.next = Node(vertex)

	def add_vertex(self):
		np.append(self.vertices, Node(counter))

	def __str__(self):
		mystr = ''
		print(self.vertices.size)

		for x in range(self.vertices.size):
			mystr += str(x)
			print(x)

		print(mystr)

		return mystr