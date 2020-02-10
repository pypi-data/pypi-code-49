# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contacts.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from . import definitions_pb2 as definitions__pb2
from . import miscellaneous_pb2 as miscellaneous__pb2
from . import peers_pb2 as peers__pb2
from . import users_pb2 as users__pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='contacts.proto',
  package='dialog',
  syntax='proto3',
  serialized_options=b'Z\006dialog\342?\026\n\024im.dlg.grpc.services',
  serialized_pb=b'\n\x0e\x63ontacts.proto\x12\x06\x64ialog\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x11\x64\x65\x66initions.proto\x1a\x13miscellaneous.proto\x1a\x0bpeers.proto\x1a\x0busers.proto\x1a\x15scalapb/scalapb.proto\"o\n\rPhoneToImport\x12#\n\x0cphone_number\x18\x01 \x01(\x03\x42\r\x8a\xea\x30\t\n\x07visible\x12\x39\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\r\x8a\xea\x30\t\n\x07visible\"h\n\rEmailToImport\x12\x1c\n\x05\x65mail\x18\x01 \x01(\tB\r\x8a\xea\x30\t\n\x07visible\x12\x39\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\r\x8a\xea\x30\t\n\x07visible\"\xe3\x01\n\x15RequestImportContacts\x12\x34\n\x06phones\x18\x01 \x03(\x0b\x32\x15.dialog.PhoneToImportB\r\x8a\xea\x30\t\n\x07\x63ompact\x12\x34\n\x06\x65mails\x18\x02 \x03(\x0b\x32\x15.dialog.EmailToImportB\r\x8a\xea\x30\t\n\x07\x63ompact\x12@\n\roptimizations\x18\x03 \x03(\x0e\x32\x1a.dialog.UpdateOptimizationB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"\x82\x01\n\x16ResponseImportContacts\x12\x0b\n\x03seq\x18\x02 \x01(\x05\x12\r\n\x05state\x18\x03 \x01(\x0c\x12\'\n\nuser_peers\x18\x04 \x03(\x0b\x32\x13.dialog.UserOutPeer:\x1d\xe2?\x1a\n\x18im.dlg.grpc.GrpcResponseJ\x04\x08\x01\x10\x02\"\xa9\x01\n\x1dRequestDeferredImportContacts\x12\x34\n\x06phones\x18\x01 \x03(\x0b\x32\x15.dialog.PhoneToImportB\r\x8a\xea\x30\t\n\x07\x63ompact\x12\x34\n\x06\x65mails\x18\x02 \x03(\x0b\x32\x15.dialog.EmailToImportB\r\x8a\xea\x30\t\n\x07\x63ompact:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"P\n\x1eResponseDeferredImportContacts\x12\x0f\n\x07task_id\x18\x01 \x01(\t:\x1d\xe2?\x1a\n\x18im.dlg.grpc.GrpcResponse\"\x9a\x01\n\x12RequestGetContacts\x12$\n\rcontacts_hash\x18\x01 \x01(\tB\r\x8a\xea\x30\t\n\x07visible\x12@\n\roptimizations\x18\x02 \x03(\x0e\x32\x1a.dialog.UpdateOptimizationB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"{\n\x13ResponseGetContacts\x12\x16\n\x0eis_not_changed\x18\x02 \x01(\x08\x12\'\n\nuser_peers\x18\x03 \x03(\x0b\x32\x13.dialog.UserOutPeer:\x1d\xe2?\x1a\n\x18im.dlg.grpc.GrpcResponseJ\x04\x08\x01\x10\x02\"s\n\x14RequestRemoveContact\x12\x1a\n\x03uid\x18\x01 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12!\n\x0b\x61\x63\x63\x65ss_hash\x18\x02 \x01(\x03\x42\x0c\x8a\xea\x30\x08\n\x06\x64\x61nger:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"p\n\x11RequestAddContact\x12\x1a\n\x03uid\x18\x01 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12!\n\x0b\x61\x63\x63\x65ss_hash\x18\x02 \x01(\x03\x42\x0c\x8a\xea\x30\x08\n\x06\x64\x61nger:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"\x88\x01\n\x15RequestSearchContacts\x12\x1e\n\x07request\x18\x01 \x01(\tB\r\x8a\xea\x30\t\n\x07visible\x12\x31\n\roptimizations\x18\x02 \x03(\x0e\x32\x1a.dialog.UpdateOptimization:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"}\n\x16ResponseSearchContacts\x12\x1b\n\x05users\x18\x01 \x03(\x0b\x32\x0c.dialog.User\x12\'\n\nuser_peers\x18\x02 \x03(\x0b\x32\x13.dialog.UserOutPeer:\x1d\xe2?\x1a\n\x18im.dlg.grpc.GrpcResponse\"\xa3\x01\n\x17UpdateContactRegistered\x12\x1a\n\x03uid\x18\x01 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12 \n\tis_silent\x18\x02 \x01(\x08\x42\r\x8a\xea\x30\t\n\x07visible\x12\x1b\n\x04\x64\x61te\x18\x03 \x01(\x03\x42\r\x8a\xea\x30\t\n\x07visible\x12-\n\x03mid\x18\x05 \x01(\x0b\x32\x11.dialog.UUIDValueB\r\x8a\xea\x30\t\n\x07visible\"p\n\x13UpdateContactsAdded\x12\x1b\n\x04uids\x18\x01 \x03(\x05\x42\r\x8a\xea\x30\t\n\x07\x63ompact\x12<\n\x07task_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\r\x8a\xea\x30\t\n\x07\x63ompact\"@\n\x1eUpdateContactsAddTaskSuspended\x12\x1e\n\x07task_id\x18\x01 \x01(\tB\r\x8a\xea\x30\t\n\x07\x63ompact\"4\n\x15UpdateContactsRemoved\x12\x1b\n\x04uids\x18\x01 \x03(\x05\x42\r\x8a\xea\x30\t\n\x07\x63ompact2\xee\x05\n\x08\x43ontacts\x12|\n\x0eImportContacts\x12\x1d.dialog.RequestImportContacts\x1a\x1e.dialog.ResponseImportContacts\"+\x82\xd3\xe4\x93\x02%\" /v1/grpc/Contacts/ImportContacts:\x01*\x12\x9c\x01\n\x16\x44\x65\x66\x65rredImportContacts\x12%.dialog.RequestDeferredImportContacts\x1a&.dialog.ResponseDeferredImportContacts\"3\x82\xd3\xe4\x93\x02-\"(/v1/grpc/Contacts/DeferredImportContacts:\x01*\x12p\n\x0bGetContacts\x12\x1a.dialog.RequestGetContacts\x1a\x1b.dialog.ResponseGetContacts\"(\x82\xd3\xe4\x93\x02\"\"\x1d/v1/grpc/Contacts/GetContacts:\x01*\x12n\n\rRemoveContact\x12\x1c.dialog.RequestRemoveContact\x1a\x13.dialog.ResponseSeq\"*\x82\xd3\xe4\x93\x02$\"\x1f/v1/grpc/Contacts/RemoveContact:\x01*\x12\x65\n\nAddContact\x12\x19.dialog.RequestAddContact\x1a\x13.dialog.ResponseSeq\"\'\x82\xd3\xe4\x93\x02!\"\x1c/v1/grpc/Contacts/AddContact:\x01*\x12|\n\x0eSearchContacts\x12\x1d.dialog.RequestSearchContacts\x1a\x1e.dialog.ResponseSearchContacts\"+\x82\xd3\xe4\x93\x02%\" /v1/grpc/Contacts/SearchContacts:\x01*B!Z\x06\x64ialog\xe2?\x16\n\x14im.dlg.grpc.servicesb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,definitions__pb2.DESCRIPTOR,miscellaneous__pb2.DESCRIPTOR,peers__pb2.DESCRIPTOR,users__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])




_PHONETOIMPORT = _descriptor.Descriptor(
  name='PhoneToImport',
  full_name='dialog.PhoneToImport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='dialog.PhoneToImport.phone_number', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dialog.PhoneToImport.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
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
  serialized_start=177,
  serialized_end=288,
)


_EMAILTOIMPORT = _descriptor.Descriptor(
  name='EmailToImport',
  full_name='dialog.EmailToImport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='dialog.EmailToImport.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dialog.EmailToImport.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
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
  serialized_start=290,
  serialized_end=394,
)


_REQUESTIMPORTCONTACTS = _descriptor.Descriptor(
  name='RequestImportContacts',
  full_name='dialog.RequestImportContacts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phones', full_name='dialog.RequestImportContacts.phones', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007compact', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emails', full_name='dialog.RequestImportContacts.emails', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007compact', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optimizations', full_name='dialog.RequestImportContacts.optimizations', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\342?\031\n\027im.dlg.grpc.GrpcRequest',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=397,
  serialized_end=624,
)


_RESPONSEIMPORTCONTACTS = _descriptor.Descriptor(
  name='ResponseImportContacts',
  full_name='dialog.ResponseImportContacts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seq', full_name='dialog.ResponseImportContacts.seq', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='dialog.ResponseImportContacts.state', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_peers', full_name='dialog.ResponseImportContacts.user_peers', index=2,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_options=b'\342?\032\n\030im.dlg.grpc.GrpcResponse',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=627,
  serialized_end=757,
)


_REQUESTDEFERREDIMPORTCONTACTS = _descriptor.Descriptor(
  name='RequestDeferredImportContacts',
  full_name='dialog.RequestDeferredImportContacts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phones', full_name='dialog.RequestDeferredImportContacts.phones', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007compact', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emails', full_name='dialog.RequestDeferredImportContacts.emails', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007compact', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\342?\031\n\027im.dlg.grpc.GrpcRequest',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=760,
  serialized_end=929,
)


_RESPONSEDEFERREDIMPORTCONTACTS = _descriptor.Descriptor(
  name='ResponseDeferredImportContacts',
  full_name='dialog.ResponseDeferredImportContacts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='dialog.ResponseDeferredImportContacts.task_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\342?\032\n\030im.dlg.grpc.GrpcResponse',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=931,
  serialized_end=1011,
)


_REQUESTGETCONTACTS = _descriptor.Descriptor(
  name='RequestGetContacts',
  full_name='dialog.RequestGetContacts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contacts_hash', full_name='dialog.RequestGetContacts.contacts_hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optimizations', full_name='dialog.RequestGetContacts.optimizations', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\342?\031\n\027im.dlg.grpc.GrpcRequest',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1014,
  serialized_end=1168,
)


_RESPONSEGETCONTACTS = _descriptor.Descriptor(
  name='ResponseGetContacts',
  full_name='dialog.ResponseGetContacts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_not_changed', full_name='dialog.ResponseGetContacts.is_not_changed', index=0,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_peers', full_name='dialog.ResponseGetContacts.user_peers', index=1,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_options=b'\342?\032\n\030im.dlg.grpc.GrpcResponse',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1170,
  serialized_end=1293,
)


_REQUESTREMOVECONTACT = _descriptor.Descriptor(
  name='RequestRemoveContact',
  full_name='dialog.RequestRemoveContact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='dialog.RequestRemoveContact.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_hash', full_name='dialog.RequestRemoveContact.access_hash', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\010\n\006danger', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\342?\031\n\027im.dlg.grpc.GrpcRequest',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1295,
  serialized_end=1410,
)


_REQUESTADDCONTACT = _descriptor.Descriptor(
  name='RequestAddContact',
  full_name='dialog.RequestAddContact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='dialog.RequestAddContact.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_hash', full_name='dialog.RequestAddContact.access_hash', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\010\n\006danger', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\342?\031\n\027im.dlg.grpc.GrpcRequest',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1412,
  serialized_end=1524,
)


_REQUESTSEARCHCONTACTS = _descriptor.Descriptor(
  name='RequestSearchContacts',
  full_name='dialog.RequestSearchContacts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='dialog.RequestSearchContacts.request', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optimizations', full_name='dialog.RequestSearchContacts.optimizations', index=1,
      number=2, type=14, cpp_type=8, label=3,
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
  serialized_options=b'\342?\031\n\027im.dlg.grpc.GrpcRequest',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1527,
  serialized_end=1663,
)


_RESPONSESEARCHCONTACTS = _descriptor.Descriptor(
  name='ResponseSearchContacts',
  full_name='dialog.ResponseSearchContacts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='dialog.ResponseSearchContacts.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_peers', full_name='dialog.ResponseSearchContacts.user_peers', index=1,
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
  serialized_options=b'\342?\032\n\030im.dlg.grpc.GrpcResponse',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1665,
  serialized_end=1790,
)


_UPDATECONTACTREGISTERED = _descriptor.Descriptor(
  name='UpdateContactRegistered',
  full_name='dialog.UpdateContactRegistered',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='dialog.UpdateContactRegistered.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_silent', full_name='dialog.UpdateContactRegistered.is_silent', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='dialog.UpdateContactRegistered.date', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mid', full_name='dialog.UpdateContactRegistered.mid', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR),
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
  serialized_start=1793,
  serialized_end=1956,
)


_UPDATECONTACTSADDED = _descriptor.Descriptor(
  name='UpdateContactsAdded',
  full_name='dialog.UpdateContactsAdded',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uids', full_name='dialog.UpdateContactsAdded.uids', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007compact', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='dialog.UpdateContactsAdded.task_id', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007compact', file=DESCRIPTOR),
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
  serialized_start=1958,
  serialized_end=2070,
)


_UPDATECONTACTSADDTASKSUSPENDED = _descriptor.Descriptor(
  name='UpdateContactsAddTaskSuspended',
  full_name='dialog.UpdateContactsAddTaskSuspended',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='dialog.UpdateContactsAddTaskSuspended.task_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007compact', file=DESCRIPTOR),
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
  serialized_start=2072,
  serialized_end=2136,
)


_UPDATECONTACTSREMOVED = _descriptor.Descriptor(
  name='UpdateContactsRemoved',
  full_name='dialog.UpdateContactsRemoved',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uids', full_name='dialog.UpdateContactsRemoved.uids', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007compact', file=DESCRIPTOR),
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
  serialized_start=2138,
  serialized_end=2190,
)

_PHONETOIMPORT.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_EMAILTOIMPORT.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_REQUESTIMPORTCONTACTS.fields_by_name['phones'].message_type = _PHONETOIMPORT
_REQUESTIMPORTCONTACTS.fields_by_name['emails'].message_type = _EMAILTOIMPORT
_REQUESTIMPORTCONTACTS.fields_by_name['optimizations'].enum_type = miscellaneous__pb2._UPDATEOPTIMIZATION
_RESPONSEIMPORTCONTACTS.fields_by_name['user_peers'].message_type = peers__pb2._USEROUTPEER
_REQUESTDEFERREDIMPORTCONTACTS.fields_by_name['phones'].message_type = _PHONETOIMPORT
_REQUESTDEFERREDIMPORTCONTACTS.fields_by_name['emails'].message_type = _EMAILTOIMPORT
_REQUESTGETCONTACTS.fields_by_name['optimizations'].enum_type = miscellaneous__pb2._UPDATEOPTIMIZATION
_RESPONSEGETCONTACTS.fields_by_name['user_peers'].message_type = peers__pb2._USEROUTPEER
_REQUESTSEARCHCONTACTS.fields_by_name['optimizations'].enum_type = miscellaneous__pb2._UPDATEOPTIMIZATION
_RESPONSESEARCHCONTACTS.fields_by_name['users'].message_type = users__pb2._USER
_RESPONSESEARCHCONTACTS.fields_by_name['user_peers'].message_type = peers__pb2._USEROUTPEER
_UPDATECONTACTREGISTERED.fields_by_name['mid'].message_type = definitions__pb2._UUIDVALUE
_UPDATECONTACTSADDED.fields_by_name['task_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['PhoneToImport'] = _PHONETOIMPORT
DESCRIPTOR.message_types_by_name['EmailToImport'] = _EMAILTOIMPORT
DESCRIPTOR.message_types_by_name['RequestImportContacts'] = _REQUESTIMPORTCONTACTS
DESCRIPTOR.message_types_by_name['ResponseImportContacts'] = _RESPONSEIMPORTCONTACTS
DESCRIPTOR.message_types_by_name['RequestDeferredImportContacts'] = _REQUESTDEFERREDIMPORTCONTACTS
DESCRIPTOR.message_types_by_name['ResponseDeferredImportContacts'] = _RESPONSEDEFERREDIMPORTCONTACTS
DESCRIPTOR.message_types_by_name['RequestGetContacts'] = _REQUESTGETCONTACTS
DESCRIPTOR.message_types_by_name['ResponseGetContacts'] = _RESPONSEGETCONTACTS
DESCRIPTOR.message_types_by_name['RequestRemoveContact'] = _REQUESTREMOVECONTACT
DESCRIPTOR.message_types_by_name['RequestAddContact'] = _REQUESTADDCONTACT
DESCRIPTOR.message_types_by_name['RequestSearchContacts'] = _REQUESTSEARCHCONTACTS
DESCRIPTOR.message_types_by_name['ResponseSearchContacts'] = _RESPONSESEARCHCONTACTS
DESCRIPTOR.message_types_by_name['UpdateContactRegistered'] = _UPDATECONTACTREGISTERED
DESCRIPTOR.message_types_by_name['UpdateContactsAdded'] = _UPDATECONTACTSADDED
DESCRIPTOR.message_types_by_name['UpdateContactsAddTaskSuspended'] = _UPDATECONTACTSADDTASKSUSPENDED
DESCRIPTOR.message_types_by_name['UpdateContactsRemoved'] = _UPDATECONTACTSREMOVED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PhoneToImport = _reflection.GeneratedProtocolMessageType('PhoneToImport', (_message.Message,), {
  'DESCRIPTOR' : _PHONETOIMPORT,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.PhoneToImport)
  })
_sym_db.RegisterMessage(PhoneToImport)

EmailToImport = _reflection.GeneratedProtocolMessageType('EmailToImport', (_message.Message,), {
  'DESCRIPTOR' : _EMAILTOIMPORT,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.EmailToImport)
  })
_sym_db.RegisterMessage(EmailToImport)

RequestImportContacts = _reflection.GeneratedProtocolMessageType('RequestImportContacts', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTIMPORTCONTACTS,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestImportContacts)
  })
_sym_db.RegisterMessage(RequestImportContacts)

ResponseImportContacts = _reflection.GeneratedProtocolMessageType('ResponseImportContacts', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEIMPORTCONTACTS,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ResponseImportContacts)
  })
_sym_db.RegisterMessage(ResponseImportContacts)

RequestDeferredImportContacts = _reflection.GeneratedProtocolMessageType('RequestDeferredImportContacts', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTDEFERREDIMPORTCONTACTS,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestDeferredImportContacts)
  })
_sym_db.RegisterMessage(RequestDeferredImportContacts)

ResponseDeferredImportContacts = _reflection.GeneratedProtocolMessageType('ResponseDeferredImportContacts', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEDEFERREDIMPORTCONTACTS,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ResponseDeferredImportContacts)
  })
_sym_db.RegisterMessage(ResponseDeferredImportContacts)

RequestGetContacts = _reflection.GeneratedProtocolMessageType('RequestGetContacts', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTGETCONTACTS,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestGetContacts)
  })
_sym_db.RegisterMessage(RequestGetContacts)

ResponseGetContacts = _reflection.GeneratedProtocolMessageType('ResponseGetContacts', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEGETCONTACTS,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ResponseGetContacts)
  })
_sym_db.RegisterMessage(ResponseGetContacts)

RequestRemoveContact = _reflection.GeneratedProtocolMessageType('RequestRemoveContact', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTREMOVECONTACT,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestRemoveContact)
  })
_sym_db.RegisterMessage(RequestRemoveContact)

RequestAddContact = _reflection.GeneratedProtocolMessageType('RequestAddContact', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTADDCONTACT,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestAddContact)
  })
_sym_db.RegisterMessage(RequestAddContact)

RequestSearchContacts = _reflection.GeneratedProtocolMessageType('RequestSearchContacts', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTSEARCHCONTACTS,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestSearchContacts)
  })
_sym_db.RegisterMessage(RequestSearchContacts)

ResponseSearchContacts = _reflection.GeneratedProtocolMessageType('ResponseSearchContacts', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSESEARCHCONTACTS,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ResponseSearchContacts)
  })
_sym_db.RegisterMessage(ResponseSearchContacts)

UpdateContactRegistered = _reflection.GeneratedProtocolMessageType('UpdateContactRegistered', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONTACTREGISTERED,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdateContactRegistered)
  })
_sym_db.RegisterMessage(UpdateContactRegistered)

UpdateContactsAdded = _reflection.GeneratedProtocolMessageType('UpdateContactsAdded', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONTACTSADDED,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdateContactsAdded)
  })
_sym_db.RegisterMessage(UpdateContactsAdded)

UpdateContactsAddTaskSuspended = _reflection.GeneratedProtocolMessageType('UpdateContactsAddTaskSuspended', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONTACTSADDTASKSUSPENDED,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdateContactsAddTaskSuspended)
  })
_sym_db.RegisterMessage(UpdateContactsAddTaskSuspended)

UpdateContactsRemoved = _reflection.GeneratedProtocolMessageType('UpdateContactsRemoved', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONTACTSREMOVED,
  '__module__' : 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdateContactsRemoved)
  })
_sym_db.RegisterMessage(UpdateContactsRemoved)


DESCRIPTOR._options = None
_PHONETOIMPORT.fields_by_name['phone_number']._options = None
_PHONETOIMPORT.fields_by_name['name']._options = None
_EMAILTOIMPORT.fields_by_name['email']._options = None
_EMAILTOIMPORT.fields_by_name['name']._options = None
_REQUESTIMPORTCONTACTS.fields_by_name['phones']._options = None
_REQUESTIMPORTCONTACTS.fields_by_name['emails']._options = None
_REQUESTIMPORTCONTACTS.fields_by_name['optimizations']._options = None
_REQUESTIMPORTCONTACTS._options = None
_RESPONSEIMPORTCONTACTS._options = None
_REQUESTDEFERREDIMPORTCONTACTS.fields_by_name['phones']._options = None
_REQUESTDEFERREDIMPORTCONTACTS.fields_by_name['emails']._options = None
_REQUESTDEFERREDIMPORTCONTACTS._options = None
_RESPONSEDEFERREDIMPORTCONTACTS._options = None
_REQUESTGETCONTACTS.fields_by_name['contacts_hash']._options = None
_REQUESTGETCONTACTS.fields_by_name['optimizations']._options = None
_REQUESTGETCONTACTS._options = None
_RESPONSEGETCONTACTS._options = None
_REQUESTREMOVECONTACT.fields_by_name['uid']._options = None
_REQUESTREMOVECONTACT.fields_by_name['access_hash']._options = None
_REQUESTREMOVECONTACT._options = None
_REQUESTADDCONTACT.fields_by_name['uid']._options = None
_REQUESTADDCONTACT.fields_by_name['access_hash']._options = None
_REQUESTADDCONTACT._options = None
_REQUESTSEARCHCONTACTS.fields_by_name['request']._options = None
_REQUESTSEARCHCONTACTS._options = None
_RESPONSESEARCHCONTACTS._options = None
_UPDATECONTACTREGISTERED.fields_by_name['uid']._options = None
_UPDATECONTACTREGISTERED.fields_by_name['is_silent']._options = None
_UPDATECONTACTREGISTERED.fields_by_name['date']._options = None
_UPDATECONTACTREGISTERED.fields_by_name['mid']._options = None
_UPDATECONTACTSADDED.fields_by_name['uids']._options = None
_UPDATECONTACTSADDED.fields_by_name['task_id']._options = None
_UPDATECONTACTSADDTASKSUSPENDED.fields_by_name['task_id']._options = None
_UPDATECONTACTSREMOVED.fields_by_name['uids']._options = None

_CONTACTS = _descriptor.ServiceDescriptor(
  name='Contacts',
  full_name='dialog.Contacts',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=2193,
  serialized_end=2943,
  methods=[
  _descriptor.MethodDescriptor(
    name='ImportContacts',
    full_name='dialog.Contacts.ImportContacts',
    index=0,
    containing_service=None,
    input_type=_REQUESTIMPORTCONTACTS,
    output_type=_RESPONSEIMPORTCONTACTS,
    serialized_options=b'\202\323\344\223\002%\" /v1/grpc/Contacts/ImportContacts:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='DeferredImportContacts',
    full_name='dialog.Contacts.DeferredImportContacts',
    index=1,
    containing_service=None,
    input_type=_REQUESTDEFERREDIMPORTCONTACTS,
    output_type=_RESPONSEDEFERREDIMPORTCONTACTS,
    serialized_options=b'\202\323\344\223\002-\"(/v1/grpc/Contacts/DeferredImportContacts:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='GetContacts',
    full_name='dialog.Contacts.GetContacts',
    index=2,
    containing_service=None,
    input_type=_REQUESTGETCONTACTS,
    output_type=_RESPONSEGETCONTACTS,
    serialized_options=b'\202\323\344\223\002\"\"\035/v1/grpc/Contacts/GetContacts:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='RemoveContact',
    full_name='dialog.Contacts.RemoveContact',
    index=3,
    containing_service=None,
    input_type=_REQUESTREMOVECONTACT,
    output_type=miscellaneous__pb2._RESPONSESEQ,
    serialized_options=b'\202\323\344\223\002$\"\037/v1/grpc/Contacts/RemoveContact:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='AddContact',
    full_name='dialog.Contacts.AddContact',
    index=4,
    containing_service=None,
    input_type=_REQUESTADDCONTACT,
    output_type=miscellaneous__pb2._RESPONSESEQ,
    serialized_options=b'\202\323\344\223\002!\"\034/v1/grpc/Contacts/AddContact:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='SearchContacts',
    full_name='dialog.Contacts.SearchContacts',
    index=5,
    containing_service=None,
    input_type=_REQUESTSEARCHCONTACTS,
    output_type=_RESPONSESEARCHCONTACTS,
    serialized_options=b'\202\323\344\223\002%\" /v1/grpc/Contacts/SearchContacts:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTACTS)

DESCRIPTOR.services_by_name['Contacts'] = _CONTACTS

# @@protoc_insertion_point(module_scope)
