import json

import requests
from utils import auth, table, profile_url


class Profile(object):

    def __init__(self):
        self.auth_list = auth() if auth() else None
        self.profile_url = profile_url

    @staticmethod
    def format_profile(item):
        """
        格式化 profile 接口返回的数据
        """

        data = item["data"]
        items = [["用户名", data["username"]],
                 ["电子邮箱", data["email"]],
                 ["用户组", data["role"]],
                 ["到期时间", data["group_expire"]],
                 ["已使用", data["disk_usage"]],
                 ["总容量", data["disk_limit"]]]
        return table(items=items, title="用户资料")

    def get_profile(self):
        """
        /profile : 获取用户个人资料
        """

        result = list()
        for auth in self.auth_list:
            headers = {"Authorization": auth}
            doc = json.loads(requests.post(self.profile_url,
                                           headers=headers).text)
            if doc["success"]:
                item = self.format_profile(doc)
                result.append(item)
            else:
                print("Authorization: {} 信息异常！".format(auth))
        return result
