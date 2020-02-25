import os
import json
from random import choice

import requests
import pyperclip
from utils import auth, table, table_err, upload_url


class Upload(object):

    __doc__ = "上传图片"

    def __init__(self):
        self.auth = choice(auth()) if auth() else None
        self.upload_url = upload_url

    def format_upload(self, item):
        """
        格式化 upload 接口返回的数据
        """

        remark = "此次上传无 Authorization，不保证图片时效！"
        if self.auth:
            remark = "Authorization：" + self.auth
        data = item["data"]
        img_url = data["url"]
        items = [
            ["文件", data["filename"]],
            ["图片地址", img_url],
            ["删除", data["delete"]],
            ["备注", remark]
        ]
        pyperclip.copy(img_url)
        return table(items=items, title="上传成功")

    def upload(self, img_path):
        """
        /upload : 上传图片
        """

        files = {"smfile": (os.path.basename(img_path), open(img_path, "rb"))}
        if self.auth:
            headers = {"Authorization": self.auth}
            html = requests.post(self.upload_url,
                                 headers=headers, files=files)
        else:
            html = requests.post(self.upload_url, files=files)
        doc = json.loads(html.text)
        if doc["success"]:
            return self.format_upload(doc)
        return table_err(doc)
