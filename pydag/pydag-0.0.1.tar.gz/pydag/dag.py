import importlib
from copy import deepcopy
from datetime import datetime

from pydag.node import Node


class DAG:
    def __init__(self, module_path):
        self._module = importlib.import_module(module_path)
        self._nodes = list(self._load_nodes(self._module))

    @staticmethod
    def _load_nodes(module):
        for name in dir(module):
            attr = getattr(module, name)
            if isinstance(attr, Node):
                yield attr

    def run(self):
        # TODO: find the correct path
        return (node for node in self._nodes)

    @staticmethod
    def graph_metadata():
        date_time = datetime.utcnow()
        return {
            'date': date_time.strftime('%d/%m/%Y'),
            'time': date_time.strftime('%H:%M:%S'),
        }

    @staticmethod
    def graph_nodes(nodes):
        return {
            node.name: {'class_name': node.__class__.__name__}
            for node in nodes
        }

    @staticmethod
    def graph_edges(nodes):
        edges = list()
        for node in nodes:
            for target in node._next:
                edges.append({'source': node.name, 'target': target.name})
        return edges

    def to_dict(self):
        metadata = self.graph_metadata()
        nodes = self.graph_nodes(self._nodes)
        edges = self.graph_edges(self._nodes)
        return {'metadata': metadata, 'nodes': nodes, 'edges': edges}
