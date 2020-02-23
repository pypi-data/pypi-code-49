# -*- coding: utf-8 -*-
# author: asyncvk
import aiohttp
import json
import requests
import time
import asyncio
import six

from enum import IntEnum

class VkEventType(IntEnum):
    """ Перечисление событий, получаемых от longpoll-сервера.
    `Подробнее в документации VK API
    <https://vk.com/dev/using_longpoll?f=3.+Структура+событий>`__
    """

    #: Замена флагов сообщения (FLAGS:=$flags)
    MESSAGE_FLAGS_REPLACE = 1

    #: Установка флагов сообщения (FLAGS|=$mask)
    MESSAGE_FLAGS_SET = 2

    #: Сброс флагов сообщения (FLAGS&=~$mask)
    MESSAGE_FLAGS_RESET = 3

    #: Добавление нового сообщения.
    MESSAGE_NEW = 4

    #: Редактирование сообщения.
    MESSAGE_EDIT = 5

    #: Прочтение всех входящих сообщений в $peer_id,
    #: пришедших до сообщения с $local_id.
    READ_ALL_INCOMING_MESSAGES = 6

    #: Прочтение всех исходящих сообщений в $peer_id,
    #: пришедших до сообщения с $local_id.
    READ_ALL_OUTGOING_MESSAGES = 7

    #: Друг $user_id стал онлайн. $extra не равен 0, если в mode был передан флаг 64.
    #: В младшем байте числа extra лежит идентификатор платформы
    #: (см. :class:`VkPlatform`).
    #: $timestamp — время последнего действия пользователя $user_id на сайте.
    USER_ONLINE = 8

    #: Друг $user_id стал оффлайн ($flags равен 0, если пользователь покинул сайт и 1,
    #: если оффлайн по таймауту). $timestamp — время последнего действия пользователя
    #: $user_id на сайте.
    USER_OFFLINE = 9

    #: Сброс флагов диалога $peer_id.
    #: Соответствует операции (PEER_FLAGS &= ~$flags).
    #: Только для диалогов сообществ.
    PEER_FLAGS_RESET = 10

    #: Замена флагов диалога $peer_id.
    #: Соответствует операции (PEER_FLAGS:= $flags).
    #: Только для диалогов сообществ.
    PEER_FLAGS_REPLACE = 11

    #: Установка флагов диалога $peer_id.
    #: Соответствует операции (PEER_FLAGS|= $flags).
    #: Только для диалогов сообществ.
    PEER_FLAGS_SET = 12

    #: Удаление всех сообщений в диалоге $peer_id с идентификаторами вплоть до $local_id.
    PEER_DELETE_ALL = 13

    #: Восстановление недавно удаленных сообщений в диалоге $peer_id с
    #: идентификаторами вплоть до $local_id.
    PEER_RESTORE_ALL = 14

    #: Один из параметров (состав, тема) беседы $chat_id были изменены.
    #: $self — 1 или 0 (вызваны ли изменения самим пользователем).
    CHAT_EDIT = 51

    #: Изменение информации чата $peer_id с типом $type_id
    #: $info — дополнительная информация об изменениях
    CHAT_UPDATE = 52

    #: Пользователь $user_id набирает текст в диалоге.
    #: Событие приходит раз в ~5 секунд при наборе текста. $flags = 1.
    USER_TYPING = 61

    #: Пользователь $user_id набирает текст в беседе $chat_id.
    USER_TYPING_IN_CHAT = 62

    #: Пользователь $user_id записывает голосовое сообщение в диалоге/беседе $peer_id
    USER_RECORDING_VOICE = 64

    #: Пользователь $user_id совершил звонок с идентификатором $call_id.
    USER_CALL = 70

    #: Счетчик в левом меню стал равен $count.
    MESSAGES_COUNTER_UPDATE = 80

    #: Изменились настройки оповещений.
    #: $peer_id — идентификатор чата/собеседника,
    #: $sound — 1/0, включены/выключены звуковые оповещения,
    #: $disabled_until — выключение оповещений на необходимый срок.
    NOTIFICATION_SETTINGS_UPDATE = 114

class event:
    def __init__(self, raw):
        self.raw = raw
        self.type = None
        self.user_id = None

        try:
            self.type = VkEventType(self.raw[0])
        except ValueError:
            self.type = self.raw[0]
        
        if self.raw[3] > int(2E9):
            self.from_chat = True
            self.chat_id = self.raw[3] - int(2E9)

            if self.raw[-1] is dict:
                self.user_id = self.raw[-1]["from"]


class VkBeeLongpoll:
    def __init__(self,vk,wait=10):
        self.wait = wait
        self.vk = vk

        self.method_url = "https://api.vk.com/method/messages.getLongPollServer"

        self.url = None
        self.key = None
        self.server = None
        self.ts = None
        self.start_time = time.time()
        self.request_count = 0

    async def update_server(self,update_ts=True):
        data = {"lp_version": 3}
        # r = await self.s.post(self.method_url, data=data)
        r = await self.vk.call("messages.getLongPollServer", data=data)
        self.key = r["key"]
        self.server = r["server"]
        self.url = f"https://{self.server}"

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
        # work_time = time.time() - self.start_time
        # avr_time = work_time / self.request_count
        # speed = self.request_count / work_time
        #print(f'All Get Events - {self.request_count}')
        # print(f'Work Time - {work_time}')
        # print(f'Requests in Second - {speed}')
        # print(f'Average Time - {avr_time}')

        response = await response.json()
        print(response)

        if "failed" not in response:
            return response["updates"]

        elif response["failed"] == 1:
            self.ts = response["ts"]

        elif response["failed"] == 2:
            await self.update_server(update_ts=False)

        elif response["failed"] == 3:
            await self.update_server()

        return []

    async def events(self):
        await self.update_server()
        while True:
            for event in await self.get_events():
                await self.update_server()
                yield event