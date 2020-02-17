#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
控制类定义了对机器人的所有操作，包括robot操作指令、rcu操作指令、机器人移动指令等。

通过调用Robot相关方法可以实现此功能

警告:
    充电过程中机器人不可运动。

    当电量不足时请及时充电。
"""

import grpc

from harix.rdk.proto.robot_skill_api import robot_control_api_pb2, robot_control_api_pb2_grpc
from harix.rdk.tools import tools


class RobotControlService(object):
    """
    机器人控制相关操作， 实现对机器人的各种操作
    """

    def __init__(self, grpc_url, authority):
        """
        初始化方法

        :param grpc_url: gRPC服务器地址
        """
        print("RobotControlService init--")
        self.grpc_url = grpc_url
        # print(grpc_url)
        channel = grpc.insecure_channel(grpc_url, options=[('grpc.default_authority', authority)])
        self.stub = robot_control_api_pb2_grpc.RobotControlServiceStub(channel)

    def reboot_rcu(self, header):
        """
        重启RCU

        :param request: 设备相关信息.
                如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """

        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.RebootRcu(robot_request)
        return res_data

    def shutdown_rcu(self, header):
        """
        关闭RCU

        :param header: robot基本信息
        :return:
        """

        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.ShutdownRcu(robot_request)
        return res_data

    def restart_app(self, header):
        """
        重启RCU上的Harix应用

        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.RestartApp(robot_request)
        return res_data

    def lock_rcu_screen(self, header):
        """
        锁屏

        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.LockRcuScreen(robot_request)
        return res_data

    def light_rcu_screen(self, header):
        """
        点亮屏幕

        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.LightRcuScreen(robot_request)
        return res_data

    def shutdown_robot(self, header):
        """
        关闭机器人

        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.ShutdownRobot(robot_request)
        return res_data

    def wakeup_robot(self, header):
        """
        唤醒机器人

        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.WakeupRobot(robot_request)
        return res_data

    def reset_robot(self, header):
        """
        重置机器人

        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.ResetRobot(robot_request)
        return res_data

    def reboot_robot(self, header):
        """
        重启机器人

        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.RebootRobot(robot_request)
        return res_data

    def reconnect_robot(self, header):
        """
        重连机器人

        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.ReconnectRobot(robot_request)
        return res_data

    def get_robot_actions(self, header):
        """
        通知RCU上报动作列表与舞蹈列表

        :param header: robot基本信息
        :return:
        """
        robot_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )
        res_data = self.stub.GetRobotActions(robot_request)
        return res_data

    def do_intent(self, header, request):
        """
        执行固定意图的任务

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        intent_request = robot_control_api_pb2.IntentRequest(
            common_req_info=tools.convert_header(header),
            intent_type=request["intent_type"],
            param=request["param"]
        )
        res_data = self.stub.DoIntent(intent_request)
        return res_data

    def do_action(self, header, request):
        """
        控制机器人执行某个动作
        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        action_request = robot_control_api_pb2.ActionRequest(
            common_req_info=tools.convert_header(header),
            action=request["action"],
            param=request["params"]
        )

        res_data = self.stub.DoAction(action_request)
        # print(res_data)
        return res_data

    def send_data(self, header, request):
        """
        发送数据到robot上
        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        send_data_request = robot_control_api_pb2.SendDataRequest(
            common_req_info=tools.convert_header(header),
            action=request["action"],
            param=request["params"]
        )

        res_data = self.stub.SendData(send_data_request)
        # print(res_data)
        return res_data

    def move(self, header, request):
        """
        移动

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """

        # print(request["map_model"])
        if "map_model" in request:
            map_model = robot_control_api_pb2.MapModel(
                angle=request["map_model"]["angle"],
                speed=request["map_model"]["speed"],
                distance=request["map_model"]["distance"]

            )
            move_request = robot_control_api_pb2.MoveRequest(
                common_req_info=tools.convert_header(header),
                map_model=map_model
            )
            res_data = self.stub.Move(move_request)
            # print(res_data)
            return res_data

        if "v_model" in request:
            v_model = robot_control_api_pb2.VelocityModel(
                vx=request["v_model"]["vx"],
                vy=request["v_model"]["vy"],
                vw=request["v_model"]["vw"]
            )
            move_request = robot_control_api_pb2.MoveRequest(
                common_req_info=tools.convert_header(header),
                v_model=v_model
            )
            res_data = self.stub.Move(move_request)
            # print(res_data)
            return res_data

        return None

    def stop(self, header):
        """
        停止

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        stop_request = robot_control_api_pb2.RobotRequest(
            common_req_info=tools.convert_header(header)
        )

        return self.stub.Stop(stop_request)

    def rotate(self, header, request):
        """
        旋转

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """

        rotate_request = robot_control_api_pb2.RotateRequest(
            common_req_info=tools.convert_header(header),
            module=request["module"],
            degree=request["degree"],
            speed=request["speed"]

        )

        res_data = self.stub.Rotate(rotate_request)
        # print(res_data)
        return res_data

    def set_position(self, header, request):
        """
        设置机器人位置

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        robot_position = robot_control_api_pb2.RobotPosition(
            x=request["x"],
            y=request["y"],
            theta=request["theta"]

        )
        position_request = robot_control_api_pb2.PositionRequest(
            common_req_info=tools.convert_header(header),
            position=robot_position

        )

        res_data = self.stub.SetPosition(position_request)
        # print(res_data)
        return res_data

    def emergency_stop(self, header, request):
        """
        急停

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        emergency_stop_request = robot_control_api_pb2.EmergencyStopRequest(
            common_req_info=tools.convert_header(header),
            emergency_stop_switch=request["emergency_stop_switch"]
        )

        res_data = self.stub.EmergencyStop(emergency_stop_request)
        # print(res_data)
        return res_data

    def start_screen_shot(self, header, request):
        """
        急停

        :param request: 设备相关信息.
        如果为空，则使用默认的关联设备
        :param header: robot基本信息
        :return:
        """
        CameraConfigs = []
        camera_configs = request["camera_configs"]

        for camera_config in camera_configs:
            name = camera_config["name"]
            grabber = camera_config["grabber"]
            CameraConfig = robot_control_api_pb2.CameraConfig(
                name=name,
                grabber=grabber
            )

            if "screen_shot" in camera_config:
                screen_shot = camera_config["screen_shot"]
                CameraConfig.screenshot.filename = screen_shot["filename"]

            if "short_video" in camera_config:
                short_video = camera_config["short_video"]
                CameraConfig.shortVideo.duration = short_video["duration"]
                CameraConfig.shortVideo.filename = short_video["filename"]

            if "cache" in camera_config:
                cache = camera_config["cache"]
                CameraConfig.cache.duration=cache["duration"]
                CameraConfig.cache.enable = cache["enable"]

            CameraConfigs.append(CameraConfig)

        config_screen_shot_request = robot_control_api_pb2.StartScreenShotRequest(
            common_req_info=tools.convert_header(header),
            camera_configs=CameraConfigs
        )

        res_data = self.stub.StartScreenShot(config_screen_shot_request)
        return res_data
