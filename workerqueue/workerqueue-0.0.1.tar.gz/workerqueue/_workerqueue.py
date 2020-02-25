import time
from enum import Enum
from queue import Queue
from threading import Thread


class WorkerQueue(Queue):
    class Signal(Enum):
        STOP = "WorkerQueueSignalSTOP"

    def __init__(self, func, thread_count=1, parse_tuple=True):
        Queue.__init__(self)

        self.func = func
        self.parse_tuple = parse_tuple
        self.threads = []
        for i in range(thread_count):
            t = Thread(target=self._worker_loop)
            t.start()
            self.threads.append(t)

    def _worker_loop(self):
        while True:
            item = self.get()
            if item != WorkerQueue.Signal.STOP:
                if self.parse_tuple:
                    self.func(*item)
                else:
                    self.func(item)
                self.task_done()
            else:
                break

    def stop(self):
        for i in range(len(self.threads)):
            # Send Signal.STOP to all threads
            self.put(WorkerQueue.Signal.STOP)

        # wait for threads to shut off
        time.sleep(1)

        for t in self.threads:
            t.join()
