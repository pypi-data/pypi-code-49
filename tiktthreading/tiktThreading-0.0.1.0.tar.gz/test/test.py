#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
import tiktThreading
import time



def show(arg,se):
    se.acquire()
    time.sleep(1)
    print('thread '+str(arg)+" running....")
    se.release()




if __name__ == '__main__':
    # 设置允许5个线程同时运行
    tt=tiktThreading.TT(2)
    for i in range(10000):
        tt.load(show,i)
        tt.start()