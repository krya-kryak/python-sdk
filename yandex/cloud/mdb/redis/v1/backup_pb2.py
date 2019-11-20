# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/redis/v1/backup.proto

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
  name='yandex/cloud/mdb/redis/v1/backup.proto',
  package='yandex.cloud.mdb.redis.v1',
  syntax='proto3',
  serialized_options=_b('\n\035yandex.cloud.api.mdb.redis.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1;redis'),
  serialized_pb=_b('\n&yandex/cloud/mdb/redis/v1/backup.proto\x12\x19yandex.cloud.mdb.redis.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbe\x01\n\x06\x42\x61\x63kup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x11source_cluster_id\x18\x04 \x01(\t\x12.\n\nstarted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x12source_shard_names\x18\x06 \x03(\tBd\n\x1dyandex.cloud.api.mdb.redis.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1;redisb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_BACKUP = _descriptor.Descriptor(
  name='Backup',
  full_name='yandex.cloud.mdb.redis.v1.Backup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.mdb.redis.v1.Backup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.mdb.redis.v1.Backup.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.mdb.redis.v1.Backup.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_cluster_id', full_name='yandex.cloud.mdb.redis.v1.Backup.source_cluster_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='yandex.cloud.mdb.redis.v1.Backup.started_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_shard_names', full_name='yandex.cloud.mdb.redis.v1.Backup.source_shard_names', index=5,
      number=6, type=9, cpp_type=9, label=3,
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
  serialized_start=103,
  serialized_end=293,
)

_BACKUP.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BACKUP.fields_by_name['started_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Backup'] = _BACKUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Backup = _reflection.GeneratedProtocolMessageType('Backup', (_message.Message,), dict(
  DESCRIPTOR = _BACKUP,
  __module__ = 'yandex.cloud.mdb.redis.v1.backup_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.Backup)
  ))
_sym_db.RegisterMessage(Backup)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)