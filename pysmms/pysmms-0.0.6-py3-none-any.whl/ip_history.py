import json

import requests
from utils import table, table_err, history_url


class IPHistory(object):

    __doc__ = "基于 IP 的临时上传历史记录"

    def __init__(self):
        self.history_url = history_url

    @staticmethod
    def format_history(item):
        """
        格式化 history 接口返回的数据
        """

        url_list = item["data"]
        if not url_list:
            return "临时上传记录为空！"

        url_list.reverse()
        url_list = url_list[:5]
        items = list()
        for data in url_list:
            items.extend([
                ["文件", data["filename"]],
                ["图片地址", data["url"]],
                ["删除", data["delete"]],
                ["-", "-"]])
        return table(items=items[:-1], title="上传记录")

    def get_history(self):
        """
        /history : 基于 IP 的临时上传历史记录
        """
        doc = json.loads(requests.get(self.history_url).text)
        if doc["success"]:
            return self.format_history(doc)
        return table_err(doc)