import json
import logging

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from history import utils
from history.models.history import History

logger = logging.getLogger(__name__)


class LoggingRequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            bodyStr = request.body.decode("utf-8")
            self.json = json.loads(bodyStr)

        except:
            self.json = None

        if settings.INCLUDE_REQUEST_PATHES == None:
            settings.INCLUDE_REQUEST_PATHES = ['Add', 'Update', 'Remove']

        username = request.session._session.get('username')
        fio = request.session._session.get('fio', 'unknown')
        if username != None:
            path = request.path.split('/')
            path = path[len(path) - 1]
            enable_logging = path in settings.INCLUDE_REQUEST_PATHES
            if enable_logging and self.json != None:
                ip_address = utils.get_ip(request)
                user_agent = request.META.get('HTTP_USER_AGENT')

                logger.debug(f'request.path : {request.path}')
                history_element = History.objects.using('history').create(
                    username=username,
                    fio=fio,
                    method=request.method,
                    ip_address=ip_address,
                    user_agent=user_agent,
                    path=request.path,
                    data=self.json
                )

                logger.debug('=========================================================================================================')
                logger.debug(f'date: {history_element.date}')
                logger.debug(f'username: {username}')
                logger.debug(f'method: {request.method}')
                logger.debug(f'path: {request.path}')
                logger.debug(f'ip_address: {ip_address}')
                logger.debug(f'user_agent: {user_agent}')
                logger.debug(f'json: {json.dumps(self.json, indent=4, sort_keys=True)}')
                logger.debug('=========================================================================================================\n')

    def process_response(self, request, response):
        return response
