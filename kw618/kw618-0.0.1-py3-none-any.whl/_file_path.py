"""
author : kerwin
function : personal settings
note : 用于修改所有文件的默认配置信息

警示： 以后再配置默认路径的时候，不要带上尾巴上的‘/’.  实际应用中看着不舒服。。。
        ("D:/自如/" 由于历史原因，不想改了。。。) //k200207:已经修改回来了
"""


"""
mac 和 linux 的路径除了开头的/Users 替换成 /root 外，其他是一样的。
"""



# 自动判断该系统是 ’windows' 还是 ‘mac’
import platform
import sys, os
    # win
if platform.system() == "Windows":
    PYTHON = "python"
    HOST = "127.0.0.1"
    FILE_PATH_FOR_DESKTOP = "C:/Users/Administrator/Desktop"
    FILE_PATH_FOR_MYCODE = "D:/kerwin/MyCode"
    FILE_PATH_FOR_ZIRU_CODE = "D:/kerwin/MyCode/Business/Ziru"
    FILE_PATH_FOR_ZIRU = "D:/自如"

    # mac
elif platform.system() == "Darwin":
    PYTHON = "python3"
    HOST = "127.0.0.1" # 本地ip  (mac上的代码默认用本地ip，若个别脚本有特别需要，可以设置成REMOTE_HOST)
    # HOST = "121.40.240.153" # 阿里云的ip
    REMOTE_HOST = "121.40.240.153" # 阿里云的ip
    FILE_PATH_FOR_DESKTOP = "/Users/kerwin/Desktop"
    FILE_PATH_FOR_MYCODE = "/Users/kerwin/MyBox/MyCode"
    FILE_PATH_FOR_ZIRU_CODE = "/Users/kerwin/MyBox/MyCode/Business/Ziru"
    FILE_PATH_FOR_ZIRU = "/Users/kerwin/MyBox/工作相关/自如"

    # linux
elif platform.system() == "Linux":
    PYTHON = "python3"
    HOST = "127.0.0.1"
    FILE_PATH_FOR_DESKTOP = "/root/kerwin/Desktop"
    FILE_PATH_FOR_MYCODE = "/root/kerwin/MyBox/MyCode"
    FILE_PATH_FOR_ZIRU_CODE = "/root/kerwin/MyBox/MyCode/Business/Ziru"
    FILE_PATH_FOR_ZIRU = "/root/kerwin/MyBox/工作相关/自如"

# 检查是否存在上述文件路径; (没有则抛出异常)
error_path = []
for path in [FILE_PATH_FOR_DESKTOP, FILE_PATH_FOR_MYCODE, FILE_PATH_FOR_ZIRU_CODE, FILE_PATH_FOR_ZIRU]:
    if not os.path.exists(path):
        error_path.append(path)
if error_path:
    raise Exception(
        "[kk异常]:\n不存在以下文件路径, 建议创建后重试:\n" + "\n".join(error_path)
    )




# 自动搜索kw618库包的位置
site_pkgs_path = [path for path in sys.path if "site-packages" in path]
FILE_PATH_FOR_KW618 = None
for path in site_pkgs_path:
    if os.path.exists(f"{path}/kw618"):
        FILE_PATH_FOR_KW618 = f"{path}/kw618"
        break
FILE_PATH_FOR_KW618 = '/Users/kerwin/MyBox/MyKernel/kw618' # <toggle>
if FILE_PATH_FOR_KW618 is None:
    raise Exception("\n\n[kk异常]:  在本地 site-packages 路径中找不到kw618库, 尝试使用 pip3 install kw618\n\n")




if __name__ == "__main__":
    print("start!")
    print(FILE_PATH_FOR_DESKTOP)
    print("end!")
