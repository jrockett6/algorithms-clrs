from graph import Graph
from digraph import Digraph
from digraph_matrix import DigraphMatrix
from graph_matrix import GraphMatrix
from queue import Queue 
from breadth_first_search import breadth_first_search
from depth_first_search import depth_first_search


# my_digraphMat = DigraphMatrix(4)
# my_digraphMat.add_vertex()
# my_digraphMat.add_edge(2, 3)
# my_digraphMat.add_edge(2, 5)

# print(my_digraphMat)


# my_graphMat = GraphMatrix(4)
# my_graphMat.add_vertex()
# my_graphMat.add_edge(2, 1)

# print(my_graphMat)

# my_queue = Queue()
# my_queue.enqueue(4)
# my_queue.enqueue(5)
# my_queue.enqueue(2)
# my_queue.dequeue()
# my_queue.enqueue(3)

# print(my_queue)

my_graph = Graph()

my_graph.add_vertex('banana')
my_graph.add_vertex('hi')
my_graph.add_edge('banana', 'hi')
my_graph.add_vertex('wassup')
my_graph.add_edge('hi','wassup')
my_graph.add_vertex('too')
my_graph.add_edge('banana','too')
my_graph.add_vertex('lalala')

print(my_graph)

# breadth_first_search(my_graph, 'banana', 'wassup')

depth_first_search(my_graph, 'banana')

print([vertex.finish_time for vertex in my_graph.vertex_object.values()])

# my_graph2 = Digraph(4)

# my_graph2.add_vertex()
# my_graph2.add_edge(2, 3)
# my_graph2.add_edge(2, 5)

# print(my_graph2)

