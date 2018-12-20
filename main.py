from graph import Graph
from digraph import Digraph

my_graph = Graph(3)

my_graph.add_vertex()
my_graph.add_edge(0, 1)
my_graph.add_edge(2, 3)

print(my_graph)

my_graph2 = Digraph(4)

my_graph2.add_vertex()
my_graph2.add_edge(2, 3)
my_graph2.add_edge(2, 4)

print(my_graph2)