import logging

import websockets


class SocketsServer:
    def __init__(self, url="socket"):
        self.users = dict()
        self.url = url

    async def notify(self, token, data):
        logging.debug(f"update on {token}: {data}")

        if token not in self.users:
            logging.warning(f"token {token} doesnt found")
            return False

        user = self.users[token]
        await user.send(data)
        return True

    async def start(self):
        logging.info(f"server started on '{str(self.url)}'")

        if isinstance(self.url, tuple):
            host, port = self.url
            await websockets.serve(self._handler, host, port)
        else:
            await websockets.unix_serve(self._handler, self.url)

    async def start_loop(self):
        import asyncio
        await self.start()
        asyncio.get_event_loop().run_forever()

    def _unregister_by_token(self, token):
        logging.debug(f"unregister token {token}")
        del self.users[token]

    def _unregister_by_socket(self, socket):
        for key, value in self.users.items():
            if value == socket:
                self._unregister_by_token(key)

    def _register(self, token, websocket):
        logging.debug(f"register new token {token}")
        self.users[token] = websocket

    async def _handler(self, websocket, _):
        try:
            async for message in websocket:
                self._register(message, websocket)
        except websockets.exceptions.ConnectionClosedError:
            self._unregister_by_socket(websocket)
        finally:
            self._unregister_by_socket(websocket)

