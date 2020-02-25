import itchat
from guang.wechat.Utils import download_file, dynamic_specified_msg, get_userName,d_time
import argparse

def downloads(nickName='caloi', fileType='mp3', d_t=60):
    """ downloads wechat files with any file type
    Args:
        d_t: Program run duration. unit: s
    """
    itchat.auto_login(hotReload=True, enableCmdQR=2)

    while d_time(d_t):
        
        msg = dynamic_specified_msg(get_userName(nickName)[nickName])
        msg, tpath = download_file(msg, fileType=fileType)
        print(tpath)
        
if __name__=="__main__":
    downloads()
