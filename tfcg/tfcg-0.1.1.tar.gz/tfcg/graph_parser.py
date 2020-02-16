import pathlib
import typing

import networkx as nx
import google.protobuf as protobuf

from .tf_attributes_parser import parse_attributes


class TfGraphParser:
    SKIPED_NAME_LIST_IN_GRAPH = ['sequential', 'init', 'metrics', 'loss',
                                 'VarIsInitializedOp', 'Variable', 'gradients',
                                 'save', 'cross_entropy', 'Adam']
    SKIPED_OP_LIST_IN_GRAPH = ['Sum', 'Mul', 'Cast', 'Equal', 'StridedSlice', 'Mean']
    def __init__(self):
        self.G = nx.DiGraph()

    def parse_graph_def(self, tf_graph_def: dict) -> nx.DiGraph:
        self.node_idx = 0
        G = self._register_nodes(self.G, tf_graph_def)
        G = self._check_non_ancestor_nodes(G, tf_graph_def)
        G = self._register_edges(G, tf_graph_def)
        G = self._register_attributes(G, tf_graph_def)
        G = self._remove_isolated_nodes(G)
        self.G = G
        return G

    def dump_img(self, filename='output.png'):
        import matplotlib.pyplot as plt
        import networkx as nx
        try:
            pos = nx.nx_agraph.graphviz_layout(self.G)
        except:
            pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos)
        labels = {idx: name.split('/')[0] for idx, name in self.G.nodes(data="name")}
        nx.draw_networkx_labels(self.G, pos, labels, font_size=16)
        plt.savefig(filename)

    def dump_yml(self, filename='output.yml'):
        nx.write_yaml(self.G, filename)

    def dump_gml(self, filename='output.gml'):
        nx.write_gml(self.G, filename)

    def _remove_isolated_nodes(self, G):
        G.remove_nodes_from(list(nx.isolates(G)))
        return G

    def _check_non_ancestor_nodes(self, G: nx.DiGraph, tf_graph_def: dict) -> nx.DiGraph:
        _name_to_idx = { name.split('/')[0]: idx for idx, name in G.nodes(data="name")}
        new_node_names: typing.List[str] = []
        for node in G.nodes(data=True):
            idx = node[0]
            for ancestor in node[1]['ancestor']:
                ancestor_name = ancestor.split('/')[0]
                try:
                    ancestor_idx = _name_to_idx[ancestor_name]
                    G.add_edge(ancestor_idx, idx)
                except KeyError as e:
                    new_node_names.append(ancestor_name)
        for name in new_node_names:
            G.add_node(self.node_idx,
                       name=name,
                       ancestor=None)
            self.node_idx += 1
        return G

    def _register_edges(self, G: nx.DiGraph, tf_graph_def: dict) -> nx.DiGraph:
        _name_to_idx = { name.split('/')[0]: idx for idx, name in G.nodes(data="name")}
        for node in G.nodes(data=True):
            if node[1]['ancestor'] is None: continue
            for ancestor in node[1]['ancestor']:
                ancestor_name = ancestor.split('/')[0]
                idx = node[0]
                ancestor = _name_to_idx[ancestor_name]
                G.add_edge(ancestor, idx)
        return G

    def _register_attributes(self, G: nx.DiGraph, tf_graph_def: dict) -> nx.DiGraph:
        return parse_attributes(G, tf_graph_def)

    def _register_nodes(self, G: nx.DiGraph, tf_graph_def: dict) -> nx.DiGraph:
        nodes = tf_graph_def['node']
        for ele in nodes:
            for s in self.SKIPED_NAME_LIST_IN_GRAPH:
                if s in ele['name']:
                    break
            else:
                if ele['op'] in self.SKIPED_OP_LIST_IN_GRAPH:
                    continue
                if 'input' in ele.keys():
                    names = ele['name'].split('/')
                    root_name = names[0]
                    # to avoid self ancestor
                    inputs = []
                    if len(names) > 4:
                        continue
                    for input in ele['input']:
                        inputs.append(input.split('/')[0])
                    continued = True
                    for i in inputs:
                        if i[0] == '^':
                            break
                        elif i == 'keras_learning_phase':
                            break
                        if i != root_name:
                            continued = False
                            break
                    if continued:
                        continue
                    if 'flatten' in root_name:
                        if len(ele['input']) == 1:
                            continue
                    if not root_name in ele['input'][0].split('/'):
                        if len(ele['input']) == 1:
                            for s in self.SKIPED_NAME_LIST_IN_GRAPH:
                                if ancestor in ele['input']:
                                    break
                            else:
                                ancestor = ele['input']
                        else:
                            ancestor = []
                            for a in ele['input'][:-1]:
                                for s in self.SKIPED_NAME_LIST_IN_GRAPH:
                                    if a in s:
                                        break
                                else:
                                    ancestor.append(a)
                        print(ele)
                        G.add_node(self.node_idx,
                                   name=root_name,
                                   ancestor=ancestor)
                        self.node_idx += 1
        return G

    @staticmethod
    def from_file(path: pathlib.Path) -> 'TfGraphParser':
        pass

    @staticmethod
    def from_graph_def(graph_def) -> 'TfGraphParser':
        tf_graph_def = protobuf.json_format.MessageToDict(graph_def)
        parser = TfGraphParser()
        _ = parser.parse_graph_def(tf_graph_def)
        return parser
