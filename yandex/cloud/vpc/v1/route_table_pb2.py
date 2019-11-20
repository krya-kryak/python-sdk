# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/vpc/v1/route_table.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/vpc/v1/route_table.proto',
  package='yandex.cloud.vpc.v1',
  syntax='proto3',
  serialized_options=_b('\n\027yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpc'),
  serialized_pb=_b('\n%yandex/cloud/vpc/v1/route_table.proto\x12\x13yandex.cloud.vpc.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb7\x02\n\nRouteTable\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12;\n\x06labels\x18\x06 \x03(\x0b\x32+.yandex.cloud.vpc.v1.RouteTable.LabelsEntry\x12\x12\n\nnetwork_id\x18\x07 \x01(\t\x12\x37\n\rstatic_routes\x18\x08 \x03(\x0b\x32 .yandex.cloud.vpc.v1.StaticRoute\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcf\x01\n\x0bStaticRoute\x12\x1c\n\x12\x64\x65stination_prefix\x18\x01 \x01(\tH\x00\x12\x1a\n\x10next_hop_address\x18\x02 \x01(\tH\x01\x12<\n\x06labels\x18\x03 \x03(\x0b\x32,.yandex.cloud.vpc.v1.StaticRoute.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\r\n\x0b\x64\x65stinationB\n\n\x08next_hopBV\n\x17yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpcb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_ROUTETABLE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.vpc.v1.RouteTable.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.vpc.v1.RouteTable.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.vpc.v1.RouteTable.LabelsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=407,
)

_ROUTETABLE = _descriptor.Descriptor(
  name='RouteTable',
  full_name='yandex.cloud.vpc.v1.RouteTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.vpc.v1.RouteTable.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.vpc.v1.RouteTable.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.vpc.v1.RouteTable.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.vpc.v1.RouteTable.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.vpc.v1.RouteTable.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.vpc.v1.RouteTable.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_id', full_name='yandex.cloud.vpc.v1.RouteTable.network_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='static_routes', full_name='yandex.cloud.vpc.v1.RouteTable.static_routes', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ROUTETABLE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=407,
)


_STATICROUTE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.vpc.v1.StaticRoute.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.vpc.v1.StaticRoute.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.vpc.v1.StaticRoute.LabelsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=407,
)

_STATICROUTE = _descriptor.Descriptor(
  name='StaticRoute',
  full_name='yandex.cloud.vpc.v1.StaticRoute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='destination_prefix', full_name='yandex.cloud.vpc.v1.StaticRoute.destination_prefix', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_hop_address', full_name='yandex.cloud.vpc.v1.StaticRoute.next_hop_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.vpc.v1.StaticRoute.labels', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STATICROUTE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='destination', full_name='yandex.cloud.vpc.v1.StaticRoute.destination',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='next_hop', full_name='yandex.cloud.vpc.v1.StaticRoute.next_hop',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=410,
  serialized_end=617,
)

_ROUTETABLE_LABELSENTRY.containing_type = _ROUTETABLE
_ROUTETABLE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ROUTETABLE.fields_by_name['labels'].message_type = _ROUTETABLE_LABELSENTRY
_ROUTETABLE.fields_by_name['static_routes'].message_type = _STATICROUTE
_STATICROUTE_LABELSENTRY.containing_type = _STATICROUTE
_STATICROUTE.fields_by_name['labels'].message_type = _STATICROUTE_LABELSENTRY
_STATICROUTE.oneofs_by_name['destination'].fields.append(
  _STATICROUTE.fields_by_name['destination_prefix'])
_STATICROUTE.fields_by_name['destination_prefix'].containing_oneof = _STATICROUTE.oneofs_by_name['destination']
_STATICROUTE.oneofs_by_name['next_hop'].fields.append(
  _STATICROUTE.fields_by_name['next_hop_address'])
_STATICROUTE.fields_by_name['next_hop_address'].containing_oneof = _STATICROUTE.oneofs_by_name['next_hop']
DESCRIPTOR.message_types_by_name['RouteTable'] = _ROUTETABLE
DESCRIPTOR.message_types_by_name['StaticRoute'] = _STATICROUTE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RouteTable = _reflection.GeneratedProtocolMessageType('RouteTable', (_message.Message,), dict(

  LabelsEntry = _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), dict(
    DESCRIPTOR = _ROUTETABLE_LABELSENTRY,
    __module__ = 'yandex.cloud.vpc.v1.route_table_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.RouteTable.LabelsEntry)
    ))
  ,
  DESCRIPTOR = _ROUTETABLE,
  __module__ = 'yandex.cloud.vpc.v1.route_table_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.RouteTable)
  ))
_sym_db.RegisterMessage(RouteTable)
_sym_db.RegisterMessage(RouteTable.LabelsEntry)

StaticRoute = _reflection.GeneratedProtocolMessageType('StaticRoute', (_message.Message,), dict(

  LabelsEntry = _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATICROUTE_LABELSENTRY,
    __module__ = 'yandex.cloud.vpc.v1.route_table_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.StaticRoute.LabelsEntry)
    ))
  ,
  DESCRIPTOR = _STATICROUTE,
  __module__ = 'yandex.cloud.vpc.v1.route_table_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.StaticRoute)
  ))
_sym_db.RegisterMessage(StaticRoute)
_sym_db.RegisterMessage(StaticRoute.LabelsEntry)


DESCRIPTOR._options = None
_ROUTETABLE_LABELSENTRY._options = None
_STATICROUTE_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)