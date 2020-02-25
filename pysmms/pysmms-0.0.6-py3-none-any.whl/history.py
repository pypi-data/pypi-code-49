import time
import json
from random import choice

import requests
from utils import auth, table, table_err, upload_history_url


class History(object):

    __doc__ = "获取用户上传记录"

    def __init__(self):
        self.auth = choice(auth()) if auth() else None
        self.upload_history_url = upload_history_url

    @staticmethod
    def format_upload_history(item):
        """
        格式化 upload_history 接口返回的数据
        """

        url_list = item["data"]
        if not url_list:
            return "历史上传记录为空！"

        url_list.reverse()
        url_list = url_list[:5]
        items = list()
        for data in url_list:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S",
                                      time.localtime(data["created_at"]))
            items.extend([
                ["文件", data["filename"]],
                ["创建时间", timestamp],
                ["图片地址", data["url"]],
                ["删除", data["delete"]],
                ["-", "-"]])
        return table(items=items[:-1], title="历史上传记录")

    def get_upload_history(self):
        """
        /upload_history : 获取用户上传记录
        """

        headers = {"Authorization": self.auth}
        doc = json.loads(requests.get(self.upload_history_url,
                                      headers=headers).text)
        if doc["success"]:
            return self.format_upload_history(doc)
        return table_err(doc)