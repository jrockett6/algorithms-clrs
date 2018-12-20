from graph import Graph
from digraph import Digraph
from digraph_matrix import DigraphMatrix
from graph_matrix import GraphMatrix


my_digraphMat = DigraphMatrix(4)
my_digraphMat.add_vertex()
my_digraphMat.add_edge(2, 3)
my_digraphMat.add_edge(2, 5)

print(my_digraphMat)


my_graphMat = GraphMatrix(4)
my_graphMat.add_vertex()
my_graphMat.add_edge(2, 1)

print(my_graphMat)

# my_graph = Graph(3)

# my_graph.add_vertex()
# my_graph.add_edge(0, 1)
# my_graph.add_edge(2, 3)
# my_graph.add_edge(4, 5)

# print(my_graph)

# my_graph2 = Digraph(4)

# my_graph2.add_vertex()
# my_graph2.add_edge(2, 3)
# my_graph2.add_edge(2, 5)

# print(my_graph2)