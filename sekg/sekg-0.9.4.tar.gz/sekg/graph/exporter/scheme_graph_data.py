from sekg.graph.exporter.graph_data import GraphData


class BaseEntity:
    def __init__(self, name_en, name_zh, declaration, example):
        self.name_en = name_en
        self.name_zh = name_zh
        self.declaration = declaration
        self.example = example

    def get_all_properties(self):
        return {
            "name_en": self.name_en,
            "name_zh": self.name_zh,
            "declaration": self.declaration,
            "example": self.example
        }


class PropertyEntity(BaseEntity):
    name_prefix = "Property:"

    def __init__(self, name_en, name_zh="", declaration="", example=""):
        BaseEntity.__init__(self, name_en=name_en, name_zh=name_zh,
                            declaration=declaration, example=example)
        self.label = "property"

    def get_all_properties(self):
        res = BaseEntity.get_all_properties(self)
        res["unique_name"] = PropertyEntity.name_prefix + self.name_en
        return res


class RelationEntity(BaseEntity):
    name_prefix = "Relation:"

    def __init__(self, name_en, name_zh="", declaration="", example=""):
        BaseEntity.__init__(self, name_en=name_en, name_zh=name_zh,
                            declaration=declaration, example=example)
        self.label = "relation"

    def get_all_properties(self):
        res = BaseEntity.get_all_properties(self)
        res["unique_name"] = RelationEntity.name_prefix + self.name_en
        return res


class DocumentFieldEntity(BaseEntity):
    name_prefix = "DocumentField:"

    def __init__(self, name_en, name_zh="", declaration="", example=""):
        BaseEntity.__init__(self, name_en=name_en, name_zh=name_zh,
                            declaration=declaration, example=example)
        self.label = "document_field"

    def get_all_properties(self):
        res = BaseEntity.get_all_properties(self)
        res["unique_name"] = DocumentFieldEntity.name_prefix + self.name_en
        return res


class LabelEntity(BaseEntity):
    name_prefix = "Label:"

    def __init__(self, name_en, name_zh="", declaration="", example=""):
        BaseEntity.__init__(self, name_en=name_en, name_zh=name_zh,
                            declaration=declaration, example=example)
        self.label = "label"

    def get_all_properties(self):
        res = BaseEntity.get_all_properties(self)
        res["unique_name"] = LabelEntity.name_prefix + self.name_en
        return res


class EntityTypeEntity(BaseEntity):
    name_prefix = "EntityType:"

    def __init__(self, name_en, name_zh="", declaration="", example=""):
        BaseEntity.__init__(self, name_en=name_en, name_zh=name_zh,
                            declaration=declaration, example=example)
        self.label = "entity_type"

    def get_all_properties(self):
        res = BaseEntity.get_all_properties(self)
        res["unique_name"] = EntityTypeEntity.name_prefix + self.name_en
        return res


class SchemaGraphData(GraphData):
    """
    GraphData metadata class, store graph data property entity,relation entity,
    documentation filed entity, tag entity, entity type entity, and so on...

    support visualization
    """
    DEFAULT_KEY_PROPERTY_QUALIFIED_NAME = "unique_name"

    def __init__(self):
        GraphData.__init__(self)

    def add_property_entity_node(self, name_en, name_zh="", declaration="", example=""):
        property_entity = PropertyEntity(name_en, name_zh, declaration, example)
        return self.add_node({property_entity.label}, property_entity.get_all_properties(),
                             primary_property_name="unique_name")

    def find_property_entity_node_by_name_en(self, name_en):
        query_name = PropertyEntity.name_prefix + name_en
        return self.find_one_node_by_property("unique_name", query_name)

    def remove_property_entity_node(self, name_en):
        node_json = self.find_property_entity_node_by_name_en(name_en)
        if node_json is None:
            return None
        return self.remove_node(node_json["id"])

    def add_relation_entity_node(self, name_en, name_zh="", declaration="", example=""):
        entity = RelationEntity(name_en, name_zh, declaration, example)
        return self.add_node({entity.label}, entity.get_all_properties(),
                             primary_property_name="unique_name")

    def find_relation_entity_node_by_name_en(self, name_en):
        query_name = RelationEntity.name_prefix + name_en
        return self.find_one_node_by_property("unique_name", query_name)

    def remove_relation_entity_node(self, name_en):
        node_json = self.find_relation_entity_node_by_name_en(name_en)
        if node_json is None:
            return None
        return self.remove_node(node_json["id"])

    def add_document_field_entity_node(self, name_en, name_zh="", declaration="", example=""):
        entity = DocumentFieldEntity(name_en, name_zh, declaration, example)
        return self.add_node({entity.label}, entity.get_all_properties(),
                             primary_property_name="unique_name")

    def find_document_field_entity_node_by_name_en(self, name_en):
        query_name = DocumentFieldEntity.name_prefix + name_en
        return self.find_one_node_by_property("unique_name", query_name)

    def remove_document_field_entity_node(self, name_en):
        node_json = self.find_document_field_entity_node_by_name_en(name_en)
        if node_json is None:
            return None
        return self.remove_node(node_json["id"])

    def add_label_entity_node(self, name_en, name_zh="", declaration="", example=""):
        entity = LabelEntity(name_en, name_zh, declaration, example)
        return self.add_node({entity.label}, entity.get_all_properties(),
                             primary_property_name="unique_name")

    def find_label_entity_node_by_name_en(self, name_en):
        query_name = LabelEntity.name_prefix + name_en
        return self.find_one_node_by_property("unique_name", query_name)

    def remove_label_filed_entity_node(self, name_en):
        node_json = self.find_label_entity_node_by_name_en(name_en)
        if node_json is None:
            return None
        return self.remove_node(node_json["id"])

    def add_entity_type_entity_node(self, name_en, name_zh="", declaration="", example=""):
        entity = EntityTypeEntity(name_en, name_zh, declaration, example)
        return self.add_node({entity.label}, entity.get_all_properties(),
                             primary_property_name="unique_name")

    def find_entity_type_entity_node_by_name_en(self, name_en):
        query_name = EntityTypeEntity.name_prefix + name_en
        return self.find_one_node_by_property("unique_name", query_name)

    def remove_entity_type_filed_entity_node(self, name_en):
        node_json = self.find_entity_type_entity_node_by_name_en(name_en)
        if node_json is None:
            return None
        return self.remove_node(node_json["id"])
