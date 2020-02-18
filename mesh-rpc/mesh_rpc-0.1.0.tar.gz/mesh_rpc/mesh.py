import grpc

from .lib.rpc_pb2 import PeerTopicInfo, PublishData, Data
from .lib.rpc_pb2_grpc import MeshStub
from .exp import MeshRPCException
from .util import getTopicsFromGeospace
from . import crypto
from .auth_gateway import AuthGateway

class MeshRPC:
    def __init__(self, endpoint, auth_token):
        pem = crypto._load_credential_from_file('ca.rpc.pravah.io.crt')
        
        gateway = AuthGateway()
        gateway.set_auth(auth_token)
        
        channel_credential = grpc.ssl_channel_credentials(pem)
        call_credential = grpc.metadata_call_credentials(gateway, 'Auth Gateway')
        composite_credentials = grpc.composite_channel_credentials(
            channel_credential,
            call_credential
        )
        c= grpc.secure_channel(endpoint, composite_credentials)
        self.stub = MeshStub(c)

    def subscribe(self, channel, geospace):
        topicList = getTopicsFromGeospace(channel, geospace)

        m = PeerTopicInfo()
        m.topics.extend(topicList)
        
        s = self.stub.Subscribe(m)

        return s
    
    def unsubscribe(self, channel, geospace):
        topicList = getTopicsFromGeospace(channel, geospace)

        m = PeerTopicInfo()
        m.topics.extend(topicList)

        return self.stub.Unsubscribe(m)

    def registerToPublish(self, channel, geospace):
        topicList = getTopicsFromGeospace(channel, geospace)

        m = PeerTopicInfo()
        m.topics.extend(topicList)

        try:
            p = self.stub.RegisterToPublish(m)
            return p
        except grpc.RpcError as e:
            raise MeshRPCException(e.details())
    
    def unregisterToPublish(self, channel, geospace):
        topicList = getTopicsFromGeospace(channel, geospace)

        m = PeerTopicInfo()
        m.topics.extend(topicList)

        try:
            p = self.stub.UnregisterToPublish(m)
            return p
        except grpc.RpcError as e:
            raise MeshRPCException(e.details())

    def publish(self, channel, geospace, raw):
        topicList = getTopicsFromGeospace(channel, geospace)

        pd = PublishData()
        
        pd.info.topics.extend(topicList)
        pd.data.raw = raw

        try:
            res = self.stub.Publish(pd)
            return res
        except grpc.RpcError as e:
            raise MeshRPCException(e.details())
