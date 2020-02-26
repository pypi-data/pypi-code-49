import asyncio
import inspect
import json
import logging
from asyncio import Queue, CancelledError

import opentracing
from sanic import Blueprint, response

import rasa.utils.endpoints
from metrics.constants import CHAT_LATENCY
from rasa.core.channels import (UserMessage, InputChannel)
from rasa.core.channels.channel import QueueOutputChannel, CollectingOutputChannel

logger = logging.getLogger(__name__)
HYDRA_CHANNEL = "OMNI_VOICE_00001"


class PersyOutputChannel(CollectingOutputChannel):
    @classmethod
    def name(cls):
        return "persy"


class PersyInput(InputChannel):
    """A custom http input channel.

    This implementation is the basis for a custom implementation of a chat
    frontend. You can customize this to send messages to Rasa Core and
    retrieve responses from the agent."""

    @classmethod
    def name(cls):
        return "persy"

    @staticmethod
    async def on_message_wrapper(on_new_message, text, queue, sender_id, channel):
        collector = QueueOutputChannel(queue)

        message = UserMessage(text, collector, sender_id,
                              input_channel=channel)
        await on_new_message(message)

        await queue.put("DONE")

    async def _extract_sender(self, req):
        return req.json.get("sender", None)

    # noinspection PyMethodMayBeStatic
    def _extract_message(self, req):
        return req.json.get("message", None)

    def _extract_confidence(self, req):
        return req.json.get("confidence", None)

    def _extract_recording(self, req):
        return req.json.get("recordingId", None)

    def _extract_channel(self, req):
        return req.json.get("channel", HYDRA_CHANNEL)

    def stream_response(self, on_new_message, text, sender_id, channel):
        async def stream(resp):
            q = Queue()
            task = asyncio.ensure_future(
                self.on_message_wrapper(on_new_message, text, q, sender_id, channel))
            while True:
                result = await q.get()
                if result == "DONE":
                    break
                else:
                    await resp.write(json.dumps(result) + "\n")
            await task

        return stream

    def blueprint(self, on_new_message):
        custom_webhook = Blueprint(
            'custom_webhook_{}'.format(type(self).__name__),
            inspect.getmodule(self).__name__)

        # noinspection PyUnusedLocal
        @custom_webhook.route("/", methods=['GET'])
        async def health(request):
            return response.json({"status": "ok"})

        @custom_webhook.route("/webhook", methods=['POST'])
        async def receive(request):
            with opentracing.tracer.start_active_span('persy_receive') as scope:
                with CHAT_LATENCY.labels(self.name(), receive.__name__).time():
                    sender_id = await self._extract_sender(request)
                    text = self._extract_message(request)
                    should_use_stream = rasa.utils.endpoints.bool_arg(
                        request, "stream", default=False
                    )

                    persy_channel = self._extract_channel(request)

                    logger.info(f"[{sender_id}] - User msg: {text}")

                    if should_use_stream:
                        return response.stream(
                            self.stream_response(on_new_message, text, sender_id, persy_channel),
                            content_type='text/event-stream')
                    else:
                        collector = PersyOutputChannel()
                        # noinspection PyBroadException
                        try:
                            if "greet" in text:
                                channelUserId = text.split().pop(1)
                                channelUserId = channelUserId.split("\"").pop(1)
                                result = await self.startTracking(channelUserId, persy_channel, sender_id)
                                # Reformat the initial string
                                if result:
                                    message = f"{text[:-1]}, {result[1:]}"
                                    text = message
                                    logger.info(f"[{sender_id}] - User tracked by IDP. Message: {message}")

                            await on_new_message(UserMessage(text, collector, sender_id,
                                                             asrConfidence=self._extract_confidence(request),
                                                             recordingId=self._extract_recording(request),
                                                             input_channel=persy_channel))
                        except CancelledError:
                            logger.error("[{}] - Message handling timed out for "
                                         "user message '{}'.".format(sender_id, text))
                        except Exception:
                            logger.exception("[{}] - An exception occured while handling "
                                             "user message '{}'.".format(sender_id, text))

                        logger.info(f"[{sender_id}] - Bot response: {collector.messages}")
                        return response.json(collector.messages)

        return custom_webhook