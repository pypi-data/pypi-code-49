# -*- coding: utf-8 -*-

import sys
import threading
from nwae.utils.Log import Log
from inspect import getframeinfo, currentframe
import json
import asyncio


class BroadcastThread(threading.Thread):

    def __init__(
            self,
            client_subscribers_list,
            mutex_client_subscribers_list,
            feed_queue
    ):
        super().__init__()
        self.client_subscribers_list = client_subscribers_list
        self.mutex_client_subscribers_list = mutex_client_subscribers_list
        self.feed_queue = feed_queue

        self.stoprequest = threading.Event()
        return

    def broadcast_blocking(
            self,
            json_msg
    ):
        Log.info(
            str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
            + ': Running Blocking Broadcast to ' + str(len(self.client_subscribers_list))
            + ' sockets..'
        )
        failed_subscribers = []

        for subscriber in self.client_subscribers_list:
            socket = subscriber['socket']
            remote_addr = subscriber['remote_addr']
            remote_port = subscriber['remote_port']
            try:
                socket.send(json_msg)
            except Exception as ex_send:
                Log.error(
                    str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                    + ': Error send to socket ' + str(remote_addr) + ':' + str(remote_port)
                    + '. Exception: ' + str(ex_send)
                )
                failed_subscribers.append(subscriber)

        for subscriber in failed_subscribers:
            self.remove_subscriber(subscriber=subscriber)
        return

    async def send(
            self,
            subscriber,
            socket,
            json_msg
    ):
        try:
            socket.send(json_msg)
            # Only useful if we have subsequent tasks after this, and are
            # giving up CPU to other concurrent tasks for the moment.
            await asyncio.sleep(0)
            return (True, subscriber)
        except Exception as ex_send:
            Log.error(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Error send to socket ' + str(socket) + ': ' + str(ex_send)
            )
            return (False, subscriber)

    async def broadcast_non_blocking(
            self,
            json_msg
    ):
        Log.info(
            str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
            + ': Running AsyncIo Broadcast to ' + str(len(self.client_subscribers_list))
            + ' sockets..'
        )

        # Create all the send tasks first, don't run the task yet
        async_tasks = []
        for subscriber in self.client_subscribers_list:
            socket = subscriber['socket']
            remote_addr = subscriber['remote_addr']
            remote_port = subscriber['remote_port']
            atask = asyncio.create_task(self.send(
                subscriber = subscriber,
                socket     = socket,
                json_msg   = json_msg
            ))
            async_tasks.append(atask)

        # Now run all the tasks simultaneously
        for atask in async_tasks:
            await atask

        # Get return values of all tasks
        failed_subscribers = []
        for atask in async_tasks:
            (ok_sent, subscriber) = atask.result()
            if not ok_sent:
                failed_subscribers.append(subscriber)

        for subscriber in failed_subscribers:
            self.remove_subscriber(subscriber=subscriber)
        return

    def run(self):
        while True:
            # Keep checking messages queue and broadcast to client subscribers
            try:
                msg_item = self.feed_queue.get(block=True, timeout=5)
                Log.important(
                    str(__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
                    + ': Broadcasting ' + str(msg_item)
                )
            except Exception:
                continue

            try:
                json_msg = json.dumps(msg_item)

                if sys.version_info >= (3, 7, 0):
                    asyncio.run(self.broadcast_non_blocking(json_msg=json_msg))
                else:
                    self.broadcast_blocking(
                        json_msg=json_msg
                    )
            except Exception as ex:
                Log.error(
                    str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                    + ': Exception in broadcast loop: ' + str(ex)
                )

    def remove_subscriber(
            self,
            subscriber
    ):
        remote_addr = subscriber['remote_addr']
        remote_port = subscriber['remote_port']
        try:
            self.mutex_client_subscribers_list.acquire()
            self.client_subscribers_list.remove(subscriber)
            Log.important(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Socket ' + str(remote_addr) + ':' + str(remote_port)
                + ' removed from subscribers list.'
            )
        except Exception as ex:
            Log.error(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Error removing socket ' + str(remote_addr) + ':' + str(remote_port)
                + ' from list: ' + str(ex)
            )
        finally:
            self.mutex_client_subscribers_list.release()
        return

