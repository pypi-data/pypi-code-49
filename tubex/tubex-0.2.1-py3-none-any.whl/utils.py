"""
Code from Effective python, Brett Slatkin
"""
from threading import Thread
from queue import Queue


class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                yield item
            finally:
                self.task_done()


class ThreadWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_channel = in_queue
        self.out_channel = out_queue

    def run(self):
        for item in self.in_channel:
            res = self.func(item)
            self.out_channel.put(res)


def start_threads(count, *args):
    threads = [ThreadWorker(*args) for _ in range(count)]
    for thread in threads:
        thread.start()
    return threads


def stop_threads(closable_queue, threads):
    for _ in threads:
        closable_queue.close()

    closable_queue.join()

    for thread in threads:
        thread.join()
