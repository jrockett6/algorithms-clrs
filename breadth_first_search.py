from my_queue import Queue
from digraph import Digraph
from graph import Graph

def breadth_first_search(graph, source, destination):
	if type(graph) == Digraph or type(graph) == Graph:
		breadth_first_search_adjlist(graph, source, destination)
	else:
		print('No current BFS for this implementation of graph')

def breadth_first_search_adjlist(graph, source, destination):
	if not source in graph.vertices:
		print('Source does not exist in graph')
		return
	if not destination in graph.vertices:
		print('destination does not exist in graph')
		return

	#Set inital parameters for source vert, enqueue source
	graph.vertex_object[source].color = 'grey'
	graph.vertex_object[source].distance = 0
	graph.vertex_object[source].prev_search = None

	bfs_queue = Queue()
	bfs_queue.enqueue(source)

	#BFS while loop. Search closest nodes and set distances from source/build tree
	while not bfs_queue.is_empty():
		current_vert = graph.vertex_object[bfs_queue.dequeue()]
		print(current_vert.name)
		for vertex in graph.vertices[current_vert.name]:
			if graph.vertex_object[vertex].color == 'white':
				graph.vertex_object[vertex].color = 'grey'
				graph.vertex_object[vertex].distance = current_vert.distance + 1
				graph.vertex_object[vertex].prev_search = current_vert.name
				bfs_queue.enqueue(vertex)

				print('Vertex:' + vertex)

	vertex_iterator = graph.vertex_object[destination]
	bfs_stack = []

	while vertex_iterator != graph.vertex_object[source]:
		if not vertex_iterator.prev_search:
			print('No path between source and destination')
			return
			
		bfs_stack.append(vertex_iterator.name)
		vertex_iterator = graph.vertex_object[vertex_iterator.prev_search]

	bfs_stack.append(source)

	print([x for x in reversed(bfs_stack)])

	#TODO:
	#Build a tree class 
	#Create shortest path tree while in BFS loop
	#Implement an option to print out shortest path to a specific node, potentially return that path
	