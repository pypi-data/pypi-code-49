# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import reactions_pb2 as reactions__pb2


class ReactionsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetReactions = channel.unary_unary(
        '/dialog.reactions.Reactions/GetReactions',
        request_serializer=reactions__pb2.GetReactionsRequest.SerializeToString,
        response_deserializer=reactions__pb2.GetReactionsResponse.FromString,
        )
    self.MessageSetReaction = channel.unary_unary(
        '/dialog.reactions.Reactions/MessageSetReaction',
        request_serializer=reactions__pb2.RequestSetMessageReaction.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.MessageRemoveReaction = channel.unary_unary(
        '/dialog.reactions.Reactions/MessageRemoveReaction',
        request_serializer=reactions__pb2.RequestRemoveMessageReaction.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ReactionsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetReactions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MessageSetReaction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MessageRemoveReaction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ReactionsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetReactions': grpc.unary_unary_rpc_method_handler(
          servicer.GetReactions,
          request_deserializer=reactions__pb2.GetReactionsRequest.FromString,
          response_serializer=reactions__pb2.GetReactionsResponse.SerializeToString,
      ),
      'MessageSetReaction': grpc.unary_unary_rpc_method_handler(
          servicer.MessageSetReaction,
          request_deserializer=reactions__pb2.RequestSetMessageReaction.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'MessageRemoveReaction': grpc.unary_unary_rpc_method_handler(
          servicer.MessageRemoveReaction,
          request_deserializer=reactions__pb2.RequestRemoveMessageReaction.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dialog.reactions.Reactions', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
