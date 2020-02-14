"""This module provides core functionalities of gntplib.

gntplib is a Growl Notification Transport Protocol (GNTP_) client library in
Python.

.. _GNTP: http://www.growlforwindows.com/gfw/help/gntp.aspx
"""

from __future__ import unicode_literals
import hashlib
import io
import re
import socket

from . import keys
from .compat import text_type
from .exceptions import GNTPError


__version__ = '0.5'
__all__ = ['notify', 'publish', 'subscribe', 'Event', 'Notifier', 'Publisher',
           'RawIcon', 'Resource', 'SocketCallback', 'Subscriber']


SUPPORTED_VERSIONS = ['1.0']
DEFAULT_PORT = 23053
DEFAULT_TIMEOUT = 10
DEFAULT_TTL = 60
MAX_MESSAGE_SIZE = 4096
MAX_LINE_SIZE = 1024
LINE_DELIMITER = b'\r\n'
SECTION_DELIMITER = SECTION_BODY_START = SECTION_BODY_END = b'\r\n'
MESSAGE_DELIMITER = b'\r\n\r\n'
MESSAGE_DELIMITER_SIZE = len(MESSAGE_DELIMITER)
RESPONSE_INFORMATION_LINE_RE = re.compile(
    b'GNTP/([^ ]+) (-OK|-ERROR|-CALLBACK) NONE')
CUSTOM_HEADER_PREFIX = 'X-'
APP_SPECIFIC_HEADER_PREFIX = 'Data-'


def publish(app_name, event_name, title, text=''):
    """Register a publisher and send a notification at a time.

    :param app_name: the name of the application.
    :param event_name: the name of the notification.
    :param title: the title of the notification.
    :param text: the text of the notification.  Defaults to ``''``.
    """
    publisher = Publisher(app_name, coerce_to_events([event_name]))
    publisher.register()
    publisher.publish(event_name, title, text)


def notify(app_name, event_name, title, text=''):
    """Deprecated notify function."""
    import warnings
    warnings.warn('notify function is deprecated, use publish function'
                  ' instead', DeprecationWarning, stacklevel=2)
    publish(app_name, event_name, title, text)


def subscribe(id_, name, hub, password, port=DEFAULT_PORT):
    """Send a subscription request and return ttl.

    :param id_: the unique id of the subscriber.
    :param name: the name of the subscriber.
    :param hub: the subscribed-to machine.  If a string is given, it is used as
                a host of the hub and default port number `23053` is used.
                If host-port tuple is given, it is used directly.
    :param password: the password of the subscribed-to machine.
    :param port: the port number of the subscriber.  Defaults to `23053`.
    """
    subscriber = Subscriber(id_, name, hub, password, port=port)
    subscriber.subscribe()
    return subscriber.ttl


class BaseApp(object):
    """Base class for applications.

    :param custom_headers: the list of key-value tuples for Custom Headers.
    :param app_specific_headers: the list of key-value tuples for App-Specific
                                 Headers.
    :param gntp_client_class: GNTP client class.  If it is `None`,
                              :class:`GNTPClient` is used.  Defaults to `None`.
    """

    def __init__(self, custom_headers=None, app_specific_headers=None,
                 gntp_client_class=None, **kwargs):
        self.custom_headers = custom_headers or []
        self.app_specific_headers = app_specific_headers or []
        if gntp_client_class is None:
            gntp_client_class = GNTPClient
        self.gntp_client = gntp_client_class(**kwargs)


class Publisher(BaseApp):
    """Publisher of Growl Notification Transport Protocol (GNTP).

    This class supports ``REGISTER`` and ``NOTIFY`` requests.  They
    are sent by :meth:`register()` and :meth:`publish()` methods respectively.
    These methods can accept the optional final callback as `callback` keyword
    argument, which run after closing the connection with the GNTP server.

    `event_defs` is a list of ``str``, ``unicode``, double (of ``str`` and
    ``bool``) or :class:`Event` instance.  It is converted to a list of
    :class:`Event` instance as follows:
    ``str`` or ``unicode`` item becomes value of the `name` attribute of
    :class:`Event` instance, whose other attributes are defaults.  Double item
    is expanded to (`name`, `enabled`) tuple, and those values are passed to
    :class:`Event` constructor.  :class:`Event` instance item is used directly.

    Optional keyword arguments are passed to the `gntp_client_class`
    constructor.

    :param name: the name of the application.
    :param event_defs: the definitions of the notifications.
    :param icon: url string or an instance of :class:`Resource` for the icon of
                 the application.  Defaults to `None`.
    :param custom_headers: the list of key-value tuples for Custom Headers.
    :param app_specific_headers: the list of key-value tuples for App-Specific
                                 Headers.
    :param gntp_client_class: GNTP client class.  If it is `None`,
                              :class:`GNTPClient` is used.  Defaults to `None`.

    .. note:: In Growl 1.3.3, `icon` of url string does not work.
    """

    def __init__(self, name, event_defs, icon=None, custom_headers=None,
                 app_specific_headers=None, gntp_client_class=None, **kwargs):
        self.name = name
        self.icon = icon
        self.events = coerce_to_events(event_defs)
        if not self.events:
            raise GNTPError('You have to set at least one notification type')
        BaseApp.__init__(self, custom_headers, app_specific_headers,
                         gntp_client_class, **kwargs)

    def register(self, callback=None):
        """Register this publisher to the GNTP server.

        :param callback: the callback run after closing the connection with
                         the GNTP server.  Defaults to `None`.
        """
        request = RegisterRequest(self.name, self.icon, self.events,
                                  self.custom_headers,
                                  self.app_specific_headers)
        self.gntp_client.process_request(request, callback)

    def publish(self, name, title, text='', id_=None, sticky=False,
                priority=0, icon=None, coalescing_id=None, callback=None,
                gntp_callback=None, **socket_callback_options):
        """Send a notification to the GNTP server.

        :param name: the name of the notification.
        :param title: the title of the notification.
        :param text: the text of the notification.  Defaults to `''`.
        :param id_: the unique ID for the notification.  If set, this should be
                    unique for every request.  Defaults to `None`.
        :param sticky: if set to `True`, the notification remains displayed
                       until dismissed by the user.  Defaults to `False`.
        :param priority: the display hint for the receiver which may be
                         ignored.  A higher number indicates a higher priority.
                         Valid values are between -2 and 2, defaults to `0`.
        :param icon: url string or an instance of :class:`Resource` to display
                     with the notification.  Defaults to `None`.
        :param coalescing_id: if set, should contain the value of the `id_` of
                              a previously-sent notification.
                              This serves as a hint to the notification system
                              that this notification should replace/update the
                              matching previous notification.  The notification
                              system may ignore this hint.  Defaults to `None`.
        :param callback: the callback run after closing the connection with
                         the GNTP server.  Defaults to `None`.
        :param gntp_callback: url string for url callback or
                              :class:`SocketCallback` instance for socket
                              callback.  Defaults to `None`.
        :param socket_callback_options: the keyword arguments to be used to
                                        instantiating :class:`SocketCallback`
                                        for socket callback.  About acceptable
                                        keyword arguments,
                                        see :class:`SocketCallback`.

        .. note:: In Growl 1.3.3, `icon` of url string does not work.

        .. note:: Growl for Windows v2.0+ and Growl v1.3+ require
                  `coalescing_id` to be the same on both the original and
                  updated notifcation, ignoring the value of `id_`.
        """
        notification = Notification(name, title, text, id_=id_, sticky=sticky,
                                    priority=priority, icon=icon,
                                    coalescing_id=coalescing_id,
                                    gntp_callback=gntp_callback,
                                    **socket_callback_options)
        request = NotifyRequest(self.name, notification,
                                self.custom_headers,
                                self.app_specific_headers)
        self.gntp_client.process_request(
            request, callback, socket_callback=notification.socket_callback)


class Notifier(Publisher):
    """Deprecated Notifier of Growl Notification Transport Protocol (GNTP)."""

    def __init__(self, name, event_defs, icon=None, custom_headers=None,
                 app_specific_headers=None, gntp_client_class=None, **kwargs):
        import warnings
        warnings.warn('Notifier is deprecated, use Publisher instead',
                      DeprecationWarning, stacklevel=2)
        Publisher.__init__(self, name, event_defs, icon,
                           custom_headers, app_specific_headers,
                           gntp_client_class, **kwargs)

    def notify(self, name, title, text='', id_=None, sticky=False,
               priority=0, icon=None, coalescing_id=None, callback=None,
               gntp_callback=None, **socket_callback_options):
        """Send a notification to the GNTP server."""
        import warnings
        warnings.warn('notify method is deprecated, use publish method'
                      ' instead', DeprecationWarning, stacklevel=2)
        self.publish(name, title, text, id_, sticky, priority, icon,
                     coalescing_id, callback, gntp_callback,
                     **socket_callback_options)


class Subscriber(BaseApp):
    """Subscriber of Growl Notification Transport Protocol (GNTP).

    This class supports ``SUBSCRIBE`` request.

    :param id_: the unique id of the subscriber.
    :param name: the name of the subscriber.
    :param hub: the subscribed-to machine.  If a string is given, it is used as
                a host of the hub and default port number `23053` is used.
                If host-port tuple is given, it is used directly.
    :param password: the password of the subscribed-to machine.
    :param port: the port number of the subscriber.  Defaults to `23053`.
    :param custom_headers: the list of key-value tuples for Custom Headers.
    :param app_specific_headers: the list of key-value tuples for App-Specific
                                 Headers.
    :param gntp_client_class: GNTP client class.  If it is `None`,
                              :class:`GNTPClient` is used.  Defaults to `None`.
    """

    def __init__(self, id_, name, hub, password, port=DEFAULT_PORT,
                 custom_headers=None, app_specific_headers=None,
                 gntp_client_class=None, **kwargs):
        self.id_ = id_
        self.name = name
        if isinstance(hub, (bytes, text_type)):
            self.hub = (hub, DEFAULT_PORT)
        else:
            self.hub = hub
        self.password = password
        self.port = port
        self.ttl = DEFAULT_TTL
        BaseApp.__init__(self, custom_headers, app_specific_headers,
                         gntp_client_class, host=self.hub[0], port=self.hub[1],
                         password=self.password, **kwargs)

    def subscribe(self, callback=None):
        """Send a subscription request.

        If `callback` is `None`, :meth:`store_ttl` is used and :attr:`ttl` is
        updated by ``Subscription-TTL`` value of the response.

        :param callback: the callback run after closing the connection with
                         the GNTP server.  Defaults to `None`.
        """
        request = SubscribeRequest(self.id_, self.name, self.port,
                                   self.custom_headers,
                                   self.app_specific_headers)
        self.gntp_client.process_request(request, callback or self.store_ttl)

    def store_ttl(self, response):
        """Update :attr:`ttl` attribute."""
        ttl = response.headers['Subscription-TTL']
        self.ttl = int(ttl)


class Event(object):
    """Represent notification type.

    :param name: the name of the notification.
    :param display_name: the display name of the notification, which is
                         appeared at the Applications tab of the Growl
                         Preferences.  Defaults to `None`.
    :param enabled: indicates if the notification should be enabled by
                    default.  Defaults to `True`.
    :param icon: url string or an instance of :class:`Resource` for the default
                 icon to display with the notifications of this notification
                 type.  Defaults to `None`.

    .. note:: In Growl 1.3.3, `icon` does not work.
    """

    def __init__(self, name, display_name=None, enabled=True, icon=None):
        self.name = name
        self.display_name = display_name
        self.enabled = enabled
        self.icon = icon


class Notification(object):
    """Represent notification."""

    def __init__(self, name, title, text='', id_=None, sticky=None,
                 priority=None, icon=None, coalescing_id=None,
                 gntp_callback=None, **socket_callback_options):
        self.name = name
        self.title = title
        self.text = text
        self.id_ = id_
        self.sticky = sticky
        self.priority = priority
        self.icon = icon
        self.coalescing_id = coalescing_id
        self.callback = coerce_to_callback(gntp_callback,
                                           **socket_callback_options)

    @property
    def socket_callback(self):
        if isinstance(self.callback, SocketCallback):
            return self.callback


class BaseRequest(object):
    """Abstract base class for GNTP request.

    :param custom_headers: the list of key-value tuples for Custom Headers.
    :param app_specific_headers: the list of key-value tuples for App-Specific
                                 Headers.
    """
    #: Request message type.  Subclasses must override this attribute.
    message_type = None

    def __init__(self, custom_headers=None, app_specific_headers=None):
        self.custom_headers = custom_headers or []
        self.app_specific_headers = app_specific_headers or []

    def write_into(self, writer):
        """Subclasses must call this method first to serialize their
        message."""
        writer.write_base_request(self)


class RegisterRequest(BaseRequest):
    """Represent ``REGISTER`` request.

    :param app_name: the name of the application.
    :param app_icon: url string or an instance of :class:`Resource` for the
                     icon of the application.
    :param events: the list of :class:`Event` instances.
    :param custom_headers: the list of key-value tuples for Custom Headers.
    :param app_specific_headers: the list of key-value tuples for App-Specific
                                 Headers.

    .. note:: In Growl 1.3.3, `app_icon` of url string does not work.
    """
    message_type = 'REGISTER'

    def __init__(self, app_name, app_icon, events, custom_headers=None,
                 app_specific_headers=None):
        BaseRequest.__init__(self, custom_headers, app_specific_headers)
        self.app_name = app_name
        self.app_icon = app_icon
        self.events = events

    def write_into(self, writer):
        BaseRequest.write_into(self, writer)
        writer.write_register_request(self)


class NotifyRequest(BaseRequest):
    """Represent ``NOTIFY`` request.

    :param app_name: the name of the application.
    :param notification: :class:`Notification` instance.
    :param custom_headers: the list of key-value tuples for Custom Headers.
    :param app_specific_headers: the list of key-value tuples for App-Specific
                                 Headers.
    """
    message_type = 'NOTIFY'

    def __init__(self, app_name, notification, custom_headers=None,
                 app_specific_headers=None):
        BaseRequest.__init__(self, custom_headers, app_specific_headers)
        self.app_name = app_name
        self.notification = notification

    def write_into(self, writer):
        BaseRequest.write_into(self, writer)
        writer.write_notify_request(self)


class SubscribeRequest(BaseRequest):
    """Represent ``SUBSCRIBE`` request.

    :param id_: the unique id of the subscriber.
    :param name: the name of the subscriber.
    :param port: the port number of the subscriber.
    :param custom_headers: the list of key-value tuples for Custom Headers.
    :param app_specific_headers: the list of key-value tuples for App-Specific
                                 Headers.
    """
    message_type = 'SUBSCRIBE'

    def __init__(self, id_, name, port, custom_headers=None,
                 app_specific_headers=None):
        BaseRequest.__init__(self, custom_headers, app_specific_headers)
        self.id_ = id_
        self.name = name
        self.port = port

    def write_into(self, writer):
        BaseRequest.write_into(self, writer)
        writer.write_subscribe_request(self)


class Response(object):
    """Base class for GNTP response.

    :param message_type: <messagetype> of the response.  `'-OK'`, `'-ERROR'` or
                         `'-CALLBACK'`.
    :param headers: headers of the response.
    """

    def __init__(self, message_type, headers):
        self.message_type = message_type
        self.headers = headers


class BaseGNTPConnection(object):
    """Abstract base class for GNTP connection."""

    def __init__(self, final_callback, socket_callback=None):
        self.final_callback = final_callback
        self.socket_callback = socket_callback

    def on_ok_message(self, message):
        r"""Callback for ``-OK`` response.

        :param message: string of response terminated by `'\\r\\n\\r\\n'`.
        """
        try:
            response = parse_response(message, '-OK')
            if self.socket_callback is not None:
                self.read_message(self.on_callback_message)
        finally:
            if self.socket_callback is None:
                self.close()
        if self.socket_callback is None and self.final_callback is not None:
            self.final_callback(response)

    def on_callback_message(self, message):
        r"""Callback for ``-CALLBACK`` response.

        :param message: string of response terminated by `'\\r\\n\\r\\n'`.
        """
        try:
            response = parse_response(message, '-CALLBACK')
            callback_result = self.socket_callback(response)
        finally:
            self.close()
        if self.final_callback is not None:
            self.final_callback(callback_result)

    def write_message(self, message):
        """Subclasses must override this method to send a message to the GNTP
        server."""
        raise NotImplementedError

    def read_message(self, callback):
        """Subclasses must override this method to receive a message from the
        GNTP server."""
        raise NotImplementedError

    def close(self):
        """Subclasses must override this method to close the connection with
        the GNTP server."""
        raise NotImplementedError


class GNTPConnection(BaseGNTPConnection):
    """Represent the connection with the GNTP server."""

    def __init__(self, address, timeout, final_callback, socket_callback=None):
        BaseGNTPConnection.__init__(self, final_callback, socket_callback)
        self.sock = socket.create_connection(address, timeout=timeout)

    def write_message(self, message):
        """Send the request message to the GNTP server."""
        self.sock.send(message)

    def read_message(self, callback):
        """Read a message from opened socket and run callback with it."""
        message = next(generate_messages(self.sock))
        callback(message)

    def close(self):
        """Close the socket."""
        self.sock.close()
        self.sock = None


class GNTPClient(object):
    """GNTP client.

    :param host: host of GNTP server.  Defaults to `'localhost'`.
    :param port: port of GNTP server.  Defaults to `23053`.
    :param timeout: timeout in seconds.  Defaults to `10`.
    :param password: the password used in creating the key.
    :param key_hashing: the type of hash algorithm used in creating the key.
                        It is `keys.MD5`, `keys.SHA1`, `keys.SHA256` or
                        `keys.SHA512`.  Defaults to `keys.SHA256`.
    :param encryption: the tyep of encryption algorithm used.
                       It is `None`, `ciphers.AES`, `ciphers.DES` or
                       `ciphers.3DES`.  `None` means no encryption.
                       Defaults to `None`.
    :param connection_class: GNTP connection class.  If it is `None`,
                             :class:`GNTPConnection` is used.  Defaults to
                             `None`.
    """

    def __init__(self, host='localhost', port=DEFAULT_PORT,
                 timeout=DEFAULT_TIMEOUT, password=None,
                 key_hashing=keys.SHA256, encryption=None,
                 connection_class=None):
        self.address = (host, port)
        self.timeout = timeout
        self.connection_class = connection_class or GNTPConnection
        if (encryption is not None and
            encryption.key_size > key_hashing.key_size):
            raise GNTPError('key_hashing key size (%s:%d) must be at'
                            ' least encryption key size (%s:%d)' % (
                    key_hashing.algorithm_id, key_hashing.key_size,
                    encryption.algorithm_id, encryption.key_size))
        self.packer_factory = MessagePackerFactory(password, key_hashing,
                                                   encryption)

    def process_request(self, request, callback, **kwargs):
        """Process a request.

        :param callback: the final callback run after closing connection.
        """
        packer = self.packer_factory.create()
        message = packer.pack(request)
        conn = self._connect(callback, **kwargs)
        conn.write_message(message)
        conn.read_message(conn.on_ok_message)

    def _connect(self, final_callback, **kwargs):
        """Connect to the GNTP server and return the connection."""
        return self.connection_class(self.address, self.timeout,
                                     final_callback, **kwargs)


def generate_messages(sock, size=1024):
    """Generate messages from opened socket."""
    buf = b''
    while True:
        buf += sock.recv(size)
        if not buf:
            break
        pos = buf.find(MESSAGE_DELIMITER)
        if ((pos < 0 and len(buf) >= MAX_MESSAGE_SIZE) or
            (pos > MAX_MESSAGE_SIZE - MESSAGE_DELIMITER_SIZE)):
            raise GNTPError('too large message: %r' % buf)
        elif pos > 0:
            pos += 4
            yield buf[:pos]
            buf = buf[pos:]


def parse_response(message, expected_message_type=None):
    """Parse response and return response object."""
    try:
        lines = [line for line in message.split(LINE_DELIMITER) if line]
        _, message_type = parse_information_line(lines.pop(0))
        if (expected_message_type is not None and
            expected_message_type != message_type):
            raise GNTPError('%s is not expected message type %s' % (
                    message_type, expected_message_type))

        headers = dict([s.strip().decode('utf-8') for s in line.split(b':', 1)]
                       for line in lines)
        if message_type == '-ERROR':
            raise GNTPError('%s: %s' % (headers['Error-Code'],
                                        headers['Error-Description']))
        return Response(message_type, headers)
    except ValueError as exc:
        raise GNTPError(exc.args[0], 'original message: %r' % message)
    except GNTPError as exc:
        exc.args = (exc.args[0], 'original message: %r' % message)
        raise exc


def parse_information_line(line):
    """Parse information line and return tuple (`<version>`,
    `<messagetype>`)."""
    matched = RESPONSE_INFORMATION_LINE_RE.match(line)
    if matched is None:
        raise GNTPError('invalid information line: %r' % line)
    version, message_type = [s.decode('utf-8') for s in matched.groups()]
    if version not in SUPPORTED_VERSIONS:
        raise GNTPError("version '%s' is not supported" % version)
    return version, message_type


def coerce_to_events(items):
    """Coerce the list of the event definitions to the list of :class:`Event`
    instances."""
    results = []
    for item in items:
        if isinstance(item, (bytes, text_type)):
            results.append(Event(item, enabled=True))
        elif isinstance(item, tuple):
            name, enabled = item
            results.append(Event(name, enabled=enabled))
        elif isinstance(item, Event):
            results.append(item)
    return results


class Resource(object):
    """Class for <uniqueid> data types.

    :param data: the binary content.
    """

    def __init__(self, data):
        self.data = data
        self._unique_value = None

    def unique_value(self):
        """Return the <uniquevalue> value."""
        if self.data is not None and self._unique_value is None:
            self._unique_value = \
                hashlib.md5(self.data).hexdigest().encode('utf-8')
        return self._unique_value

    def unique_id(self):
        """Return the <uniqueid> value."""
        if self.data is not None:
            return b'x-growl-resource://' + self.unique_value()


class RawIcon(Resource):
    """Deprecated icon class."""

    def __init__(self, data):
        import warnings
        warnings.warn('RawIcon is deprecated, use Resource instead',
                      DeprecationWarning, stacklevel=2)
        Resource.__init__(self, data)


class SocketCallback(object):
    """Base class for socket callback.

    Each of the callbacks takes one positional argument, which is
    :class:`Response` instance.

    :param context: value of ``Notification-Callback-Context``.
                    Defaults to ``'None'``.
    :param context-type: value of ``Notification-Callback-Context-Type``.
                         Defaults to ``'None'``.
    :param on_click: the callback run at ``CLICKED`` callback result.
    :param on_close: the callback run at ``CLOSED`` callback result.
    :param on_timeout: the callback run at ``TIMEDOUT`` callback result.

    .. note:: TIMEDOUT callback does not occur in my Growl 1.3.3.
    """

    def __init__(self, context='None', context_type='None',
                 on_click=None, on_close=None, on_timeout=None):
        self.context = context
        self.context_type = context_type
        self.on_click_callback = on_click
        self.on_close_callback = on_close
        self.on_timeout_callback = on_timeout

    def on_click(self, response):
        """Run ``CLICKED`` event callback."""
        if self.on_click_callback is not None:
            return self.on_click_callback(response)

    def on_close(self, response):
        """Run ``CLOSED`` event callback."""
        if self.on_close_callback is not None:
            return self.on_close_callback(response)

    def on_timeout(self, response):
        """Run ``TIMEDOUT`` event callback."""
        if self.on_timeout_callback is not None:
            return self.on_timeout_callback(response)

    def __call__(self, response):
        """This is the callback.  Delegate to ``on_`` methods depending on
        ``Notification-Callback-Result`` value.

        :param response: :class:`Response` instance.
        """
        callback_result = response.headers['Notification-Callback-Result']
        delegate_map = {
            'CLICKED': self.on_click, 'CLICK': self.on_click,
            'CLOSED': self.on_close, 'CLOSE': self.on_close,
            'TIMEDOUT': self.on_timeout, 'TIMEOUT': self.on_timeout,
            }
        return delegate_map[callback_result](response)

    def write_into(self, writer):
        writer.write_socket_callback(self)


class URLCallback(object):
    """Class for url callback."""

    def __init__(self, url):
        self.url = url

    def write_into(self, writer):
        writer.write_url_callback(self)


def coerce_to_callback(gntp_callback=None, **socket_callback_options):
    """Return :class:`URLCallback` instance for url callback or
    :class:`SocketCallback` instance for socket callback.

    If `gntp_callback` is not `None`, `socket_callback_options` must be empty.
    Moreover, if `gntp_callback` is string, then a instance of
    :class:`URLCallback` is returned.  Otherwise, `gntp_callback` is returned
    directly.

    If `gntp_callback` is `None` and `socket_callback_options` is not empty,
    new instance of :class:`SocketCallback` is created from given keyword
    arguments and it is returned.  Acceptable keyword arguments are same as
    constructor's of :class:`SocketCallback`.
    """
    if gntp_callback is not None:
        if socket_callback_options:
            raise GNTPError('If gntp_callback is not None,'
                            ' socket_callback_options must be empty')
        if isinstance(gntp_callback, (bytes, text_type)):
            return URLCallback(gntp_callback)
        else:
            return gntp_callback
    if socket_callback_options:
        return SocketCallback(**socket_callback_options)


class _NullCipher(object):
    """Null object for the encryption of messages."""

    algorithm = None
    algorithm_id = 'NONE'
    encrypt = lambda self, text: text
    decrypt = lambda self, text: text
    __bool__ = lambda self: False
    __nonzero__ = __bool__


NullCipher = _NullCipher()


class MessagePackerFactory(object):
    """The factory of :class:`MessagePacker`.

    If `password` is None, `hashing` and `encryption` are ignored.
    """

    def __init__(self, password=None, hashing=keys.SHA256, encryption=None):
        self.password = password
        self.hashing = password and hashing
        self.encryption = (password and encryption) or NullCipher

    def create(self):
        """Create an instance of :class:`MessagePacker` and return it."""
        key = self.password and self.hashing.key(self.password)
        cipher = self.encryption and self.encryption.cipher(key)
        return MessagePacker(key, cipher)


class MessagePacker(object):
    """The serializer for messages.

    `key` and `cipher` have random-generated salt and iv respectively.

    :param key: an instance of :class:`keys.Key`.
    :param cipher: an instance of :class:`ciphers.Cipher` or `NullCipher`.
    """

    def __init__(self, key=None, cipher=None):
        self.key = key
        self.cipher = cipher or NullCipher

    def pack(self, request):
        """Return utf-8 encoded request message."""
        return (InformationLinePacker(self.key, self.cipher).pack(request) +
                LINE_DELIMITER +
                HeaderPacker(self.cipher).pack(request) +
                SectionPacker(self.cipher).pack(request) +
                LINE_DELIMITER)


class InformationLinePacker(object):

    def __init__(self, key, cipher):
        self.key = key
        self.cipher = cipher

    def pack(self, request):
        """Return utf-8 encoded information line."""
        result = (b'GNTP/1.0 ' +
                  request.message_type.encode('utf-8') +
                  b' ' +
                  self.cipher.algorithm_id.encode('utf-8'))
        if self.cipher.algorithm is not None:
            result += b':' + self.cipher.iv_hex
        if self.key is not None:
            result += (b' ' +
                       self.key.algorithm_id.encode('utf-8') +
                       b':' +
                       self.key.key_hash_hex +
                       b'.' +
                       self.key.salt_hex)
        return result


class HeaderPacker(object):

    def __init__(self, cipher):
        self.writer = io.BytesIO()
        self.cipher = cipher

    def pack(self, request):
        """Return utf-8 encoded headers."""
        request.write_into(self)
        headers = self.writer.getvalue()
        result = self.cipher.encrypt(headers)
        if self.cipher.algorithm is not None:
            result += LINE_DELIMITER
        return result

    def write_base_request(self, request):
        self._write_additional_headers(request.custom_headers,
                                       CUSTOM_HEADER_PREFIX)
        self._write_additional_headers(request.app_specific_headers,
                                       APP_SPECIFIC_HEADER_PREFIX)

    def _write_additional_headers(self, headers, prefix):
        for key, value in headers:
            if not key.startswith(prefix):
                key = prefix + key
            self.write(key.encode('utf-8'), value)

    def write_register_request(self, request):
        self.write(b'Application-Name', request.app_name)
        self.write(b'Application-Icon', request.app_icon)
        self.write(b'Notifications-Count', len(request.events))
        for event in request.events:
            self.writer.write(LINE_DELIMITER)
            self.write(b'Notification-Name', event.name)
            self.write(b'Notification-Display-Name', event.display_name)
            self.write(b'Notification-Enabled', event.enabled)
            self.write(b'Notification-Icon', event.icon)

    def write_notify_request(self, request):
        self.write(b'Application-Name', request.app_name)
        self._write_notification(request.notification)

    def write_subscribe_request(self, request):
        self.write(b'Subscriber-ID', request.id_)
        self.write(b'Subscriber-Name', request.name)
        self.write(b'Subscriber-Port', request.port)

    def _write_notification(self, notification):
        self.write(b'Notification-Name', notification.name)
        self.write(b'Notification-ID', notification.id_)
        self.write(b'Notification-Title', notification.title)
        self.write(b'Notification-Text', notification.text)
        self.write(b'Notification-Sticky', notification.sticky)
        self.write(b'Notification-Priority', notification.priority)
        self.write(b'Notification-Icon', notification.icon)
        self.write(b'Notification-Coalescing-ID', notification.coalescing_id)
        if notification.callback is not None:
            notification.callback.write_into(self)

    def write_socket_callback(self, callback):
        self.write(b'Notification-Callback-Context', callback.context)
        self.write(b'Notification-Callback-Context-Type',
                   callback.context_type)

    def write_url_callback(self, callback):
        self.write(b'Notification-Callback-Target', callback.url)

    def write(self, name, value):
        """Write utf-8 encoded header into writer.

        :param name: the name of the header.
        :param value: the value of the header.
        """
        if isinstance(value, Resource):
            value = value.unique_id()
        if value is not None:
            if not isinstance(value, bytes):
                value = text_type(value).encode('utf-8')
            self.writer.write(name)
            self.writer.write(b': ')
            self.writer.write(value)
            self.writer.write(LINE_DELIMITER)


class SectionPacker(object):

    def __init__(self, cipher):
        self.writer = io.BytesIO()
        self.cipher = cipher

    def pack(self, request):
        """Return utf-8 encoded message body."""
        request.write_into(self)
        return self.writer.getvalue()

    def write_base_request(self, request):
        for _, value in request.custom_headers:
            self.write(value)
        for _, value in request.app_specific_headers:
            self.write(value)

    def write_register_request(self, request):
        self.write(request.app_icon)
        for event in request.events:
            self.write(event.icon)

    def write_notify_request(self, request):
        self.write(request.notification.icon)

    def write_subscribe_request(self, request):
        pass

    def write(self, resource):
        """Write utf-8 encoded resource into writer.

        :param headers: the iterable of (`name`, `value`) tuple of the header.
        :param body: bytes of section body.
        """
        if isinstance(resource, Resource) and resource.data is not None:
            data = self.cipher.encrypt(resource.data)
            self.writer.write(SECTION_DELIMITER)
            self.writer.write(b'Identifier: ')
            self.writer.write(resource.unique_value())
            self.writer.write(LINE_DELIMITER)
            self.writer.write(b'Length: ')
            self.writer.write(text_type(len(data)).encode('utf-8'))
            self.writer.write(LINE_DELIMITER)
            self.writer.write(SECTION_BODY_START)
            self.writer.write(data)
            self.writer.write(SECTION_BODY_END)
