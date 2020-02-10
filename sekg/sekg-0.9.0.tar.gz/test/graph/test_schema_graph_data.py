from unittest import TestCase
from networkx import nx
from sekg.graph.exporter.graph_data import GraphData
from sekg.graph.exporter.scheme_graph_data import SchemaGraphData
from sekg.graph.exporter.scheme_graph_util import SchemaGraphUtil
from sekg.ir.doc.wrapper import MultiFieldDocumentCollection, MultiFieldDocument
import matplotlib.pyplot as plt

import pylab


class TestSchemaGraphData(TestCase):
    def test_schema_data(self):
        graph_data = SchemaGraphData()
        graph_data.add_property_entity_node(name_en="qualified_name", name_zh="全限定名", declaration="entity full name",
                                            example="java.lang.StringBuffer")
        match_node = graph_data.find_property_entity_node_by_name_en("qualified_name")
        print(match_node)
        self.assertEqual(match_node["properties"]["name_en"], "qualified_name")

    def create_graph_data(self):
        graph_data = GraphData()
        graph_data.create_index_on_property("qualified_name", "alias")

        graph_data.add_node({"method"}, {"qualified_name": "ArrayList.add"})
        graph_data.add_node({"override method"}, {"qualified_name": "ArrayList.pop"})
        graph_data.add_node({"method"}, {"qualified_name": "ArrayList.remove"})
        graph_data.add_node({"method"}, {"qualified_name": "ArrayList.clear", "alias": ["clear"]})
        graph_data.add_node({"method"},
                            {"qualified_name": "List.clear", "alias": ["clear", "List.clear", "List clear"]})
        graph_data.add_relation_with_property(1, "related to", 2, extra_info_key="as")
        graph_data.add_relation_with_property(1, "related to", 3, extra_info_key="ab")
        graph_data.add_relation_with_property(1, "related to", 4, extra_info_key="cs")
        graph_data.add_relation_with_property(2, "related to", 3, extra_info_key="ca")
        graph_data.add_relation_with_property(3, "related to", 4)

        return graph_data

    def create_doc_collection(self, graph_data):
        document_collection = MultiFieldDocumentCollection()
        for node_id, node_json in graph_data.graph.nodes(data=True):
            new_doc = MultiFieldDocument(id=node_id,
                                         name=node_json[GraphData.DEFAULT_KEY_NODE_PROPERTIES]["qualified_name"])
            new_doc.add_field("short_description", node_json[GraphData.DEFAULT_KEY_NODE_PROPERTIES]["qualified_name"])
            document_collection.add_document(new_doc)
        return document_collection

    def test_schema_graph_util_import(self):
        graph_data = self.create_graph_data()
        doc_collection = self.create_doc_collection(graph_data)
        save_path = ""
        schema_graph_util = SchemaGraphUtil(graph_data=graph_data, doc_collection=doc_collection, save_path=save_path)
        schema_graph_util.create_from_source()
        schema_graph_util.draw_schema_graph()

    def test_draw_test(self):
        G = nx.Graph()
        G.add_node('Golf', size='small')
        G.add_node('Hummer', size='huge')
        G.add_edge('Golf', 'Hummer')
        labels = dict((n, d['size']) for n, d in G.nodes(data=True))
        nx.draw(G, labels=labels, node_size=1000)
        pylab.show()

    def test_draw_diff_color(self):
        G = nx.Graph()
        G.add_edges_from(
            [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
             ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])

        val_map = {'A': 1.0,
                   'D': 0.5714285714285714,
                   'H': 0.0}

        values = [val_map.get(node, 0.25) for node in G.nodes()]
        nx.draw(G, cmap=plt.get_cmap('viridis'), node_color=values, with_labels=True, font_color='white')
        plt.show()
