# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


import sys
import json
import time

from .component import *
from .tools import *
from .log import logger


def get_url(cmd, text):
    timestamp = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    md5 = MD5(cmd + timestamp + text)
    return '%s?timestamp=%s&sign=%s' % (cmd, timestamp, md5)


authorization = ''
login_time = 0


class OCC:
    def __init__(self, conf):
        self.conf = conf

    def logout(self):
        global authorization, login_time
        authorization = ''
        login_time = 0

    def login(self):
        global authorization, login_time

        if authorization and time.time() - login_time < 25 * 50:
            return

        cmd = '/api/base/auth/login'
        body = {
            "name": self.conf.username,
            "password": self.conf.password
        }
        js, code = self.request(cmd, body)
        if code == 0:
            if 'userToken' in js:
                authorization = js['userToken']
                login_time = time.time()
        return code

    def upload(self, version, type, filename):
        from requests_toolbelt import MultipartEncoder
        global authorization, login_time
        cmd = '/api/resource/component/upload'

        m = MultipartEncoder(
            fields={
                'version': version.upper(),
                'type': type,
                'file': (os.path.basename(filename), open(filename, 'rb'))
            }
        )
        headers = {
            'Content-Type': m.content_type,
            'Authorization': authorization,
        }

        _, error = self.request(cmd, m.to_string(), headers, sign=False)
        if error == -2:
            self.logout()
            self.login()
            _, error = self.request(cmd, m, headers, sign=False)
        return error

    def yocGetInfo(self, name):
        cmd = '/api/resource/component/getInfo'
        body = {}
        js, _ = self.request(cmd, body)

    def getComponentPage(self, pageIndex, components):
        pageSize = 100
        cmd = '/api/resource/component/getList'
        body = {
            "type": "",
            "name": "",
            "pageIndex": pageIndex,
            "pageSize": pageSize,
        }

        js, _ = self.request(cmd, body)
        # logger.debug(json.dumps(js, indent=4))

        if 'packages' in js:
            for p in js['packages']:
                pack = Component()
                pack.loader_json(p)
                pack.path = os.path.join(self.conf.yoc_path, pack.path)
                components.add(pack)
                # pack.show()

            return len(js['packages']) == pageSize

    def yocComponentList(self, chipId, lastUpdateTime):
        time = self.lastUpdateTime()

        if time > lastUpdateTime:
            idx = 1
            packs = ComponentGroup()
            while self.getComponentPage(idx, packs):
                idx += 1

            return packs, time
        return None, 0

    def lastUpdateTime(self):
        cmd = '/api/resource/component/lastUpdateTime'
        js, code = self.request(cmd, {})
        if code == 0:
            return int(js)
        else:
            return 0

    def request(self, url, body, headers=None, sign=True):
        if sign:
            body = json.dumps(body)
            url = get_url(url, body)

        connection = http.HTTPSConnection(self.conf.occ_host)

        try:
            if not headers:
                headers = {"Content-type": "application/json"}
            connection.request('POST', url, body, headers)
            response = connection.getresponse()
            if response.status == 200:
                text = response.read()
                js = json.loads(text)

                if js['code'] != 0:
                    logger.error(js['msg'])
                return js['result'], js['code']
        except Exception as e:
            logger.error(str(e))

        return {}, -1
