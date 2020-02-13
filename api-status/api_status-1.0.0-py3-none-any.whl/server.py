from aiohttp import web


class Server():
    """ A sample aiohttp server to register routes. """

    def __init__(self, host=None, port=None):
        """
        :param str host: HOST to listen on, '0.0.0.0' if None (default).
        :param int port: PORT to listed on, 8080 if None (default).
        """
        self.app = web.Application()
        self.host = host
        self.port = port
        self.routes = []
        self._runner = None

    async def start(self):
        """ Start the server. """
        self.app.add_routes(self.routes)
        self._runner = web.AppRunner(self.app)
        await self._runner.setup()
        site = web.TCPSite(self._runner, self.host, self.port)
        await site.start()

    async def stop(self):
        """ Shutdown the server. """
        if self._runner:
            await self._runner.cleanup()
            await self.app.shutdown()

    def add_route(self, coro, method="GET", path=r"/status"):
        """ Register a new route. Route response with predefined 'application/json'
        content type and data encoded by dumps (json.dumps() by default).

        :param coroutine: Handler for the route. Does'nt take parameters.
                          Reponse is forwarded to aiohttp.web.json_response
        :param str method: HTTP method (GET, POST, etc). Default "GET".
        :param str path: Path to resource. Default "/status".
        """
        async def wrapper(*args, **kwargs):
            response = await coro()
            return web.json_response(response)
        self.routes.append(web.route(method, path, wrapper))
