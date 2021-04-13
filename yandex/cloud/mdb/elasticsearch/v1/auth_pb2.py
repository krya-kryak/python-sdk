# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/elasticsearch/v1/auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/elasticsearch/v1/auth.proto',
  package='yandex.cloud.mdb.elasticsearch.v1',
  syntax='proto3',
  serialized_options=b'\n%yandex.cloud.api.mdb.elasticsearch.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/elasticsearch/v1;elasticsearch',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,yandex/cloud/mdb/elasticsearch/v1/auth.proto\x12!yandex.cloud.mdb.elasticsearch.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a\x1dyandex/cloud/validation.proto\"S\n\rAuthProviders\x12\x42\n\tproviders\x18\x01 \x03(\x0b\x32/.yandex.cloud.mdb.elasticsearch.v1.AuthProvider\"\x80\x03\n\x0c\x41uthProvider\x12\x42\n\x04type\x18\x01 \x01(\x0e\x32\x34.yandex.cloud.mdb.elasticsearch.v1.AuthProvider.Type\x12*\n\x04name\x18\x02 \x01(\tB\x1c\x8a\xc8\x31\x04<=50\xf2\xc7\x31\x10[a-z][a-z0-9_-]*\x12\r\n\x05order\x18\x03 \x01(\x03\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12\x0e\n\x06hidden\x18\x05 \x01(\x08\x12\x1d\n\x0b\x64\x65scription\x18\x06 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x17\n\x04hint\x18\x07 \x01(\tB\t\x8a\xc8\x31\x05<=250\x12\x17\n\x04icon\x18\x08 \x01(\tB\t\x8a\xc8\x31\x05<=250\x12?\n\x04saml\x18\t \x01(\x0b\x32/.yandex.cloud.mdb.elasticsearch.v1.SamlSettingsH\x00\"2\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06NATIVE\x10\x01\x12\x08\n\x04SAML\x10\x02\x42\n\n\x08settings\"\xc8\x02\n\x0cSamlSettings\x12 \n\ridp_entity_id\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05<=250\x12&\n\x11idp_metadata_file\x18\x02 \x01(\x0c\x42\x0b\x8a\xc8\x31\x07<=10000\x12\x1f\n\x0csp_entity_id\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=250\x12\x1d\n\nkibana_url\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=250\x12%\n\x13\x61ttribute_principal\x18\x05 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\"\n\x10\x61ttribute_groups\x18\x06 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12 \n\x0e\x61ttribute_name\x18\x07 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12!\n\x0f\x61ttribute_email\x18\x08 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1e\n\x0c\x61ttribute_dn\x18\t \x01(\tB\x08\x8a\xc8\x31\x04<=50B|\n%yandex.cloud.api.mdb.elasticsearch.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/elasticsearch/v1;elasticsearchb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_AUTHPROVIDER_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProvider.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NATIVE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SAML', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=586,
  serialized_end=636,
)
_sym_db.RegisterEnumDescriptor(_AUTHPROVIDER_TYPE)


_AUTHPROVIDERS = _descriptor.Descriptor(
  name='AuthProviders',
  full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProviders',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='providers', full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProviders.providers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=178,
  serialized_end=261,
)


_AUTHPROVIDER = _descriptor.Descriptor(
  name='AuthProvider',
  full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProvider',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProvider.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProvider.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50\362\3071\020[a-z][a-z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProvider.order', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProvider.enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hidden', full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProvider.hidden', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProvider.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hint', full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProvider.hint', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=250', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='icon', full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProvider.icon', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=250', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='saml', full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProvider.saml', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AUTHPROVIDER_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='settings', full_name='yandex.cloud.mdb.elasticsearch.v1.AuthProvider.settings',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=264,
  serialized_end=648,
)


_SAMLSETTINGS = _descriptor.Descriptor(
  name='SamlSettings',
  full_name='yandex.cloud.mdb.elasticsearch.v1.SamlSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='idp_entity_id', full_name='yandex.cloud.mdb.elasticsearch.v1.SamlSettings.idp_entity_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=250', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idp_metadata_file', full_name='yandex.cloud.mdb.elasticsearch.v1.SamlSettings.idp_metadata_file', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\007<=10000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sp_entity_id', full_name='yandex.cloud.mdb.elasticsearch.v1.SamlSettings.sp_entity_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=250', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kibana_url', full_name='yandex.cloud.mdb.elasticsearch.v1.SamlSettings.kibana_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=250', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attribute_principal', full_name='yandex.cloud.mdb.elasticsearch.v1.SamlSettings.attribute_principal', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attribute_groups', full_name='yandex.cloud.mdb.elasticsearch.v1.SamlSettings.attribute_groups', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attribute_name', full_name='yandex.cloud.mdb.elasticsearch.v1.SamlSettings.attribute_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attribute_email', full_name='yandex.cloud.mdb.elasticsearch.v1.SamlSettings.attribute_email', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attribute_dn', full_name='yandex.cloud.mdb.elasticsearch.v1.SamlSettings.attribute_dn', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=651,
  serialized_end=979,
)

_AUTHPROVIDERS.fields_by_name['providers'].message_type = _AUTHPROVIDER
_AUTHPROVIDER.fields_by_name['type'].enum_type = _AUTHPROVIDER_TYPE
_AUTHPROVIDER.fields_by_name['saml'].message_type = _SAMLSETTINGS
_AUTHPROVIDER_TYPE.containing_type = _AUTHPROVIDER
_AUTHPROVIDER.oneofs_by_name['settings'].fields.append(
  _AUTHPROVIDER.fields_by_name['saml'])
_AUTHPROVIDER.fields_by_name['saml'].containing_oneof = _AUTHPROVIDER.oneofs_by_name['settings']
DESCRIPTOR.message_types_by_name['AuthProviders'] = _AUTHPROVIDERS
DESCRIPTOR.message_types_by_name['AuthProvider'] = _AUTHPROVIDER
DESCRIPTOR.message_types_by_name['SamlSettings'] = _SAMLSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthProviders = _reflection.GeneratedProtocolMessageType('AuthProviders', (_message.Message,), {
  'DESCRIPTOR' : _AUTHPROVIDERS,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.AuthProviders)
  })
_sym_db.RegisterMessage(AuthProviders)

AuthProvider = _reflection.GeneratedProtocolMessageType('AuthProvider', (_message.Message,), {
  'DESCRIPTOR' : _AUTHPROVIDER,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.AuthProvider)
  })
_sym_db.RegisterMessage(AuthProvider)

SamlSettings = _reflection.GeneratedProtocolMessageType('SamlSettings', (_message.Message,), {
  'DESCRIPTOR' : _SAMLSETTINGS,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.SamlSettings)
  })
_sym_db.RegisterMessage(SamlSettings)


DESCRIPTOR._options = None
_AUTHPROVIDER.fields_by_name['name']._options = None
_AUTHPROVIDER.fields_by_name['description']._options = None
_AUTHPROVIDER.fields_by_name['hint']._options = None
_AUTHPROVIDER.fields_by_name['icon']._options = None
_SAMLSETTINGS.fields_by_name['idp_entity_id']._options = None
_SAMLSETTINGS.fields_by_name['idp_metadata_file']._options = None
_SAMLSETTINGS.fields_by_name['sp_entity_id']._options = None
_SAMLSETTINGS.fields_by_name['kibana_url']._options = None
_SAMLSETTINGS.fields_by_name['attribute_principal']._options = None
_SAMLSETTINGS.fields_by_name['attribute_groups']._options = None
_SAMLSETTINGS.fields_by_name['attribute_name']._options = None
_SAMLSETTINGS.fields_by_name['attribute_email']._options = None
_SAMLSETTINGS.fields_by_name['attribute_dn']._options = None
# @@protoc_insertion_point(module_scope)