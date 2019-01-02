import numpy as np

class Node:
	def __init__(self, name):
		self.name = name
		self.next = None
		self.color = 'white'
		self.distance = -1
		self.finish_time = -1
		self.prev_search = None

class Digraph:
	def __init__(self):
		self.vertex_object = {}
		self.vertices = {}

	def add_edge(self, vertex1, vertex2):
		try:
			if not vertex1 in self.vertices or not vertex2 in self.vertices:
				raise IndexError

			for edges in self.vertices[vertex1]:
				if edges == vertex2:
					print('Edge already exists in graph')
					return

			self.vertices[vertex1].append(vertex2)

		except IndexError:
			if vertex1 not in self.vertices:
				print('Cannot add edge (' + str(vertex1) + ', ' + str(vertex2) + '), vertex "' + str(vertex1) + '" does not exist in graph')
			if vertex2 not in self.vertices:
				print('Cannot add edge (' + str(vertex1) + ', ' + str(vertex2) + '), vertex "' + str(vertex2) + '" does not exist in graph')

	def add_vertex(self, vertex):
		self.vertices[vertex] = []
		self.vertex_object[vertex] = Node(vertex)

	def __str__(self):
		mystr = ''

		for vertex in self.vertices:
			if type(vertex) != str:
				mystr += str(vertex) + ': '
			else:
				mystr += vertex + ': '

			for edge in self.vertices[vertex]:
				if type(edge) != str:
					mystr += str(edge) + ', '
				else:
					mystr += edge + ', '

			mystr = mystr[:-2]
			mystr += '\n'

		return mystr