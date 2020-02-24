import os
import re
import sys
import json
import time
import random
import configparser

import requests
import pyperclip
from terminaltables import SingleTable


class SMMS(object):

    __doc__ = "此脚本基于 SM.MS 图床，使用 v2 版本接口，" \
              "相关 API 文档见：https://doc.sm.ms/"

    def __init__(self):
        self.base_url = "https://sm.ms/api/v2/"
        self.profile_url = self.base_url + "profile"
        self.history_url = self.base_url + "history"
        self.upload_history_url = self.base_url + "upload_history"
        self.upload_url = self.base_url + "upload"
        self.auth = None

    def format_error(self, item):
        """
        处理异常消息
        """

        if item["code"] == "image_repeated":
            url = re.findall("Image upload repeated limit, this image exists at: (.*)",
                             item["message"])[0]
            items = [
                ["Code", item["code"]],
                ["Message", "此图已存在"],
                ["URL", url],
                ["Request Id", item["RequestId"]]
            ]
        else:
            items = [
                ["Code", item["code"]],
                ["Message", item["message"]],
                ["Request Id", item["RequestId"]]
            ]
        table_instance = SingleTable(items, "SM.MS - 异常")
        table_instance.inner_row_border = True
        return table_instance.table

    @staticmethod
    def format_profile(item):
        """
        格式化 profile 接口返回的数据
        """

        data = item["data"]
        items = [
            ["用户名", data["username"]],
            ["电子邮箱", data["email"]],
            ["用户组", data["role"]],
            ["到期时间", data["group_expire"]],
            ["已使用", data["disk_usage"]],
            ["总容量", data["disk_limit"]]
        ]
        table_instance = SingleTable(items, "SM.MS - 用户资料")
        table_instance.inner_row_border = True
        return table_instance.table

    def get_profile(self):
        """
        /profile : 获取用户个人资料
        """

        headers = {"Authorization": self.auth}
        doc = json.loads(requests.post(self.profile_url,
                                       headers=headers).text)
        if doc["success"]:
            return self.format_profile(doc)
        return self.format_error(doc)

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
        table_instance = SingleTable(items[:-1], "SM.MS - 上传记录")
        table_instance.inner_row_border = True
        return table_instance.table

    def get_history(self):
        """
        /history : 基于 IP 的临时上传历史记录
        """
        doc = json.loads(requests.get(self.history_url).text)
        if doc["success"]:
            return self.format_history(doc)
        return self.format_error(doc)

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
        table_instance = SingleTable(items[:-1], "SM.MS - 历史上传记录")
        table_instance.inner_row_border = True
        return table_instance.table

    def get_upload_history(self):
        """
        /upload_history : 获取用户上传记录
        """

        headers = {"Authorization": self.auth}
        doc = json.loads(requests.get(self.upload_history_url,
                                      headers=headers).text)
        if doc["success"]:
            return self.format_upload_history(doc)
        return self.format_error(doc)

    def format_upload(self, item, flag):
        """
        格式化 upload 接口返回的数据
        """

        remark = "此次上传无 Authorization，不保证图片时效！"
        if flag:
            remark = "此次上传携带 Authorization：" + self.auth
        data = item["data"]
        img_url = data["url"]
        items = [
            ["文件", data["filename"]],
            ["图片地址", img_url],
            ["删除", data["delete"]],
            ["备注", remark]
        ]
        table_instance = SingleTable(items, "SM.MS - 上传成功")
        table_instance.inner_row_border = True
        pyperclip.copy(img_url)
        return table_instance.table

    def upload(self, img_path):
        """
        /upload : 上传图片
        """

        files = {"smfile": (os.path.basename(img_path),
                            open(img_path, "rb"))}
        if self.auth:
            flag = True
            headers = {"Authorization": self.auth}
            html = requests.post(self.upload_url,
                                 headers=headers, files=files)
        else:
            flag = False
            html = requests.post(self.upload_url, files=files)
        doc = json.loads(html.text)
        if doc["success"]:
            return self.format_upload(doc, flag)
        return self.format_error(doc)

    def help(self):
        """
        显示帮助信息
        """

        return ("pysmms {arg}\n\n"
                "   profile          查看用户资料（需要配置 Authorization）\n"
                "   ip_history       基于 IP 的临时上传历史记录\n"
                "   history          获取用户上传记录（需要配置 Authorization）\n"
                "   /path/to/picture 上传图片（需要配置 Authorization）\n\n"
                "上传图片不需要配置 Authorization，但不保证图片的使用时效。\n"
                "配置 Authorization 需要在用户根目录创建 .pysmms 文件，文件写入以下内容：\n\n"
                "    [sm.ms]\n"
                "    auth=['wKSlYH******z8eb8qSr']\n\n"
                "注意：auth 以列表存放，支持多个 auth 随机上传。")

    def main(self):
        if len(sys.argv) < 2:
            sys.exit("缺少参数！使用 'pysmms help' 命令查看所有参数。")

        pysmms = configparser.ConfigParser()
        _pysmms = pysmms.read(os.path.expanduser('~') + '/.pysmms')
        if _pysmms:
            try:
                self.auth = random.choice(eval(pysmms["sm.ms"]["auth"]))
                if os.path.exists(sys.argv[1]):
                    result = self.upload(sys.argv[1])
                    sys.exit(result)
                args = {
                    "profile": self.get_profile,
                    "ip_history": self.get_history,
                    "history": self.get_upload_history,
                    "help": self.help
                }
                result = args.get(sys.argv[1], self.help)()
                sys.exit(result)
            except KeyError:
                result = self.help()
                sys.exit(result)
        else:
            if os.path.exists(sys.argv[1]):
                result = self.upload(sys.argv[1])
                sys.exit(result)
            elif sys.argv[1] == "ip_history":
                result = self.get_history()
                sys.exit(result)
            else:
                result = self.help()
                sys.exit(result)


def app():
    pysmms = SMMS()
    pysmms.main()


if __name__ == '__main__':
    app()
