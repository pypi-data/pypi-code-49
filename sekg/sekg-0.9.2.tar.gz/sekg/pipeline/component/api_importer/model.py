import traceback

from sqlalchemy import Column, Integer, String, Text, MetaData, ForeignKey, Index, func, or_
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sekg.constant.code import CodeEntityCategory, CodeEntityRelationCategory

Base = declarative_base()
metadata = MetaData()


# api_relation_table = Table(
#     'java_api_relation', metadata,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("start_api_id", Integer, ForeignKey('java_all_api_entity.id'), nullable=False, index=True),
#     Column("end_api_id", Integer, ForeignKey('java_all_api_entity.id'), nullable=False, index=True),
#     Column("relation_type", Integer, index=True),
# )
# api_entity_table = Table(
#     'java_all_api_entity', metadata,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("api_type", Integer, index=True),
#     Column("qualified_name", String(1024), index=True),
#     Column("full_declaration", String(1024), nullable=True, index=True),
#     Column("short_description", Text(), nullable=True),
#     Column("added_in_version", String(128), nullable=True),
# )


class APIRelation(Base):
    __tablename__ = 'java_api_relation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_api_id = Column(Integer, ForeignKey('java_all_api_entity.id'), nullable=False, index=True)
    end_api_id = Column(Integer, ForeignKey('java_all_api_entity.id'), nullable=False, index=True)
    relation_type = Column(Integer, index=True)

    __table_args__ = (Index('unique_index', start_api_id, end_api_id, relation_type),
                      Index('all_relation_index', start_api_id, end_api_id),
                      {
                          "mysql_charset": "utf8",
                      })

    def __init__(self, start_api_id, end_api_id, relation_type):
        self.start_api_id = start_api_id
        self.end_api_id = end_api_id
        self.relation_type = relation_type

    def exist_in_remote(self, session):
        try:
            if session.query(APIRelation.id).filter_by(start_api_id=self.start_api_id,
                                                       end_api_id=self.end_api_id,
                                                       relation_type=self.relation_type).first():
                return True
            else:
                return False
        except Exception:
            traceback.print_exc()
            return False

    def get_remote_object(self, session):
        if self.id:
            return self
        else:
            try:
                return session.query(APIRelation).filter_by(start_api_id=self.start_api_id,
                                                            end_api_id=self.end_api_id,
                                                            relation_type=self.relation_type).first()
            except Exception:
                # traceback.print_exc()
                return None

    def find_or_create(self, session, autocommit=True):
        remote_instance = self.get_remote_object(session)
        if not remote_instance:
            session.add(self)
            if autocommit:
                session.commit()
            return self
        else:
            return remote_instance

    def __repr__(self):
        return '<APIRelation: %r-%r: type=%r >' % (self.start_api_id, self.end_api_id, self.relation_type)

    @staticmethod
    def get_api_relation_by_start_and_end_api_id(session, start_api_id, end_api_id):
        try:
            api_relation = session.query(APIRelation).filter_by(start_api_id=start_api_id,
                                                                end_api_id=end_api_id).first()
            return api_relation
        except Exception:
            traceback.print_exc()
            return None

    @staticmethod
    def get_type_string(relation_type):
        if relation_type in CodeEntityRelationCategory.category_code_to_str_map:
            return CodeEntityRelationCategory.category_code_to_str_map[relation_type]
        else:
            return ""

    @staticmethod
    def get_relation_by_relation_type(session, relation_type):
        try:
            return session.query(APIRelation).filter_by(relation_type=relation_type).all()
        except Exception:
            traceback.print_exc()
            return None


class APIEntity(Base):
    __tablename__ = 'java_all_api_entity'
    id = Column(Integer, primary_key=True, autoincrement=True)
    api_type = Column(Integer, index=True)
    qualified_name = Column(String(1024), index=True)
    full_declaration = Column(String(1024), nullable=True, index=True)
    short_description = Column(Text(), nullable=True)
    added_in_version = Column(String(128), nullable=True)

    out_relation = relationship('APIRelation', foreign_keys=[APIRelation.start_api_id],
                                backref='start_api')
    in_relation = relationship('APIRelation', foreign_keys=[APIRelation.end_api_id],
                               backref='end_api')

    __table_args__ = {
        "mysql_charset": "utf8"
    }

    def __init__(self, qualified_name, api_type, full_declaration=None, short_description=None, added_in_version=None):
        self.api_type = api_type
        self.qualified_name = qualified_name
        self.full_declaration = full_declaration
        self.short_description = short_description
        self.added_in_version = added_in_version

    def find_or_create(self, session, autocommit=True):
        if self.api_type == CodeEntityCategory.CATEGORY_PARAMETER or self.api_type == CodeEntityCategory.CATEGORY_RETURN_VALUE or self.api_type == CodeEntityCategory.CATEGORY_EXCEPTION_CONDITION:
            remote_instance = self.get_remote_parameter_object(session)
        else:
            remote_instance = self.get_remote_object(session)
        if not remote_instance:
            session.add(self)
            if autocommit:
                session.commit()
            return self
        else:
            return remote_instance

    def get_remote_object(self, session):
        if self.id:
            return self
        else:
            try:
                return session.query(APIEntity).filter(
                    APIEntity.qualified_name == func.binary(self.qualified_name)).first()
            except Exception:
                traceback.print_exc()
                return None

    def get_remote_parameter_object(self, session):
        if self.id:
            return self
        else:
            try:
                return session.query(APIEntity).filter_by(qualified_name=self.qualified_name,
                                                          full_declaration=self.full_declaration,
                                                          short_description=self.short_description).first()
            except Exception:
                traceback.print_exc()
                return None

    @staticmethod
    def exist(session, qualified_name):
        try:
            if session.query(APIEntity.id).filter(APIEntity.qualified_name == func.binary(qualified_name)).first():
                return True
            else:
                return False
        except Exception:
            traceback.print_exc()
            return None

    @staticmethod
    def find_by_id(session, api_entity_id):
        try:
            return session.query(APIEntity).filter(APIEntity.id == api_entity_id).first()
        except Exception:
            return None

    @staticmethod
    def find_by_qualifier(session, qualified_name):
        try:
            return session.query(APIEntity).filter(APIEntity.qualified_name == func.binary(qualified_name)).first()
        except Exception:
            traceback.print_exc()
            return None

    @staticmethod
    def find_by_full_declaration_and_description(session, full_declaration, description):
        try:
            return session.query(APIEntity).filter_by(full_declaration=func.binary(full_declaration),
                                                      short_description=description).first()
        except Exception:
            traceback.print_exc()
            return None

    @staticmethod
    def get_api_type_string(type):
        if type in CodeEntityCategory.category_code_to_str_list_map:
            return CodeEntityCategory.category_code_to_str_list_map[type]
        return []

    @staticmethod
    def get_simple_type_string(type):
        if type in CodeEntityCategory.category_code_to_str_map:
            return CodeEntityCategory.category_code_to_str_map[type]
        return ""

    def __repr__(self):
        return '<APIEntity: id=%r name=%r>' % (self.id, self.qualified_name)

    def __eq__(self, other):
        if isinstance(other, APIEntity):
            return self.id == other.id
        else:
            return False

    def __hash__(self):
        return hash(self.id)

    @staticmethod
    def get_api_id_list(session):
        try:
            return session.query(APIEntity.id).all()
        except Exception:
            traceback.print_exc()
            return None

    @staticmethod
    def get_api_id_and_qualified_name_list(session):
        try:
            return session.query(APIEntity.id, APIEntity.qualified_name).all()
        except Exception:
            traceback.print_exc()
            return None

    @staticmethod
    def get_all_API_entity(session):
        try:
            return session.query(APIEntity).all()
        except Exception:
            traceback.print_exc()
            return []

    @staticmethod
    def get_all_value_instance_api(session):
        try:
            return session.query(APIEntity).filter(
                or_(APIEntity.api_type == CodeEntityCategory.CATEGORY_EXCEPTION_CONDITION,
                    APIEntity.api_type == CodeEntityCategory.CATEGORY_PARAMETER,
                    APIEntity.api_type == CodeEntityCategory.CATEGORY_RETURN_VALUE)).all()
        except Exception:
            traceback.print_exc()
            return []

    @staticmethod
    def get_qualified_by_id(session, id):
        try:
            return session.query(APIEntity.qualified_name).filter_by(id=id).first()
        except Exception:
            traceback.print_exc()
            return None


class APIHTMLText(Base):
    __tablename__ = 'java_api_html_text'
    id = Column(Integer, primary_key=True, autoincrement=True)
    api_id = Column(Integer, ForeignKey('java_all_api_entity.id'), nullable=False)
    html = Column(LONGTEXT(), nullable=False)
    clean_text = Column(LONGTEXT(), nullable=True)  # text with no html tags
    reserve_part_tag_text = Column(LONGTEXT(), nullable=True)  # text with only code tags text
    html_type = Column(Integer, nullable=True)

    __table_args__ = (Index('api_id_text_type_index', api_id, html_type), {
        "mysql_charset": "utf8",
    })

    HTML_TYPE_UNKNOWN = 0
    HTML_TYPE_API_DECLARATION = 1
    HTML_TYPE_API_SHORT_DESCRIPTION = 2
    HTML_TYPE_API_DETAIL_DESCRIPTION = 3
    HTML_TYPE_METHOD_RETURN_VALUE_DESCRIPTION = 4

    def __init__(self, api_id, html, html_type=HTML_TYPE_UNKNOWN):
        self.api_id = api_id
        self.html = html
        self.html_type = html_type

    def create(self, session, autocommit=True):
        session.add(self)
        if autocommit:
            session.commit()
        return self

    @staticmethod
    def get_by_id(session, id):
        try:
            return session.query(APIHTMLText).filter_by(id=id).first()
        except Exception:
            traceback.print_exc()
            return None

    @staticmethod
    def get_text_by_api_id_and_type(session, api_id, html_type):
        try:
            return session.query(APIHTMLText.clean_text).filter_by(api_id=api_id, html_type=html_type).first()
        except Exception:
            traceback.print_exc()
            return None

    @staticmethod
    def get_remote_object(session, api_id, html_type):
        try:
            return session.query(APIHTMLText).filter_by(api_id=api_id, html_type=html_type).first()
        except Exception:
            traceback.print_exc()
            return None

    @staticmethod
    def get_html_text_id(session, api_id, html_type):
        try:
            return session.query(APIHTMLText.id).filter_by(api_id=api_id, html_type=html_type).first()
        except Exception:
            traceback.print_exc()
            return None

    @staticmethod
    def get_all_html_text_by_html_type(session, html_type):
        try:
            return session.query(APIHTMLText).filter_by(html_type=html_type).all()
        except Exception:
            traceback.print_exc()
            return None

    def find_or_create(self, session, autocommit=True):
        remote_instance = self.get_remote_object(session, api_id=self.api_id, html_type=self.html_type)
        if not remote_instance:
            session.add(self)
            if autocommit:
                session.commit()
            return self
        else:
            return remote_instance
