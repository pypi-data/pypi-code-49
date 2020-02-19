import json
from typing import Any, Text, Dict, Union

import sqlalchemy as sa
from sqlalchemy import UniqueConstraint, CheckConstraint
from sqlalchemy.orm import relationship


from ragex.community.database import utils
from ragex.community.database.base import Base

from sqlalchemy import Boolean, CheckConstraint, Column, Float, ForeignKey, Index, Integer, String, Table, Text, UniqueConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

metadata = Base.metadata

# class IntentResTemplate(Base):
#     """ intent에 대한 response type 별 응답 템플릿 저장
#         admin web에서 CRUD가 이루어짐
#     """
#     __tablename__ = "intent_res_template"
#
#     intent_id = sa.Column(sa.Integer,
#                           sa.ForeignKey("domain_intent.intent_id"), primary_key=True
#                           )
#     response_type = sa.Column(sa.String, primary_key=True, nullable=False)
#     domain_id = sa.Column(sa.Integer, sa.ForeignKey("domain.id"), nullable=False)
#     intent = sa.Column(sa.String, nullable=False, index=True )
#     UniqueConstraint('intent', 'response_type', name='unique_intent_nm_type')
#     use_yn = sa.Column(sa.String, nullable=False)
#     CheckConstraint('( (use_yn in ("Y", "N")) and check_use_yn(intent_id, use_yn) = 0 )', name='check_id_unique_y')
#     CheckConstraint('response_type in ( "1", "2", "3", "4", "5", "6", "7", "8" , "9", "10" )', name='check_response_type_range')
#     response_template = sa.Column(sa.String, nullable=False)

class IntentResTemplate(Base):
    """ intent에 대한 response type 별 응답 템플릿 저장
           admin web에서 CRUD가 이루어짐
       """
    __tablename__ = 'intent_res_template'
    __table_args__ = (
        CheckConstraint("((use_yn)::text = ANY (ARRAY[('Y'::character varying)::text, ('N'::character varying)::text])) AND (check_use_yn(intent, use_yn, response_type) = 0)"),
        CheckConstraint("(response_type)::text = ANY (ARRAY[('1'::character varying)::text, ('2'::character varying)::text, ('3'::character varying)::text, ('4'::character varying)::text, ('5'::character varying)::text])"),
    )

    intent = Column(String(255), primary_key=True, nullable=False)
    use_yn = Column(String(1), server_default=text("'N'::character varying"))
    response_type = Column(String(1), primary_key=True, nullable=False)
    response_template = Column(Text)

    def as_dict(self) -> Dict[Text, Any]:
        return {

            "intent": self.intent,
            "use_yn": self.use_yn,
            "response_type": self.response_type,
            "response_template": self.response_template,

        }