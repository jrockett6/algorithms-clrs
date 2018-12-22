from queue import Queue

def breadth_first_search(graph, source):
	if type(graph) == Graph:
		breadth_first_search_adjlist(graph, source):
	else:
		print('No current BFS for this implementation of graph')

def breadth_first_search_adjlist(graph, source):
	#Set inital parameters for source vert, enqueue source
	graph.vertices[source].color = 'grey'
	graph.vertices[source].distance = 0
	graph.vertices[source].prevBFS = None

	bfs_queue = Queue()
	bfs_queue.enqueue(graph.vertices[source])

	#BFS while loop. Search closest nodes and set distances from source/build tree
	while not bfs_queue.is_empty():
		vertex_iterator = bfs_queue.dequeue()
		while vertex_iterator.next != None:
			if vertex_iterator.next.color == 'white':
				vertex_iterator.next.color = 'grey'
				vertex_iterator.next.distance = vertex_iterator.distance + 1
				vertex_iterator.next.prev = vertex_iterator
				bfs_queue.enqueue(vertex_iterator.next)

				vertex_iterator = vertex_iterator.next

	#TODO:
	#Build a tree class 
	#Create shortest path tree while in BFS loop
	#Implement an option to print out shortest path to a specific node, potentially return that path