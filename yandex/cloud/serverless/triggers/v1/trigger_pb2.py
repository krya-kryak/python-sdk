# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/triggers/v1/trigger.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/serverless/triggers/v1/trigger.proto',
  package='yandex.cloud.serverless.triggers.v1',
  syntax='proto3',
  serialized_options=_b('\n\'yandex.cloud.api.serverless.triggers.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/triggers/v1;triggers'),
  serialized_pb=_b('\n1yandex/cloud/serverless/triggers/v1/trigger.proto\x12#yandex.cloud.serverless.triggers.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xe4\t\n\x07Trigger\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1f\n\tfolder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\x04name\x18\x04 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12H\n\x06labels\x18\x06 \x03(\x0b\x32\x38.yandex.cloud.serverless.triggers.v1.Trigger.LabelsEntry\x12\x45\n\x04rule\x18\x08 \x01(\x0b\x32\x31.yandex.cloud.serverless.triggers.v1.Trigger.RuleB\x04\xe8\xc7\x31\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xfd\x01\n\x04Rule\x12\x43\n\x05timer\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.Trigger.TimerH\x00\x12R\n\rmessage_queue\x18\x03 \x01(\x0b\x32\x39.yandex.cloud.serverless.triggers.v1.Trigger.MessageQueueH\x00\x12N\n\x0biot_message\x18\x04 \x01(\x0b\x32\x37.yandex.cloud.serverless.triggers.v1.Trigger.IoTMessageH\x00\x42\x0c\n\x04rule\x12\x04\xc0\xc1\x31\x01\x1a\x93\x01\n\x05Timer\x12&\n\x0f\x63ron_expression\x18\x01 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05<=100\x12R\n\x0finvoke_function\x18\x65 \x01(\x0b\x32\x37.yandex.cloud.serverless.triggers.v1.InvokeFunctionOnceH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\xc2\x02\n\x0cMessageQueue\x12\x10\n\x08queue_id\x18\x0b \x01(\t\x12(\n\x12service_account_id\x18\x03 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12P\n\x0e\x62\x61tch_settings\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.BatchSettingsB\x04\xe8\xc7\x31\x01\x12@\n\x12visibility_timeout\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05<=12h\x12R\n\x0finvoke_function\x18\x65 \x01(\x0b\x32\x37.yandex.cloud.serverless.triggers.v1.InvokeFunctionOnceH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\xb7\x01\n\nIoTMessage\x12\x19\n\x0bregistry_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x12\n\nmqtt_topic\x18\x03 \x01(\t\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\"i\n\x12InvokeFunctionOnce\x12!\n\x0b\x66unction_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x14\n\x0c\x66unction_tag\x18\x02 \x01(\t\x12\x1a\n\x12service_account_id\x18\x03 \x01(\t\"\xba\x01\n\x17InvokeFunctionWithRetry\x12!\n\x0b\x66unction_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x14\n\x0c\x66unction_tag\x18\x02 \x01(\t\x12\x1a\n\x12service_account_id\x18\x03 \x01(\t\x12J\n\x0eretry_settings\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.RetrySettings\"X\n\rBatchSettings\x12\x16\n\x04size\x18\x01 \x01(\x03\x42\x08\xfa\xc7\x31\x04\x30-10\x12/\n\x06\x63utoff\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\xe8\xc7\x31\x01\"c\n\rRetrySettings\x12\x1f\n\x0eretry_attempts\x18\x01 \x01(\x03\x42\x07\xfa\xc7\x31\x03\x31-5\x12\x31\n\x08interval\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\xe8\xc7\x31\x01*Z\n\x0bTriggerType\x12\x1c\n\x18TRIGGER_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TIMER\x10\x02\x12\x11\n\rMESSAGE_QUEUE\x10\x03\x12\x0f\n\x0bIOT_MESSAGE\x10\x04\x42{\n\'yandex.cloud.api.serverless.triggers.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/triggers/v1;triggersb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])

_TRIGGERTYPE = _descriptor.EnumDescriptor(
  name='TriggerType',
  full_name='yandex.cloud.serverless.triggers.v1.TriggerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRIGGER_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMER', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE_QUEUE', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IOT_MESSAGE', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1928,
  serialized_end=2018,
)
_sym_db.RegisterEnumDescriptor(_TRIGGERTYPE)

TriggerType = enum_type_wrapper.EnumTypeWrapper(_TRIGGERTYPE)
TRIGGER_TYPE_UNSPECIFIED = 0
TIMER = 2
MESSAGE_QUEUE = 3
IOT_MESSAGE = 4



_TRIGGER_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.serverless.triggers.v1.Trigger.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.serverless.triggers.v1.Trigger.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.serverless.triggers.v1.Trigger.LabelsEntry.value', index=1,
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
  serialized_start=477,
  serialized_end=522,
)

_TRIGGER_RULE = _descriptor.Descriptor(
  name='Rule',
  full_name='yandex.cloud.serverless.triggers.v1.Trigger.Rule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timer', full_name='yandex.cloud.serverless.triggers.v1.Trigger.Rule.timer', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_queue', full_name='yandex.cloud.serverless.triggers.v1.Trigger.Rule.message_queue', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iot_message', full_name='yandex.cloud.serverless.triggers.v1.Trigger.Rule.iot_message', index=2,
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
      name='rule', full_name='yandex.cloud.serverless.triggers.v1.Trigger.Rule.rule',
      index=0, containing_type=None, fields=[], serialized_options=_b('\300\3011\001')),
  ],
  serialized_start=525,
  serialized_end=778,
)

_TRIGGER_TIMER = _descriptor.Descriptor(
  name='Timer',
  full_name='yandex.cloud.serverless.triggers.v1.Trigger.Timer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cron_expression', full_name='yandex.cloud.serverless.triggers.v1.Trigger.Timer.cron_expression', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\005<=100'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invoke_function', full_name='yandex.cloud.serverless.triggers.v1.Trigger.Timer.invoke_function', index=1,
      number=101, type=11, cpp_type=10, label=1,
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
      name='action', full_name='yandex.cloud.serverless.triggers.v1.Trigger.Timer.action',
      index=0, containing_type=None, fields=[], serialized_options=_b('\300\3011\001')),
  ],
  serialized_start=781,
  serialized_end=928,
)

_TRIGGER_MESSAGEQUEUE = _descriptor.Descriptor(
  name='MessageQueue',
  full_name='yandex.cloud.serverless.triggers.v1.Trigger.MessageQueue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queue_id', full_name='yandex.cloud.serverless.triggers.v1.Trigger.MessageQueue.queue_id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.serverless.triggers.v1.Trigger.MessageQueue.service_account_id', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_settings', full_name='yandex.cloud.serverless.triggers.v1.Trigger.MessageQueue.batch_settings', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visibility_timeout', full_name='yandex.cloud.serverless.triggers.v1.Trigger.MessageQueue.visibility_timeout', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\005<=12h'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invoke_function', full_name='yandex.cloud.serverless.triggers.v1.Trigger.MessageQueue.invoke_function', index=4,
      number=101, type=11, cpp_type=10, label=1,
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
      name='action', full_name='yandex.cloud.serverless.triggers.v1.Trigger.MessageQueue.action',
      index=0, containing_type=None, fields=[], serialized_options=_b('\300\3011\001')),
  ],
  serialized_start=931,
  serialized_end=1253,
)

_TRIGGER_IOTMESSAGE = _descriptor.Descriptor(
  name='IoTMessage',
  full_name='yandex.cloud.serverless.triggers.v1.Trigger.IoTMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registry_id', full_name='yandex.cloud.serverless.triggers.v1.Trigger.IoTMessage.registry_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='yandex.cloud.serverless.triggers.v1.Trigger.IoTMessage.device_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mqtt_topic', full_name='yandex.cloud.serverless.triggers.v1.Trigger.IoTMessage.mqtt_topic', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invoke_function', full_name='yandex.cloud.serverless.triggers.v1.Trigger.IoTMessage.invoke_function', index=3,
      number=101, type=11, cpp_type=10, label=1,
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
      name='action', full_name='yandex.cloud.serverless.triggers.v1.Trigger.IoTMessage.action',
      index=0, containing_type=None, fields=[], serialized_options=_b('\300\3011\001')),
  ],
  serialized_start=1256,
  serialized_end=1439,
)

_TRIGGER = _descriptor.Descriptor(
  name='Trigger',
  full_name='yandex.cloud.serverless.triggers.v1.Trigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.serverless.triggers.v1.Trigger.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.serverless.triggers.v1.Trigger.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.serverless.triggers.v1.Trigger.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.serverless.triggers.v1.Trigger.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.serverless.triggers.v1.Trigger.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.serverless.triggers.v1.Trigger.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule', full_name='yandex.cloud.serverless.triggers.v1.Trigger.rule', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRIGGER_LABELSENTRY, _TRIGGER_RULE, _TRIGGER_TIMER, _TRIGGER_MESSAGEQUEUE, _TRIGGER_IOTMESSAGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=1439,
)


_INVOKEFUNCTIONONCE = _descriptor.Descriptor(
  name='InvokeFunctionOnce',
  full_name='yandex.cloud.serverless.triggers.v1.InvokeFunctionOnce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='function_id', full_name='yandex.cloud.serverless.triggers.v1.InvokeFunctionOnce.function_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='function_tag', full_name='yandex.cloud.serverless.triggers.v1.InvokeFunctionOnce.function_tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.serverless.triggers.v1.InvokeFunctionOnce.service_account_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1441,
  serialized_end=1546,
)


_INVOKEFUNCTIONWITHRETRY = _descriptor.Descriptor(
  name='InvokeFunctionWithRetry',
  full_name='yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='function_id', full_name='yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetry.function_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='function_tag', full_name='yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetry.function_tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetry.service_account_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retry_settings', full_name='yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetry.retry_settings', index=3,
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
  serialized_start=1549,
  serialized_end=1735,
)


_BATCHSETTINGS = _descriptor.Descriptor(
  name='BatchSettings',
  full_name='yandex.cloud.serverless.triggers.v1.BatchSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='yandex.cloud.serverless.triggers.v1.BatchSettings.size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\0040-10'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cutoff', full_name='yandex.cloud.serverless.triggers.v1.BatchSettings.cutoff', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
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
  serialized_start=1737,
  serialized_end=1825,
)


_RETRYSETTINGS = _descriptor.Descriptor(
  name='RetrySettings',
  full_name='yandex.cloud.serverless.triggers.v1.RetrySettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retry_attempts', full_name='yandex.cloud.serverless.triggers.v1.RetrySettings.retry_attempts', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\0031-5'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='yandex.cloud.serverless.triggers.v1.RetrySettings.interval', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
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
  serialized_start=1827,
  serialized_end=1926,
)

_TRIGGER_LABELSENTRY.containing_type = _TRIGGER
_TRIGGER_RULE.fields_by_name['timer'].message_type = _TRIGGER_TIMER
_TRIGGER_RULE.fields_by_name['message_queue'].message_type = _TRIGGER_MESSAGEQUEUE
_TRIGGER_RULE.fields_by_name['iot_message'].message_type = _TRIGGER_IOTMESSAGE
_TRIGGER_RULE.containing_type = _TRIGGER
_TRIGGER_RULE.oneofs_by_name['rule'].fields.append(
  _TRIGGER_RULE.fields_by_name['timer'])
_TRIGGER_RULE.fields_by_name['timer'].containing_oneof = _TRIGGER_RULE.oneofs_by_name['rule']
_TRIGGER_RULE.oneofs_by_name['rule'].fields.append(
  _TRIGGER_RULE.fields_by_name['message_queue'])
_TRIGGER_RULE.fields_by_name['message_queue'].containing_oneof = _TRIGGER_RULE.oneofs_by_name['rule']
_TRIGGER_RULE.oneofs_by_name['rule'].fields.append(
  _TRIGGER_RULE.fields_by_name['iot_message'])
_TRIGGER_RULE.fields_by_name['iot_message'].containing_oneof = _TRIGGER_RULE.oneofs_by_name['rule']
_TRIGGER_TIMER.fields_by_name['invoke_function'].message_type = _INVOKEFUNCTIONONCE
_TRIGGER_TIMER.containing_type = _TRIGGER
_TRIGGER_TIMER.oneofs_by_name['action'].fields.append(
  _TRIGGER_TIMER.fields_by_name['invoke_function'])
_TRIGGER_TIMER.fields_by_name['invoke_function'].containing_oneof = _TRIGGER_TIMER.oneofs_by_name['action']
_TRIGGER_MESSAGEQUEUE.fields_by_name['batch_settings'].message_type = _BATCHSETTINGS
_TRIGGER_MESSAGEQUEUE.fields_by_name['visibility_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TRIGGER_MESSAGEQUEUE.fields_by_name['invoke_function'].message_type = _INVOKEFUNCTIONONCE
_TRIGGER_MESSAGEQUEUE.containing_type = _TRIGGER
_TRIGGER_MESSAGEQUEUE.oneofs_by_name['action'].fields.append(
  _TRIGGER_MESSAGEQUEUE.fields_by_name['invoke_function'])
_TRIGGER_MESSAGEQUEUE.fields_by_name['invoke_function'].containing_oneof = _TRIGGER_MESSAGEQUEUE.oneofs_by_name['action']
_TRIGGER_IOTMESSAGE.fields_by_name['invoke_function'].message_type = _INVOKEFUNCTIONWITHRETRY
_TRIGGER_IOTMESSAGE.containing_type = _TRIGGER
_TRIGGER_IOTMESSAGE.oneofs_by_name['action'].fields.append(
  _TRIGGER_IOTMESSAGE.fields_by_name['invoke_function'])
_TRIGGER_IOTMESSAGE.fields_by_name['invoke_function'].containing_oneof = _TRIGGER_IOTMESSAGE.oneofs_by_name['action']
_TRIGGER.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRIGGER.fields_by_name['labels'].message_type = _TRIGGER_LABELSENTRY
_TRIGGER.fields_by_name['rule'].message_type = _TRIGGER_RULE
_INVOKEFUNCTIONWITHRETRY.fields_by_name['retry_settings'].message_type = _RETRYSETTINGS
_BATCHSETTINGS.fields_by_name['cutoff'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_RETRYSETTINGS.fields_by_name['interval'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['Trigger'] = _TRIGGER
DESCRIPTOR.message_types_by_name['InvokeFunctionOnce'] = _INVOKEFUNCTIONONCE
DESCRIPTOR.message_types_by_name['InvokeFunctionWithRetry'] = _INVOKEFUNCTIONWITHRETRY
DESCRIPTOR.message_types_by_name['BatchSettings'] = _BATCHSETTINGS
DESCRIPTOR.message_types_by_name['RetrySettings'] = _RETRYSETTINGS
DESCRIPTOR.enum_types_by_name['TriggerType'] = _TRIGGERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Trigger = _reflection.GeneratedProtocolMessageType('Trigger', (_message.Message,), dict(

  LabelsEntry = _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), dict(
    DESCRIPTOR = _TRIGGER_LABELSENTRY,
    __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.LabelsEntry)
    ))
  ,

  Rule = _reflection.GeneratedProtocolMessageType('Rule', (_message.Message,), dict(
    DESCRIPTOR = _TRIGGER_RULE,
    __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.Rule)
    ))
  ,

  Timer = _reflection.GeneratedProtocolMessageType('Timer', (_message.Message,), dict(
    DESCRIPTOR = _TRIGGER_TIMER,
    __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.Timer)
    ))
  ,

  MessageQueue = _reflection.GeneratedProtocolMessageType('MessageQueue', (_message.Message,), dict(
    DESCRIPTOR = _TRIGGER_MESSAGEQUEUE,
    __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.MessageQueue)
    ))
  ,

  IoTMessage = _reflection.GeneratedProtocolMessageType('IoTMessage', (_message.Message,), dict(
    DESCRIPTOR = _TRIGGER_IOTMESSAGE,
    __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.IoTMessage)
    ))
  ,
  DESCRIPTOR = _TRIGGER,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger)
  ))
_sym_db.RegisterMessage(Trigger)
_sym_db.RegisterMessage(Trigger.LabelsEntry)
_sym_db.RegisterMessage(Trigger.Rule)
_sym_db.RegisterMessage(Trigger.Timer)
_sym_db.RegisterMessage(Trigger.MessageQueue)
_sym_db.RegisterMessage(Trigger.IoTMessage)

InvokeFunctionOnce = _reflection.GeneratedProtocolMessageType('InvokeFunctionOnce', (_message.Message,), dict(
  DESCRIPTOR = _INVOKEFUNCTIONONCE,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.InvokeFunctionOnce)
  ))
_sym_db.RegisterMessage(InvokeFunctionOnce)

InvokeFunctionWithRetry = _reflection.GeneratedProtocolMessageType('InvokeFunctionWithRetry', (_message.Message,), dict(
  DESCRIPTOR = _INVOKEFUNCTIONWITHRETRY,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetry)
  ))
_sym_db.RegisterMessage(InvokeFunctionWithRetry)

BatchSettings = _reflection.GeneratedProtocolMessageType('BatchSettings', (_message.Message,), dict(
  DESCRIPTOR = _BATCHSETTINGS,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.BatchSettings)
  ))
_sym_db.RegisterMessage(BatchSettings)

RetrySettings = _reflection.GeneratedProtocolMessageType('RetrySettings', (_message.Message,), dict(
  DESCRIPTOR = _RETRYSETTINGS,
  __module__ = 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.RetrySettings)
  ))
_sym_db.RegisterMessage(RetrySettings)


DESCRIPTOR._options = None
_TRIGGER_LABELSENTRY._options = None
_TRIGGER_RULE.oneofs_by_name['rule']._options = None
_TRIGGER_TIMER.oneofs_by_name['action']._options = None
_TRIGGER_TIMER.fields_by_name['cron_expression']._options = None
_TRIGGER_MESSAGEQUEUE.oneofs_by_name['action']._options = None
_TRIGGER_MESSAGEQUEUE.fields_by_name['service_account_id']._options = None
_TRIGGER_MESSAGEQUEUE.fields_by_name['batch_settings']._options = None
_TRIGGER_MESSAGEQUEUE.fields_by_name['visibility_timeout']._options = None
_TRIGGER_IOTMESSAGE.oneofs_by_name['action']._options = None
_TRIGGER_IOTMESSAGE.fields_by_name['registry_id']._options = None
_TRIGGER.fields_by_name['folder_id']._options = None
_TRIGGER.fields_by_name['name']._options = None
_TRIGGER.fields_by_name['rule']._options = None
_INVOKEFUNCTIONONCE.fields_by_name['function_id']._options = None
_INVOKEFUNCTIONWITHRETRY.fields_by_name['function_id']._options = None
_BATCHSETTINGS.fields_by_name['size']._options = None
_BATCHSETTINGS.fields_by_name['cutoff']._options = None
_RETRYSETTINGS.fields_by_name['retry_attempts']._options = None
_RETRYSETTINGS.fields_by_name['interval']._options = None
# @@protoc_insertion_point(module_scope)