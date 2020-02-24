import traceback

from .client import NotErrorsClient


_default_client = None
_clients = {}
_config = {}


def _get_client(type=None):
    global _config, _clients, _default_client

    if type:
        client = _clients.get(type)
        if client is None:
            if not _config:
                raise Exception('NotErrors SDK not initialized.')
            kwargs = _config['kwargs']
            kwargs['type'] = type
            client = _clients[type] = NotErrorsClient.init(*_config['args'], **kwargs)
    else:
        client = _default_client
    return client


def capture_message(message, type=None):
    return _get_client(type).capture_message(message)


def handle_exception(type=None):
    try:
        return _get_client(type).handle_exception()
    except:
        tb = traceback.format_exc()
        print('NOTERRORS EXCEPTION:', tb)


def noterrors_init(*args, type='basic', **kwargs):
    global _config, _clients, _default_client

    _config = {'args': args, 'kwargs': {**kwargs, 'type': type}}
    _clients[type] = _default_client = NotErrorsClient.init(*args, type=type, **kwargs)
