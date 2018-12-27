from digraph import Digraph, Node

class Graph(Digraph):
	def __init__(self,size):
		Digraph.__init__(self, size)

	def add_edge(self, vertex1, vertex2):
		try:
			#Add first direction edge
			if vertex2 >= len(self.vertices):
				raise IndexError

			node_iterator = self.vertices[vertex1]

			while node_iterator.next != None:
				if node_iterator.next.data == vertex2:
					return
				node_iterator = node_iterator.next

			node_iterator.next = Node(vertex2)

			#Add second direction edge
			node_iterator = self.vertices[vertex2]

			if vertex1 >= len(self.vertices):
				raise IndexError
				
			while node_iterator.next != None:
				if node_iterator.next.data == vertex1:
					return
				node_iterator = node_iterator.next

			node_iterator.next = Node(vertex1)

		except IndexError:
			if vertex1 >= len(self.vertices):
				print('Cannot add edge (' + str(vertex1) + ', ' + str(vertex2) + '), vertex ' + str(vertex1) + ' does not exist in graph')
			if vertex2 >= len(self.vertices):
				print('Cannot add edge (' + str(vertex1) + ', ' + str(vertex2) + '), vertex ' + str(vertex2) + ' does not exist in graph')