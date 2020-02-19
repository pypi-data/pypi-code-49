#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author: isky
@Email: 19110240019@fudan.edu.cn
@Created: 2019/10/28
------------------------------------------
@Modify: 2019/11/18
------------------------------------------
@Description: A file for import the API entity table from the database to the graph
"""
from sekg.constant.code import CodeEntityCategory, CodeEntityRelationCategory
from sekg.constant.constant import CodeConstant
from sekg.graph.builder.code_kg_builder import CodeElementGraphDataBuilder
from sekg.graph.creator import NodeBuilder
from sekg.graph.exporter.graph_data import GraphData

from sekg.pipeline.component.api_importer.model import APIRelation, APIEntity
from sekg.pipeline.component.base import Component


class APIDBImporterComponent(Component):
    LABEL_CODE_ELEMENT = "code_element"
    SUPPORT_LANGUAGE_JAVA = "java"
    SUPPORT_LANGUAGE_C_SHARP = "c#"

    def provided_entities(self):
        entity_labels = set()
        entity_labels.add(APIDBImporterComponent.LABEL_CODE_ELEMENT)
        category_codes = CodeEntityCategory.category_code_to_str_list_map.keys()
        for category_code in category_codes:
            entity_labels.update(set(CodeEntityCategory.to_str_list(category_code)))
        return entity_labels
        # TODO: add interface for the constant

    def dependent_entities(self):
        return set()

    def provided_relations(self):
        relations = set()
        category_codes = CodeEntityRelationCategory.category_code_to_str_map.keys()
        for category_code in category_codes:
            relations.add(CodeEntityRelationCategory.to_str(category_code))
        return relations
        # TODO: add interface for the constant

    def dependent_relations(self):
        return set()

    def provided_document_fields(self):
        return set()

    def dependent_document_fields(self):
        return set()

    # filter_entity_type_set 是一个存放entity type对应数字的集合，把对应的类型过滤掉
    # filter_entity_type_set 是一个存放relation type对应数字的集合，把对应的类型过滤掉

    def __init__(
            self, graph_data=None, session=None, api_entity_table_name=None, api_relation_table_name=None,
            pro_name=None, do_import_primary_type=True, do_infer_extra_relation=True, do_build_aliases=True,
            filter_entity_type_set=None, filter_relation_type_set=None, language=SUPPORT_LANGUAGE_JAVA
    ):
        super().__init__(graph_data)
        if graph_data is None:
            self.graph_data = GraphData()
        self.do_import_primary_type = do_import_primary_type
        self.do_infer_extra_relation = do_infer_extra_relation
        self.do_build_aliases = do_build_aliases
        self.api_entity_table_name = api_entity_table_name
        self.api_relation_table_name = api_relation_table_name
        self.session = session
        self.api_entity_type = None
        self.api_relation_type = None
        self.pro_name = pro_name
        self.code_element_kg_builder = CodeElementGraphDataBuilder(self.graph_data)
        self.language = language
        if filter_entity_type_set is not None:
            self.filter_entity_type_set = filter_entity_type_set
        else:
            self.filter_entity_type_set = set()
        if filter_relation_type_set is not None:
            self.filter_relation_type_set = filter_relation_type_set
        else:
            self.filter_relation_type_set = set()

    def run(self, **config):
        print("running component %r" % (self.type()))
        print("import API entities from table %r" % self.api_entity_table_name)
        print("import API entity relations from table %r" % self.api_relation_table_name)
        self.api_entity_type = APIEntity
        self.api_entity_type.__table__.name = self.api_entity_table_name
        self.api_relation_type = APIRelation
        self.api_relation_type.__table__.name = self.api_relation_table_name
        if self.do_import_primary_type:
            self.import_primary_type()
        api_id_to_node_id_map = self.import_entity_from_api_table()
        self.import_relation_from_table(self.session, api_id_to_node_id_map)
        if self.do_infer_extra_relation:
            self.infer_extra_relation()
        if self.do_build_aliases:
            self.build_aliases()
        self.add_source_label(self.pro_name)

    def before_run(self, **config):
        super().before_run(**config)
        print("before running component %r" % (self.type()))

    def add_source_label(self, source_label):
        """
        给来自不同项目的API打上不同的标签
        :param source_label:
        :return:
        """
        self.code_element_kg_builder.add_source_label(source_label)

    def import_entity_from_api_table(self):
        """
        从数据库表中读取所有的API实体，添加到graphData当中
        """
        print("start api from table")
        api_entity_list = self.session.query(self.api_entity_type).all()
        api_id_to_node_id_map = {}
        for i, entity_info_row in enumerate(api_entity_list):
            api_entity_json = dict(entity_info_row.__dict__)
            api_entity_json.pop('_sa_instance_state', None)
            api_id = api_entity_json["id"]
            qualified_name = api_entity_json[CodeConstant.QUALIFIED_NAME]
            api_type = api_entity_json["api_type"]
            # 过滤掉一些不想要的api类型
            if api_type in self.filter_entity_type_set:
                continue

            normal_entity_types = {
                CodeEntityCategory.CATEGORY_CLASS,
                CodeEntityCategory.CATEGORY_PACKAGE,
                CodeEntityCategory.CATEGORY_METHOD,
                CodeEntityCategory.CATEGORY_INTERFACE,
                CodeEntityCategory.CATEGORY_EXCEPTION_CLASS,
                CodeEntityCategory.CATEGORY_ENUM_CLASS,
                CodeEntityCategory.CATEGORY_ERROR_CLASS,
                CodeEntityCategory.CATEGORY_ANNOTATION_CLASS,
            }
            node_id = GraphData.UNASSIGNED_NODE_ID
            if api_type in normal_entity_types:
                node_id = self.import_normal_entity(api_entity_json)
            if api_type == CodeEntityCategory.CATEGORY_CONSTRUCT_METHOD:
                node_id = self.import_construct_method_entity(api_entity_json)

            if api_type == CodeEntityCategory.CATEGORY_FIELD_OF_CLASS:
                node_id = self.import_qualified_field_entity(api_entity_json)

            if api_type == CodeEntityCategory.CATEGORY_ENUM_CONSTANTS:
                node_id = self.import_qualified_enum_constants_entity(api_entity_json)
            if api_type == CodeEntityCategory.CATEGORY_PRIMARY_TYPE:
                node_id = self.add_primary_type(primary_type_name=qualified_name, **api_entity_json)

            if api_type == CodeEntityCategory.CATEGORY_PARAMETER:
                node_id = self.import_parameter_entity(api_entity_json)
            if api_type == CodeEntityCategory.CATEGORY_RETURN_VALUE:
                node_id = self.import_return_value_entity(api_entity_json)
            if api_type == CodeEntityCategory.CATEGORY_EXCEPTION_CONDITION:
                node_id = self.import_exception_condition_entity(api_entity_json)
            if node_id == GraphData.UNASSIGNED_NODE_ID:
                print("Adding fail %d %s %r " % (api_id, qualified_name, CodeEntityCategory.to_str(api_type)))
                continue
            api_id_to_node_id_map[api_id] = node_id

        self.graph_data.print_graph_info()
        print("end import from api_table ")

        return api_id_to_node_id_map

    def import_relation_from_table(self, session, api_id_to_node_id_map):
        """
        :param session: 数据库连接session
        :param api_id_to_node_id_map: 数据库api_id到nodeId的映射map
        :return:
        """
        print("start import relation")
        self.graph_data.print_graph_info()

        valid_api_types = CodeEntityRelationCategory.relation_set()
        valid_api_types = valid_api_types - self.filter_relation_type_set
        for relation_type in valid_api_types:
            relation_str = CodeEntityRelationCategory.to_str(relation_type)
            print("start import_test relation %s" % (relation_str))
            api_relation_list = session.query(self.api_relation_type).filter(
                self.api_relation_type.relation_type == relation_type).all()
            for relation in api_relation_list:
                if relation.start_api_id not in api_id_to_node_id_map:
                    print("start_id %d can't found its node id" % (relation.start_api_id))
                    continue
                if relation.end_api_id not in api_id_to_node_id_map:
                    print("end_id %d can't found its node id" % (relation.end_api_id))
                    continue
                self.graph_data.add_relation(startId=api_id_to_node_id_map[relation.start_api_id],
                                             endId=api_id_to_node_id_map[relation.end_api_id],
                                             relationType=relation_str)
        print("end import relation")
        self.graph_data.print_graph_info()

    def after_run(self, **config):
        super().before_run(**config)
        print("after running component %r" % (self.type()))

    def import_normal_entity(self, api_entity_json):

        format_qualified_name = self.code_element_kg_builder.format_qualified_name(
            api_entity_json[CodeConstant.QUALIFIED_NAME])

        if not format_qualified_name:
            return
        api_entity_json.pop(CodeConstant.QUALIFIED_NAME)
        node_id = self.code_element_kg_builder.add_normal_code_element_entity(format_qualified_name,
                                                                              api_entity_json["api_type"],
                                                                              **api_entity_json)
        return node_id

    def import_parameter_entity(self, api_entity_json):
        extra_properties = {}

        qualified_name = api_entity_json[CodeConstant.QUALIFIED_NAME]
        short_description = api_entity_json["short_description"]

        value_type = qualified_name.split(" ")[0].strip()
        value_name = qualified_name.split(" ")[1].strip()
        node_id = self.code_element_kg_builder.add_base_value_entity_node(value_type=value_type, value_name=value_name,
                                                                          short_description=short_description,
                                                                          entity_category=CodeEntityCategory.CATEGORY_PARAMETER,
                                                                          **extra_properties)

        if node_id == GraphData.UNASSIGNED_NODE_ID:
            print("fail to add parameter node %r" % (api_entity_json))

        return node_id

    def import_return_value_entity(self, api_entity_json):
        extra_properties = {}

        qualified_name = api_entity_json[CodeConstant.QUALIFIED_NAME]
        short_description = api_entity_json["short_description"]

        value_type = qualified_name.split(" ")[0].strip()
        node_id = self.code_element_kg_builder.add_base_value_entity_node(value_type=value_type, value_name="<R>",
                                                                          short_description=short_description,
                                                                          entity_category=CodeEntityCategory.CATEGORY_RETURN_VALUE,
                                                                          **extra_properties)

        if node_id == GraphData.UNASSIGNED_NODE_ID:
            print("fail to add parameter node %r" % (api_entity_json))

        return node_id

    def import_exception_condition_entity(self, api_entity_json):
        extra_properties = {}

        qualified_name = api_entity_json[CodeConstant.QUALIFIED_NAME]
        short_description = api_entity_json["short_description"]

        value_type = qualified_name.split(" ")[0].strip()
        node_id = self.code_element_kg_builder.add_base_value_entity_node \
            (value_type=value_type, value_name="<E>",
             short_description=short_description,
             entity_category=CodeEntityCategory.CATEGORY_EXCEPTION_CONDITION,
             **extra_properties)

        if node_id == GraphData.UNASSIGNED_NODE_ID:
            print("fail to add parameter node %r" % (api_entity_json))

        return node_id

    def import_construct_method_entity(self, api_entity_json):

        format_qualified_name = self.code_element_kg_builder.format_qualified_name(
            api_entity_json[CodeConstant.QUALIFIED_NAME])

        method_name = self.code_element_kg_builder.parse_construct_to_javaparser_style(format_qualified_name)

        if not method_name:
            return GraphData.UNASSIGNED_NODE_ID

        api_entity_json.pop(CodeConstant.QUALIFIED_NAME)
        node_id = self.code_element_kg_builder.add_normal_code_element_entity(method_name,
                                                                              api_entity_json["api_type"],
                                                                              **api_entity_json)

        return node_id

    def import_qualified_field_entity(self, api_entity_json):

        qualified_name = self.code_element_kg_builder.format_qualified_name(
            api_entity_json[CodeConstant.QUALIFIED_NAME])
        if not qualified_name:
            print(
                "import_qualified_field_entity %r %r" % (api_entity_json[CodeConstant.QUALIFIED_NAME], api_entity_json))
            return GraphData.UNASSIGNED_NODE_ID

        api_entity_json.pop(CodeConstant.QUALIFIED_NAME)
        api_entity_json.pop("api_type")

        node_id = self.code_element_kg_builder.add_normal_code_element_entity(qualified_name,
                                                                              CodeEntityCategory.CATEGORY_FIELD_OF_CLASS,
                                                                              **api_entity_json)

        return node_id

    def import_qualified_enum_constants_entity(self, api_entity_json):

        qualified_name = self.code_element_kg_builder.format_qualified_name(
            api_entity_json[CodeConstant.QUALIFIED_NAME])
        if not qualified_name:
            print(
                "import_qualified_field_entity %r %r" % (api_entity_json[CodeConstant.QUALIFIED_NAME], api_entity_json))
            return GraphData.UNASSIGNED_NODE_ID

        api_entity_json.pop(CodeConstant.QUALIFIED_NAME)
        api_entity_json.pop("api_type")

        node_id = self.code_element_kg_builder.add_normal_code_element_entity(qualified_name,
                                                                              CodeEntityCategory.CATEGORY_ENUM_CONSTANTS,
                                                                              **api_entity_json)

        return node_id

    def add_primary_type(self, primary_type_name, **properties):
        """
        添加一些默认的基础数据类型
        """
        properties[CodeConstant.QUALIFIED_NAME] = primary_type_name

        cate_labels = CodeEntityCategory.to_str_list(CodeEntityCategory.CATEGORY_PRIMARY_TYPE)
        builder = NodeBuilder()
        builder = builder.add_property(**properties).add_entity_label().add_labels(
            APIDBImporterComponent.LABEL_CODE_ELEMENT, *cate_labels)
        node_id = self.graph_data.add_node(
            node_id=GraphData.UNASSIGNED_NODE_ID,
            node_labels=builder.get_labels(),
            node_properties=builder.get_properties(),
            primary_property_name=CodeConstant.QUALIFIED_NAME)
        return node_id

    def import_primary_type(self):
        # todo: this is a not wrong. should be a config of the component, language.
        type_list = []
        if self.language == APIDBImporterComponent.SUPPORT_LANGUAGE_JAVA:
            type_list = CodeEntityCategory.java_primary_types()
        if self.language == APIDBImporterComponent.SUPPORT_LANGUAGE_C_SHARP:
            type_list = CodeEntityCategory.net_primary_types()

        for item in type_list:
            code_element = {
                CodeConstant.QUALIFIED_NAME: item["name"],
                "api_type": CodeEntityCategory.CATEGORY_PRIMARY_TYPE,
                "short_description": item["description"]
            }
            self.add_primary_type(item["name"], **code_element)

        print(self.graph_data)
        self.graph_data.print_label_count()

    def build_aliases(self):
        """
        为API添加别名信息
        """
        self.code_element_kg_builder.build_aliases_for_code_element()
        self.graph_data.refresh_indexer()

    def infer_extra_relation(self):
        self.code_element_kg_builder.build_belong_to_relation()
        self.code_element_kg_builder.build_abstract_overloading_relation()
        self.code_element_kg_builder.build_belong_to_relation()
        self.code_element_kg_builder.build_override_relation()

    def save(self, path):
        self.graph_data.save(path)
