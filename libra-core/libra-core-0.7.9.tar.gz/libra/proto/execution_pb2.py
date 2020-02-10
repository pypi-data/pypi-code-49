# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: execution.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import get_with_proof_pb2 as get__with__proof__pb2
import ledger_info_pb2 as ledger__info__pb2
import transaction_pb2 as transaction__pb2
import validator_set_pb2 as validator__set__pb2
import vm_errors_pb2 as vm__errors__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='execution.proto',
  package='execution',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0f\x65xecution.proto\x12\texecution\x1a\x14get_with_proof.proto\x1a\x11ledger_info.proto\x1a\x11transaction.proto\x1a\x13validator_set.proto\x1a\x0fvm_errors.proto\"p\n\x13\x45xecuteBlockRequest\x12.\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x18.types.SignedTransaction\x12\x17\n\x0fparent_block_id\x18\x02 \x01(\x0c\x12\x10\n\x08\x62lock_id\x18\x03 \x01(\x0c\"\x84\x01\n\x14\x45xecuteBlockResponse\x12\x11\n\troot_hash\x18\x01 \x01(\x0c\x12\x1f\n\x06status\x18\x02 \x03(\x0b\x32\x0f.types.VMStatus\x12\x0f\n\x07version\x18\x03 \x01(\x04\x12\'\n\nvalidators\x18\x04 \x01(\x0b\x32\x13.types.ValidatorSet\"T\n\x12\x43ommitBlockRequest\x12>\n\x15ledger_info_with_sigs\x18\x01 \x01(\x0b\x32\x1f.types.LedgerInfoWithSignatures\"C\n\x13\x43ommitBlockResponse\x12,\n\x06status\x18\x01 \x01(\x0e\x32\x1c.execution.CommitBlockStatus\"\x93\x01\n\x13\x45xecuteChunkRequest\x12<\n\x13txn_list_with_proof\x18\x01 \x01(\x0b\x32\x1f.types.TransactionListWithProof\x12>\n\x15ledger_info_with_sigs\x18\x02 \x01(\x0b\x32\x1f.types.LedgerInfoWithSignatures\"\x16\n\x14\x45xecuteChunkResponse*.\n\x11\x43ommitBlockStatus\x12\r\n\tSUCCEEDED\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x32\x81\x02\n\tExecution\x12Q\n\x0c\x45xecuteBlock\x12\x1e.execution.ExecuteBlockRequest\x1a\x1f.execution.ExecuteBlockResponse\"\x00\x12N\n\x0b\x43ommitBlock\x12\x1d.execution.CommitBlockRequest\x1a\x1e.execution.CommitBlockResponse\"\x00\x12Q\n\x0c\x45xecuteChunk\x12\x1e.execution.ExecuteChunkRequest\x1a\x1f.execution.ExecuteChunkResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[get__with__proof__pb2.DESCRIPTOR,ledger__info__pb2.DESCRIPTOR,transaction__pb2.DESCRIPTOR,validator__set__pb2.DESCRIPTOR,vm__errors__pb2.DESCRIPTOR,])

_COMMITBLOCKSTATUS = _descriptor.EnumDescriptor(
  name='CommitBlockStatus',
  full_name='execution.CommitBlockStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=706,
  serialized_end=752,
)
_sym_db.RegisterEnumDescriptor(_COMMITBLOCKSTATUS)

CommitBlockStatus = enum_type_wrapper.EnumTypeWrapper(_COMMITBLOCKSTATUS)
SUCCEEDED = 0
FAILED = 1



_EXECUTEBLOCKREQUEST = _descriptor.Descriptor(
  name='ExecuteBlockRequest',
  full_name='execution.ExecuteBlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='execution.ExecuteBlockRequest.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_block_id', full_name='execution.ExecuteBlockRequest.parent_block_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_id', full_name='execution.ExecuteBlockRequest.block_id', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=128,
  serialized_end=240,
)


_EXECUTEBLOCKRESPONSE = _descriptor.Descriptor(
  name='ExecuteBlockResponse',
  full_name='execution.ExecuteBlockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='root_hash', full_name='execution.ExecuteBlockResponse.root_hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='execution.ExecuteBlockResponse.status', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='execution.ExecuteBlockResponse.version', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validators', full_name='execution.ExecuteBlockResponse.validators', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=243,
  serialized_end=375,
)


_COMMITBLOCKREQUEST = _descriptor.Descriptor(
  name='CommitBlockRequest',
  full_name='execution.CommitBlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_info_with_sigs', full_name='execution.CommitBlockRequest.ledger_info_with_sigs', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=377,
  serialized_end=461,
)


_COMMITBLOCKRESPONSE = _descriptor.Descriptor(
  name='CommitBlockResponse',
  full_name='execution.CommitBlockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='execution.CommitBlockResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=463,
  serialized_end=530,
)


_EXECUTECHUNKREQUEST = _descriptor.Descriptor(
  name='ExecuteChunkRequest',
  full_name='execution.ExecuteChunkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txn_list_with_proof', full_name='execution.ExecuteChunkRequest.txn_list_with_proof', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ledger_info_with_sigs', full_name='execution.ExecuteChunkRequest.ledger_info_with_sigs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=533,
  serialized_end=680,
)


_EXECUTECHUNKRESPONSE = _descriptor.Descriptor(
  name='ExecuteChunkResponse',
  full_name='execution.ExecuteChunkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=682,
  serialized_end=704,
)

_EXECUTEBLOCKREQUEST.fields_by_name['transactions'].message_type = transaction__pb2._SIGNEDTRANSACTION
_EXECUTEBLOCKRESPONSE.fields_by_name['status'].message_type = vm__errors__pb2._VMSTATUS
_EXECUTEBLOCKRESPONSE.fields_by_name['validators'].message_type = validator__set__pb2._VALIDATORSET
_COMMITBLOCKREQUEST.fields_by_name['ledger_info_with_sigs'].message_type = ledger__info__pb2._LEDGERINFOWITHSIGNATURES
_COMMITBLOCKRESPONSE.fields_by_name['status'].enum_type = _COMMITBLOCKSTATUS
_EXECUTECHUNKREQUEST.fields_by_name['txn_list_with_proof'].message_type = transaction__pb2._TRANSACTIONLISTWITHPROOF
_EXECUTECHUNKREQUEST.fields_by_name['ledger_info_with_sigs'].message_type = ledger__info__pb2._LEDGERINFOWITHSIGNATURES
DESCRIPTOR.message_types_by_name['ExecuteBlockRequest'] = _EXECUTEBLOCKREQUEST
DESCRIPTOR.message_types_by_name['ExecuteBlockResponse'] = _EXECUTEBLOCKRESPONSE
DESCRIPTOR.message_types_by_name['CommitBlockRequest'] = _COMMITBLOCKREQUEST
DESCRIPTOR.message_types_by_name['CommitBlockResponse'] = _COMMITBLOCKRESPONSE
DESCRIPTOR.message_types_by_name['ExecuteChunkRequest'] = _EXECUTECHUNKREQUEST
DESCRIPTOR.message_types_by_name['ExecuteChunkResponse'] = _EXECUTECHUNKRESPONSE
DESCRIPTOR.enum_types_by_name['CommitBlockStatus'] = _COMMITBLOCKSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExecuteBlockRequest = _reflection.GeneratedProtocolMessageType('ExecuteBlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEBLOCKREQUEST,
  '__module__' : 'execution_pb2'
  # @@protoc_insertion_point(class_scope:execution.ExecuteBlockRequest)
  })
_sym_db.RegisterMessage(ExecuteBlockRequest)

ExecuteBlockResponse = _reflection.GeneratedProtocolMessageType('ExecuteBlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEBLOCKRESPONSE,
  '__module__' : 'execution_pb2'
  # @@protoc_insertion_point(class_scope:execution.ExecuteBlockResponse)
  })
_sym_db.RegisterMessage(ExecuteBlockResponse)

CommitBlockRequest = _reflection.GeneratedProtocolMessageType('CommitBlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMMITBLOCKREQUEST,
  '__module__' : 'execution_pb2'
  # @@protoc_insertion_point(class_scope:execution.CommitBlockRequest)
  })
_sym_db.RegisterMessage(CommitBlockRequest)

CommitBlockResponse = _reflection.GeneratedProtocolMessageType('CommitBlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMMITBLOCKRESPONSE,
  '__module__' : 'execution_pb2'
  # @@protoc_insertion_point(class_scope:execution.CommitBlockResponse)
  })
_sym_db.RegisterMessage(CommitBlockResponse)

ExecuteChunkRequest = _reflection.GeneratedProtocolMessageType('ExecuteChunkRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTECHUNKREQUEST,
  '__module__' : 'execution_pb2'
  # @@protoc_insertion_point(class_scope:execution.ExecuteChunkRequest)
  })
_sym_db.RegisterMessage(ExecuteChunkRequest)

ExecuteChunkResponse = _reflection.GeneratedProtocolMessageType('ExecuteChunkResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTECHUNKRESPONSE,
  '__module__' : 'execution_pb2'
  # @@protoc_insertion_point(class_scope:execution.ExecuteChunkResponse)
  })
_sym_db.RegisterMessage(ExecuteChunkResponse)



_EXECUTION = _descriptor.ServiceDescriptor(
  name='Execution',
  full_name='execution.Execution',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=755,
  serialized_end=1012,
  methods=[
  _descriptor.MethodDescriptor(
    name='ExecuteBlock',
    full_name='execution.Execution.ExecuteBlock',
    index=0,
    containing_service=None,
    input_type=_EXECUTEBLOCKREQUEST,
    output_type=_EXECUTEBLOCKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CommitBlock',
    full_name='execution.Execution.CommitBlock',
    index=1,
    containing_service=None,
    input_type=_COMMITBLOCKREQUEST,
    output_type=_COMMITBLOCKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ExecuteChunk',
    full_name='execution.Execution.ExecuteChunk',
    index=2,
    containing_service=None,
    input_type=_EXECUTECHUNKREQUEST,
    output_type=_EXECUTECHUNKRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXECUTION)

DESCRIPTOR.services_by_name['Execution'] = _EXECUTION

# @@protoc_insertion_point(module_scope)
