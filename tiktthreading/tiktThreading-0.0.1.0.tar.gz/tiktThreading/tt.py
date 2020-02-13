import threading
import time

class TT:
    def __init__(self,num=5):
        self.semaphore = threading.BoundedSemaphore(num)
    def load(self,func,args):
        self.t = threading.Thread(target=func, args=(args,self.semaphore))

        pass #
    def start(self):
        try:
            self.t.start()
        except :
            pass
        pass #

    def func(self,arg,se):
        se.acquire()
        time.sleep(1)
        print('thread '+str(arg)+" running....")
        se.release()


def show(arg,se):
    se.acquire()
    time.sleep(1)
    print('thread '+str(arg)+" running....")
    se.release()

if __name__ == '__main__':
    # 设置允许5个线程同时运行
    tt=TT()
    for i in range(10000):
        tt.load(show,i)
        
        tt.start()


# #自定义类
# import threading

# class TThreading(threading.Thread):

#     def __init__(self, func, arg):
#         super(TThreading,self).__init__()
#         self.func = func
#         self.arg = arg

#     def run(self):
#         self.func(self.arg)

# def my_func(args):
#     """
#     你可以把任何你想让线程做的事定义在这里
   
#     """
#     time.sleep(1)
#     print('thread '+str(args)+" running....")
#     pass

# obj = TThreading(my_func, 123)
# obj.start()