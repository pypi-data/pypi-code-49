from queue import Queue
from .general_middleware import GeneralMiddleware
from .sql_middleware import SQLMiddleware
from .time_middleware import TimeMiddleware
from ..track import track
from ..thread import MoonroofThread

MAX_QUEUE_SIZE=10000
MAX_BATCH_SIZE=100

class MoonroofMiddleware(object):

    def __init__(self, get_response):
        self.queue = Queue(MAX_QUEUE_SIZE)
        self.thread = MoonroofThread(queue=self.queue, max_batch_size=MAX_BATCH_SIZE)
        self.middlewares = [TimeMiddleware(), GeneralMiddleware(), SQLMiddleware()]
        self.get_response = get_response
        self.thread.start()

    def __call__(self, request):
        [middleware.before(request) for middleware in self.middlewares]
        response = self.get_response(request)
        data = {middleware.key(): middleware.value(request, response) for middleware in self.middlewares}
        data['version'] = '0.1'
        track(self.queue, request.get_full_path(), data)
        return response
