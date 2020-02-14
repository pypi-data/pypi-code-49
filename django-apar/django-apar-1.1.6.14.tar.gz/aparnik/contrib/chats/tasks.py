"""Celery tasks."""

from __future__ import absolute_import, unicode_literals

from celery import shared_task

from aparnik.contrib.chats.api.serializers import ChatSessionMessageDetailsSerializer
from aparnik.contrib.chats.models import *
from aparnik.contrib.messaging.utils import notify
from aparnik.utils.utils import get_request


@shared_task
def send_chat_message(chat_message_id):
    """Send chat message create notification and etc via a channel to celery."""
    chat_message = ChatSessionMessage.objects.get(pk=chat_message_id)
    chat_session = chat_message.chat_session
    user = chat_message.user
    owner = chat_session.owner

    chat_notifications = []
    members = chat_session.members.prefetch_related('user').exclude(user=user)
    for member in members:
        if member.user != user.pk:
            chat_notifications.append(
                ChatMessageNotification(
                    chat_message=chat_message,
                    user=member.user,
                ),
            )

    if owner.pk != user.pk:
        chat_notifications.append(
            ChatMessageNotification(
                chat_message=chat_message,
                user=owner,
            ),
        )

    ChatMessageNotification.objects.bulk_create(chat_notifications)

    """Send notification via a channel to celery."""
    serializer = ChatSessionMessageDetailsSerializer(chat_message, many=False, read_only=True,
                                                     context={'request': get_request()})
    notify(
        uri=chat_session.uri,
        source=user,
        source_display_name=user.get_full_name(),
        recipient=None,
        action='Create',
        obj=chat_message,
        short_description='You a new message',
        extra_data={
            'uri': chat_session.uri,
            'message': serializer.data,
        },
        channels=['websocket'],
        silent=True,
    )
