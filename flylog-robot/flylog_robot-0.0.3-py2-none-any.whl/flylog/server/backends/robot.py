# -*- coding: utf-8 -*-
import json
import requests


class DingRobot(object):

    def __init__(self, web_hook_list):
        self.web_hook_list = web_hook_list

    def emit(self, title, content):

        full_content = '\n\n'.join([title, content])
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({"msgtype": "text", "text": {"content": full_content}})

        res_list = []
        for web_hook in self.web_hook_list:
            rsp = requests.post(web_hook, data=data, headers=headers).json()
            res_list.append(rsp['errcode'] == 0)

        return False not in res_list
