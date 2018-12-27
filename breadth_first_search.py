from my_queue import Queue
from digraph import Digraph
from graph import Graph

def breadth_first_search(graph, source, destination):
	if type(graph) == Digraph or type(graph) == Graph:
		breadth_first_search_adjlist(graph, source, destination)
	else:
		print('No current BFS for this implementation of graph')

def breadth_first_search_adjlist(graph, source, destination):
	#Set inital parameters for source vert, enqueue source
	graph.vertices[source].color = 'grey'
	graph.vertices[source].distance = 0
	graph.vertices[source].prevBFS = None

	bfs_queue = Queue()
	bfs_queue.enqueue(graph.vertices[source])

	#BFS while loop. Search closest nodes and set distances from source/build tree
	while not bfs_queue.is_empty():
		current_vert = graph.vertices[bfs_queue.dequeue().data]
		vertex_iterator = current_vert.next
		while vertex_iterator != None:
			if graph.vertices[vertex_iterator.data].color == 'white':
				graph.vertices[vertex_iterator.data].color = 'grey'
				graph.vertices[vertex_iterator.data].distance = current_vert.distance + 1
				graph.vertices[vertex_iterator.data].prevBFS = current_vert.data
				bfs_queue.enqueue(vertex_iterator)
			vertex_iterator = vertex_iterator.next

	vertex_iterator = graph.vertices[destination]
	bfs_stack = []

	while vertex_iterator != graph.vertices[source]:
		if not vertex_iterator.prevBFS:
			print('No path between source and destination')
			return
			
		bfs_stack.append(vertex_iterator.data)
		vertex_iterator = graph.vertices[vertex_iterator.prevBFS]

	bfs_stack.append(source)

	print([x for x in reversed(bfs_stack)])

	#TODO:
	#Build a tree class 
	#Create shortest path tree while in BFS loop
	#Implement an option to print out shortest path to a specific node, potentially return that path
	#FIX GRAPH/DIGRAPH CLASS ADD_EDGE METHOD TO CORRECTLY ADD EDGES REFRENCING THE GRAPHS VERTICES, NOT NEW NODES
	