# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_with_proof.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import access_path_pb2 as access__path__pb2
import account_state_blob_pb2 as account__state__blob__pb2
import events_pb2 as events__pb2
import ledger_info_pb2 as ledger__info__pb2
import proof_pb2 as proof__pb2
import transaction_pb2 as transaction__pb2
import validator_change_pb2 as validator__change__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_with_proof.proto',
  package='types',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14get_with_proof.proto\x12\x05types\x1a\x11\x61\x63\x63\x65ss_path.proto\x1a\x18\x61\x63\x63ount_state_blob.proto\x1a\x0c\x65vents.proto\x1a\x11ledger_info.proto\x1a\x0bproof.proto\x1a\x11transaction.proto\x1a\x16validator_change.proto\"h\n\x1bUpdateToLatestLedgerRequest\x12\x1c\n\x14\x63lient_known_version\x18\x01 \x01(\x04\x12+\n\x0frequested_items\x18\x02 \x03(\x0b\x32\x12.types.RequestItem\"\xf7\x02\n\x0bRequestItem\x12\x42\n\x19get_account_state_request\x18\x01 \x01(\x0b\x32\x1d.types.GetAccountStateRequestH\x00\x12q\n2get_account_transaction_by_sequence_number_request\x18\x02 \x01(\x0b\x32\x33.types.GetAccountTransactionBySequenceNumberRequestH\x00\x12[\n\'get_events_by_event_access_path_request\x18\x03 \x01(\x0b\x32(.types.GetEventsByEventAccessPathRequestH\x00\x12\x41\n\x18get_transactions_request\x18\x04 \x01(\x0b\x32\x1d.types.GetTransactionsRequestH\x00\x42\x11\n\x0frequested_items\"\x8e\x02\n\x1cUpdateToLatestLedgerResponse\x12+\n\x0eresponse_items\x18\x01 \x03(\x0b\x32\x13.types.ResponseItem\x12>\n\x15ledger_info_with_sigs\x18\x02 \x01(\x0b\x32\x1f.types.LedgerInfoWithSignatures\x12;\n\x16validator_change_proof\x18\x03 \x01(\x0b\x32\x1b.types.ValidatorChangeProof\x12\x44\n\x18ledger_consistency_proof\x18\x04 \x01(\x0b\x32\".types.AccumulatorConsistencyProof\"\xff\x02\n\x0cResponseItem\x12\x44\n\x1aget_account_state_response\x18\x03 \x01(\x0b\x32\x1e.types.GetAccountStateResponseH\x00\x12s\n3get_account_transaction_by_sequence_number_response\x18\x04 \x01(\x0b\x32\x34.types.GetAccountTransactionBySequenceNumberResponseH\x00\x12]\n(get_events_by_event_access_path_response\x18\x05 \x01(\x0b\x32).types.GetEventsByEventAccessPathResponseH\x00\x12\x43\n\x19get_transactions_response\x18\x06 \x01(\x0b\x32\x1e.types.GetTransactionsResponseH\x00\x42\x10\n\x0eresponse_items\")\n\x16GetAccountStateRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\"Y\n\x17GetAccountStateResponse\x12>\n\x18\x61\x63\x63ount_state_with_proof\x18\x01 \x01(\x0b\x32\x1c.types.AccountStateWithProof\"n\n,GetAccountTransactionBySequenceNumberRequest\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0c\x12\x17\n\x0fsequence_number\x18\x02 \x01(\x04\x12\x14\n\x0c\x66\x65tch_events\x18\x03 \x01(\x08\"\xb4\x01\n-GetAccountTransactionBySequenceNumberResponse\x12;\n\x16transaction_with_proof\x18\x02 \x01(\x0b\x32\x1b.types.TransactionWithProof\x12\x46\n proof_of_current_sequence_number\x18\x03 \x01(\x0b\x32\x1c.types.AccountStateWithProof\"\x8a\x01\n!GetEventsByEventAccessPathRequest\x12&\n\x0b\x61\x63\x63\x65ss_path\x18\x01 \x01(\x0b\x32\x11.types.AccessPath\x12\x1b\n\x13start_event_seq_num\x18\x02 \x01(\x04\x12\x11\n\tascending\x18\x03 \x01(\x08\x12\r\n\x05limit\x18\x04 \x01(\x04\"\x93\x01\n\"GetEventsByEventAccessPathResponse\x12\x30\n\x11\x65vents_with_proof\x18\x01 \x03(\x0b\x32\x15.types.EventWithProof\x12;\n\x15proof_of_latest_event\x18\x02 \x01(\x0b\x32\x1c.types.AccountStateWithProof\"T\n\x16GetTransactionsRequest\x12\x15\n\rstart_version\x18\x01 \x01(\x04\x12\r\n\x05limit\x18\x02 \x01(\x04\x12\x14\n\x0c\x66\x65tch_events\x18\x03 \x01(\x08\"W\n\x17GetTransactionsResponse\x12<\n\x13txn_list_with_proof\x18\x01 \x01(\x0b\x32\x1f.types.TransactionListWithProofb\x06proto3')
  ,
  dependencies=[access__path__pb2.DESCRIPTOR,account__state__blob__pb2.DESCRIPTOR,events__pb2.DESCRIPTOR,ledger__info__pb2.DESCRIPTOR,proof__pb2.DESCRIPTOR,transaction__pb2.DESCRIPTOR,validator__change__pb2.DESCRIPTOR,])




_UPDATETOLATESTLEDGERREQUEST = _descriptor.Descriptor(
  name='UpdateToLatestLedgerRequest',
  full_name='types.UpdateToLatestLedgerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_known_version', full_name='types.UpdateToLatestLedgerRequest.client_known_version', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requested_items', full_name='types.UpdateToLatestLedgerRequest.requested_items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=165,
  serialized_end=269,
)


_REQUESTITEM = _descriptor.Descriptor(
  name='RequestItem',
  full_name='types.RequestItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='get_account_state_request', full_name='types.RequestItem.get_account_state_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_account_transaction_by_sequence_number_request', full_name='types.RequestItem.get_account_transaction_by_sequence_number_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_events_by_event_access_path_request', full_name='types.RequestItem.get_events_by_event_access_path_request', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_transactions_request', full_name='types.RequestItem.get_transactions_request', index=3,
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
    _descriptor.OneofDescriptor(
      name='requested_items', full_name='types.RequestItem.requested_items',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=272,
  serialized_end=647,
)


_UPDATETOLATESTLEDGERRESPONSE = _descriptor.Descriptor(
  name='UpdateToLatestLedgerResponse',
  full_name='types.UpdateToLatestLedgerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_items', full_name='types.UpdateToLatestLedgerResponse.response_items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ledger_info_with_sigs', full_name='types.UpdateToLatestLedgerResponse.ledger_info_with_sigs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validator_change_proof', full_name='types.UpdateToLatestLedgerResponse.validator_change_proof', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ledger_consistency_proof', full_name='types.UpdateToLatestLedgerResponse.ledger_consistency_proof', index=3,
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
  serialized_start=650,
  serialized_end=920,
)


_RESPONSEITEM = _descriptor.Descriptor(
  name='ResponseItem',
  full_name='types.ResponseItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='get_account_state_response', full_name='types.ResponseItem.get_account_state_response', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_account_transaction_by_sequence_number_response', full_name='types.ResponseItem.get_account_transaction_by_sequence_number_response', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_events_by_event_access_path_response', full_name='types.ResponseItem.get_events_by_event_access_path_response', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_transactions_response', full_name='types.ResponseItem.get_transactions_response', index=3,
      number=6, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='response_items', full_name='types.ResponseItem.response_items',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=923,
  serialized_end=1306,
)


_GETACCOUNTSTATEREQUEST = _descriptor.Descriptor(
  name='GetAccountStateRequest',
  full_name='types.GetAccountStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='types.GetAccountStateRequest.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=1308,
  serialized_end=1349,
)


_GETACCOUNTSTATERESPONSE = _descriptor.Descriptor(
  name='GetAccountStateResponse',
  full_name='types.GetAccountStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_state_with_proof', full_name='types.GetAccountStateResponse.account_state_with_proof', index=0,
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
  serialized_start=1351,
  serialized_end=1440,
)


_GETACCOUNTTRANSACTIONBYSEQUENCENUMBERREQUEST = _descriptor.Descriptor(
  name='GetAccountTransactionBySequenceNumberRequest',
  full_name='types.GetAccountTransactionBySequenceNumberRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='types.GetAccountTransactionBySequenceNumberRequest.account', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='types.GetAccountTransactionBySequenceNumberRequest.sequence_number', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fetch_events', full_name='types.GetAccountTransactionBySequenceNumberRequest.fetch_events', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1442,
  serialized_end=1552,
)


_GETACCOUNTTRANSACTIONBYSEQUENCENUMBERRESPONSE = _descriptor.Descriptor(
  name='GetAccountTransactionBySequenceNumberResponse',
  full_name='types.GetAccountTransactionBySequenceNumberResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_with_proof', full_name='types.GetAccountTransactionBySequenceNumberResponse.transaction_with_proof', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proof_of_current_sequence_number', full_name='types.GetAccountTransactionBySequenceNumberResponse.proof_of_current_sequence_number', index=1,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1555,
  serialized_end=1735,
)


_GETEVENTSBYEVENTACCESSPATHREQUEST = _descriptor.Descriptor(
  name='GetEventsByEventAccessPathRequest',
  full_name='types.GetEventsByEventAccessPathRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_path', full_name='types.GetEventsByEventAccessPathRequest.access_path', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_event_seq_num', full_name='types.GetEventsByEventAccessPathRequest.start_event_seq_num', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ascending', full_name='types.GetEventsByEventAccessPathRequest.ascending', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='types.GetEventsByEventAccessPathRequest.limit', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_start=1738,
  serialized_end=1876,
)


_GETEVENTSBYEVENTACCESSPATHRESPONSE = _descriptor.Descriptor(
  name='GetEventsByEventAccessPathResponse',
  full_name='types.GetEventsByEventAccessPathResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events_with_proof', full_name='types.GetEventsByEventAccessPathResponse.events_with_proof', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proof_of_latest_event', full_name='types.GetEventsByEventAccessPathResponse.proof_of_latest_event', index=1,
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
  serialized_start=1879,
  serialized_end=2026,
)


_GETTRANSACTIONSREQUEST = _descriptor.Descriptor(
  name='GetTransactionsRequest',
  full_name='types.GetTransactionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_version', full_name='types.GetTransactionsRequest.start_version', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='types.GetTransactionsRequest.limit', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fetch_events', full_name='types.GetTransactionsRequest.fetch_events', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=2028,
  serialized_end=2112,
)


_GETTRANSACTIONSRESPONSE = _descriptor.Descriptor(
  name='GetTransactionsResponse',
  full_name='types.GetTransactionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txn_list_with_proof', full_name='types.GetTransactionsResponse.txn_list_with_proof', index=0,
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
  serialized_start=2114,
  serialized_end=2201,
)

_UPDATETOLATESTLEDGERREQUEST.fields_by_name['requested_items'].message_type = _REQUESTITEM
_REQUESTITEM.fields_by_name['get_account_state_request'].message_type = _GETACCOUNTSTATEREQUEST
_REQUESTITEM.fields_by_name['get_account_transaction_by_sequence_number_request'].message_type = _GETACCOUNTTRANSACTIONBYSEQUENCENUMBERREQUEST
_REQUESTITEM.fields_by_name['get_events_by_event_access_path_request'].message_type = _GETEVENTSBYEVENTACCESSPATHREQUEST
_REQUESTITEM.fields_by_name['get_transactions_request'].message_type = _GETTRANSACTIONSREQUEST
_REQUESTITEM.oneofs_by_name['requested_items'].fields.append(
  _REQUESTITEM.fields_by_name['get_account_state_request'])
_REQUESTITEM.fields_by_name['get_account_state_request'].containing_oneof = _REQUESTITEM.oneofs_by_name['requested_items']
_REQUESTITEM.oneofs_by_name['requested_items'].fields.append(
  _REQUESTITEM.fields_by_name['get_account_transaction_by_sequence_number_request'])
_REQUESTITEM.fields_by_name['get_account_transaction_by_sequence_number_request'].containing_oneof = _REQUESTITEM.oneofs_by_name['requested_items']
_REQUESTITEM.oneofs_by_name['requested_items'].fields.append(
  _REQUESTITEM.fields_by_name['get_events_by_event_access_path_request'])
_REQUESTITEM.fields_by_name['get_events_by_event_access_path_request'].containing_oneof = _REQUESTITEM.oneofs_by_name['requested_items']
_REQUESTITEM.oneofs_by_name['requested_items'].fields.append(
  _REQUESTITEM.fields_by_name['get_transactions_request'])
_REQUESTITEM.fields_by_name['get_transactions_request'].containing_oneof = _REQUESTITEM.oneofs_by_name['requested_items']
_UPDATETOLATESTLEDGERRESPONSE.fields_by_name['response_items'].message_type = _RESPONSEITEM
_UPDATETOLATESTLEDGERRESPONSE.fields_by_name['ledger_info_with_sigs'].message_type = ledger__info__pb2._LEDGERINFOWITHSIGNATURES
_UPDATETOLATESTLEDGERRESPONSE.fields_by_name['validator_change_proof'].message_type = validator__change__pb2._VALIDATORCHANGEPROOF
_UPDATETOLATESTLEDGERRESPONSE.fields_by_name['ledger_consistency_proof'].message_type = proof__pb2._ACCUMULATORCONSISTENCYPROOF
_RESPONSEITEM.fields_by_name['get_account_state_response'].message_type = _GETACCOUNTSTATERESPONSE
_RESPONSEITEM.fields_by_name['get_account_transaction_by_sequence_number_response'].message_type = _GETACCOUNTTRANSACTIONBYSEQUENCENUMBERRESPONSE
_RESPONSEITEM.fields_by_name['get_events_by_event_access_path_response'].message_type = _GETEVENTSBYEVENTACCESSPATHRESPONSE
_RESPONSEITEM.fields_by_name['get_transactions_response'].message_type = _GETTRANSACTIONSRESPONSE
_RESPONSEITEM.oneofs_by_name['response_items'].fields.append(
  _RESPONSEITEM.fields_by_name['get_account_state_response'])
_RESPONSEITEM.fields_by_name['get_account_state_response'].containing_oneof = _RESPONSEITEM.oneofs_by_name['response_items']
_RESPONSEITEM.oneofs_by_name['response_items'].fields.append(
  _RESPONSEITEM.fields_by_name['get_account_transaction_by_sequence_number_response'])
_RESPONSEITEM.fields_by_name['get_account_transaction_by_sequence_number_response'].containing_oneof = _RESPONSEITEM.oneofs_by_name['response_items']
_RESPONSEITEM.oneofs_by_name['response_items'].fields.append(
  _RESPONSEITEM.fields_by_name['get_events_by_event_access_path_response'])
_RESPONSEITEM.fields_by_name['get_events_by_event_access_path_response'].containing_oneof = _RESPONSEITEM.oneofs_by_name['response_items']
_RESPONSEITEM.oneofs_by_name['response_items'].fields.append(
  _RESPONSEITEM.fields_by_name['get_transactions_response'])
_RESPONSEITEM.fields_by_name['get_transactions_response'].containing_oneof = _RESPONSEITEM.oneofs_by_name['response_items']
_GETACCOUNTSTATERESPONSE.fields_by_name['account_state_with_proof'].message_type = account__state__blob__pb2._ACCOUNTSTATEWITHPROOF
_GETACCOUNTTRANSACTIONBYSEQUENCENUMBERRESPONSE.fields_by_name['transaction_with_proof'].message_type = transaction__pb2._TRANSACTIONWITHPROOF
_GETACCOUNTTRANSACTIONBYSEQUENCENUMBERRESPONSE.fields_by_name['proof_of_current_sequence_number'].message_type = account__state__blob__pb2._ACCOUNTSTATEWITHPROOF
_GETEVENTSBYEVENTACCESSPATHREQUEST.fields_by_name['access_path'].message_type = access__path__pb2._ACCESSPATH
_GETEVENTSBYEVENTACCESSPATHRESPONSE.fields_by_name['events_with_proof'].message_type = events__pb2._EVENTWITHPROOF
_GETEVENTSBYEVENTACCESSPATHRESPONSE.fields_by_name['proof_of_latest_event'].message_type = account__state__blob__pb2._ACCOUNTSTATEWITHPROOF
_GETTRANSACTIONSRESPONSE.fields_by_name['txn_list_with_proof'].message_type = transaction__pb2._TRANSACTIONLISTWITHPROOF
DESCRIPTOR.message_types_by_name['UpdateToLatestLedgerRequest'] = _UPDATETOLATESTLEDGERREQUEST
DESCRIPTOR.message_types_by_name['RequestItem'] = _REQUESTITEM
DESCRIPTOR.message_types_by_name['UpdateToLatestLedgerResponse'] = _UPDATETOLATESTLEDGERRESPONSE
DESCRIPTOR.message_types_by_name['ResponseItem'] = _RESPONSEITEM
DESCRIPTOR.message_types_by_name['GetAccountStateRequest'] = _GETACCOUNTSTATEREQUEST
DESCRIPTOR.message_types_by_name['GetAccountStateResponse'] = _GETACCOUNTSTATERESPONSE
DESCRIPTOR.message_types_by_name['GetAccountTransactionBySequenceNumberRequest'] = _GETACCOUNTTRANSACTIONBYSEQUENCENUMBERREQUEST
DESCRIPTOR.message_types_by_name['GetAccountTransactionBySequenceNumberResponse'] = _GETACCOUNTTRANSACTIONBYSEQUENCENUMBERRESPONSE
DESCRIPTOR.message_types_by_name['GetEventsByEventAccessPathRequest'] = _GETEVENTSBYEVENTACCESSPATHREQUEST
DESCRIPTOR.message_types_by_name['GetEventsByEventAccessPathResponse'] = _GETEVENTSBYEVENTACCESSPATHRESPONSE
DESCRIPTOR.message_types_by_name['GetTransactionsRequest'] = _GETTRANSACTIONSREQUEST
DESCRIPTOR.message_types_by_name['GetTransactionsResponse'] = _GETTRANSACTIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateToLatestLedgerRequest = _reflection.GeneratedProtocolMessageType('UpdateToLatestLedgerRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETOLATESTLEDGERREQUEST,
  '__module__' : 'get_with_proof_pb2'
  # @@protoc_insertion_point(class_scope:types.UpdateToLatestLedgerRequest)
  })
_sym_db.RegisterMessage(UpdateToLatestLedgerRequest)

RequestItem = _reflection.GeneratedProtocolMessageType('RequestItem', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTITEM,
  '__module__' : 'get_with_proof_pb2'
  # @@protoc_insertion_point(class_scope:types.RequestItem)
  })
_sym_db.RegisterMessage(RequestItem)

UpdateToLatestLedgerResponse = _reflection.GeneratedProtocolMessageType('UpdateToLatestLedgerResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETOLATESTLEDGERRESPONSE,
  '__module__' : 'get_with_proof_pb2'
  # @@protoc_insertion_point(class_scope:types.UpdateToLatestLedgerResponse)
  })
_sym_db.RegisterMessage(UpdateToLatestLedgerResponse)

ResponseItem = _reflection.GeneratedProtocolMessageType('ResponseItem', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEITEM,
  '__module__' : 'get_with_proof_pb2'
  # @@protoc_insertion_point(class_scope:types.ResponseItem)
  })
_sym_db.RegisterMessage(ResponseItem)

GetAccountStateRequest = _reflection.GeneratedProtocolMessageType('GetAccountStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTSTATEREQUEST,
  '__module__' : 'get_with_proof_pb2'
  # @@protoc_insertion_point(class_scope:types.GetAccountStateRequest)
  })
_sym_db.RegisterMessage(GetAccountStateRequest)

GetAccountStateResponse = _reflection.GeneratedProtocolMessageType('GetAccountStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTSTATERESPONSE,
  '__module__' : 'get_with_proof_pb2'
  # @@protoc_insertion_point(class_scope:types.GetAccountStateResponse)
  })
_sym_db.RegisterMessage(GetAccountStateResponse)

GetAccountTransactionBySequenceNumberRequest = _reflection.GeneratedProtocolMessageType('GetAccountTransactionBySequenceNumberRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTTRANSACTIONBYSEQUENCENUMBERREQUEST,
  '__module__' : 'get_with_proof_pb2'
  # @@protoc_insertion_point(class_scope:types.GetAccountTransactionBySequenceNumberRequest)
  })
_sym_db.RegisterMessage(GetAccountTransactionBySequenceNumberRequest)

GetAccountTransactionBySequenceNumberResponse = _reflection.GeneratedProtocolMessageType('GetAccountTransactionBySequenceNumberResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTTRANSACTIONBYSEQUENCENUMBERRESPONSE,
  '__module__' : 'get_with_proof_pb2'
  # @@protoc_insertion_point(class_scope:types.GetAccountTransactionBySequenceNumberResponse)
  })
_sym_db.RegisterMessage(GetAccountTransactionBySequenceNumberResponse)

GetEventsByEventAccessPathRequest = _reflection.GeneratedProtocolMessageType('GetEventsByEventAccessPathRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETEVENTSBYEVENTACCESSPATHREQUEST,
  '__module__' : 'get_with_proof_pb2'
  # @@protoc_insertion_point(class_scope:types.GetEventsByEventAccessPathRequest)
  })
_sym_db.RegisterMessage(GetEventsByEventAccessPathRequest)

GetEventsByEventAccessPathResponse = _reflection.GeneratedProtocolMessageType('GetEventsByEventAccessPathResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETEVENTSBYEVENTACCESSPATHRESPONSE,
  '__module__' : 'get_with_proof_pb2'
  # @@protoc_insertion_point(class_scope:types.GetEventsByEventAccessPathResponse)
  })
_sym_db.RegisterMessage(GetEventsByEventAccessPathResponse)

GetTransactionsRequest = _reflection.GeneratedProtocolMessageType('GetTransactionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSACTIONSREQUEST,
  '__module__' : 'get_with_proof_pb2'
  # @@protoc_insertion_point(class_scope:types.GetTransactionsRequest)
  })
_sym_db.RegisterMessage(GetTransactionsRequest)

GetTransactionsResponse = _reflection.GeneratedProtocolMessageType('GetTransactionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSACTIONSRESPONSE,
  '__module__' : 'get_with_proof_pb2'
  # @@protoc_insertion_point(class_scope:types.GetTransactionsResponse)
  })
_sym_db.RegisterMessage(GetTransactionsResponse)


# @@protoc_insertion_point(module_scope)
