# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/containerregistry/v1/repository_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.containerregistry.v1 import repository_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/containerregistry/v1/repository_service.proto',
  package='yandex.cloud.containerregistry.v1',
  syntax='proto3',
  serialized_options=_b('\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistry'),
  serialized_pb=_b('\n:yandex/cloud/containerregistry/v1/repository_service.proto\x12!yandex.cloud.containerregistry.v1\x1a yandex/cloud/api/operation.proto\x1a yandex/cloud/access/access.proto\x1a\x32yandex/cloud/containerregistry/v1/repository.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1cgoogle/api/annotations.proto\";\n\x14GetRepositoryRequest\x12#\n\rrepository_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"}\n\x1aGetRepositoryByNameRequest\x12_\n\x0frepository_name\x18\x01 \x01(\tBF\xe8\xc7\x31\x01\xf2\xc7\x31>[a-z0-9]+(?:[._-][a-z0-9]+)*(/([a-z0-9]+(?:[._-][a-z0-9]+)*))*\"\xcc\x01\n\x17ListRepositoriesRequest\x12\x1d\n\x0bregistry_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1b\n\tfolder_id\x18\x06 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"x\n\x18ListRepositoriesResponse\x12\x43\n\x0crepositories\x18\x01 \x03(\x0b\x32-.yandex.cloud.containerregistry.v1.Repository\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xa8\t\n\x11RepositoryService\x12\xaa\x01\n\x03Get\x12\x37.yandex.cloud.containerregistry.v1.GetRepositoryRequest\x1a-.yandex.cloud.containerregistry.v1.Repository\";\x82\xd3\xe4\x93\x02\x35\x12\x33/container-registry/v1/repositories/{repository_id}\x12y\n\tGetByName\x12=.yandex.cloud.containerregistry.v1.GetRepositoryByNameRequest\x1a-.yandex.cloud.containerregistry.v1.Repository\x12\xac\x01\n\x04List\x12:.yandex.cloud.containerregistry.v1.ListRepositoriesRequest\x1a;.yandex.cloud.containerregistry.v1.ListRepositoriesResponse\"+\x82\xd3\xe4\x93\x02%\x12#/container-registry/v1/repositories\x12\xc3\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"L\x82\xd3\xe4\x93\x02\x46\x12\x44/container-registry/v1/repositories/{resource_id}:listAccessBindings\x12\xf3\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x8b\x01\x82\xd3\xe4\x93\x02H\"C/container-registry/v1/repositories/{resource_id}:setAccessBindings:\x01*\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x12\xff\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x91\x01\x82\xd3\xe4\x93\x02K\"F/container-registry/v1/repositories/{resource_id}:updateAccessBindings:\x01*\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.EmptyB\x80\x01\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistryb\x06proto3')
  ,
  dependencies=[yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_access_dot_access__pb2.DESCRIPTOR,yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETREPOSITORYREQUEST = _descriptor.Descriptor(
  name='GetRepositoryRequest',
  full_name='yandex.cloud.containerregistry.v1.GetRepositoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository_id', full_name='yandex.cloud.containerregistry.v1.GetRepositoryRequest.repository_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
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
  serialized_start=318,
  serialized_end=377,
)


_GETREPOSITORYBYNAMEREQUEST = _descriptor.Descriptor(
  name='GetRepositoryByNameRequest',
  full_name='yandex.cloud.containerregistry.v1.GetRepositoryByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository_name', full_name='yandex.cloud.containerregistry.v1.GetRepositoryByNameRequest.repository_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\362\3071>[a-z0-9]+(?:[._-][a-z0-9]+)*(/([a-z0-9]+(?:[._-][a-z0-9]+)*))*'), file=DESCRIPTOR),
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
  serialized_start=379,
  serialized_end=504,
)


_LISTREPOSITORIESREQUEST = _descriptor.Descriptor(
  name='ListRepositoriesRequest',
  full_name='yandex.cloud.containerregistry.v1.ListRepositoriesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registry_id', full_name='yandex.cloud.containerregistry.v1.ListRepositoriesRequest.registry_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.containerregistry.v1.ListRepositoriesRequest.folder_id', index=1,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.containerregistry.v1.ListRepositoriesRequest.page_size', index=2,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\006<=1000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.containerregistry.v1.ListRepositoriesRequest.page_token', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=100'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='yandex.cloud.containerregistry.v1.ListRepositoriesRequest.filter', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\006<=1000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_by', full_name='yandex.cloud.containerregistry.v1.ListRepositoriesRequest.order_by', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=100'), file=DESCRIPTOR),
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
  serialized_start=507,
  serialized_end=711,
)


_LISTREPOSITORIESRESPONSE = _descriptor.Descriptor(
  name='ListRepositoriesResponse',
  full_name='yandex.cloud.containerregistry.v1.ListRepositoriesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repositories', full_name='yandex.cloud.containerregistry.v1.ListRepositoriesResponse.repositories', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.containerregistry.v1.ListRepositoriesResponse.next_page_token', index=1,
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
  serialized_start=713,
  serialized_end=833,
)

_LISTREPOSITORIESRESPONSE.fields_by_name['repositories'].message_type = yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__pb2._REPOSITORY
DESCRIPTOR.message_types_by_name['GetRepositoryRequest'] = _GETREPOSITORYREQUEST
DESCRIPTOR.message_types_by_name['GetRepositoryByNameRequest'] = _GETREPOSITORYBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['ListRepositoriesRequest'] = _LISTREPOSITORIESREQUEST
DESCRIPTOR.message_types_by_name['ListRepositoriesResponse'] = _LISTREPOSITORIESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetRepositoryRequest = _reflection.GeneratedProtocolMessageType('GetRepositoryRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREPOSITORYREQUEST,
  __module__ = 'yandex.cloud.containerregistry.v1.repository_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.GetRepositoryRequest)
  ))
_sym_db.RegisterMessage(GetRepositoryRequest)

GetRepositoryByNameRequest = _reflection.GeneratedProtocolMessageType('GetRepositoryByNameRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREPOSITORYBYNAMEREQUEST,
  __module__ = 'yandex.cloud.containerregistry.v1.repository_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.GetRepositoryByNameRequest)
  ))
_sym_db.RegisterMessage(GetRepositoryByNameRequest)

ListRepositoriesRequest = _reflection.GeneratedProtocolMessageType('ListRepositoriesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTREPOSITORIESREQUEST,
  __module__ = 'yandex.cloud.containerregistry.v1.repository_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.ListRepositoriesRequest)
  ))
_sym_db.RegisterMessage(ListRepositoriesRequest)

ListRepositoriesResponse = _reflection.GeneratedProtocolMessageType('ListRepositoriesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTREPOSITORIESRESPONSE,
  __module__ = 'yandex.cloud.containerregistry.v1.repository_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.ListRepositoriesResponse)
  ))
_sym_db.RegisterMessage(ListRepositoriesResponse)


DESCRIPTOR._options = None
_GETREPOSITORYREQUEST.fields_by_name['repository_id']._options = None
_GETREPOSITORYBYNAMEREQUEST.fields_by_name['repository_name']._options = None
_LISTREPOSITORIESREQUEST.fields_by_name['registry_id']._options = None
_LISTREPOSITORIESREQUEST.fields_by_name['folder_id']._options = None
_LISTREPOSITORIESREQUEST.fields_by_name['page_size']._options = None
_LISTREPOSITORIESREQUEST.fields_by_name['page_token']._options = None
_LISTREPOSITORIESREQUEST.fields_by_name['filter']._options = None
_LISTREPOSITORIESREQUEST.fields_by_name['order_by']._options = None

_REPOSITORYSERVICE = _descriptor.ServiceDescriptor(
  name='RepositoryService',
  full_name='yandex.cloud.containerregistry.v1.RepositoryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=836,
  serialized_end=2028,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.containerregistry.v1.RepositoryService.Get',
    index=0,
    containing_service=None,
    input_type=_GETREPOSITORYREQUEST,
    output_type=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__pb2._REPOSITORY,
    serialized_options=_b('\202\323\344\223\0025\0223/container-registry/v1/repositories/{repository_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetByName',
    full_name='yandex.cloud.containerregistry.v1.RepositoryService.GetByName',
    index=1,
    containing_service=None,
    input_type=_GETREPOSITORYBYNAMEREQUEST,
    output_type=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__pb2._REPOSITORY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.containerregistry.v1.RepositoryService.List',
    index=2,
    containing_service=None,
    input_type=_LISTREPOSITORIESREQUEST,
    output_type=_LISTREPOSITORIESRESPONSE,
    serialized_options=_b('\202\323\344\223\002%\022#/container-registry/v1/repositories'),
  ),
  _descriptor.MethodDescriptor(
    name='ListAccessBindings',
    full_name='yandex.cloud.containerregistry.v1.RepositoryService.ListAccessBindings',
    index=3,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._LISTACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_access_dot_access__pb2._LISTACCESSBINDINGSRESPONSE,
    serialized_options=_b('\202\323\344\223\002F\022D/container-registry/v1/repositories/{resource_id}:listAccessBindings'),
  ),
  _descriptor.MethodDescriptor(
    name='SetAccessBindings',
    full_name='yandex.cloud.containerregistry.v1.RepositoryService.SetAccessBindings',
    index=4,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._SETACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002H\"C/container-registry/v1/repositories/{resource_id}:setAccessBindings:\001*\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAccessBindings',
    full_name='yandex.cloud.containerregistry.v1.RepositoryService.UpdateAccessBindings',
    index=5,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._UPDATEACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002K\"F/container-registry/v1/repositories/{resource_id}:updateAccessBindings:\001*\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty'),
  ),
])
_sym_db.RegisterServiceDescriptor(_REPOSITORYSERVICE)

DESCRIPTOR.services_by_name['RepositoryService'] = _REPOSITORYSERVICE

# @@protoc_insertion_point(module_scope)