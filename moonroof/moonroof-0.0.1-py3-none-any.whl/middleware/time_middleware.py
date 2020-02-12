from datetime import datetime


class TimeMiddleware(object):

    def before(self, request):
        self.start = datetime.now()

    def key(self):
        return 'time'

    def value(self, request, response):
        end = datetime.now()
        return (end - self.start).total_seconds()

