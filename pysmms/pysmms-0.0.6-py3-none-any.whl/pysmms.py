import os
import sys

from upload import Upload
from profile import Profile
from ip_history import IPHistory
from history import History
from help import help


def app():
    """
    此脚本基于 SM.MS 图床，使用 v2 版本接口，
    相关 API 文档见：https://doc.sm.ms/。
    """

    if len(sys.argv) < 2:
        sys.exit("缺少参数！使用 'pysmms help' 命令查看所有参数。")

    if os.path.exists(sys.argv[1]):
        allowed_file_extensions = ['.jpeg','.jpg','.png','.gif','.bmp']
        if os.path.splitext(sys.argv[1])[1] not in allowed_file_extensions:
            sys.exit("文件类型不支持！")
        up = Upload()
        result = up.upload(sys.argv[1])
        sys.exit(result)
    elif sys.argv[1] == "profile":
        profile = Profile()
        result = profile.get_profile()
        for r in result:
            print(r)
        sys.exit()
    elif sys.argv[1] == "history":
        history = History()
        result = history.get_upload_history()
        sys.exit(result)
    elif sys.argv[1] == "ip_history":
        ip_history = IPHistory()
        result = ip_history.get_history()
        sys.exit(result)
    else:
        result = help()
        sys.exit(result)


if __name__ == '__main__':
    app()
