import json

from ..base import get_expiry, validate_template, validate_arn_endpoint
from ..common import Waterfall,ClientPlatform
from ..proto import notification_hub_pb2 as pb


class Push:
    _default_expiry_offset = 7  # 7 Days

    def __init__(
            self,
            token: str,
            template: str,
            context: dict = None,
            user_id: str = None,
            waterfall_config: Waterfall = None,
            expiry: int = None,
            extra_payload: dict = None,
            client_platform: ClientPlatform = ClientPlatform.ANDROID,
            dry_run: bool = False
    ):
        """
        Parameters:
            token (str): List of ARN endpoints to whom the push message will be sent
            template (str): The template URL which will get rendered with the variable data provided
            context (dict, optional): A dictionary of variable data to be rendered in the template
            user_id (str, optional): The ID of the user to whom the notification is being sent
            waterfall_config (Waterfall, optional): The configuration to be used by Hub priority engine to schedule
                this channel
            expiry (int, optional): The Epoch timestamp at which this notification task should expire if still not sent
            extra_payload(dict,optional): extra_payload for sending client level configuration and extra data in
               notification
            client_platform(ClientPlatform, optional): identifying client for fcm to build respective request
            dry_run(bool, optional): to enable dry run i.e won't send notification just validate client token
        """
        self._push = pb.Push()
        validate_arn_endpoint(token)
        self._push.token = token
        validate_template(template)
        self._push.template = template
        self._push.extraPayload = json.dumps(extra_payload) if extra_payload else "{}"
        self._push.context = json.dumps(context) if context else '{}'
        self._push.userID = user_id if user_id else ''
        self._push.expiry = expiry if expiry else get_expiry(self._default_expiry_offset)
        self.__set_waterfall(waterfall_config)
        self._push.clientPlatform = client_platform
        self._push.dryRun = dry_run

    def __set_waterfall(self, value: Waterfall = None):
        if not value:
            value = Waterfall()
        self._push.waterfallConfig.CopyFrom(value.proto)

    @property
    def proto(self) -> pb.Push:
        return self._push
