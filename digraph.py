import numpy as np

class Node:
	def __init__(self, data):
		self.value = data
		self.next = None
		self.color = 'white'

class Digraph:
	def __init__(self, size):
		self.vertices = []

		for x in range(size):
			self.vertices.append(Node(x))

	def add_edge(self, vertex1, vertex2):
		try:
			if vertex1 >= len(self.vertices) or vertex2 >= len(self.vertices):
				raise IndexError

			node_iterator = self.vertices[vertex1]

			while node_iterator.next != None:
				if node_iterator.next.value == vertex2:
					return
				node_iterator = node_iterator.next

			node_iterator.next = Node(vertex2)

		except IndexError:
			if vertex1 >= len(self.vertices):
				print('Cannot add edge (' + str(vertex1) + ', ' + str(vertex2) + '), vertex ' + str(vertex1) + ' does not exist in graph')
			if vertex2 >= len(self.vertices):
				print('Cannot add edge (' + str(vertex1) + ', ' + str(vertex2) + '), vertex ' + str(vertex2) + ' does not exist in graph')

	def add_vertex(self):
		self.vertices.append(Node(len(self.vertices)))

	def __str__(self):
		mystr = ''

		for x in range(len(self.vertices)):
			mystr += str(x) 
			node_iterator = self.vertices[x]

			while node_iterator.next != None:
				mystr += ' ' + str(node_iterator.next.value)
				node_iterator = node_iterator.next

			mystr +='\n'

		return mystr