# -*- coding: utf-8 -*-

import websockets
import asyncio
import json
import sys
import re
import ssl
import certifi


class SampleBroadcasterClient:

    @staticmethod
    def get_server_uri(server):
        uri = 'ws://localhost:7003/livestream'
        if server == 'staging':
            uri = 'wss://staging-bot.bimariobot.com/livestream/'
        return uri

    @staticmethod
    async def start_ws_client(server_uri):
        ws_client = SampleBroadcasterClient(
            server_uri = server_uri
        )
        await ws_client.run()

    def __init__(self, server_uri):
        if sys.version_info < (3, 7, 0):
            raise Exception(
                'Python version ' + str(sys.version) + ' not supported'
            )

        self.server_uri = server_uri
        self.conn_disconnected = False

        # self.access_token = BiBotLiveStreamClient.get_access_token(bot_info = bot_info)
        #
        # self.ping_packet = ClientRequest(
        #     event_type   = ClientRequest.VALUE_EVENT_TYPE_PING,
        #     access_token = self.access_token
        # ).to_json()

        return

    async def init_ws(
            self
    ):
        #
        # We need to do this to make sure it won't fail SSL Cert verification
        #
        ssl_context = None
        need_ssl = re.match(pattern='^(wss:)', string=self.server_uri)
        if need_ssl:
            ssl_context = ssl.create_default_context()
            ssl_context.load_verify_locations(certifi.where())

        self.ws = await websockets.connect(
            self.server_uri,
            ssl = ssl_context
        )
        print('Websocket to "' + str(self.server_uri) + '" formed..')

        conn_packet = json.dumps({'provider': 'nwae.broadcaster'})

        # First connection
        await self.ws.send(json.dumps(conn_packet))
        print('Sent connection packet:\n\r' + str(conn_packet))

        server_reply = await self.ws.recv()
        # print(server_reply)
        print('Server reply (type ' + str(type(server_reply)) + '): ' + str(server_reply))
        return

    async def handle_ws(
            self
    ):
        while True:
            packet = await self.ws.recv()
            try:
                print('Received: ' + str(packet))
            except Exception as ex:
                print('Could not get server response. Exception "' + str(ex) + '"')

    async def run(self):
        await self.init_ws()
        #
        # Even if we run both together, they are not multi-threading, just asynchronous.
        # Thus ping function will still need to wait for the blocking input() call.
        #
        await asyncio.gather(
            self.handle_ws(),
            # ws_client.ping_server()
        )


if __name__ == '__main__':
    asyncio.run(SampleBroadcasterClient.start_ws_client(
        server_uri = SampleBroadcasterClient.get_server_uri(server='local')
    ))
    exit(0)

# asyncio.get_event_loop().run_until_complete(
#     WsClient.chat(server = 'local')
# )
