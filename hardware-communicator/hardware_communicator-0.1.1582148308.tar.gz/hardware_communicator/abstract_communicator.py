from background_task_manager.runner import ThreadedBackgroundTaskRunner, AsyncBackgroundTaskRunner


ASYNC=True
class AbstractCommunicator(AsyncBackgroundTaskRunner if ASYNC else ThreadedBackgroundTaskRunner):
    def __init__(self, interpreter,**kwargs):
        super().__init__(**kwargs)
        self._interpreter = None
        self.interpreter=interpreter
        self.send_queue = []

    @property
    def interpreter(self):
        return self._interpreter

    @interpreter.setter
    def interpreter(self, interpreter):
        self._interpreter = interpreter
