# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from chirpstack_api.as_pb.external.api import serviceProfile_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ServiceProfileServiceStub(object):
  """ServiceProfileService is the service managing service-profiles.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/api.ServiceProfileService/Create',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.CreateServiceProfileRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.CreateServiceProfileResponse.FromString,
        )
    self.Get = channel.unary_unary(
        '/api.ServiceProfileService/Get',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.GetServiceProfileRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.GetServiceProfileResponse.FromString,
        )
    self.Update = channel.unary_unary(
        '/api.ServiceProfileService/Update',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.UpdateServiceProfileRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Delete = channel.unary_unary(
        '/api.ServiceProfileService/Delete',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.DeleteServiceProfileRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.List = channel.unary_unary(
        '/api.ServiceProfileService/List',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.ListServiceProfileRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.ListServiceProfileResponse.FromString,
        )


class ServiceProfileServiceServicer(object):
  """ServiceProfileService is the service managing service-profiles.
  """

  def Create(self, request, context):
    """Create creates the given service-profile.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Get returns the service-profile matching the given id.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Update updates the given serviceprofile.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Delete deletes the service-profile matching the given id.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """List lists the available service-profiles.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServiceProfileServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.CreateServiceProfileRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.CreateServiceProfileResponse.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.GetServiceProfileRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.GetServiceProfileResponse.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.UpdateServiceProfileRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.DeleteServiceProfileRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.ListServiceProfileRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_serviceProfile__pb2.ListServiceProfileResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.ServiceProfileService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
