#!/usr/bin/env python3
# coding=utf-8
# => Author: Abby Cin
# => Mail: abbytsing@gmail.com
# => Created Time: Sat 31 Mar 2018 12:45:38 PM CST

from .websocket import create_connection
import json
import time
import math
import random
import requests
import sys
import re
import qrcode
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from multiprocessing import Process

schema_list = ["wss://webalfa-cm10.dingtalk.com/long",
	    "wss://webalfa.dingtalk.com/long", "wss://webalfa-cm3.dingtalk.com/long"]
host_list = ["webalfa-cm10.dingtalk.com",
    "webalfa.dingtalk.com", "webalfa-cm3.dingtalk.com"]
ua = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36 OS(windows/6.1) Browser(chrome/74.0.3729.169) DingWeb/3.6.3 LANG/zh_CN"

class Message():   
    def __init__(self, phone, did):
        self.phone = phone
        self.token = None
        self.app_key = "85A09F60A599F5E1867EAB915A8BB07F"
        self.device_id = did
        self.reg = {
            "lwp": "/reg", "headers": {
                "cache-header": "token app-key did ua vhost wv",
                "vhost": "WK",
                "ua": ua,
                "app-key": self.app_key,
                "wv": "im:3,au:3,sy:4",
                "mid": "f61f0002 0",
                "did": self.device_id
            },
            "body": None
        }
        self.keep_alive = {
            "lwp": "/!",
            "headers": {
                "mid": "fb420007 0"
            },
            "body": None
        }
        self.check_license = {
            "lwp": "/r/Adaptor/LoginI/checkLicense",
            "headers": {
                "mid": "9113001a 0"
            },
            "body": [self.phone, 0]
        }
        self.subscribe = {
            "lwp": "/subscribe",
            "headers": {
                "token": "access token of login response",
                "sync": "0,0;0;0;",
                "set-ver": "0",
                "mid": "b91b000d 0"
            }
        }
        self.switch_status = {"lwp": "/r/Sync/getSwitchStatus",
                              "headers": {"mid": "0b75000e 0"}, "body": []}
        self.confirm_info = {"lwp": "/r/Adaptor/IDLDing/getConfirmStatusInfo",
                             "headers": {"mid": "98d9000f 0"}, "body": []}
        self.accept_license = {"lwp": "/r/Adaptor/LoginI/acceptLicense",
                               "headers": {"mid": "caae001f 0"}, "body": [self.phone, 0]}
        self.create_session = {
            "lwp": "/r/Adaptor/LoginI/createTempSessionInfo",
            "headers": {
                "mid": "f6970023 0"
            },
            "body": []
        }

    def get_mid(self):
        curr = int(time.time())
        return hex(curr)[2:] + " 0"

    def get_random(self):
        return str(math.ceil(time.time() * 1e3)) + str(math.ceil(random.random() * 1e3))

    def get_reg_msg(self):
        reg = self.reg
        reg["mid"] = self.get_mid()
        return reg

    def get_keepalive_msg(self):
        res = self.keep_alive
        res["mid"] = self.get_mid()
        return res

    def get_subscribe_msg(self, access_token):
        res = self.subscribe
        res["headers"]["token"] = access_token
        res["headers"]["mid"] = self.get_mid()
        # res['headers']['set-ver'] = "154001657378" # fixed version, get from websocket /subscribe
        return res

    def get_switch_status_msg(self):
        res = self.switch_status
        res["headers"]["mid"] = self.get_mid()
        return res

    def get_confirm_msg(self):
        res = self.confirm_info
        res["headers"]["mid"] = self.get_mid()

    def get_create_session_msg(self):
        res = self.create_session
        res["headers"]["mid"] = self.get_mid()
        return res

def get_header():
    header = {
        "Host": "login.dingtalk.com",
        "Connection": "keep-alive",
        "User-Agent": ua,
        "Accept": "*/*",
        "Referer": "https://im.dingtalk.com/",
        "Accept-Encoding": "gzip, deflate, br"
    }
    return header

def get_qrcode():
    url = "https://login.dingtalk.com/user/qrcode/generate.jsonp"
    r = requests.get(url)
    matches = re.search(r'.*\((.+?)\);$', r.text)
    j = json.loads(matches.group(1))
    guid = j['result']
    return guid

def show_qrcode(guid):
    print('show_qrcode: {}'.format(guid))
    url = 'http://qr.dingtalk.com/action/login?code={}'.format(guid)
    png = 'qrcode.png'
    qrcode.make(url).save(png)
    img = mpimg.imread(png)
    plt.imshow(img)
    plt.show()

def is_logged_in(uuid):
    print('is_logged_in: {}'.format(uuid))
    base = "https://login.dingtalk.com/user/qrcode/is_logged.jsonp"
    params = {
        "qrcode": uuid,
        "pdmToken": "TAB2ADF2E0706AAC01FE45DAE1F90726276B4742885DC5C13D9CE34F3F5", # non necessary
        "pdmTitle": "Windows 7",
        "pdmModel": "Windows 7 Web",
        "appKey": "85A09F60A599F5E1867EAB915A8BB07F",
        "callback": "angular.callbacks._2q" # non necessary
    }

    count = 0
    j = {}
    while True and count < 10:
        count += 1
        r = requests.get(base, params = params, headers = get_header())
        m = re.search(r'.*\(({.+?})\);$', r.text)
        j = json.loads(m.group(1))
        if j['success']:
            break
        time.sleep(1)
    
    if count >= 10:
        print("can't login, exit")
        sys.exit(1)
        
    # set cookie
    params = {
        "code": j['result']['tmpCode'],
        "appkey": j['result']['appKey'],
        "isSession": True,
        "callback": "__jp0"
    }
    h = get_header()
    h['Host'] = 'webalfa-cm10.dingtalk.com'
    h['Connection'] = 'close'
    device_id = ""
    idx = 0
    for i in range(len(host_list)):
        r = requests.get("https://{}/setCookie".format(host_list[i]), params=params, headers=h)
        if r.text.find('200'):
            idx = i
            cookie = r.headers['set-cookie']
            device_id = cookie.split(';')[0].split('=')[1]
            break
            
    return (j, device_id, idx)

def connect(device_id, schema_idx):
    ws = None
    ws = create_connection(schema_list[schema_idx], host=host_list[schema_idx], origin='https://im.dingtalk.com', cookie='{}; deviceid_exist=true'.format(device_id))

    if ws == None or ws.connected == False:
        print("can't connect to these hosts: {h}".format(h=schema_list[schema_idx]))
        sys.exit(1)
    
    return ws

def heartbeat(ws, msg):
    ws.send(msg)
    ws.recv()

def get_cookie():
    guid = get_qrcode()
    handle = Process(target = show_qrcode, args = (guid,))
    handle.start()
    
    r, device_id, schema_idx = is_logged_in(guid)
    res = r['result']

    handle.terminate()

    phone = int(res['userProfileExtensionModel']['userProfileModel']['mobile'])
    msg = Message(phone, device_id)

    ws = connect(msg.device_id, schema_idx)
    ws.send(json.dumps(msg.get_reg_msg()))
    ws.recv()
        
    token = res['accessToken']
    ws.send(json.dumps(msg.get_subscribe_msg(access_token=token)))
    res = json.loads(ws.recv())
    code = res['code']
    echo = json.dumps(msg.get_keepalive_msg())
    count = 0
    while code != 200 and count < 3:
        count += 1
        heartbeat(ws, echo)
        time.sleep(1)
        ws.send(json.dumps(msg.get_subscribe_msg(access_token=token)))
        res = json.loads(ws.recv())
        print(res['body']['reason'])
        code = res['code']

    ws.send(json.dumps(msg.get_switch_status_msg()))
    res = json.loads(ws.recv())

    ws.send(json.dumps(msg.get_confirm_msg()))
    ws.recv()
    ws.recv()  # why response twice ??

    ws.send(json.dumps(msg.get_create_session_msg()))
    res = json.loads(ws.recv())
    if res["code"] == 400:
        print(res["body"]["reason"])

    sid = res["headers"]["sid"]

    # create tmp session
    header = get_header()
    header["Cookie"] = "deciveid={did}; deviceid_exist=true; dd_sid={session_id}".format(did=msg.device_id, session_id=sid)

    tmp = str(math.ceil(time.time() * 1e3))
    payload = {
        "callback": "jQuery19104339311785622433_{t}".format(t=tmp),
        "sessionId": res["body"],
        "_": "{t}".format(t=tmp)
    }
    resp = requests.get("https://login.dingtalk.com/login/createSessionInfoByTemp.jsonp", params=payload, headers=header)
    dt_s = resp.headers.get("Set-Cookie").split(';')[0]

    # build cookie
    cookie_factory = "deviceid={did}; deviceid_exist=true; up_ab=y; preview_ab=y; dd_sid={session_id}; {dts}"
    cookie = cookie_factory.format(did=msg.device_id, session_id=sid, dts=dt_s)
    return cookie


def renew_cookie(cookie_filepath):
    cookie = get_cookie()
    expiration_time = math.ceil(time.time())
    try:
        fd = open(cookie_filepath, 'w')
        data = {"expiration": expiration_time, "cookie": cookie}
        fd.write(json.dumps(data))
        fd.close()
    except Exception as e:
        print("Error: {err}".format(err=e.args))
        sys.exit(1)
    return cookie


def generate_cookie(cookie_filepath):
    week_sec = 60 * 60 * 24 * 6
    tmp = None
    try:
        with open(cookie_filepath, 'r') as fd:
            tmp = fd.read()
            fd.close()
    except Exception:
        return renew_cookie(cookie_filepath)

    data = json.loads(tmp)
    cookie = data["cookie"]
    # check if cookie valid
    now = math.ceil(time.time())
    old = int(data["expiration"])
    if now - old > week_sec:
        cookie = renew_cookie(cookie_filepath)
    return cookie
