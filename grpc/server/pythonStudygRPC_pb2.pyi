from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class messageData(_message.Message):
    __slots__ = ("nickName", "msg")
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    nickName: str
    msg: str
    def __init__(self, nickName: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...
