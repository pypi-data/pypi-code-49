import pathlib
import typing

import networkx as nx
import google.protobuf as protobuf

from .tf_attributes_parser import parse_attributes


class TfGraphParser:
    SKIPED_NAME_LIST_IN_GRAPH = ['sequential', 'init', 'metrics', 'loss',
                                 'VarIsInitializedOp', 'gradients', 'AssignVariableOp',
                                 'save', 'cross_entropy', 'Adam', 'ArgMax']
    SKIPED_ROOT_NAME_LIST_IN_GRAPH = ['sequential', 'init', 'metrics', 'loss',
                                      'VarIsInitializedOp', 'gradients', 'AssignVariableOp',
                                      'save', 'cross_entropy', 'Adam', 'ArgMax' ,
                                      'init', 'Sum', 'Mul', 'Cast', 'Equal', 'Mean', 'Adam',
                                      'save', 'cross_entropy', 'Adam', 'mul', 'Variable']
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
        _name_to_idx = {name.split('/')[0]: idx for idx, name in G.nodes(data="name")}
        new_node_names: typing.List[str] = []
        for node in G.nodes(data=True):
            idx = node[0]
            for ancestor in node[1]['ancestor']:
                ancestor_name = ancestor.split('/')[0]
                try:
                    ancestor_idx = _name_to_idx[ancestor_name]
                    G.add_edge(ancestor_idx, idx)
                except KeyError as e:
                    if not self._remove_batch_dimmension(ancestor_name):
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
                if self._remove_batch_dimmension(ancestor_name): continue
                idx = node[0]
                ancestor = _name_to_idx[ancestor_name]
                G.add_edge(ancestor, idx)
        return G

    def _register_attributes(self, G: nx.DiGraph, tf_graph_def: dict) -> nx.DiGraph:
        return parse_attributes(G, tf_graph_def)

    def _remove_batch_dimmension(self, root_name) -> bool:
        skipped = False
        try:
            # to remove batch dimmension information
            second_from_the_last, the_last = root_name.split('_')[-2], root_name.split('_')[-1]
            l = int(the_last)
            s = int(second_from_the_last)
            if l != s:
                skipped = True
        except:
            pass
        return skipped

    def _register_nodes(self, G: nx.DiGraph, tf_graph_def: dict) -> nx.DiGraph:
        nodes = tf_graph_def['node']
        graph_nodes: dict = {}
        for ele in nodes:
            if 'input' in ele.keys():
                names = ele['name'].split('/')
                root_name = names[0]
                if self._remove_batch_dimmension(root_name):
                    continue
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
                    elif 'enabled_node_nums' in i:
                        break
                    if i != root_name:
                        continued = False
                        break
                if continued:
                    continue
                if 'flatten' in root_name:
                    if len(ele['input']) == 1:
                        continue

                if not root_name in graph_nodes.keys():
                    graph_nodes[root_name] = {
                        'ancestor': []}
                if len(ele['input']) == 1:
                    ancestor = ele['input'][0]
                    graph_nodes[root_name]['ancestor'].append(ancestor)
                else:
                    ancestors = ele['input'][:-1]
                    graph_nodes[root_name]['ancestor'] += ancestors

        for name in graph_nodes:
            for s in self.SKIPED_ROOT_NAME_LIST_IN_GRAPH:
                if s in name:
                    break
            else:
                ancestors = list(set([i.split('/')[0] for
                                     i in graph_nodes[name]['ancestor']]))
                pruned_ancestors = []
                for a in ancestors:
                    if not self._remove_batch_dimmension(a):
                        pruned_ancestors.append(a)
                G.add_node(self.node_idx,
                           name=name,
                           ancestor=pruned_ancestors)
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
