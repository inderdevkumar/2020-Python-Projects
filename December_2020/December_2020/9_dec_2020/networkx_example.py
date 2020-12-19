import networkx as nx
G = nx.Graph()
nodes = [1,2,3,4,5]
edges = [(1,2),(2,3),(1,3),(5,4),(3,4),(4,5)]
G.add_edges_from(edges)
print(G.number_of_edges())

