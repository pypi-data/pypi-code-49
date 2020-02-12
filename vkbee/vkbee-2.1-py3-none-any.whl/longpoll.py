import aiohttp
import json
import requests
import time
import asyncio

from collections import defaultdict
from datetime import datetime
from enum import IntEnum

import six
from six.moves import range

CHAT_START_ID = int(2E9)  # id с которого начинаются беседы

"""
:authors: sergeyfilippov1, YamkaFox
:license: Mozilla Public License, version 2.0, see LICENSE file
:copyright: (c) 2020 asyncvk
"""


class Event(object):
    """ Событие, полученное от longpoll-сервера.
    Имеет поля в соответствии с `документацией
    <https://vk.com/dev/using_longpoll_2?f=3.%2BСтруктура%2Bсобытий>`_.
    События `MESSAGE_NEW` и `MESSAGE_EDIT` имеют (среди прочих) такие поля:
        - `text` - `экранированный <https://ru.wikipedia.org/wiki/Мнемоники_в_HTML>`_ текст
        - `message` - оригинальный текст сообщения.
    События с полем `timestamp` также дополнительно имеют поле `datetime`.
    """

    def __init__(self, raw):
        self.raw = raw

        self.from_user = False
        self.from_chat = False
        self.from_group = False
        self.from_me = False
        self.to_me = False

        self.attachments = {}
        self.message_data = None

        self.message_id = None
        self.timestamp = None
        self.peer_id = None
        self.flags = None
        self.extra = None
        self.extra_values = None
        self.type_id = None

        try:
            self.type = EventType(self.raw[0])
            self._list_to_attr(self.raw[1:], EVENT_ATTRS_MAPPING[self.type])
        except ValueError:
            self.type = self.raw[0]

        if self.extra_values:
            self._dict_to_attr(self.extra_values)

        if self.type in PARSE_PEER_ID_EVENTS:
            self._parse_peer_id()

        if self.type in PARSE_MESSAGE_FLAGS_EVENTS:
            self._parse_message_flags()

        if self.type is EventType.CHAT_UPDATE:
            self._parse_chat_info()
            try:
                self.update_type = VkChatEventType(self.type_id)
            except ValueError:
                self.update_type = self.type_id

        elif self.type is EventType.NOTIFICATION_SETTINGS_UPDATE:
            self._dict_to_attr(self.values)
            self._parse_peer_id()

        elif self.type is EventType.PEER_FLAGS_REPLACE:
            self._parse_peer_flags()

        elif self.type in [EventType.MESSAGE_NEW, EventType.MESSAGE_EDIT]:
            self._parse_message()

        elif self.type in [EventType.USER_ONLINE, EventType.USER_OFFLINE]:
            self.user_id = abs(self.user_id)
            self._parse_online_status()

        elif self.type is EventType.USER_RECORDING_VOICE:
            if isinstance(self.user_id, list):
                self.user_id = self.user_id[0]

        if self.timestamp:
            self.datetime = datetime.utcfromtimestamp(self.timestamp)

    def _list_to_attr(self, raw, attrs):
        for i in range(min(len(raw), len(attrs))):
            self.__setattr__(attrs[i], raw[i])

    def _dict_to_attr(self, values):
        for k, v in six.iteritems(values):
            self.__setattr__(k, v)

    def _parse_peer_id(self):
        if self.peer_id < 0:  # Сообщение от/для группы
            self.from_group = True
            self.group_id = abs(self.peer_id)

        elif self.peer_id > CHAT_START_ID:  # Сообщение из беседы
            self.from_chat = True
            self.chat_id = self.peer_id - CHAT_START_ID

            if self.extra_values and 'from' in self.extra_values:
                self.user_id = int(self.extra_values['from'])

        else:  # Сообщение от/для пользователя
            self.from_user = True
            self.user_id = self.peer_id

    def _parse_message_flags(self):
        self.message_flags = set(
            x for x in VkMessageFlag if self.flags & x
        )

    def _parse_peer_flags(self):
        self.peer_flags = set(
            x for x in VkPeerFlag if self.flags & x
        )

    def _parse_message(self):
        if self.type is EventType.MESSAGE_NEW:
            if self.flags & VkMessageFlag.OUTBOX:
                self.from_me = True
            else:
                self.to_me = True

        # ВК возвращает сообщения в html-escaped виде,
        # при этом переводы строк закодированы как <br> и не экранированы

        self.text = self.text.replace('<br>', '\n')
        self.message = self.text \
            .replace('&lt;', '<') \
            .replace('&gt;', '>') \
            .replace('&quot;', '"') \
            .replace('&amp;', '&')


class ChatEventType(IntEnum):
    """ Идентификатор типа изменения в чате """

    #: Изменилось название беседы
    TITLE = 1

    #: Сменилась обложка беседы
    PHOTO = 2

    #: Назначен новый администратор
    ADMIN_ADDED = 3

    #: Изменены настройки беседы
    SETTINGS_CHANGED = 4

    #: Закреплено сообщение
    MESSAGE_PINNED = 5

    #: Пользователь присоединился к беседе
    USER_JOINED = 6

    #: Пользователь покинул беседу
    USER_LEFT = 7

    #: Пользователя исключили из беседы
    USER_KICKED = 8

    #: С пользователя сняты права администратора
    ADMIN_REMOVED = 9

    #: Бот прислал клавиатуру
    KEYBOARD_RECEIVED = 11


class EventType(IntEnum):
    """ Перечисление событий, получаемых от longpoll-сервера.
    `Подробнее в документации VK API
    <https://vk.com/dev/using_longpoll?f=3.+Структура+событий>`__
    """

    MESSAGE_FLAGS_REPLACE = 1
    MESSAGE_FLAGS_SET = 2
    MESSAGE_FLAGS_RESET = 3
    MESSAGE_NEW = 4
    MESSAGE_EDIT = 5
    READ_ALL_INCOMING_MESSAGES = 6
    READ_ALL_OUTGOING_MESSAGES = 7
    USER_ONLINE = 8
    USER_OFFLINE = 9
    PEER_FLAGS_RESET = 10
    PEER_FLAGS_REPLACE = 11
    PEER_FLAGS_SET = 12
    PEER_DELETE_ALL = 13
    PEER_RESTORE_ALL = 14
    CHAT_EDIT = 51
    CHAT_UPDATE = 52
    USER_TYPING = 61
    USER_TYPING_IN_CHAT = 62
    USER_RECORDING_VOICE = 64
    USER_CALL = 70
    MESSAGES_COUNTER_UPDATE = 80
    NOTIFICATION_SETTINGS_UPDATE = 114


MESSAGE_EXTRA_FIELDS = [
    'peer_id', 'timestamp', 'text', 'extra_values', 'attachments', 'random_id'
]

MSGID = 'message_id'

EVENT_ATTRS_MAPPING = {
    EventType.MESSAGE_FLAGS_REPLACE: [MSGID, 'flags'] + MESSAGE_EXTRA_FIELDS,
    EventType.MESSAGE_FLAGS_SET: [MSGID, 'mask'] + MESSAGE_EXTRA_FIELDS,
    EventType.MESSAGE_FLAGS_RESET: [MSGID, 'mask'] + MESSAGE_EXTRA_FIELDS,
    EventType.MESSAGE_NEW: [MSGID, 'flags'] + MESSAGE_EXTRA_FIELDS,
    EventType.MESSAGE_EDIT: [MSGID, 'mask'] + MESSAGE_EXTRA_FIELDS,

    EventType.READ_ALL_INCOMING_MESSAGES: ['peer_id', 'local_id'],
    EventType.READ_ALL_OUTGOING_MESSAGES: ['peer_id', 'local_id'],

    EventType.USER_ONLINE: ['user_id', 'extra', 'timestamp'],
    EventType.USER_OFFLINE: ['user_id', 'flags', 'timestamp'],

    EventType.PEER_FLAGS_RESET: ['peer_id', 'mask'],
    EventType.PEER_FLAGS_REPLACE: ['peer_id', 'flags'],
    EventType.PEER_FLAGS_SET: ['peer_id', 'mask'],

    EventType.PEER_DELETE_ALL: ['peer_id', 'local_id'],
    EventType.PEER_RESTORE_ALL: ['peer_id', 'local_id'],

    EventType.CHAT_EDIT: ['chat_id', 'self'],
    EventType.CHAT_UPDATE: ['type_id', 'peer_id', 'info'],

    EventType.USER_TYPING: ['user_id', 'flags'],
    EventType.USER_TYPING_IN_CHAT: ['user_id', 'chat_id'],
    EventType.USER_RECORDING_VOICE: ['peer_id', 'user_id', 'flags', 'timestamp'],

    EventType.USER_CALL: ['user_id', 'call_id'],

    EventType.MESSAGES_COUNTER_UPDATE: ['count'],
    EventType.NOTIFICATION_SETTINGS_UPDATE: ['values']
}

PARSE_PEER_ID_EVENTS = [
    k for k, v in six.iteritems(EVENT_ATTRS_MAPPING) if 'peer_id' in v
]
PARSE_MESSAGE_FLAGS_EVENTS = [
    EventType.MESSAGE_FLAGS_REPLACE,
    EventType.MESSAGE_NEW
]


class VkBeeLongpoll:
    PRELOAD_MESSAGE_EVENTS = [
        EventType.MESSAGE_NEW,
        EventType.MESSAGE_EDIT
    ]

    def __init__(self, vk, wait=10):
        self.wait = wait
        self.vk = vk

        self.method_url = "https://api.vk.com/method/messages.getLongPollServer"

        self.url = None
        self.key = None
        self.server = None
        self.ts = None
        self.start_time = time.time()
        self.request_count = 0

    def _parse_event(self, raw_event):
        return Event(raw_event)

    async def update_server(self, update_ts=True):
        data = {"lp_version": 3}

        r = await self.vk.call("messages.getLongPollServer", data=data)

        self.key = r["key"]
        self.server = r["server"]
        self.url = self.server

        if update_ts:
            self.ts = r["ts"]

    async def get_events(self):
        params = {
            "act": "a_check",
            "key": self.key,
            "ts": self.ts,
            "wait": self.wait,
            "mode": 234
        }

        response = await self.vk.s.get(self.url, params=params)

        self.request_count += 1

        response = await response.json()

        if 'failed' not in response:
            self.ts = response['ts']

            events = [
                self._parse_event(raw_event)
                for raw_event in response['updates']
            ]

            if self.preload_messages:
                self.preload_message_events_data(events)

            return events

        elif response["failed"] == 1:
            self.ts = response["ts"]

        elif response["failed"] == 2:
            self.update_server()(update_ts=False)

        elif response["failed"] == 3:
            self.update_server()

        return []

    async def events(self):
        await self.update_server()
        while True:
            for event in await self.get_events():
                await self.update_server()
                yield event
