import sys
import types
import atexit
import linecache
import importlib
import traceback


class NotErrorsClient:
    origin_excepthook = sys.excepthook
    instance = False

    def __init__(self, project_token, auth_key, type='basic', host=None):
        address = host or 'http://noterrors.com'
        module = importlib.import_module('noterrors_sdk.integrations.%s' % type)
        ClientCls = getattr(module, type.capitalize() + 'Client')
        self.client = ClientCls(address, project_token, auth_key)

    @classmethod
    def init(cls, project_token, auth_key, type='basic', host=None):
        self = cls(project_token, auth_key, type, host)
        if not cls.instance:
            cls.instance = self
            sys.excepthook = cls.excepthook
        atexit.register(cls.sync_all)
        return self

    @classmethod
    def sync_all(cls):
        pass

    @classmethod
    def excepthook(cls, type, value, traceback):
        cls.instance._handle_exception(type, value, traceback, handled=False, level='error')
        cls.origin_excepthook(type, value, traceback)

    def _check_value(self, value):
        if isinstance(value, (types.ModuleType, types.FunctionType, types.BuiltinFunctionType, types.BuiltinMethodType)):
            return False
        if str(value).startswith('<class'):
            return False
        return True

    def beautify(self, value):
        if value is None or isinstance(value, (int, float, bool)):
            return value
        if isinstance(value, str):
            return value[:300]
        if isinstance(value, (bytes, bytearray)):
            return value.decode(errors='ignore')[:300]
        if isinstance(value, (Exception,)):
            return str(value)
        return repr(value)

    def handle_exception(self, level=None, handled=True):
        ex_type, value, traceback = sys.exc_info()
        self._handle_exception(ex_type, value, traceback, level=level, handled=handled)

    def _handle_exception(self, ex_type=None, value=None, _tb=None, level=None, handled=True):
        tb = _tb
        raw_stacktrace = ''.join(traceback.format_exception(ex_type, value, _tb))
        stacktrace = []
        while tb:
            frame = tb.tb_frame
            filename = frame.f_code.co_filename
            line = tb.tb_lineno
            code = linecache.getlines(filename)
            stacktrace.append({
                'method': frame.f_code.co_name,
                'package': frame.f_locals.get('__name__') or frame.f_globals.get('__name__'),
                'filename': filename,
                'line': line,
                'code': {
                    'before': code[line-6: line-1],
                    'line': code[line-1],
                    'after': code[line: line + 5],
                } if code else {},
                'vars': {n: self.beautify(v) for n, v in frame.f_locals.items() if not n.startswith('__') and self._check_value(v)}
            })
            tb = tb.tb_next
        if stacktrace:
            tags = {
                'level': level,
                'handled': handled,
                'server_name': '',
                'runtime': sys.version
            }
            self.capture_message({
                'name': value.__class__.__name__,
                'title': str(value),
                'function': stacktrace[-1]['method'],
                'filename': stacktrace[-1]['filename'],
                'package': stacktrace[-1]['package'],
                'stacktrace': stacktrace,
                'raw_stacktrace': raw_stacktrace,
                'level': level,
                'tags': tags,
                'meta': {
                    'handled': handled,
                    'platform': {
                        'type': sys.platform,
                        'runtime': sys.version
                    },
                    'extra': {
                        'argv': sys.argv
                    }

                }
            }, type='error')

    def capture_message(self, message, type='message'):
        self.client.capture_message(message, type)
