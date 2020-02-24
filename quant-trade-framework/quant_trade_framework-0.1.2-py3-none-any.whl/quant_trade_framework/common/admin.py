#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 14:20
# @Author  : chuan.yang
# @File    : admin.py
# @Desc    :
from pymongo import MongoClient
from quant_trade_framework.common.constant import SystemConfig
from quant_trade_framework.common.logConfig import Logger
from datetime import datetime
import hashlib

logger = Logger.module_logger("system")
class UserManager:

    @staticmethod
    def user_create(user_name:str,user_pwd:str):
        """
        create user information
        :param user_name: string,user name
        :param user_pwd:string,user password
        :return: None
        """
        result = False
        if SystemConfig.WORKING_MODE == SystemConfig.WORKING_MODE_SUPERVISOR:
            try:
                mc = MongoClient(
                    host=SystemConfig.MONGODB_HOST,
                    port=SystemConfig.MONGODB_PORT,
                    username=SystemConfig.MONGODB_USER,
                    password=SystemConfig.MONGODB_PWD
                )
                passwd_md5 = hashlib.md5(user_pwd.encode('utf8')).hexdigest()
                db = mc[SystemConfig.MONGODB_DB_ADMIN]
                collection = db[SystemConfig.MONGODB_COL_USERS]
                cursor = collection.insert_one({"name": user_name, "password": passwd_md5,"create_datetime":datetime.now()})
                if cursor:
                    result = True
            except BaseException as e:
                logger.error(str(e))
        else:
            logger.error("no authority to run this method")
        return result

    @staticmethod
    def user_verify(user_name:str,user_pwd:str):
        """
        verify user name and password
        :param user_name:string,user name
        :param pwd:string,user password
        :return: bool, true or false
        """
        result = False
        try:
            mc = MongoClient(
                host=SystemConfig.MONGODB_HOST,
                port=SystemConfig.MONGODB_PORT,
                username=SystemConfig.MONGODB_USER,
                password=SystemConfig.MONGODB_PWD
            )
            passwd_md5 = hashlib.md5(user_pwd.encode('utf8')).hexdigest()
            db = mc[SystemConfig.MONGODB_DB_ADMIN]
            collection = db[SystemConfig.MONGODB_COL_USERS]
            cursor = collection.find_one({"name": user_name,"password":passwd_md5})
            if cursor:
                result = True
        except BaseException as e:
            logger.error(str(e))
        return result