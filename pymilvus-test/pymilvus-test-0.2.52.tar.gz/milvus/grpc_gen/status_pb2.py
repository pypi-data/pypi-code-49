# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='status.proto',
  package='milvus.grpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cstatus.proto\x12\x0bmilvus.grpc\"D\n\x06Status\x12*\n\nerror_code\x18\x01 \x01(\x0e\x32\x16.milvus.grpc.ErrorCode\x12\x0e\n\x06reason\x18\x02 \x01(\t*\xab\x04\n\tErrorCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x14\n\x10UNEXPECTED_ERROR\x10\x01\x12\x12\n\x0e\x43ONNECT_FAILED\x10\x02\x12\x15\n\x11PERMISSION_DENIED\x10\x03\x12\x14\n\x10TABLE_NOT_EXISTS\x10\x04\x12\x14\n\x10ILLEGAL_ARGUMENT\x10\x05\x12\x11\n\rILLEGAL_RANGE\x10\x06\x12\x15\n\x11ILLEGAL_DIMENSION\x10\x07\x12\x16\n\x12ILLEGAL_INDEX_TYPE\x10\x08\x12\x16\n\x12ILLEGAL_TABLE_NAME\x10\t\x12\x10\n\x0cILLEGAL_TOPK\x10\n\x12\x15\n\x11ILLEGAL_ROWRECORD\x10\x0b\x12\x15\n\x11ILLEGAL_VECTOR_ID\x10\x0c\x12\x19\n\x15ILLEGAL_SEARCH_RESULT\x10\r\x12\x12\n\x0e\x46ILE_NOT_FOUND\x10\x0e\x12\x0f\n\x0bMETA_FAILED\x10\x0f\x12\x10\n\x0c\x43\x41\x43HE_FAILED\x10\x10\x12\x18\n\x14\x43\x41NNOT_CREATE_FOLDER\x10\x11\x12\x16\n\x12\x43\x41NNOT_CREATE_FILE\x10\x12\x12\x18\n\x14\x43\x41NNOT_DELETE_FOLDER\x10\x13\x12\x16\n\x12\x43\x41NNOT_DELETE_FILE\x10\x14\x12\x15\n\x11\x42UILD_INDEX_ERROR\x10\x15\x12\x11\n\rILLEGAL_NLIST\x10\x16\x12\x17\n\x13ILLEGAL_METRIC_TYPE\x10\x17\x12\x11\n\rOUT_OF_MEMORY\x10\x18\x62\x06proto3')
)

_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='milvus.grpc.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNEXPECTED_ERROR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECT_FAILED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERMISSION_DENIED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TABLE_NOT_EXISTS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_ARGUMENT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_RANGE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_DIMENSION', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_INDEX_TYPE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_TABLE_NAME', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_TOPK', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_ROWRECORD', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_VECTOR_ID', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_SEARCH_RESULT', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILE_NOT_FOUND', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='META_FAILED', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CACHE_FAILED', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CREATE_FOLDER', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CREATE_FILE', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_DELETE_FOLDER', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_DELETE_FILE', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUILD_INDEX_ERROR', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_NLIST', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_METRIC_TYPE', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUT_OF_MEMORY', index=24, number=24,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=100,
  serialized_end=655,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)

ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
SUCCESS = 0
UNEXPECTED_ERROR = 1
CONNECT_FAILED = 2
PERMISSION_DENIED = 3
TABLE_NOT_EXISTS = 4
ILLEGAL_ARGUMENT = 5
ILLEGAL_RANGE = 6
ILLEGAL_DIMENSION = 7
ILLEGAL_INDEX_TYPE = 8
ILLEGAL_TABLE_NAME = 9
ILLEGAL_TOPK = 10
ILLEGAL_ROWRECORD = 11
ILLEGAL_VECTOR_ID = 12
ILLEGAL_SEARCH_RESULT = 13
FILE_NOT_FOUND = 14
META_FAILED = 15
CACHE_FAILED = 16
CANNOT_CREATE_FOLDER = 17
CANNOT_CREATE_FILE = 18
CANNOT_DELETE_FOLDER = 19
CANNOT_DELETE_FILE = 20
BUILD_INDEX_ERROR = 21
ILLEGAL_NLIST = 22
ILLEGAL_METRIC_TYPE = 23
OUT_OF_MEMORY = 24



_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='milvus.grpc.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='milvus.grpc.Status.error_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='milvus.grpc.Status.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=97,
)

_STATUS.fields_by_name['error_code'].enum_type = _ERRORCODE
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.enum_types_by_name['ErrorCode'] = _ERRORCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'status_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.Status)
  })
_sym_db.RegisterMessage(Status)


# @@protoc_insertion_point(module_scope)
