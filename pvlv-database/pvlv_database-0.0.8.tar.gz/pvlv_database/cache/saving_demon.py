from time import sleep
from threading import Timer
from pvlv_database.configurations.configuration import logger


class SavingDemon(object):

    def __init__(self):
        self.thread = None

    def start_loop(self, action, interval):

        def func():
            while True:
                action()
                sleep(interval)

        try:
            self.thread = Timer(interval=interval, function=func)
            self.thread.start()

        except Exception as e:
            logger.error(e)
