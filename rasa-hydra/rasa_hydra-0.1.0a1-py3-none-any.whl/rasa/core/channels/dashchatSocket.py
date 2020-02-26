import logging
from typing import Optional, Text, Any, List, Dict, Iterable
import uuid

import opentracing
from sanic import Blueprint, response
from socketio import AsyncServer

from metrics.constants import CURRENT_USER, CHAT_LATENCY
from rasa.core.channels import InputChannel
from rasa.core.channels.channel import UserMessage, OutputChannel

logger = logging.getLogger(__name__)
HYDRA_CHANNEL = "OMNI_DASHCHAT_00001"


class SocketBlueprint(Blueprint):
    def __init__(self, sio: AsyncServer, socketio_path, *args, **kwargs):
        self.sio = sio
        self.socketio_path = socketio_path
        super(SocketBlueprint, self).__init__(*args, **kwargs)

    def register(self, app, options):
        self.sio.attach(app, self.socketio_path)
        super(SocketBlueprint, self).register(app, options)


class DashChatOutput(OutputChannel):
    @classmethod
    def name(cls):
        return "dashchat"

    def __init__(self, sio, sid, namespace, bot_message_evt):
        self.sio = sio
        self.sid = sid
        self.namespace = namespace
        self.bot_message_evt = bot_message_evt

    async def _send_message(self, socket_id, response):
        # type: (Text, Any) -> None
        """Sends a message to the recipient using the bot event."""

        logger.info(f"[{socket_id}] - Bot response: {response}")
        await self.sio.emit(self.bot_message_evt, response, room=socket_id, namespace=self.namespace)

    async def send_text_message(
            self, recipient_id: Text, text: Text, **kwargs: Any
    ) -> None:
        """Send a message through this channel."""

        await self._send_message(self.sid, {"text": text})

    async def send_image_url(
            self, recipient_id: Text, image: Text, **kwargs: Any
    ) -> None:
        """Sends an image to the output"""

        message = {"attachment": {"type": "image", "payload": {"src": image}}}
        await self._send_message(self.sid, message)

    async def send_text_with_buttons(
            self,
            recipient_id: Text,
            text: Text,
            buttons: List[Dict[Text, Any]],
            **kwargs: Any
    ) -> None:
        """Sends buttons to the output."""

        message = {"text": text, "quick_replies": []}

        for button in buttons:
            message["quick_replies"].append(
                {
                    "content_type": "text",
                    "title": button["title"],
                    "payload": button["payload"],
                }
            )

        await self._send_message(self.sid, message)

    async def send_elements(
            self, recipient_id: Text, elements: Iterable[Dict[Text, Any]], **kwargs: Any
    ) -> None:
        """Sends elements to the output."""

        message = {
            "attachment": {
                "type": "template",
                "payload": {"template_type": "generic", "elements": elements[0]},
            }
        }

        await self._send_message(self.sid, message)

    async def send_custom_json(
            self, recipient_id: Text, json_message: Dict[Text, Any], **kwargs: Any
    ) -> None:
        """Sends custom json to the output"""

        logger.info(f"[{self.sid}] - Bot response: {json_message}")
        await self.sio.emit(self.bot_message_evt, json_message, room=self.sid, namespace=self.namespace)


class DashChatInput(InputChannel):
    """A socket.io input channel."""

    @classmethod
    def name(cls):
        return "dashchat"

    @classmethod
    def from_credentials(cls, credentials):
        credentials = credentials or {}
        return cls(credentials.get("user_message_evt", "user_uttered"),
                   credentials.get("bot_message_evt", "bot_uttered"),
                   credentials.get("namespace"),
                   credentials.get("session_persistence", False),
                   credentials.get("socketio_path", "/dashchat_socket.io"),
                   )

    def __init__(self,
                 user_message_evt="user_uttered",
                 bot_message_evt="bot_uttered",
                 namespace: Optional[Text] = None,
                 session_persistence: bool = False,
                 socketio_path: Optional[Text] = '/dashchat_socket.io'
                 ):
        self.bot_message_evt = bot_message_evt
        self.session_persistence = session_persistence
        self.user_message_evt = user_message_evt
        self.namespace = '/dashchat'
        self.socketio_path = socketio_path

    def blueprint(self, on_new_message):
        sio = AsyncServer(async_mode='sanic', cors_allowed_origins='*')
        dashchat_webhook = SocketBlueprint(sio, self.socketio_path,
                                           'dashchat_webhook', __name__)

        @dashchat_webhook.route("/", methods=['GET'])
        async def health(request):
            return response.json({"status": "ok"})

        @sio.on('connect', namespace=self.namespace)
        async def connect(sid, environ):
            logger.info(f"[{sid}] - User {sid} connected to socketIO endpoint.")
            await sio.emit('identify', uuid.uuid4().hex, room=sid, namespace=self.namespace)
            CURRENT_USER.labels(self.name()).inc()

        @sio.on('disconnect', namespace=self.namespace)
        async def disconnect(sid):
            logger.info(f"[{sid}] - User {sid} disconnected from socketIO endpoint.")
            output_channel = DashChatOutput(sio, sid, self.namespace, self.bot_message_evt)
            message = UserMessage('/goodbye', output_channel, sid, input_channel=HYDRA_CHANNEL)
            await on_new_message(message)
            CURRENT_USER.labels(self.name()).dec()

        @sio.on('session_request', namespace=self.namespace)
        async def session_request(sid, data):
            if data is None:
                data = {}
            if 'session_id' not in data or data['session_id'] is None:
                data['session_id'] = uuid.uuid4().hex
            await sio.emit("session_confirm", data['session_id'], room=sid)
            logger.debug("User {} connected to socketIO endpoint."
                         "".format(sid))

        @sio.on(self.user_message_evt, namespace=self.namespace)
        async def handle_message(sid, data):
            with opentracing.tracer.start_active_span('web_socket_handle_message'):
                with CHAT_LATENCY.labels(self.name(), handle_message.__name__).time():
                    output_channel = DashChatOutput(sio, sid, self.namespace, self.bot_message_evt)

                    if self.session_persistence:
                        if not data.get("session_id"):
                            logger.warning("A message without a valid sender_id "
                                           "was received. This message will be "
                                           "ignored. Make sure to set a proper "
                                           "session id using the "
                                           "`session_request` socketIO event.")
                            return
                        sender_id = data['session_id']
                    else:
                        sender_id = sid

                    logger.info(f"[{sid}] - User msg: {data['message']}")

                    if "greet" in data.get("message"):
                        channelUserId = data.get("message").split().pop(1)
                        channelUserId = channelUserId.split("\"").pop(1)
                        result = await self.startTracking(channelUserId, HYDRA_CHANNEL, sid)
                        # Reformat the initial string
                        if result:
                            message = f"{data['message'][:-1]}, {result[1:]}"
                            data['message'] = message
                            logger.info(f"[{sid}] - User tracked by IDP. Message: {message}")

                    message = UserMessage(data['message'], output_channel, sender_id,
                                          input_channel=HYDRA_CHANNEL)

                    await on_new_message(message)

        return dashchat_webhook
