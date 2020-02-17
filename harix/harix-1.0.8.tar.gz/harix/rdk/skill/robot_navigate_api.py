#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
导航类模块，本模块封装了机器人运动导航相关的类、方法、结构
"""

import grpc
from harix.rdk.proto.robot_skill_api import robot_navigate_api_pb2, robot_navigate_api_pb2_grpc
from harix.rdk.tools import tools


class RobotNavigateService(object):
    """
    导航相关类
    """

    def __init__(self, grpc_url, authority):
        """
        初始化方法

        :param grpc_url: gRPC服务器地址
        """
        print("RobotNavigateService init--")
        self.grpc_url = grpc_url
        channel = grpc.insecure_channel(grpc_url, options=[('grpc.default_authority', authority)])
        self.stub = robot_navigate_api_pb2_grpc.RobotNavigateServiceStub(channel)

    def get_map(self, header, request):
        """
        获取机器人地图信息

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """

        map_request = robot_navigate_api_pb2.MapRequest(
            common_req_info=tools.convert_header(header),
            query_type=request["query_type"],
            map_id=request["map_id"],
            map_name=request["map_name"]

        )
        res_data = self.stub.GetRobotMapList(map_request)
        return res_data

    def get_map_location(self, header, request):
        """
        获取地图上预先定义的兴趣点

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        map_request = robot_navigate_api_pb2.MapRequest(
            common_req_info=tools.convert_header(header),
            query_type=request["query_type"],
            map_id=request["map_id"],
            map_name=request["map_name"]

        )
        res_data = self.stub.GetMapLocation(map_request)
        return res_data

    def get_patrol_route(self, header, request):
        """
        获取巡逻路径信息

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        patrol_request = robot_navigate_api_pb2.GetPatrolRequest(
            common_req_info=tools.convert_header(header),
            query_type=request["query_type"],
            map_id=request["map_id"],
            map_name=request["map_name"],
            route_id=request["route_id"],
            route_name=request["route_name"]
        )
        res_data = self.stub.GetPatrolRoute(patrol_request)
        return res_data

    def delete_robot_map(self, header, request):
        """
        删除机器人的地图

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        map_request = robot_navigate_api_pb2.MapRequest(
            common_req_info=tools.convert_header(header),
            query_type=request["query_type"],
            map_id=request["map_id"],
            map_name=request["map_name"]

        )
        res_data = self.stub.DeleteRobotMap(map_request)
        return res_data

    def set_active_map(self, header, request):
        """
        设置机器人当前使用的地图

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        map_request = robot_navigate_api_pb2.MapRequest(
            common_req_info=tools.convert_header(header),
            query_type=request["query_type"],
            map_id=request["map_id"],
            map_name=request["map_name"]

        )
        res_data = self.stub.setActiveMap(map_request)
        return res_data

    def notify_map_updated(self, header, request):
        """
        通知机器人地图状态的改变

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        map_request = robot_navigate_api_pb2.MapRequest(
            common_req_info=tools.convert_header(header),
            query_type=request["query_type"],
            map_id=request["map_id"],
            map_name=request["map_name"]

        )
        res_data = self.stub.NotifyMapUpdated(map_request)
        return res_data

    def start_patrol(self, header, request):
        """
        启动巡逻

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        print(request["locations"])
        patrol_request = robot_navigate_api_pb2.PatrolRequest(
            common_req_info=tools.convert_header(header),
            map_id=request["map_id"],
            map_name=request["map_name"],
            route_id=request["route_id"],
            route_name=request["route_name"],
            mode=request["mode"],
            start_time=request["start_time"],
            end_time=request["end_time"],
            patrol_times=request["patrol_times"],
            points=request["points"],
            locations=request["locations"]
        )
        res_data = self.stub.StartPatrol(patrol_request)
        return res_data

    def pause_patrol(self, header, request):
        """
        暂停巡逻

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        patrol_request = robot_navigate_api_pb2.PatrolRequest(
            common_req_info=tools.convert_header(header),
            map_id=request["map_id"],
            map_name=request["map_name"],
            route_id=request["route_id"],
            route_name=request["route_name"],
            mode=request["mode"],
            start_time=request["start_time"],
            end_time=request["end_time"],
            patrol_times=request["patrol_times"],
            points=request["points"],
            locations=request["locations"]

        )
        res_data = self.stub.PausePatrol(patrol_request)
        return res_data

    def resume_patrol(self, header, request):
        """
        恢复巡逻

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        patrol_request = robot_navigate_api_pb2.PatrolRequest(
            common_req_info=tools.convert_header(header),
            map_id=request["map_id"],
            map_name=request["map_name"],
            route_id=request["route_id"],
            route_name=request["route_name"],
            mode=request["mode"],
            start_time=request["start_time"],
            end_time=request["end_time"],
            patrol_times=request["patrol_times"],
            points=request["points"],
            locations=request["locations"],

        )
        res_data = self.stub.ResumePatrol(patrol_request)
        return res_data

    def stop_patrol(self, header, request):
        """
        停止巡逻

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        patrol_request = robot_navigate_api_pb2.PatrolRequest(
            common_req_info=tools.convert_header(header),
            map_id=request["map_id"],
            map_name=request["map_name"],
            route_id=request["route_id"],
            route_name=request["route_name"],
            mode=request["mode"],
            start_time=request["start_time"],
            end_time=request["end_time"],
            patrol_times=request["patrol_times"],
            points=request["points"],
            locations=request["locations"],

        )
        res_data = self.stub.StopPatrol(patrol_request)
        return res_data

    def enable_calibrationpoints(self, header, request):
        """
        校准点上传

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        enable_calibration_points_request = robot_navigate_api_pb2.EnableCalibrationPointsRequest(
            common_req_info=tools.convert_header(header),
            enable_calibration_points=request["enable_calibration_points"]
        )
        res_data = self.stub.EnableCalibrationPoints(enable_calibration_points_request)
        return res_data

    def move_to(self, header, request):
        """
        移动到指定位置
        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        point_json = request["point"]
        point = robot_navigate_api_pb2.Point(
            mapId=point_json["map_id"],
            mapName=point_json["map_name"],
            x=point_json["x"],
            y=point_json["y"],
            yaw=point_json["yaw"]
        )
        moveto_request = robot_navigate_api_pb2.MoveToRequest(
            common_req_info=tools.convert_header(header),
            mode=request["mode"],
            angle=request["angle"],
            speed=request["speed"],
            point=point,
            location_id=request["location_id"]
        )
        res_data = self.stub.MoveTo(moveto_request)
        return res_data

    def move_by_path(self, header, request):
        """
        移动一段路径

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """

        points = []
        input_points = request["points"]

        for input_point in input_points:
            point = robot_navigate_api_pb2.Point(
                mapId=input_point["map_id"],
                mapName=input_point["map_name"],
                x=input_point["x"],
                y=input_point["y"],
                yaw=input_point["yaw"]
            )
            points.append(point)

        move_by_path_request = robot_navigate_api_pb2.MoveByPathRequest(
            common_req_info=tools.convert_header(header),
            mode=request["mode"],
            speed=request["speed"],
            patrol_times=request["patrol_times"],
            points=points,
            locations=request["locations"]
        )
        res_data = self.stub.MoveByPath(move_by_path_request)
        return res_data

    def set_robot_location(self, header, request):
        """
        设置机器人位置

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        point = robot_navigate_api_pb2.Point(
            mapId=request["map_id"],
            mapName=request["map_name"],
            x=request["x"],
            y=request["y"],
            yaw=request["yaw"]
        )
        set_robot_location_request = robot_navigate_api_pb2.SetRobotLocationRequest(
            common_req_info=tools.convert_header(header),
            point=point,
        )
        res_data = self.stub.SetRobotLocation(set_robot_location_request)
        return res_data

    def set_default_charging_site(self, header, request):
        """
        设置默认充电桩位置

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        position = robot_navigate_api_pb2.Position(
            x=request["x"],
            y=request["y"],
            theta=request["theta"]
        )
        charging_site_request = robot_navigate_api_pb2.ChargingSiteRequest(
            common_req_info=tools.convert_header(header),
            charging_site_name=request["charging_site_name"],
            position=position,

        )
        res_data = self.stub.SetDefaultChargingSite(charging_site_request)
        return res_data

    def attach_charging_pile(self, header, request):
        """
        充电

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """
        position = robot_navigate_api_pb2.Position(
            x=request["x"],
            y=request["y"],
            theta=request["theta"]
        )
        charging_site_request = robot_navigate_api_pb2.ChargingSiteRequest(
            common_req_info=tools.convert_header(header),
            charging_site_name=request["charging_site_name"],
            position=position,

        )
        res_data = self.stub.AttachChargingPile(charging_site_request)
        return res_data

    def detach_charging_pile(self, header, request):
        """
        取消充电

        :param header: robot基本信息
        :param request: 地图相关参数
        :return:
        """

        position = robot_navigate_api_pb2.Position(
            x=request["x"],
            y=request["y"],
            theta=request["theta"]
        )
        charging_site_request = robot_navigate_api_pb2.ChargingSiteRequest(
            common_req_info=tools.convert_header(header),
            charging_site_name=request["charging_site_name"],
            position=position,

        )
        res_data = self.stub.DetachChargingPile(charging_site_request)
        return res_data
