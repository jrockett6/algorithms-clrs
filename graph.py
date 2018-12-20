from digraph import Digraph, Node

class Graph(Digraph):
	def __init__(self,size):
		Digraph.__init__(self, size)

	def add_edge(self, vertex, vertex2):
		#Add first direction edge
		try:
			node_iterator = self.vertices[vertex]

			while node_iterator.next != None:
				if node_iterator.next.value == vertex2:
					return
				node_iterator = node_iterator.next

			node_iterator.next = Node(vertex2)

			#Add second direction edge
			node_iterator = self.vertices[vertex2]

			while node_iterator.next != None:
				if node_iterator.next.value == vertex:
					return
				node_iterator = node_iterator.next

			node_iterator.next = Node(vertex)

		except IndexError:
			if vertex >= len(self.vertices):
				print('Cannot add edge (' + str(vertex) + ', ' + str(vertex2) + '), vertex ' + str(vertex) + ' does not exist in graph')
			if vertex2 >= len(self.vertices):
				print('Cannot add edge (' + str(vertex) + ', ' + str(vertex2) + '), vertex ' + str(vertex2) + ' does not exist in graph')