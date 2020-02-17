from harix.rdk.proto.robot_mind import robotmind_pb2, robotmind_pb2_grpc
import grpc
from harix.rdk.tools import tools


class RobotMindSubscribe(object):

    def __init__(self, grpc_url,authority):
        """
        初始化方法

        :param grpc_url: gRPC服务器地址
        """
        print("robot mind Subscribe init--")
        self.grpc_url = grpc_url
        channel = grpc.insecure_channel(grpc_url, options=[('grpc.default_authority', authority)])
        self.stub = robotmind_pb2_grpc.RobotMindServiceStub(channel)

    def subscribe(self, request):
        """
        订阅
        :return:
        """
        register_skill_request = robotmind_pb2.RegisterSkillRequest(
            name=request["name"],
            skill_addr=request["skill_addr"]
        )

        if "skills" in request:
            register_skill_request.skills = request["skills"]

        if "skill_info" in request:
            register_skill_request.skill_info = request["skill_info"]

        res_data = self.stub.RegisterSkill(register_skill_request)
        return res_data














