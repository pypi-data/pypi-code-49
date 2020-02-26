import json

from ..base import validate_template, get_expiry, validate_mobile
from ..common import Waterfall
from ..proto import notification_hub_pb2 as pb


class Whatsapp:
    _default_expiry_offset = 7  # 7 Days

    def __init__(
            self,
            send_to: str,
            template: str,
            context: dict = None,
            user_id: str = None,
            waterfall_config: Waterfall = None,
            expiry: int = None
    ):
        """
        Parameters:
            send_to (str): The mobile number to which WhatsApp needs to be sent
            template (str): The template URL which will get rendered with the variable data provided
            context (dict, optional): A dictionary of variable data to be rendered in the template
            user_id (str, optional): The ID of the user to whom the notification is being sent
            waterfall_config (Waterfall, optional): The configuration to be used by Hub priority engine to schedule
                this channel
            expiry (int, optional): The Epoch timestamp at which this notification task should expire if still not sent
        """
        self._whatsapp = pb.Whatsapp()

        validate_mobile(send_to)
        self._whatsapp.mobile = send_to

        validate_template(template)
        self._whatsapp.template = template

        self._whatsapp.userID = user_id if user_id else ''

        self._whatsapp.context = json.dumps(context) if context else '{}'

        self._whatsapp.expiry = expiry if expiry else get_expiry(self._default_expiry_offset)

        self.__set_waterfall(waterfall_config)

    def __set_waterfall(self, value: Waterfall = None):
        if not value:
            value = Waterfall()
        self._whatsapp.waterfallConfig.CopyFrom(value.proto)

    @property
    def proto(self) -> pb.Whatsapp:
        return self._whatsapp
