import json
import logging
from json import JSONDecodeError

from django.utils.deprecation import MiddlewareMixin

from isc_common import getAttr
from isc_common.auth.models.user import User
from isc_common.models.history import History
from project import settings

logger = logging.getLogger(__name__)


class LoggingRequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            bodyStr = request.body.decode("utf-8")
            self.json = json.loads(bodyStr)

        except JSONDecodeError:
            self.json = None

        if settings.EXCLUDE_REQUEST_PATHES == None:
            settings.EXCLUDE_REQUEST_PATHES = ['Info', 'Params', 'Get']

        user_id = getAttr(request.session._session, 'user_id')
        if user_id != None:
            user = User.objects.get(id=user_id)
            enable_logging = len([item for item in settings.EXCLUDE_REQUEST_PATHES if request.path.find(item) != -1]) == 0
            if enable_logging and self.json != None:
                history_element = History.objects.create(user=user, method=request.method, path=request.path, data=self.json)

                logger.debug('=========================================================================================================')
                logger.debug(f'date: {history_element.date}')
                logger.debug(f'user: {user}')
                logger.debug(f'method: {request.method}')
                logger.debug(f'path: {request.path}')
                logger.debug(f'json: {self.json}')
                logger.debug('=========================================================================================================\n')

    def process_response(self, request, response):
        return response
