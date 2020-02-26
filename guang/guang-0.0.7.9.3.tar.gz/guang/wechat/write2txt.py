import itchat
from itchat.content import TEXT
from .Utils import get_userName, _txt
from multiprocessing import Process
from multiprocessing import Pool
import threading
from concurrent.futures import ThreadPoolExecutor
"""
python 由于GIL的缘故，仅使用线程的话，即使在多核cpu的主机上运行也只会使用单个核，
解决这个问题的一个简单方法是在多进程的基础下使用多线程， 多个Python进程有各自独立的GIL锁，互不影响这样依旧能利用多核cpu。 
况且还有协程这个方案可以。
"""
def write(name_list):
    """name_list such as ['filehelper', 'caloi']"""

    lock = threading.Lock()
    def run(nickName):
        print(nickName, ":start")

        @itchat.msg_register([TEXT])
        def write2file(msg):
            userName = get_userName(nickName)[nickName]
            if msg.user.userName == userName:
                _txt(msg)

        lock.acquire()
        itchat.auto_login(hotReload=True, enableCmdQR=2)
        itchat.run()
        lock.release()

    try:
        # --------------thread----------------
        #     t = [threading.Thread(target=run, args=(name,)) for name in name_list]
        #     [i.start() for i in t]
        #     [i.join() for i in t]

        # ------------ 线程池不加锁会导致多次写入信息, 加上线程锁便正常了 --------------------
        with ThreadPoolExecutor(max_workers=len(name_list)) as executor:
            for name in name_list:
                dict1 = {'nickName': name}
                executor.submit(run, **dict1)

    #     ------------process pool------------
    #     with Pool(len(name_list)) as pool:
    #         pool.map(run, name_list)
    except:
        print("try is not successful !")

if __name__ == "__main__":
    name_list = ["filehelper", "caloi"]
    write(name_list)
