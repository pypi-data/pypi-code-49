from typing import List, Optional

from pydantic.main import BaseModel


class Schema(BaseModel):
    schemaname: str


class Enum(BaseModel):
    schemaname: str
    name: str
    elements: List[str]


class Relation(BaseModel):
    attname: str
    collation: Optional[str]
    comment: Optional[str]
    datatype: str
    datatypestring: str
    defaultdef: Optional[str]
    definition: Optional[str]
    enum_name: Optional[str]
    enum_schema: Optional[str]
    forcerowsecurity: bool
    is_enum: bool
    name: str
    not_null: bool
    oid: int
    parent_table: Optional[str]
    partition_def: Optional[str]
    position_number: int
    relationtype: str
    rowsecurity: str
    schemaname: str


class Index(BaseModel):
    definition: str
    extension_oid: Optional[int]
    is_clustered: bool
    is_exclusion: bool
    is_immediate: bool
    is_pk: bool
    is_unique: bool
    key_collations: Optional[List[int]]  # oidvector
    key_columns: str
    key_expressions: Optional[str]
    key_options: Optional[List[int]]  # int2vector
    name: str
    num_att: int
    oid: int
    partial_predicate: Optional[str]
    schemaname: str
    table_name: str


class Sequence(BaseModel):
    schemaname: str
    name: str


class Constraint(BaseModel):
    constraint_type: str
    definition: str
    extension_oid: Optional[int]
    index: Optional[str]
    name: str
    schemaname: str
    table_name: str


class Extension(BaseModel):
    name: str
    oid: int
    schemaname: str
    version: str


class Function(BaseModel):
    comment: str
    data_type: str
    definition: str
    extension_oid: int
    full_definition: str
    has_user_defined_returntype: bool
    identity_arguments: str
    language: str
    name: str
    oid: int
    parameter_default: str
    parameter_mode: str
    parameter_name: str
    position_number: int
    result_string: str
    returntype: str
    schemaname: str
    security_type: str
    strictness: str
    volatility: str


class Dep(BaseModel):
    identity_arguments: str
    identity_arguments_dependent_on: str
    name: str
    name_dependent_on: str
    objid: int
    objid_dependent_on: int
    schema_dependent_on: str
    schemaname: str


class Privilege(BaseModel):
    name: str
    object_type: str
    privilege: str
    schemaname: str
    user: str


class Trigger(BaseModel):
    enabled: str
    full_definition: str
    name: str
    proc_name: str
    proc_schema: str
    schemaname: str
    table_name: str


class Collation(BaseModel):
    encoding: int
    lc_collate: str
    lc_ctype: str
    name: str
    provider: str
    schemaname: str
    version: str


class RlsPolicy(BaseModel):
    commandtype: str
    name: str
    permissive: bool
    qual: Optional[str]
    roles: Optional[List[str]]
    schemaname: str
    table_name: str
    withcheck: Optional[str]


class Type(BaseModel):
    columns: str
    columnsjson: str  # json
    description: str
    internal_name: str
    name: str
    schemaname: str
    size: str


class Domain(BaseModel):
    check: str
    collation: str
    constraint_name: str
    data_type: str
    default: str
    name: str
    not_null: bool
    schemaname: str
