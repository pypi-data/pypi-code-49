import itchat
from guang.wechat.Utils import download_file, dynamic_specified_msg, get_userName,d_time
import argparse

def downloads(nickName='caloi', fileType='mp3', d_t=60):
    """ downloads wechat files with any file type
    Args:
        d_t: Program run duration. unit: s
    """
    itchat.auto_login(hotReload=True)

    while d_time(d_t):
        
        msg = dynamic_specified_msg(get_userName(nickName)[nickName])
        msg = download_file(msg, fileType=fileType)
        
if __name__=="__main__":
    downloads()
