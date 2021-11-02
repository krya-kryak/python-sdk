# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cdn/v1/provider_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/cdn/v1/provider_service.proto',
  package='yandex.cloud.cdn.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdn',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*yandex/cloud/cdn/v1/provider_service.proto\x12\x13yandex.cloud.cdn.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"_\n\x17\x41\x63tivateProviderRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12#\n\rprovider_type\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\";\n\x18\x41\x63tivateProviderMetadata\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"@\n\x1dListActivatedProvidersRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"3\n\x1eListActivatedProvidersResponse\x12\x11\n\tproviders\x18\x01 \x03(\t2\xe1\x02\n\x0fProviderService\x12\xb7\x01\n\x08\x41\x63tivate\x12,.yandex.cloud.cdn.v1.ActivateProviderRequest\x1a!.yandex.cloud.operation.Operation\"Z\x82\xd3\xe4\x93\x02\x1f\"\x1a/cdn/v1/providers:activate:\x01*\xb2\xd2*1\n\x18\x41\x63tivateProviderMetadata\x12\x15google.protobuf.Empty\x12\x93\x01\n\rListActivated\x12\x32.yandex.cloud.cdn.v1.ListActivatedProvidersRequest\x1a\x33.yandex.cloud.cdn.v1.ListActivatedProvidersResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/cdn/v1/providersBV\n\x17yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdnb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_ACTIVATEPROVIDERREQUEST = _descriptor.Descriptor(
  name='ActivateProviderRequest',
  full_name='yandex.cloud.cdn.v1.ActivateProviderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.cdn.v1.ActivateProviderRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider_type', full_name='yandex.cloud.cdn.v1.ActivateProviderRequest.provider_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=202,
  serialized_end=297,
)


_ACTIVATEPROVIDERMETADATA = _descriptor.Descriptor(
  name='ActivateProviderMetadata',
  full_name='yandex.cloud.cdn.v1.ActivateProviderMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.cdn.v1.ActivateProviderMetadata.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=299,
  serialized_end=358,
)


_LISTACTIVATEDPROVIDERSREQUEST = _descriptor.Descriptor(
  name='ListActivatedProvidersRequest',
  full_name='yandex.cloud.cdn.v1.ListActivatedProvidersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.cdn.v1.ListActivatedProvidersRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=360,
  serialized_end=424,
)


_LISTACTIVATEDPROVIDERSRESPONSE = _descriptor.Descriptor(
  name='ListActivatedProvidersResponse',
  full_name='yandex.cloud.cdn.v1.ListActivatedProvidersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='providers', full_name='yandex.cloud.cdn.v1.ListActivatedProvidersResponse.providers', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=426,
  serialized_end=477,
)

DESCRIPTOR.message_types_by_name['ActivateProviderRequest'] = _ACTIVATEPROVIDERREQUEST
DESCRIPTOR.message_types_by_name['ActivateProviderMetadata'] = _ACTIVATEPROVIDERMETADATA
DESCRIPTOR.message_types_by_name['ListActivatedProvidersRequest'] = _LISTACTIVATEDPROVIDERSREQUEST
DESCRIPTOR.message_types_by_name['ListActivatedProvidersResponse'] = _LISTACTIVATEDPROVIDERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActivateProviderRequest = _reflection.GeneratedProtocolMessageType('ActivateProviderRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATEPROVIDERREQUEST,
  '__module__' : 'yandex.cloud.cdn.v1.provider_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.ActivateProviderRequest)
  })
_sym_db.RegisterMessage(ActivateProviderRequest)

ActivateProviderMetadata = _reflection.GeneratedProtocolMessageType('ActivateProviderMetadata', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATEPROVIDERMETADATA,
  '__module__' : 'yandex.cloud.cdn.v1.provider_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.ActivateProviderMetadata)
  })
_sym_db.RegisterMessage(ActivateProviderMetadata)

ListActivatedProvidersRequest = _reflection.GeneratedProtocolMessageType('ListActivatedProvidersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTACTIVATEDPROVIDERSREQUEST,
  '__module__' : 'yandex.cloud.cdn.v1.provider_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.ListActivatedProvidersRequest)
  })
_sym_db.RegisterMessage(ListActivatedProvidersRequest)

ListActivatedProvidersResponse = _reflection.GeneratedProtocolMessageType('ListActivatedProvidersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTACTIVATEDPROVIDERSRESPONSE,
  '__module__' : 'yandex.cloud.cdn.v1.provider_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.ListActivatedProvidersResponse)
  })
_sym_db.RegisterMessage(ListActivatedProvidersResponse)


DESCRIPTOR._options = None
_ACTIVATEPROVIDERREQUEST.fields_by_name['folder_id']._options = None
_ACTIVATEPROVIDERREQUEST.fields_by_name['provider_type']._options = None
_ACTIVATEPROVIDERMETADATA.fields_by_name['folder_id']._options = None
_LISTACTIVATEDPROVIDERSREQUEST.fields_by_name['folder_id']._options = None

_PROVIDERSERVICE = _descriptor.ServiceDescriptor(
  name='ProviderService',
  full_name='yandex.cloud.cdn.v1.ProviderService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=480,
  serialized_end=833,
  methods=[
  _descriptor.MethodDescriptor(
    name='Activate',
    full_name='yandex.cloud.cdn.v1.ProviderService.Activate',
    index=0,
    containing_service=None,
    input_type=_ACTIVATEPROVIDERREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\037\"\032/cdn/v1/providers:activate:\001*\262\322*1\n\030ActivateProviderMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListActivated',
    full_name='yandex.cloud.cdn.v1.ProviderService.ListActivated',
    index=1,
    containing_service=None,
    input_type=_LISTACTIVATEDPROVIDERSREQUEST,
    output_type=_LISTACTIVATEDPROVIDERSRESPONSE,
    serialized_options=b'\202\323\344\223\002\023\022\021/cdn/v1/providers',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROVIDERSERVICE)

DESCRIPTOR.services_by_name['ProviderService'] = _PROVIDERSERVICE

# @@protoc_insertion_point(module_scope)