from datetime import datetime
import threading

from django.http import Http404
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin
import os


class HoLoggingMiddleware(MiddlewareMixin):

    thread_local = threading.local()

    def process_request(self, request):

        self.thread_local.pid = os.getpid()
        self.thread_local.query = self.thread_local.end_at = self.thread_local.response = None
        self.thread_local.request = request
        self.thread_local.current_user = request.user
        self.thread_local.body = request.body
        self.thread_local.start_at = datetime.now().isoformat()

        try:
            self.thread_local.application = resolve(request.path).func.__module__.split('.')[0]
        except Http404:
            self.thread_local.application = ''

    def process_exception(self, request, exception):
        self.process_request(request)

    def process_response(self, request, response):

        self.thread_local.end_at = datetime.now().isoformat()
        self.thread_local.response = response
        return response
