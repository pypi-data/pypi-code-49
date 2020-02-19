from sekg.graph.exporter.graph_data import GraphData
from sekg.graph.exporter.scheme_graph_data import SchemaGraphData
from sekg.ir.doc.wrapper import MultiFieldDocumentCollection
import matplotlib.pyplot as plt
from networkx import nx


class SchemaGraphUtil:
    """
    A tool to create schemaGraph based on GraphData/DocumentCollection
    """
    Entity_Type_Name_Prefix = "entity_type_"
    Relation_Has_Label = "has label"
    Relation_Has_Property = "has property"
    Relation_Has_Field = "has field"
    Relation_Start_Relation = "start"
    Relation_End_Relation = "end"
    label_2_color_map = {"entity_type": 1, "label": 0.8231, "document_field": 0.3714285714285714, "relation": 0.7,
                         "property": 0.66}

    def __init__(self, graph_data: GraphData = None, doc_collection: MultiFieldDocumentCollection = None, save_path=""):
        self.graph_data = graph_data
        self.doc_collection = doc_collection
        self.schema_graph = SchemaGraphData()
        self.schema_save_path = save_path
        self.entity_type_entity_id_index = 0
        self.entity_type_entity_key_id_map = dict()
        self.node_id_2_entity_type = dict()

    def create_related_index(self):
        self.schema_graph.create_index_on_property("unique_name")

    def create_relation_entity_nodes(self):
        relation_set = self.graph_data.get_all_relation_types()
        for relation_name in relation_set:
            self.schema_graph.add_relation_entity_node(relation_name)
        return True

    def create_doc_filed_entity_nodes(self):
        if self.doc_collection is None:
            print("doc_collection is None!")
            return
        for field_name in self.doc_collection.get_field_set():
            self.schema_graph.add_document_field_entity_node(field_name)
        return True

    def create_all_labels(self):
        label_set = self.graph_data.get_all_labels()
        for label in label_set:
            self.schema_graph.add_label_entity_node(label)
        return True

    def add_all_property_nodes(self):
        for node_id, node_json in self.graph_data.graph.nodes(data=True):
            if GraphData.DEFAULT_KEY_NODE_PROPERTIES in node_json:
                properties = node_json[GraphData.DEFAULT_KEY_NODE_PROPERTIES]
                for p in properties:
                    self.schema_graph.add_property_entity_node(p)
        return True

    def get_key(self, label_set):
        key = ""
        for label in label_set:
            key += (label + "&")
        return key

    def create_all_entity_types(self):
        """
        unique label set represent one entity type
        """
        for node_id, node_json in self.graph_data.graph.nodes(data=True):
            if GraphData.DEFAULT_KEY_NODE_LABELS in node_json:
                label_set = node_json[GraphData.DEFAULT_KEY_NODE_LABELS]
                key = self.get_key(label_set)
                if key in self.entity_type_entity_key_id_map:
                    self.node_id_2_entity_type[node_id] = self.entity_type_entity_key_id_map[key]
                    continue
                else:
                    self.entity_type_entity_key_id_map[key] = SchemaGraphUtil.Entity_Type_Name_Prefix + str(
                        self.entity_type_entity_id_index)
                    self.node_id_2_entity_type[node_id] = self.entity_type_entity_key_id_map[key]
                    self.entity_type_entity_id_index += 1
                    self.schema_graph.add_entity_type_entity_node(self.entity_type_entity_key_id_map[key])
        return True

    def link_entity_type_2_relations(self):
        all_relation_pairs = self.graph_data.get_relations()
        for start_node_id, relation_name, end_node_id in all_relation_pairs:
            relation_entity_node = self.schema_graph.find_relation_entity_node_by_name_en(relation_name)
            if relation_entity_node is None:
                print("relation_entity_node is None")
                continue
            start_entity_type = self.node_id_2_entity_type[start_node_id]
            start_entity_node = self.schema_graph.find_entity_type_entity_node_by_name_en(start_entity_type)
            if start_entity_type is None:
                print("start_entity_type is None")

            self.schema_graph.add_relation(start_entity_node["id"], SchemaGraphUtil.Relation_Start_Relation,
                                           relation_entity_node["id"])
            end_entity_type = self.node_id_2_entity_type[end_node_id]
            if end_entity_type is None:
                print("end_entity_type is None")
            end_entity_node = self.schema_graph.find_entity_type_entity_node_by_name_en(end_entity_type)
            self.schema_graph.add_relation(end_entity_node["id"], SchemaGraphUtil.Relation_End_Relation,
                                           relation_entity_node["id"])

    def link_entity_type_2_property_label(self):
        for node_id, node_json in self.graph_data.graph.nodes(data=True):
            if GraphData.DEFAULT_KEY_NODE_LABELS in node_json and GraphData.DEFAULT_KEY_NODE_PROPERTIES in node_json:
                label_set = node_json[GraphData.DEFAULT_KEY_NODE_LABELS]
                property_set = node_json[GraphData.DEFAULT_KEY_NODE_PROPERTIES]
                key = self.get_key(label_set)
                if key not in self.entity_type_entity_key_id_map:
                    print("must create_all_entity_types first")
                    continue
                entity_type_json = self.schema_graph.find_entity_type_entity_node_by_name_en(
                    self.entity_type_entity_key_id_map[key])
                if entity_type_json is None:
                    print("not find entity type")
                    continue
                for label in label_set:
                    label_node_json = self.schema_graph.find_label_entity_node_by_name_en(label)
                    if label_node_json is None:
                        print("not find label node")
                        continue
                    self.schema_graph.add_relation(entity_type_json["id"], SchemaGraphUtil.Relation_Has_Label,
                                                   label_node_json["id"])

                for property_name in property_set:
                    property_node_json = self.schema_graph.find_property_entity_node_by_name_en(property_name)
                    if property_node_json is None:
                        print("not find property node")
                        continue
                    self.schema_graph.add_relation(entity_type_json["id"],
                                                   SchemaGraphUtil.Relation_Has_Property,
                                                   property_node_json["id"])

    def link_entity_type_2_doc_filed(self):
        document_list = self.doc_collection.get_document_list()
        for i, document in enumerate(document_list):
            node_id = document.id
            field_set = document.get_field_set()
            entity_type_name = self.node_id_2_entity_type[node_id]
            entity_type_json = self.schema_graph.find_entity_type_entity_node_by_name_en(entity_type_name)
            if entity_type_json is None:
                print("not find entity type")
                continue

            for field in field_set:
                document_field_entity = self.schema_graph.find_document_field_entity_node_by_name_en(field)
                if document_field_entity is None:
                    print("document_field_entity is None")
                    continue
                self.schema_graph.add_relation(entity_type_json["id"], SchemaGraphUtil.Relation_Has_Field,
                                               document_field_entity["id"])

    def create_from_source(self):
        """
        try to create all node info from Graph and Doc
        :return:
        """
        self.add_all_property_nodes()
        self.create_relation_entity_nodes()
        self.create_doc_filed_entity_nodes()
        self.create_all_labels()
        self.create_all_entity_types()
        self.link_all_relation()

    def create_from_graph(self):
        """
        try to create all node info from Graph
        :return:
        """
        self.add_all_property_nodes()
        self.create_relation_entity_nodes()
        self.create_all_labels()
        self.create_all_entity_types()

    def create_from_doc(self):
        self.create_doc_filed_entity_nodes()

    def link_all_relation(self):
        self.link_graph_relation()
        self.link_doc_relation()

    def link_graph_relation(self):
        self.link_entity_type_2_property_label()
        self.link_entity_type_2_relations()

    def link_doc_relation(self):
        self.link_entity_type_2_doc_filed()

    def draw_schema_graph(self):
        G = self.schema_graph.graph
        labels = dict()
        val_map = dict()
        for n, d in G.nodes(data=True):
            labels[n] = d[SchemaGraphData.DEFAULT_KEY_NODE_PROPERTIES][
                SchemaGraphData.DEFAULT_KEY_PROPERTY_QUALIFIED_NAME]
            val_map[n] = SchemaGraphUtil.label_2_color_map[list(d[SchemaGraphData.DEFAULT_KEY_NODE_LABELS])[0]]
        values = [val_map.get(node, 0.25) for node in G.nodes()]
        pos = nx.spring_layout(G)
        edge_labels = {}

        all_relations = self.schema_graph.get_relations()
        for s, r, e in all_relations:
            edge_labels[(s, e)] = r

        nx.draw(G, pos=pos, labels=labels, alpha=0.9, node_size=1000,
                node_color=values,
                cmap=plt.get_cmap('viridis'), font_size=10,
                )
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)
        plt.show()

    def save(self):
        self.schema_graph.save(self.schema_save_path)
