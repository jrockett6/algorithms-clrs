from digraph import Digraph
from graph import Graph

def depth_first_search(graph, source):
	if type(graph) == Digraph or type(graph) == Graph:
		depth_first_search_adjlist(graph, source)
	else:
		print('No current DFS for this implementation of graph')

time = 0

def depth_first_search_adjlist(graph, source):
	global time

	for vertex in graph.vertex_object.values():
		if vertex.color == 'white':
			depth_first_search_visit(graph, vertex)

def depth_first_search_visit(graph, vertex):
	global time

	time = time + 1
	vertex.distance = time
	vertex.color = 'grey'

	for node in graph.vertices[vertex.name]:
		if graph.vertex_object[node].color == 'white':
			graph.vertex_object[node].prev_search = vertex.name
			depth_first_search_visit(graph, graph.vertex_object[node])

	time = time + 1
	vertex.finish_time = time - 1

#TODO:
#Update finishing time to act as a global variable