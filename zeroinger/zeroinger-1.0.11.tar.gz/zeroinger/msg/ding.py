from logzero import logger
import json
import requests


class DingSender:
    def __init__(self, access_key: str):
        # 钉钉机器人的webhook地址
        self._url = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(access_key)
        logger.info('DingSender|object init done')

    def send_msg_to_robot(self, msg_text: str, is_at_all: bool = False, at_mobile_list: list = None) -> None:
        if at_mobile_list is None:
            at_mobile_list = []
        headers = {"Content-Type": "application/json ;charset=utf-8"}
        data = {
            "msgtype": "text",
            "text": {"content": msg_text},
            "at": {
                "atMobiles": at_mobile_list,
                "isAtAll": 1 if is_at_all else 0  # 如果需要@所有人，这些写1
            }
        }
        data_str = json.dumps(data)
        res = requests.post(self._url, data=data_str, headers=headers)
        logger.info("send_msg_to_robot|消息已发送|{}|{}".format(data_str, res.text))
