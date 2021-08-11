# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/organizationmanager/v1/organization_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.organizationmanager.v1 import organization_pb2 as yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_organization__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/organizationmanager/v1/organization_service.proto',
  package='yandex.cloud.organizationmanager.v1',
  syntax='proto3',
  serialized_options=b'\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanager',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>yandex/cloud/organizationmanager/v1/organization_service.proto\x12#yandex.cloud.organizationmanager.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a\x36yandex/cloud/organizationmanager/v1/organization.proto\x1a yandex/cloud/access/access.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"?\n\x16GetOrganizationRequest\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"t\n\x18ListOrganizationsRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"~\n\x19ListOrganizationsResponse\x12H\n\rorganizations\x18\x01 \x03(\x0b\x32\x31.yandex.cloud.organizationmanager.v1.Organization\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xe1\x01\n\x19UpdateOrganizationRequest\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x18\n\x05title\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=256\"5\n\x1aUpdateOrganizationMetadata\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\"\x88\x01\n!ListOrganizationOperationsRequest\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"t\n\"ListOrganizationOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xa0\x0c\n\x13OrganizationService\x12\xb7\x01\n\x03Get\x12;.yandex.cloud.organizationmanager.v1.GetOrganizationRequest\x1a\x31.yandex.cloud.organizationmanager.v1.Organization\"@\x82\xd3\xe4\x93\x02:\x12\x38/organization-manager/v1/organizations/{organization_id}\x12\xb5\x01\n\x04List\x12=.yandex.cloud.organizationmanager.v1.ListOrganizationsRequest\x1a>.yandex.cloud.organizationmanager.v1.ListOrganizationsResponse\".\x82\xd3\xe4\x93\x02(\x12&/organization-manager/v1/organizations\x12\xde\x01\n\x06Update\x12>.yandex.cloud.organizationmanager.v1.UpdateOrganizationRequest\x1a!.yandex.cloud.operation.Operation\"q\x82\xd3\xe4\x93\x02=28/organization-manager/v1/organizations/{organization_id}:\x01*\xb2\xd2**\n\x1aUpdateOrganizationMetadata\x12\x0cOrganization\x12\xee\x01\n\x0eListOperations\x12\x46.yandex.cloud.organizationmanager.v1.ListOrganizationOperationsRequest\x1aG.yandex.cloud.organizationmanager.v1.ListOrganizationOperationsResponse\"K\x82\xd3\xe4\x93\x02\x45\x12\x43/organization-manager/v1/organizations/{organization_id}/operations\x12\xc6\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"O\x82\xd3\xe4\x93\x02I\x12G/organization-manager/v1/organizations/{resource_id}:listAccessBindings\x12\xf6\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x8e\x01\x82\xd3\xe4\x93\x02K\"F/organization-manager/v1/organizations/{resource_id}:setAccessBindings:\x01*\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x12\x82\x02\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x94\x01\x82\xd3\xe4\x93\x02N\"I/organization-manager/v1/organizations/{resource_id}:updateAccessBindings:\x01*\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.EmptyB\x86\x01\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanagerb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_organization__pb2.DESCRIPTOR,yandex_dot_cloud_dot_access_dot_access__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETORGANIZATIONREQUEST = _descriptor.Descriptor(
  name='GetOrganizationRequest',
  full_name='yandex.cloud.organizationmanager.v1.GetOrganizationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='yandex.cloud.organizationmanager.v1.GetOrganizationRequest.organization_id', index=0,
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
  serialized_start=362,
  serialized_end=425,
)


_LISTORGANIZATIONSREQUEST = _descriptor.Descriptor(
  name='ListOrganizationsRequest',
  full_name='yandex.cloud.organizationmanager.v1.ListOrganizationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.organizationmanager.v1.ListOrganizationsRequest.page_size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0060-1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.organizationmanager.v1.ListOrganizationsRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='yandex.cloud.organizationmanager.v1.ListOrganizationsRequest.filter', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=427,
  serialized_end=543,
)


_LISTORGANIZATIONSRESPONSE = _descriptor.Descriptor(
  name='ListOrganizationsResponse',
  full_name='yandex.cloud.organizationmanager.v1.ListOrganizationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organizations', full_name='yandex.cloud.organizationmanager.v1.ListOrganizationsResponse.organizations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.organizationmanager.v1.ListOrganizationsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=545,
  serialized_end=671,
)


_UPDATEORGANIZATIONREQUEST = _descriptor.Descriptor(
  name='UpdateOrganizationRequest',
  full_name='yandex.cloud.organizationmanager.v1.UpdateOrganizationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='yandex.cloud.organizationmanager.v1.UpdateOrganizationRequest.organization_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='yandex.cloud.organizationmanager.v1.UpdateOrganizationRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.organizationmanager.v1.UpdateOrganizationRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.organizationmanager.v1.UpdateOrganizationRequest.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=256', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='yandex.cloud.organizationmanager.v1.UpdateOrganizationRequest.title', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=256', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=674,
  serialized_end=899,
)


_UPDATEORGANIZATIONMETADATA = _descriptor.Descriptor(
  name='UpdateOrganizationMetadata',
  full_name='yandex.cloud.organizationmanager.v1.UpdateOrganizationMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='yandex.cloud.organizationmanager.v1.UpdateOrganizationMetadata.organization_id', index=0,
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
  serialized_start=901,
  serialized_end=954,
)


_LISTORGANIZATIONOPERATIONSREQUEST = _descriptor.Descriptor(
  name='ListOrganizationOperationsRequest',
  full_name='yandex.cloud.organizationmanager.v1.ListOrganizationOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='yandex.cloud.organizationmanager.v1.ListOrganizationOperationsRequest.organization_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.organizationmanager.v1.ListOrganizationOperationsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0060-1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.organizationmanager.v1.ListOrganizationOperationsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=957,
  serialized_end=1093,
)


_LISTORGANIZATIONOPERATIONSRESPONSE = _descriptor.Descriptor(
  name='ListOrganizationOperationsResponse',
  full_name='yandex.cloud.organizationmanager.v1.ListOrganizationOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='yandex.cloud.organizationmanager.v1.ListOrganizationOperationsResponse.operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.organizationmanager.v1.ListOrganizationOperationsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1095,
  serialized_end=1211,
)

_LISTORGANIZATIONSRESPONSE.fields_by_name['organizations'].message_type = yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_organization__pb2._ORGANIZATION
_UPDATEORGANIZATIONREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_LISTORGANIZATIONOPERATIONSRESPONSE.fields_by_name['operations'].message_type = yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION
DESCRIPTOR.message_types_by_name['GetOrganizationRequest'] = _GETORGANIZATIONREQUEST
DESCRIPTOR.message_types_by_name['ListOrganizationsRequest'] = _LISTORGANIZATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListOrganizationsResponse'] = _LISTORGANIZATIONSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateOrganizationRequest'] = _UPDATEORGANIZATIONREQUEST
DESCRIPTOR.message_types_by_name['UpdateOrganizationMetadata'] = _UPDATEORGANIZATIONMETADATA
DESCRIPTOR.message_types_by_name['ListOrganizationOperationsRequest'] = _LISTORGANIZATIONOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListOrganizationOperationsResponse'] = _LISTORGANIZATIONOPERATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetOrganizationRequest = _reflection.GeneratedProtocolMessageType('GetOrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONREQUEST,
  '__module__' : 'yandex.cloud.organizationmanager.v1.organization_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.GetOrganizationRequest)
  })
_sym_db.RegisterMessage(GetOrganizationRequest)

ListOrganizationsRequest = _reflection.GeneratedProtocolMessageType('ListOrganizationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTORGANIZATIONSREQUEST,
  '__module__' : 'yandex.cloud.organizationmanager.v1.organization_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.ListOrganizationsRequest)
  })
_sym_db.RegisterMessage(ListOrganizationsRequest)

ListOrganizationsResponse = _reflection.GeneratedProtocolMessageType('ListOrganizationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTORGANIZATIONSRESPONSE,
  '__module__' : 'yandex.cloud.organizationmanager.v1.organization_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.ListOrganizationsResponse)
  })
_sym_db.RegisterMessage(ListOrganizationsResponse)

UpdateOrganizationRequest = _reflection.GeneratedProtocolMessageType('UpdateOrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEORGANIZATIONREQUEST,
  '__module__' : 'yandex.cloud.organizationmanager.v1.organization_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.UpdateOrganizationRequest)
  })
_sym_db.RegisterMessage(UpdateOrganizationRequest)

UpdateOrganizationMetadata = _reflection.GeneratedProtocolMessageType('UpdateOrganizationMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEORGANIZATIONMETADATA,
  '__module__' : 'yandex.cloud.organizationmanager.v1.organization_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.UpdateOrganizationMetadata)
  })
_sym_db.RegisterMessage(UpdateOrganizationMetadata)

ListOrganizationOperationsRequest = _reflection.GeneratedProtocolMessageType('ListOrganizationOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTORGANIZATIONOPERATIONSREQUEST,
  '__module__' : 'yandex.cloud.organizationmanager.v1.organization_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.ListOrganizationOperationsRequest)
  })
_sym_db.RegisterMessage(ListOrganizationOperationsRequest)

ListOrganizationOperationsResponse = _reflection.GeneratedProtocolMessageType('ListOrganizationOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTORGANIZATIONOPERATIONSRESPONSE,
  '__module__' : 'yandex.cloud.organizationmanager.v1.organization_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.ListOrganizationOperationsResponse)
  })
_sym_db.RegisterMessage(ListOrganizationOperationsResponse)


DESCRIPTOR._options = None
_GETORGANIZATIONREQUEST.fields_by_name['organization_id']._options = None
_LISTORGANIZATIONSREQUEST.fields_by_name['page_size']._options = None
_LISTORGANIZATIONSREQUEST.fields_by_name['page_token']._options = None
_LISTORGANIZATIONSREQUEST.fields_by_name['filter']._options = None
_UPDATEORGANIZATIONREQUEST.fields_by_name['organization_id']._options = None
_UPDATEORGANIZATIONREQUEST.fields_by_name['name']._options = None
_UPDATEORGANIZATIONREQUEST.fields_by_name['description']._options = None
_UPDATEORGANIZATIONREQUEST.fields_by_name['title']._options = None
_LISTORGANIZATIONOPERATIONSREQUEST.fields_by_name['organization_id']._options = None
_LISTORGANIZATIONOPERATIONSREQUEST.fields_by_name['page_size']._options = None
_LISTORGANIZATIONOPERATIONSREQUEST.fields_by_name['page_token']._options = None

_ORGANIZATIONSERVICE = _descriptor.ServiceDescriptor(
  name='OrganizationService',
  full_name='yandex.cloud.organizationmanager.v1.OrganizationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1214,
  serialized_end=2782,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.organizationmanager.v1.OrganizationService.Get',
    index=0,
    containing_service=None,
    input_type=_GETORGANIZATIONREQUEST,
    output_type=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_organization__pb2._ORGANIZATION,
    serialized_options=b'\202\323\344\223\002:\0228/organization-manager/v1/organizations/{organization_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.organizationmanager.v1.OrganizationService.List',
    index=1,
    containing_service=None,
    input_type=_LISTORGANIZATIONSREQUEST,
    output_type=_LISTORGANIZATIONSRESPONSE,
    serialized_options=b'\202\323\344\223\002(\022&/organization-manager/v1/organizations',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.organizationmanager.v1.OrganizationService.Update',
    index=2,
    containing_service=None,
    input_type=_UPDATEORGANIZATIONREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002=28/organization-manager/v1/organizations/{organization_id}:\001*\262\322**\n\032UpdateOrganizationMetadata\022\014Organization',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListOperations',
    full_name='yandex.cloud.organizationmanager.v1.OrganizationService.ListOperations',
    index=3,
    containing_service=None,
    input_type=_LISTORGANIZATIONOPERATIONSREQUEST,
    output_type=_LISTORGANIZATIONOPERATIONSRESPONSE,
    serialized_options=b'\202\323\344\223\002E\022C/organization-manager/v1/organizations/{organization_id}/operations',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListAccessBindings',
    full_name='yandex.cloud.organizationmanager.v1.OrganizationService.ListAccessBindings',
    index=4,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._LISTACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_access_dot_access__pb2._LISTACCESSBINDINGSRESPONSE,
    serialized_options=b'\202\323\344\223\002I\022G/organization-manager/v1/organizations/{resource_id}:listAccessBindings',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetAccessBindings',
    full_name='yandex.cloud.organizationmanager.v1.OrganizationService.SetAccessBindings',
    index=5,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._SETACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002K\"F/organization-manager/v1/organizations/{resource_id}:setAccessBindings:\001*\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAccessBindings',
    full_name='yandex.cloud.organizationmanager.v1.OrganizationService.UpdateAccessBindings',
    index=6,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._UPDATEACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002N\"I/organization-manager/v1/organizations/{resource_id}:updateAccessBindings:\001*\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORGANIZATIONSERVICE)

DESCRIPTOR.services_by_name['OrganizationService'] = _ORGANIZATIONSERVICE

# @@protoc_insertion_point(module_scope)
