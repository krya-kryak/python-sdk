# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.datatransfer.v1 import endpoint_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/datatransfer/v1/endpoint_service.proto',
  package='yandex.cloud.datatransfer.v1',
  syntax='proto3',
  serialized_options=b'\n yandex.cloud.api.datatransfer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1;datatransfer',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3yandex/cloud/datatransfer/v1/endpoint_service.proto\x12\x1cyandex.cloud.datatransfer.v1\x1a\x1cgoogle/api/annotations.proto\x1a+yandex/cloud/datatransfer/v1/endpoint.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\")\n\x12GetEndpointRequest\x12\x13\n\x0b\x65ndpoint_id\x18\x01 \x01(\t\"\x8f\x01\n\x15\x43reateEndpointRequest\x12\x11\n\tfolder_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12@\n\x08settings\x18\x34 \x01(\x0b\x32..yandex.cloud.datatransfer.v1.EndpointSettings\"-\n\x16\x43reateEndpointMetadata\x12\x13\n\x0b\x65ndpoint_id\x18\x01 \x01(\t\"\x91\x01\n\x15UpdateEndpointRequest\x12\x13\n\x0b\x65ndpoint_id\x18\n \x01(\t\x12\x0c\n\x04name\x18\x0b \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0c \x01(\t\x12@\n\x08settings\x18\x34 \x01(\x0b\x32..yandex.cloud.datatransfer.v1.EndpointSettings\"-\n\x16UpdateEndpointMetadata\x12\x13\n\x0b\x65ndpoint_id\x18\x01 \x01(\t\",\n\x15\x44\x65leteEndpointRequest\x12\x13\n\x0b\x65ndpoint_id\x18\x01 \x01(\t\"-\n\x16\x44\x65leteEndpointMetadata\x12\x13\n\x0b\x65ndpoint_id\x18\x01 \x01(\t2\xa3\x05\n\x0f\x45ndpointService\x12\x83\x01\n\x03Get\x12\x30.yandex.cloud.datatransfer.v1.GetEndpointRequest\x1a&.yandex.cloud.datatransfer.v1.Endpoint\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1/endpoint/{endpoint_id}\x12\x9f\x01\n\x06\x43reate\x12\x33.yandex.cloud.datatransfer.v1.CreateEndpointRequest\x1a!.yandex.cloud.operation.Operation\"=\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/endpoint:\x01*\xb2\xd2*\"\n\x16\x43reateEndpointMetadata\x12\x08\x45ndpoint\x12\xad\x01\n\x06Update\x12\x33.yandex.cloud.datatransfer.v1.UpdateEndpointRequest\x1a!.yandex.cloud.operation.Operation\"K\x82\xd3\xe4\x93\x02\x1f\x32\x1a/v1/endpoint/{endpoint_id}:\x01*\xb2\xd2*\"\n\x16UpdateEndpointMetadata\x12\x08\x45ndpoint\x12\xb7\x01\n\x06\x44\x65lete\x12\x33.yandex.cloud.datatransfer.v1.DeleteEndpointRequest\x1a!.yandex.cloud.operation.Operation\"U\x82\xd3\xe4\x93\x02\x1c*\x1a/v1/endpoint/{endpoint_id}\xb2\xd2*/\n\x16\x44\x65leteEndpointMetadata\x12\x15google.protobuf.EmptyBq\n yandex.cloud.api.datatransfer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1;datatransferb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,])




_GETENDPOINTREQUEST = _descriptor.Descriptor(
  name='GetEndpointRequest',
  full_name='yandex.cloud.datatransfer.v1.GetEndpointRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint_id', full_name='yandex.cloud.datatransfer.v1.GetEndpointRequest.endpoint_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=234,
  serialized_end=275,
)


_CREATEENDPOINTREQUEST = _descriptor.Descriptor(
  name='CreateEndpointRequest',
  full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='settings', full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest.settings', index=3,
      number=52, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=278,
  serialized_end=421,
)


_CREATEENDPOINTMETADATA = _descriptor.Descriptor(
  name='CreateEndpointMetadata',
  full_name='yandex.cloud.datatransfer.v1.CreateEndpointMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint_id', full_name='yandex.cloud.datatransfer.v1.CreateEndpointMetadata.endpoint_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=423,
  serialized_end=468,
)


_UPDATEENDPOINTREQUEST = _descriptor.Descriptor(
  name='UpdateEndpointRequest',
  full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint_id', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest.endpoint_id', index=0,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest.name', index=1,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest.description', index=2,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='settings', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest.settings', index=3,
      number=52, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=471,
  serialized_end=616,
)


_UPDATEENDPOINTMETADATA = _descriptor.Descriptor(
  name='UpdateEndpointMetadata',
  full_name='yandex.cloud.datatransfer.v1.UpdateEndpointMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint_id', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointMetadata.endpoint_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=618,
  serialized_end=663,
)


_DELETEENDPOINTREQUEST = _descriptor.Descriptor(
  name='DeleteEndpointRequest',
  full_name='yandex.cloud.datatransfer.v1.DeleteEndpointRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint_id', full_name='yandex.cloud.datatransfer.v1.DeleteEndpointRequest.endpoint_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=665,
  serialized_end=709,
)


_DELETEENDPOINTMETADATA = _descriptor.Descriptor(
  name='DeleteEndpointMetadata',
  full_name='yandex.cloud.datatransfer.v1.DeleteEndpointMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint_id', full_name='yandex.cloud.datatransfer.v1.DeleteEndpointMetadata.endpoint_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=711,
  serialized_end=756,
)

_CREATEENDPOINTREQUEST.fields_by_name['settings'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2._ENDPOINTSETTINGS
_UPDATEENDPOINTREQUEST.fields_by_name['settings'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2._ENDPOINTSETTINGS
DESCRIPTOR.message_types_by_name['GetEndpointRequest'] = _GETENDPOINTREQUEST
DESCRIPTOR.message_types_by_name['CreateEndpointRequest'] = _CREATEENDPOINTREQUEST
DESCRIPTOR.message_types_by_name['CreateEndpointMetadata'] = _CREATEENDPOINTMETADATA
DESCRIPTOR.message_types_by_name['UpdateEndpointRequest'] = _UPDATEENDPOINTREQUEST
DESCRIPTOR.message_types_by_name['UpdateEndpointMetadata'] = _UPDATEENDPOINTMETADATA
DESCRIPTOR.message_types_by_name['DeleteEndpointRequest'] = _DELETEENDPOINTREQUEST
DESCRIPTOR.message_types_by_name['DeleteEndpointMetadata'] = _DELETEENDPOINTMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetEndpointRequest = _reflection.GeneratedProtocolMessageType('GetEndpointRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETENDPOINTREQUEST,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.GetEndpointRequest)
  })
_sym_db.RegisterMessage(GetEndpointRequest)

CreateEndpointRequest = _reflection.GeneratedProtocolMessageType('CreateEndpointRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEENDPOINTREQUEST,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.CreateEndpointRequest)
  })
_sym_db.RegisterMessage(CreateEndpointRequest)

CreateEndpointMetadata = _reflection.GeneratedProtocolMessageType('CreateEndpointMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEENDPOINTMETADATA,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.CreateEndpointMetadata)
  })
_sym_db.RegisterMessage(CreateEndpointMetadata)

UpdateEndpointRequest = _reflection.GeneratedProtocolMessageType('UpdateEndpointRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEENDPOINTREQUEST,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.UpdateEndpointRequest)
  })
_sym_db.RegisterMessage(UpdateEndpointRequest)

UpdateEndpointMetadata = _reflection.GeneratedProtocolMessageType('UpdateEndpointMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEENDPOINTMETADATA,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.UpdateEndpointMetadata)
  })
_sym_db.RegisterMessage(UpdateEndpointMetadata)

DeleteEndpointRequest = _reflection.GeneratedProtocolMessageType('DeleteEndpointRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEENDPOINTREQUEST,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.DeleteEndpointRequest)
  })
_sym_db.RegisterMessage(DeleteEndpointRequest)

DeleteEndpointMetadata = _reflection.GeneratedProtocolMessageType('DeleteEndpointMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEENDPOINTMETADATA,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.DeleteEndpointMetadata)
  })
_sym_db.RegisterMessage(DeleteEndpointMetadata)


DESCRIPTOR._options = None

_ENDPOINTSERVICE = _descriptor.ServiceDescriptor(
  name='EndpointService',
  full_name='yandex.cloud.datatransfer.v1.EndpointService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=759,
  serialized_end=1434,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.datatransfer.v1.EndpointService.Get',
    index=0,
    containing_service=None,
    input_type=_GETENDPOINTREQUEST,
    output_type=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2._ENDPOINT,
    serialized_options=b'\202\323\344\223\002\034\022\032/v1/endpoint/{endpoint_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.datatransfer.v1.EndpointService.Create',
    index=1,
    containing_service=None,
    input_type=_CREATEENDPOINTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\021\"\014/v1/endpoint:\001*\262\322*\"\n\026CreateEndpointMetadata\022\010Endpoint',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.datatransfer.v1.EndpointService.Update',
    index=2,
    containing_service=None,
    input_type=_UPDATEENDPOINTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\0372\032/v1/endpoint/{endpoint_id}:\001*\262\322*\"\n\026UpdateEndpointMetadata\022\010Endpoint',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.datatransfer.v1.EndpointService.Delete',
    index=3,
    containing_service=None,
    input_type=_DELETEENDPOINTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\034*\032/v1/endpoint/{endpoint_id}\262\322*/\n\026DeleteEndpointMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENDPOINTSERVICE)

DESCRIPTOR.services_by_name['EndpointService'] = _ENDPOINTSERVICE

# @@protoc_insertion_point(module_scope)