from requests_toolbelt import MultipartEncoder
import requests
import re


# class Easyqr():
QRDE_UP = 'https://upload.api.cli.im/upload.php?kid=cliim'
QRDE_URL = 'https://cli.im/apis/up/deqrimg'
QR_URL = 'https://cli.im/api/qrcode/code?text='
HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
}


def upload(path):
    """
    上传二维码图片
    """
    data = MultipartEncoder(
        fields={
            "Filedata": (path, open(path, "rb"), "image/png")
        }
    )
    headers = {
        "referer": "https://cli.im/tools",
        "origin": "https://cli.im",
        "pragma": "no-cache",
        "content-type": data.content_type,

    }
    headers.update(HEADERS)
    info = requests.post(QRDE_UP, headers=headers, data=data)
    content = info.json()
    # print(content)
    if content['status'] != "1":
        print(content)
        exit()
    return content['data']['path']


def online(url):
    """
    解析二维码内容
    """
    data = dict()
    data['img'] = url
    headers = HEADERS
    headers["accept"] = "application/json"
    # print(HEADERS)
    info = requests.post(QRDE_URL, headers=headers, data=data).json()
    # print(info)
    if info["status"] != 1:
        return "图片不是二维码,请重新确认图片!"
    return info['info']['data'][0]


def code(txt):
    """
    文字转二维码
    return : string
    """
    # print(HEADERS)
    html = requests.get(QR_URL+txt, headers=HEADERS)
    if html.status_code != 200:
        print("文字转码访问状态异常:")
        exit()
    try:
        content = re.findall("qrcode_plugins_img =\"(.*?)\"", html.text)[0]
        # print("本次转码地址: http:" + content)
    except:
        print("正则获取地址失败,请联系管理更新正则匹配!")
    with open(txt+".png", "wb") as f:
        f.write(requests.get("http:" + content).content)
    return txt + "\t已完成转换"


# if __name__ == "__main__":
    # print(Qrde_Online())
    # Qrcode("Python,Golang!")
    # online_url = Qrde_upload('02.png')
    # print(Qrde_Online(online_url))
    # Bd_upload('Python,Golang!.png')
