'''
@File: dingdinghelper.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-12-27 17:30:23
'''

import os, json, math, time, sys
from urllib import request, parse
from filechunkio import FileChunkIO
from pathlib import Path
import requests

from .ws import get_cookie, Message 

class DingDingHelper:
  """
  DingDing Helper
  """

  def __init__(self):
    self._cookie = None
    self._username = 'Unknown'
    self._password = 'Unknown'
    self._msgurl = 'Unknown'
    self._corpid = 'Unknown'
    self._corpsecret = 'Unknown'
    self._cookiepath = str(Path.home()) + os.sep + ".dingding_cookie"

  @property
  def username(self):
    return self._username
  
  @username.setter
  def username(self, value):
    self._username = value

  @property
  def password(self):
    return self._password

  @password.setter
  def password(self, value):
    self._password = value

  @property
  def msgurl(self):
    return self._msgurl

  @msgurl.setter
  def msgurl(self, value):
    self._msgurl = value

  @property
  def corpid(self):
    return self._corpid

  @corpid.setter
  def corpid(self, value):
    self._corpid = value

  @property
  def corpsecret(self):
    return self._corpsecret

  @property
  def cookiepath(self):
    return self._cookiepath

  @corpsecret.setter
  def corpsecret(self, value):
    self._corpsecret = value
  
  def get_access_token(self):
    self._access_token = ""
    params = parse.urlencode({'corpid': self.corpid, 'corpsecret': self.corpsecret})
    url = 'https://oapi.dingtalk.com/gettoken?%s' % params
    with request.urlopen(url) as f:
      res = json.loads(f.read().decode('utf-8'))
      if res.get("errmsg") == "ok":
        self._access_token = res.get("access_token")
    return self._access_token

  def send_msg(self, msg):
    data = {
      "msgtype": "text",
      "text": { "content": msg },
      "at": { "isAtAll": False }
    }
    data = json.dumps(data).encode(encoding='utf-8')
    req = request.Request(url=self.msgurl, data=data, headers={
      "Content-Type": "application/json", "charset": "utf-8"
    })
    res = request.urlopen(req)
    res = res.read()
    if not (json.loads(res).get('errmsg') == 'ok'):
      self.send_msg(msg)

  def _get_uploadid(self, access_token, size):
    uploadid = ''
    params = parse.urlencode({'access_token': access_token, 'size': size})
    url = 'https://oapi.dingtalk.com/file/upload/create?%s' % params
    with request.urlopen(url) as f:
      res = json.loads(f.read().decode('utf-8'))
      if res.get('code') == '0':
        uploadid = res.get('uploadid')
      else:
        print('Error: get uploadid failed.')
    return uploadid

  def _upload(self, access_token, uploadid, file_path, file_size, chunk_size):
    mediaid = ''
    params = parse.urlencode({'access_token': access_token, 'uploadid': uploadid})
    url = 'https://oapi.dingtalk.com/file/upload?%s' % params
    chunk_cnt = int(math.ceil(file_size * 1.0 / chunk_size))
    for i in range(0, chunk_cnt):
      offset = i * chunk_size
      lens = min(chunk_size, file_size - offset)
      chunk = FileChunkIO(file_path, 'r', offset=offset, bytes=lens)
      ndpartition = "bytes={s}-{e}".format(s = chunk_size * i, e = chunk_size * (i + 1) - 1)
      if i == chunk_cnt - 1:
        ndpartition = "bytes={s}-{e}".format(s = chunk_size * i, e = file_size - 1)
      headers = { "NDPartition": ndpartition }
      files = { 'file': ('blob', chunk, "application/octet-stream") }
      print("uploading {i}/{t}.".format(i = i+1, t = chunk_cnt))
      res = requests.post(url, files=files, headers=headers).json()
      if res.get('code') == '0':
        print("upload {i}/{t} successfully.".format(i = i+1, t = chunk_cnt))
        if i == chunk_cnt - 1:
          mediaid = res.get("filepath", "")
      else:
        print("upload {i}/{t} failed.".format(i = i+1, t = chunk_cnt))
    return mediaid

  def _add_file_to_space(self, access_token, mediaid, space_id, space_path):
    params = parse.urlencode({'access_token': access_token})
    url = "https://im.dingtalk.com/v1/space/file/add?%s" % params
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "im.dingtalk.com",
        "Cookie": self._cookie,
        "Origin": "https://im.dingtalk.com",
        "Referer": "https://im.dingtalk.com/?spm=a3140.8736650.2231772.1.7eb3e3dwxRnir&source=2202&lwfrom=2017120202092064209309201",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
    }
    data = {
      "autoRename": True,
      "fromIm": False,
      "notification": False,
      "path": space_path,
      "spaceId": space_id,
      "tempUrl": mediaid
    }
    res = requests.post(url, json=data, headers=headers)
    if res.json().get("success"):
      print("Add file to space successfully.")
    else:
      print("Add file to space failed.")

  def generate_cookie(self):
    tmp = None
    try:
      with open(self.cookiepath, 'r') as fd:
        tmp = fd.read()
    except Exception:
      self.renew_cookie()
      return

    data = json.loads(tmp)
    self._cookie = data["cookie"]
    # check if cookie valid
    now = math.ceil(time.time())
    old = int(data["expiration"])
    if now - old > int(3600 * 24 * 6.5):
      self.renew_cookie()

  def renew_cookie(self):
    self._cookie = get_cookie()
    expiration_time = math.ceil(time.time())
    try:
      fd = open(self.cookiepath, 'w')
      data = {"expiration": expiration_time, "cookie": self._cookie}
      print(json.dumps(data))
      fd.write(json.dumps(data))
      fd.close()
    except Exception as e:
      print("Error: {err}".format(err = e.args))
      sys.exit(1)

  def upload_file(self, file_path, space_id, space_path):
    """
    API: https://g.alicdn.com/dingding/opendoc/docs/_server/tab10-50.html#%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6
    """
    print("file_path = ", file_path)
    # get access_token
    access_token = self.get_access_token()
    print("access_token = ", access_token)

    # calc size
    size = os.path.getsize(file_path)
    print("size = ", size)

    # get uploadid
    uploadid = self._get_uploadid(access_token, size)
    print("uploadid = ", uploadid)
    if uploadid == '':
      return False

    # upload file chunk
    chunk_size = 1024 * 1024
    mediaid = self._upload(access_token, uploadid, file_path, size, chunk_size)
    print("mediaid = ", mediaid)
    if mediaid == '':
      return False

    # add file to space
    self.generate_cookie()
    self._add_file_to_space(access_token, mediaid, space_id, space_path + "/" + os.path.basename(file_path))

    return True
