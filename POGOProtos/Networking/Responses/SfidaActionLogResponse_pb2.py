# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Responses/SfidaActionLogResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Data.Logs import ActionLogEntry_pb2 as POGOProtos_dot_Data_dot_Logs_dot_ActionLogEntry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Responses/SfidaActionLogResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n<POGOProtos/Networking/Responses/SfidaActionLogResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a)POGOProtos/Data/Logs/ActionLogEntry.proto\"\xc5\x01\n\x16SfidaActionLogResponse\x12N\n\x06result\x18\x01 \x01(\x0e\x32>.POGOProtos.Networking.Responses.SfidaActionLogResponse.Result\x12\x39\n\x0blog_entries\x18\x02 \x03(\x0b\x32$.POGOProtos.Data.Logs.ActionLogEntry\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Data_dot_Logs_dot_ActionLogEntry__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SFIDAACTIONLOGRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='POGOProtos.Networking.Responses.SfidaActionLogResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=306,
  serialized_end=338,
)
_sym_db.RegisterEnumDescriptor(_SFIDAACTIONLOGRESPONSE_RESULT)


_SFIDAACTIONLOGRESPONSE = _descriptor.Descriptor(
  name='SfidaActionLogResponse',
  full_name='POGOProtos.Networking.Responses.SfidaActionLogResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Networking.Responses.SfidaActionLogResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_entries', full_name='POGOProtos.Networking.Responses.SfidaActionLogResponse.log_entries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SFIDAACTIONLOGRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=338,
)

_SFIDAACTIONLOGRESPONSE.fields_by_name['result'].enum_type = _SFIDAACTIONLOGRESPONSE_RESULT
_SFIDAACTIONLOGRESPONSE.fields_by_name['log_entries'].message_type = POGOProtos_dot_Data_dot_Logs_dot_ActionLogEntry__pb2._ACTIONLOGENTRY
_SFIDAACTIONLOGRESPONSE_RESULT.containing_type = _SFIDAACTIONLOGRESPONSE
DESCRIPTOR.message_types_by_name['SfidaActionLogResponse'] = _SFIDAACTIONLOGRESPONSE

SfidaActionLogResponse = _reflection.GeneratedProtocolMessageType('SfidaActionLogResponse', (_message.Message,), dict(
  DESCRIPTOR = _SFIDAACTIONLOGRESPONSE,
  __module__ = 'POGOProtos.Networking.Responses.SfidaActionLogResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.SfidaActionLogResponse)
  ))
_sym_db.RegisterMessage(SfidaActionLogResponse)


# @@protoc_insertion_point(module_scope)
