import guang
from guang.wechat.Utils import * 
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--name', help='nike name', type=str, default='桂花香')
    args = parser.parse_args()
    nickName = args.name

    itchat.auto_login(hotReload=True, enableCmdQR=2)
    # print(get_all_info())
    while d_time(60):
        
        msg = dynamic_specified_msg(get_userName(nickName)[nickName])
        # msg = download_file(msg)
        msg = get_txt(msg)
        