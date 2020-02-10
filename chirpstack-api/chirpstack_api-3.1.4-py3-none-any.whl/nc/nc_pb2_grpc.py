# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from chirpstack_api.nc import nc_pb2 as chirpstack__api_dot_nc_dot_nc__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class NetworkControllerServiceStub(object):
  """NetworkControllerService is the server to be implemeted by the network-controller.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.HandleUplinkMetaData = channel.unary_unary(
        '/nc.NetworkControllerService/HandleUplinkMetaData',
        request_serializer=chirpstack__api_dot_nc_dot_nc__pb2.HandleUplinkMetaDataRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.HandleDownlinkMetaData = channel.unary_unary(
        '/nc.NetworkControllerService/HandleDownlinkMetaData',
        request_serializer=chirpstack__api_dot_nc_dot_nc__pb2.HandleDownlinkMetaDataRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.HandleUplinkMACCommand = channel.unary_unary(
        '/nc.NetworkControllerService/HandleUplinkMACCommand',
        request_serializer=chirpstack__api_dot_nc_dot_nc__pb2.HandleUplinkMACCommandRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class NetworkControllerServiceServicer(object):
  """NetworkControllerService is the server to be implemeted by the network-controller.
  """

  def HandleUplinkMetaData(self, request, context):
    """HandleUplinkMetaData handles uplink meta-rata.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HandleDownlinkMetaData(self, request, context):
    """HandleDownlinkMetaData handles downlink meta-data.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HandleUplinkMACCommand(self, request, context):
    """HandleUplinkMACCommand handles an uplink mac-command.
    This method will only be called in case the mac-command request was
    enqueued throught the API or when the CID is >= 0x80 (proprietary
    mac-command range).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NetworkControllerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'HandleUplinkMetaData': grpc.unary_unary_rpc_method_handler(
          servicer.HandleUplinkMetaData,
          request_deserializer=chirpstack__api_dot_nc_dot_nc__pb2.HandleUplinkMetaDataRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'HandleDownlinkMetaData': grpc.unary_unary_rpc_method_handler(
          servicer.HandleDownlinkMetaData,
          request_deserializer=chirpstack__api_dot_nc_dot_nc__pb2.HandleDownlinkMetaDataRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'HandleUplinkMACCommand': grpc.unary_unary_rpc_method_handler(
          servicer.HandleUplinkMACCommand,
          request_deserializer=chirpstack__api_dot_nc_dot_nc__pb2.HandleUplinkMACCommandRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'nc.NetworkControllerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
