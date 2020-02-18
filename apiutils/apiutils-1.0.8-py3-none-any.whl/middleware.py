# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime
import logging
import time

from apiview import utility
from constance import config
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from rest_framework.request import Request


class TimeLogMiddleware(MiddlewareMixin):

    logger = logging.getLogger("timelog")

    def process_request(self, request):
        try:
            start = time.time()
            request.start = start
            if config.SL_CPROFILE_LOG:
                skippath = config.SL_CPROFILE_LOG_SKIP_PATH.split(',')
                if request.path in skippath:
                    return
            else:
                whitepath = config.SL_CPROFILE_LOG_WHITE_PATH.split(',')
                if request.path not in whitepath:
                    return

            import cProfile
            pr = cProfile.Profile()
            pr.enable()
            request.pr = pr
        except Exception:
            self.logger.exception("request")

    def process_response(self, request, response):
        try:
            if isinstance(request, Request):
                request = request._request
            end = time.time()
            exec_time = end - request.start
            if exec_time > config.SL_LONG_TIME_MAIL_MIN_SECONDS:
                skip_path = config.SL_CPROFILE_LOG_SKIP_PATH.split(',')
                if request.path not in skip_path:
                    content = 'time: %fs <br> path:%s <br> querystring:%s <br> request:<pre>%s</pre>' % (
                        exec_time, request.path, request.META['QUERY_STRING'], request
                    )
                    content += '<br><p>IP:%s (%s)</p>' % (settings.SERVER_IP, datetime.datetime.now())
                    subject = u'长时间请求'
                    utility.sendEmail(subject, settings.ADMINS, content)
            if exec_time > config.SL_CPROFILE_LOG_MIN_SECONDS:
                self.logger.info("stat exec_time: time: %fs  path:%s  querystring:%s" % (
                    exec_time, request.path, request.META['QUERY_STRING']
                ))
            if hasattr(request, 'pr'):
                import pstats
                from io import StringIO
                request.pr.disable()
                s = StringIO()
                sort_by = 'cumulative'
                ps = pstats.Stats(request.pr, stream=s).sort_stats(sort_by)
                ps.print_stats()
                if exec_time > config.SL_CPROFILE_LOG_MIN_SECONDS:
                    self.logger.info("%s %s time:%f stat: %s" % (
                        request.path, request.META['QUERY_STRING'], exec_time, s.getvalue()
                    ))
        except Exception:
            self.logger.exception("response")
        return response
