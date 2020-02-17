from .server import SocketsServer
from aiohttp import web


class WebServer:
    def __init__(self, url, socket_server):
        self.app = web.Application()
        self.app.add_routes([web.post('/' + url + '/{token}', self.handler)])
        self.socket_server = socket_server

    # !! you can override this
    async def handler(self, request):
        token = request.match_info.get('token')
        data = await request.text()

        res = await self.socket_server.notify(token, data)
        return web.Response(text='ok' if res else 'not ok')

    async def _on_startup(self, _):
        await self.socket_server.start()

    def start(self, port, ssl=None):
        self.app.on_startup.append(self._on_startup)

        web.run_app(
            self.app,
            host='0.0.0.0',
            port=port,
            ssl_context=ssl
        )


def start_with_webserver(port, web_url, socket_url="socket", ssl=None):
    socket_server = SocketsServer(socket_url)
    web_server = WebServer(web_url, socket_server)
    web_server.start(port, ssl)
