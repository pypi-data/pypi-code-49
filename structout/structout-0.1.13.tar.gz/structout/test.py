import structout as so
import networkx as nx
g=nx.path_graph(5)

so.gprint(g, zoomlevel=1, zoomnodes=[1])
so.gprint([g,g], zoomlevel=1, zoomnodes=[[1],[1]])

