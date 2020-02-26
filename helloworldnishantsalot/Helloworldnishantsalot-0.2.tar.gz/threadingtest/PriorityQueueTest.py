from queue import Queue
from threading import Thread, Lock
import time

exitflag = 0
class myThread(Thread):

    def __init__(self, threadID,  name, queue):
        Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.threadID = threadID

    def run(self):
        print("starting" + self.name)
        process_data(self.name, self.queue)
        print("end "+ self.name)

def process_data(threadname, queue):
    while not exitflag:
        queuelock.acquire()
        if not workqueue.empty():
            data = queue.get()
            queuelock.release()
            print('processing %s  %s' % (threadname, data))
        else:
            queuelock.release()
            time.sleep(1)



threadlist = ['t1', 't2', 't3']
namelist = ['one', 'two' ,'three', 'two' ,'three', 'two' ,'three', 'two' ,'three']
queuelock = Lock()
workqueue = Queue(10)
threads = []
threadID = 1

for tName in threadlist:
    thread = myThread(threadID, tName, workqueue)
    thread.start()
    threads.append(thread)
    threadID += 1

queuelock.acquire()
for word in namelist:
    workqueue.put(word)
queuelock.release()

while not workqueue.empty():
    pass

exitflag = 1

for t in threads:
    t.join()
print("Exiting main thread")