# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from chirpstack_api.as_pb.external.api import multicastGroup_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class MulticastGroupServiceStub(object):
  """MulticastGroupService is the service managing multicast-groups.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/api.MulticastGroupService/Create',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.CreateMulticastGroupRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.CreateMulticastGroupResponse.FromString,
        )
    self.Get = channel.unary_unary(
        '/api.MulticastGroupService/Get',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.GetMulticastGroupRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.GetMulticastGroupResponse.FromString,
        )
    self.Update = channel.unary_unary(
        '/api.MulticastGroupService/Update',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.UpdateMulticastGroupRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Delete = channel.unary_unary(
        '/api.MulticastGroupService/Delete',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.DeleteMulticastGroupRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.List = channel.unary_unary(
        '/api.MulticastGroupService/List',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.ListMulticastGroupRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.ListMulticastGroupResponse.FromString,
        )
    self.AddDevice = channel.unary_unary(
        '/api.MulticastGroupService/AddDevice',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.AddDeviceToMulticastGroupRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.RemoveDevice = channel.unary_unary(
        '/api.MulticastGroupService/RemoveDevice',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.RemoveDeviceFromMulticastGroupRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Enqueue = channel.unary_unary(
        '/api.MulticastGroupService/Enqueue',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.EnqueueMulticastQueueItemRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.EnqueueMulticastQueueItemResponse.FromString,
        )
    self.FlushQueue = channel.unary_unary(
        '/api.MulticastGroupService/FlushQueue',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.FlushMulticastGroupQueueItemsRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListQueue = channel.unary_unary(
        '/api.MulticastGroupService/ListQueue',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.ListMulticastGroupQueueItemsRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.ListMulticastGroupQueueItemsResponse.FromString,
        )


class MulticastGroupServiceServicer(object):
  """MulticastGroupService is the service managing multicast-groups.
  """

  def Create(self, request, context):
    """Create creates the given multicast-group.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Get returns a multicast-group given an ID.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Update updates the given multicast-group.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Delete deletes a multicast-group given an ID.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """List lists the available multicast-groups.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddDevice(self, request, context):
    """AddDevice adds the given device to the multicast-group.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveDevice(self, request, context):
    """RemoveDevice removes the given device from the multicast-group.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Enqueue(self, request, context):
    """Enqueue adds the given item to the multicast-queue.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FlushQueue(self, request, context):
    """FlushQueue flushes the multicast-group queue.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListQueue(self, request, context):
    """ListQueue lists the items in the multicast-group queue.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MulticastGroupServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.CreateMulticastGroupRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.CreateMulticastGroupResponse.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.GetMulticastGroupRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.GetMulticastGroupResponse.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.UpdateMulticastGroupRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.DeleteMulticastGroupRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.ListMulticastGroupRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.ListMulticastGroupResponse.SerializeToString,
      ),
      'AddDevice': grpc.unary_unary_rpc_method_handler(
          servicer.AddDevice,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.AddDeviceToMulticastGroupRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'RemoveDevice': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveDevice,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.RemoveDeviceFromMulticastGroupRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Enqueue': grpc.unary_unary_rpc_method_handler(
          servicer.Enqueue,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.EnqueueMulticastQueueItemRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.EnqueueMulticastQueueItemResponse.SerializeToString,
      ),
      'FlushQueue': grpc.unary_unary_rpc_method_handler(
          servicer.FlushQueue,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.FlushMulticastGroupQueueItemsRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListQueue': grpc.unary_unary_rpc_method_handler(
          servicer.ListQueue,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.ListMulticastGroupQueueItemsRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.ListMulticastGroupQueueItemsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.MulticastGroupService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
