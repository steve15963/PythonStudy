# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pythonStudygRPC_pb2 as pythonStudygRPC__pb2


class ChatStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.send = channel.unary_unary(
                '/pythonStudygRPC.Chat/send',
                request_serializer=pythonStudygRPC__pb2.messageData.SerializeToString,
                response_deserializer=pythonStudygRPC__pb2.messageData.FromString,
                )


class ChatServicer(object):
    """Missing associated documentation comment in .proto file."""

    def send(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'send': grpc.unary_unary_rpc_method_handler(
                    servicer.send,
                    request_deserializer=pythonStudygRPC__pb2.messageData.FromString,
                    response_serializer=pythonStudygRPC__pb2.messageData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pythonStudygRPC.Chat', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Chat(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def send(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pythonStudygRPC.Chat/send',
            pythonStudygRPC__pb2.messageData.SerializeToString,
            pythonStudygRPC__pb2.messageData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)