import igraph
import networkx as nx
import pandas as pd
from abc import ABCMeta, abstractmethod

class NetworkInterface(metaclass=ABCMeta):
    """ This class is abstract for building a network graph using networkx """
    def __init__(self):
        self.nodes = None
        self.nodes_x = None
        self.nodes_y = None
        self.edges = None
        self.graph = None
        
        
    @abstractmethod
    def get_nodes(self):
        """ Extract the nodes with their details from the data source (netwrokx format) """
        pass
    
    def get_nodes_list(self):
        """ Return the list of nodes ids (id could be a name) without any other details """
        return [n[0] for n in self.nodes]
    
    @property
    def num_nodes(self):
        return len(self.nodes)
    
    @abstractmethod
    def get_edges(self):
        """ Extract the edges with their details from the data source (netwrokx format)"""
        pass
    
    @property
    def num_edges(self):
        return len(self.edges)
    
    def get_edges_list(self):
        """ Return the list of edges without any other details """
        return [e[:-1] for e in self.edges]
    
    def create_network_graph(self, directed=False):
        # Get nodes and edges
        self.get_nodes()
        self.get_edges()
        
        # Create the graph
        if directed:
            self.graph = nx.DiGraph()
        else:
            self.graph = nx.Graph()
            
        self.graph.add_nodes_from(self.nodes)
        self.graph.add_edges_from(self.edges)        
    
    def to_json(self):
        """ This function is to serialize the network graph according to the front end 
            requirements 
        """
        return {
            'nodes': self.nodes,
            'edges': self.edges
        }
    
    @staticmethod
    def nodes_df_to_nodes_list(df):
        """ This function convert nodes df to the format that networkx accept 
            It is assumed that the dataframe index is the node index
        """
        
        # Dropping nodes duplicates if any
        df = df.loc[~df.index.duplicated()] 
        
        return [(ind, row.to_dict()) for ind, row in df.iterrows()]
    
    def calculate_nodes_positions(self, directed, layout, **kwargs):
        # https://igraph.org/python/doc/igraph.Graph-class.html
        # Create the network graph
        nodes_list = self.get_nodes_list()
        edges_list = self.get_edges_list()
        
        g = igraph.Graph(directed=directed)
        g.add_vertices(nodes_list)
        g.add_edges(edges_list)

        # Compute the nodes locations
        if layout == 'layout_bipartite':
            layout = g.layout_bipartite(**kwargs)

        elif layout == 'layout_circle':
            layout = g.layout_circle(**kwargs)

        elif layout == 'layout_drl':
            layout = g.layout_drl(**kwargs)

        elif layout == 'layout_fruchterman_reingold':  # Good for retweet graph
            layout = g.layout_fruchterman_reingold(**kwargs)

        elif layout == 'layout_graphopt':
            layout = g.layout_graphopt(**kwargs)

        elif layout == 'layout_grid':
            layout = g.layout_grid(**kwargs)

        elif layout == 'layout_grid_fruchterman_reingold':
            layout = g.layout_grid_fruchterman_reingold(**kwargs)

        elif layout == 'layout_kamada_kawai':  # Good for social network graph
            layout = g.layout_kamada_kawai(**kwargs)

        elif layout == 'layout_lgl':
            layout = g.layout_lgl(**kwargs)

        elif layout == 'layout_mds':
            layout = g.layout_mds(**kwargs)

        elif layout == 'layout_reingold_tilford':
            layout = g.layout_reingold_tilford(**kwargs)

        elif layout == 'layout_reingold_tilford_circular':
            layout = g.layout_reingold_tilford_circular(**kwargs)

        elif layout == 'layout_star':
            layout = g.layout_star(**kwargs)
        
        self.nodes_x, self.nodes_y = dict(), dict()
        for ind, nd in enumerate(nodes_list):
            self.nodes_x[nd] = layout.coords[ind][0]
            self.nodes_y[nd] = layout.coords[ind][1]
    
        self.append_nodes_positions_to_nodes_attributes()
    
    def append_nodes_positions_to_nodes_attributes(self):
        """ It is a separated function to support getting nodes positions from an 
            outer source other than the provided algorithms 
        """
        for node_id, node_attrs in self.nodes:
            node_attrs['x'] = self.nodes_x[node_id]
            node_attrs['y'] = self.nodes_y[node_id]
    
    def get_nodes_pos_dict(self, scalar=1):
        """ Useful for plotting """
        return {nd_id: [nd_attrs['x']*scalar , nd_attrs['y']*scalar] 
                for nd_id, nd_attrs in self.nodes}