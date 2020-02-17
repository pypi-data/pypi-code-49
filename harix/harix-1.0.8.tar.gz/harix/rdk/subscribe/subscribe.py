from harix.rdk.proto.robot_mind import robotskill_pb2, robotskill_pb2_grpc
import grpc
from harix.rdk.tools import tools


class Subscribe(object):

    def __init__(self, grpc_url,authority):
        """
        初始化方法

        :param grpc_url: gRPC服务器地址
        """
        print("Subscribe init--")
        self.grpc_url = grpc_url
        channel = grpc.insecure_channel(grpc_url, options=[('grpc.default_authority', authority)])
        self.stub = robotskill_pb2_grpc.RobotSkillServiceStub(channel)

    def subscribe(self, header, request):
        """
        订阅
        :param request: 参数
        :param header: robot基本信息
        :return:
        """
        common_req_info = tools.convert_header(header)

        enable_request = robotskill_pb2.EnableSkillRequest(
            common_req_info=common_req_info
        )

        if "ability" in request:
            enable_request.ability = request["ability"]

        if "param" in request:
            enable_request.param = request["param"]

        if "sub_addr" in request:
            enable_request.sub_addr = request["sub_addr"]

        if "sub_name" in request:
            enable_request.sub_name = request["sub_name"]

        if "extra_type" in request:
            enable_request.sub_name = request["extra_type"]

        res_data = self.stub.EnableSkill(enable_request)
        return res_data





