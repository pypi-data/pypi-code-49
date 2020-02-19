from datetime import datetime

from isc_common.auth.models.user import User
from isc_common.http.DSRequest import DSRequest
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.ws import WS_CANNEL, WS_PORT, WS_HOST
from tracker.models.messages_state import Messages_state


class LoginRequest(DSRequest):
    def __init__(self, request):
        DSRequest.__init__(self, request)
        data = self.get_data()
        login = data.get('login', None)
        errorMessage = "Аутентификация не прошла :-("

        try:
            user = User.objects.get(username=login)
            if user.check_password(data.get('password', None)):
                ws_channel = f'{WS_CANNEL}_{login}'

                self.response = dict(
                    status=RPCResponseConstant.statusSuccess,
                    login=login,
                    userId=user.id,
                    captionUser=login,
                    codeGroup="",
                    isAdmin=user.is_admin,
                    isDevelop=user.is_develop,
                    message_state_new_id=Messages_state.objects.get(code="new").id,
                    message_state_new_name=Messages_state.objects.get(code="new").name,
                    ws_channel=ws_channel,
                    ws_host=WS_HOST,
                    ws_port=WS_PORT
                )
                request.session['ws_channel'] = ws_channel
                request.session['ws_port'] = WS_PORT
                request.session['host'] = request.headers.get('Host').split(':')[0]
                request.session['user_id'] = user.id
                user.last_login = datetime.now()
                user.save()
            else:
                self.response = dict(status=RPCResponseConstant.statusLoginIncorrect, errorMessage=errorMessage)

        except User.DoesNotExist:
            self.response = dict(status=RPCResponseConstant.statusLoginIncorrect, errorMessage=errorMessage)
