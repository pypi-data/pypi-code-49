"""Provides the MindspaceFactory class."""

import os.path

from json import loads, dumps
from socket import getfqdn

from attr import attrs, attrib, Factory
from autobahn.twisted.websocket import (
    listenWS, WebSocketServerFactory, WebSocketServerProtocol
)
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from klein import Klein
from mindspace_protocol import MindspaceParser
from twisted.internet import reactor
from twisted.web.server import Site

__all__ = ['WebApp', 'WebSocketProtocol', 'MindspaceFactory']
NoneType = type(None)
templates_dir = os.path.join(os.path.dirname(__file__), 'templates')


class WebSocketProtocol(WebSocketServerProtocol):
    """A websocket implementation using the mindspace protocol."""

    def onMessage(self, payload, is_binary):
        """Handle an incoming command."""
        if is_binary:
            return self.handle_binary(payload)
        command_name, command_args, command_kwargs = loads(payload)
        return self.handle_command(
            command_name, *command_args, **command_kwargs
        )

    def handle_command(self, command_name, *args, **kwargs):
        """Handle a command from the other side."""
        parser = self.factory.mindspace_factory.get_parser(self)
        return parser.handle_command(command_name, self, *args, **kwargs)

    def handle_binary(self, payload):
        """Handle a binary payload."""
        raise NotImplementedError

    def send_command(self, command_name, *args):
        """Have JavaScript execute a method."""
        data = dict(command=command_name, args=args)
        string = dumps(data)
        self.sendMessage(string.encode())


class WebApp(Klein):
    """A Klein app with some useful methods."""
    def __init__(self, *args, **kwargs):
        """Add an environment."""
        super().__init__(*args, **kwargs)
        self.environment = Environment(
            loader=FileSystemLoader([
                templates_dir,
                os.path.join(os.getcwd(), 'templates')]
            )
        )
        self.environment.filters['getmtime'] = os.path.getmtime
        self.route('/')(self.index)
        self.route('/socketurl.js', branch=False)(self.javascript)

    @property
    def loader(self):
        """Return the jinja2 loader for easy access."""
        return self.environment.loader

    def index(self, request):
        try:
            return self.render_template('index.html')
        except TemplateNotFound:
            return self.render_template('_index.html')

    def javascript(self, request):
        try:
            return self.render_template(
                'mindspace.js', mindspace=self.mindspace_factory
            )
        except TemplateNotFound:
            return self.render_template(
                '_mindspace.js', mindspace=self.mindspace_factory
            )

    def render_template(self, template, **kwargs):
        """Render a template, and return a string."""
        t = self.environment.get_template(template)
        return t.render(**kwargs)

    def render_string(self, string, **kwargs):
        """Render a string as a template, and return the result."""
        t = self.environment.from_string(string)
        return t.render(**kwargs)


@attrs
class MindspaceFactory:
    """The main object for creating mindspace projects."""

    parser = attrib(default=Factory(MindspaceParser))
    interface = attrib(default=Factory(lambda: '0.0.0.0'))
    http_port = attrib(default=Factory(lambda: 6463))
    websocket_port = attrib(default=Factory(lambda: 6464))
    websocket_class = attrib(default=Factory(lambda: WebSocketProtocol))
    websocket_listener = attrib(default=Factory(NoneType), init=False)
    klein_app = attrib(default=Factory(WebApp))
    hostname = attrib(default=Factory(getfqdn), init=False)

    def __attrs_post_init__(self):
        self.klein_app.mindspace_factory = self

    def get_parser(self, connection):
        """By default returns self.parser. Override to provide different parser
        instances for different types of connection."""
        return self.parser

    def run(self):
        """Listen for connections."""
        websocket_factory = WebSocketServerFactory(
            f'ws://{self.interface}:{self.websocket_port}'
        )
        websocket_factory.protocol = self.websocket_class
        websocket_factory.mindspace_factory = self
        self.websocket_listener = listenWS(websocket_factory)
        http_site = Site(self.klein_app.resource())
        self.http_listener = reactor.listenTCP(self.http_port, http_site)
        reactor.run()
