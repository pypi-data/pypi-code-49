# main.py
# (C) 2020 Masato Kokubo
from abc import abstractmethod
import configparser
import datetime
import inspect
import logging
from logging import config
import os
import sys
import traceback
from debugtrace import _print as pr

_DO_NOT_OUTPUT = 'Do not output'

_config_path = './' + __package__ + '.ini'
_config = configparser.ConfigParser()
if os.path.exists(_config_path):
    _config.read(_config_path)

def _get_config_value(key: str, fallback: object) -> object:
    value = fallback
    try:
        if type(fallback) == bool:
            value = _config.getboolean(__package__, key, fallback=fallback)
        elif type(fallback) == int:
            value = _config.getint(__package__, key, fallback=fallback)
        else:
            value = _config.get(__package__, key, fallback=fallback)
            value = value.replace('\\s', ' ')

    except BaseException as ex:
        pr._print('debugtrace: (' + _config_path + ') key: ' + key + ', error: '  + str(ex), sys.stderr)

    return value

_logger_name                  = _get_config_value('logger'                      , 'stderr'                  ).lower()
_logging_config_file          = _get_config_value('logging_config_file'         , 'logging.conf'            )
_logging_logger_name          = _get_config_value('logging_logger_name'         , __package__               )
_logging_level                = _get_config_value('logging_level'               , 'DEBUG'                   ).upper()
_is_enabled                   = _get_config_value('is_enabled'                  , True                      )
_enter_string                 = _get_config_value('enter_string'                , 'Enter'                   )
_leave_string                 = _get_config_value('leave_string'                , 'Leave'                   )
_limit_string                 = _get_config_value('limit_string'                , '...'                     )
_maximum_indents              = _get_config_value('maximum_indents'             , 20                        )
_code_indent_string           = _get_config_value('code_indent_string'          , '|   '                    )
_data_indent_string           = _get_config_value('data_indent_string'          , '  '                      )
_non_output_string            = _get_config_value('non_output_string'           , '...'                     )
_cyclic_reference_string      = _get_config_value('cyclic_reference_string'     , '*** Cyclic Reference ***')
_varname_value_separator      = _get_config_value('varname_value_separator'     , ' = '                     )
_key_value_separator          = _get_config_value('key_value_separator'         , ': '                      )
_log_datetime_format          = _get_config_value('log_datetime_format'         , '%Y-%m-%d %H:%M:%S.%f'    )
_enter_format                 = _get_config_value('enter_format'                , '{0} ({1}:{2})'           )
_leave_format                 = _get_config_value('leave_format'                , '{0} ({1}:{2}) time: {3}' )
_count_format                 = _get_config_value('count_format'                , 'count:{}'                )
_minimum_output_count         = _get_config_value('minimum_output_count'        , 5                         )
_length_format                = _get_config_value('length_format'               , 'length:{}'               )
_minimum_output_length        = _get_config_value('minimum_output_length'       , 5                         )
_maximum_data_output_width    = _get_config_value('maximum_data_output_width'   , 80                        )
_bytes_count_in_line          = _get_config_value('bytes_count_in_line'         , 16                        )
_collection_limit             = _get_config_value('collection_limit'            , 256                       )
_string_limit                 = _get_config_value('string_limit'                , 2048                      )
_bytes_limit                  = _get_config_value('bytes_limit'                 , 512                       )
_reflection_nest_limit        = _get_config_value('reflection_nest_limit'       , 4                         )

class _LoggerBase(object):
    @abstractmethod
    def print(self, message: str) -> None:
        pass

class _Std(_LoggerBase):
    def __init__(self, iostream):
        self.iostream = iostream
    
    def print(self, message: str) -> None:
        pr._print(datetime.datetime.now().strftime(_log_datetime_format) + ' ' + message, self.iostream)

class StdOut(_Std):
    def __init__(self):
        super().__init__(sys.stdout)

    def __str__(self):
        return 'sys.stsdout'

class StdErr(_Std):
    def __init__(self):
        super().__init__(sys.stderr)

    def __str__(self):
        return 'sys.stderr'

class Logger(_LoggerBase):
    def __init__(self):
        if os.path.exists(_logging_config_file):
            config.fileConfig(_logging_config_file)
        else:
            pr._print('debugtrace: (' + _config_path + ') _logging_config_file = ' + _logging_config_file + \
                ' (Not found)', sys.stderr)

        self.logger = logging.getLogger(_logging_logger_name)
        self._logging_level = \
            logging.CRITICAL if _logging_level == 'CRITICAL' else \
            logging.ERROR    if _logging_level == 'ERROR'    else \
            logging.WARNING  if _logging_level == 'WARNING'  else \
            logging.INFO     if _logging_level == 'INFO'     else \
            logging.DEBUG    if _logging_level == 'DEBUG'    else \
            logging.NOTSET   if _logging_level == 'NOTSET'   else \
            logging.DEBUG

    def print(self, message: str) -> None:
        self.logger.log(self._logging_level, message)

    def __str__(self):
        return "logging.Logger('" + _logging_logger_name + "'), logging level: " + _logging_level

_logger = StdErr()
if _logger_name == 'stdout':
    _logger = StdOut()
elif _logger_name == 'stderr':
    _logger = StdErr()
elif _logger_name == 'logger':
    _logger = Logger()
else:
    pr._print('debugtrace: (' + _config_path + ') logger = ' + _logger_name + ' (Unknown)', sys.stderr)

_code_nest_level     = 0
_previous_nest_level = 0
_data_nest_level     = 0
_last_print_strings  = []
_reflected_objects   = []

def _up_nest() -> None:
    global _previous_nest_level
    global _code_nest_level

    _previous_nest_level = _code_nest_level
    _code_nest_level += 1

def _down_nest() -> None:
    global _previous_nest_level
    global _code_nest_level

    _previous_nest_level = _code_nest_level
    _code_nest_level -= 1

def _get_indent_string() -> str:
    return _code_indent_string * min(max(0, _code_nest_level), _maximum_indents)

def _get_data_indent_string() -> str:
    return _data_indent_string * min(max(0, _data_nest_level), _maximum_indents)

def _to_strings(name: str,
        value: object,
        force_reflection: bool,
        output_private: bool,
        output_method: bool) -> list:
    strings = []
    string = name + _varname_value_separator if name != '' else ''
    if isinstance(value, type(None)):
        # None
        string += 'None'

    elif isinstance(value, str):
        # str
        strings = _to_strings_str(value)

    elif isinstance(value, bytes) or isinstance(value, bytearray):
        # str
        strings = _to_strings_bytes(value)

    elif isinstance(value, int) or isinstance(value, float) or \
        isinstance(value, datetime.date) or isinstance(value, datetime.time) or \
        isinstance(value, datetime.datetime):
        # int, float, datetime.date, datetime.time, datetime.datetime
        string += str(value)

    elif isinstance(value, list) or \
            isinstance(value, set) or isinstance(value, frozenset) or \
            isinstance(value, tuple) or \
            isinstance(value, dict):
        # list, set, frozenset, tuple, dict
        strings = _to_strings_iterator(value, force_reflection, output_private, output_method)

    else:
        has_str, has_repr = _has_str_repr_method(value)
        if not force_reflection and (has_str or has_repr):
            # has __str__ or __repr__ method
            if has_repr:
                string += 'repr(): '
                string += repr(value)
            else:
                string += 'str(): '
                string += str(value)

        else:
            # use refrection
            if any(map(lambda obj: value is obj, _reflected_objects)):
                # cyclic reference
                strings.append(_cyclic_reference_string)
            elif len(_reflected_objects) > _reflection_nest_limit:
                # over reflection level limitation
                strings.append(_limit_string)
            else:
                _reflected_objects.append(value)
                strings = _to_strings_using_refrection(value, force_reflection, output_private, output_method)
                _reflected_objects.pop()

    if len(string) > 0:
        if len(strings) > 0:
            strings[0] = string + strings[0]
        else:
            strings.append(string)
    return strings

def _to_strings_str(value: str) -> list:
    has_single_quote = False
    has_double_quote = False
    single_quote_str = ''
    if len(value) >= _minimum_output_length:
        single_quote_str += '('
        single_quote_str += _length_format.format(len(value))
        single_quote_str += ')'
    double_quote_str = single_quote_str
    single_quote_str += "'"
    double_quote_str += '"'
    count = 1
    for char in value:
        if count > _string_limit:
            single_quote_str += _limit_string
            double_quote_str += _limit_string
            break
        if char == "'":
            single_quote_str += "\\'"
            double_quote_str += char
            has_single_quote = True
        elif char == '"':
            single_quote_str += char
            double_quote_str += '\\"'
            has_double_quote = True
        elif char == '\\':
            single_quote_str += '\\\\'
            double_quote_str += '\\\\'
        elif char == '\n':
            single_quote_str += '\\n'
            double_quote_str += '\\n'
        elif char == '\r':
            single_quote_str += '\\r'
            double_quote_str += '\\r'
        elif char == '\t':
            single_quote_str += '\\t'
            double_quote_str += '\\t'
        elif char < ' ':
            num_str = format(ord(char), '02X')
            single_quote_str += '\\x' + num_str
            double_quote_str += '\\x' + num_str
        else:
            single_quote_str += char
            double_quote_str += char
        count += 1

    double_quote_str += '"'
    single_quote_str += "'"
    if has_single_quote and not has_double_quote:
        return [double_quote_str]
    return [single_quote_str]

def _to_strings_bytes(value: bytes) -> list:
    global _data_nest_level
    global _bytes_limit

    bytes_length = len(value)
    strings = []
    string = '('
    if type(value) == bytes:
        string += 'bytes '
    elif type(value) == bytearray:
        string += 'bytearray '
    if bytes_length >= _minimum_output_length:
        string += _length_format.format(bytes_length)
    string += ')['
    chars = ''

    _data_nest_level += 1
    indent_string = _get_data_indent_string()
    multi_lines = bytes_length >= _bytes_count_in_line
    count = 0
    for element in value:
        if count % _bytes_count_in_line == 0:
            if multi_lines:
                string += '  '
                string += chars
                strings.append(string)
                string = indent_string
                chars = ''
        else:
            string += ' '
        if (count >= _bytes_limit):
            string += _limit_string
            break
        string += '{:02X}'.format(element)
        chars += chr(element) if element >= 0x20 and element <= 0x7E else '.'
        count += 1

    if multi_lines:
        # padding
        full_length = len(indent_string) + 3 * _bytes_count_in_line - 1
        string += ' ' * (full_length - len(string))
    string += '  '
    string += chars

    _data_nest_level -= 1
    if multi_lines:
        strings.append(string)
        string = _get_data_indent_string()
    string += ']'
    strings.append(string)

    return strings

def _to_strings_using_refrection(value: object,
        force_reflection: bool,
        output_private: bool,
        output_method: bool) -> list:
    global _data_nest_level

    members = []
    try:
        base_members = inspect.getmembers(value,
            lambda v: not inspect.isclass(v) and
                (output_method or not inspect.ismethod(v)) and
                not inspect.isbuiltin(v))

        members = [m for m in base_members
                if (not m[0].startswith('__') or not m[0].endswith('__')) and
                    (output_private or not m[0].startswith('_'))]
    except BaseException as ex:
        return [str(ex)]

    strings = []
    _data_nest_level += 1
    indent_string = _get_data_indent_string()

    string = _get_type_name(value)
    string += '{'

    member_index = 0
    line_breaked = False
    string_backup = string
    for member in members:
        name = member[0]
        value_strings = _to_strings('', member[1], force_reflection, output_private, output_method)

        if not line_breaked and len(value_strings) > 1:
            # multi line value strings
            strings.append(string)
            string = indent_string
            line_breaked = True

        string_backup2 = string
        string += name
        string += _key_value_separator

        value_index = 0
        for value_string in value_strings:
            if value_index == 0:
                string += value_string
            else:
                strings.append(string)
                string = value_string

            if not line_breaked and len(string) > _maximum_data_output_width:
                if len(strings) == 0:
                    # first line break
                    strings.append(string_backup)
                    right_string = string[len(string_backup):]
                    string = indent_string
                    string += right_string
                else:
                    strings.append(string_backup2)
                    string = indent_string
                    string += name
                    string += _key_value_separator
                    string += value_string
            value_index += 1

        if member_index < len(members) - 1:
            string += ', '
        line_breaked = False
        member_index += 1

    _data_nest_level -= 1
    if not line_breaked and len(strings) > 0:
        strings.append(string)
        string = _get_data_indent_string()
    string += '}'
    strings.append(string)

    return strings

def _to_strings_iterator(values: object,
        force_reflection: bool,
        output_private: bool,
        output_method: bool) -> list:
    global _data_nest_level

    open_char = '{' # set, frozenset, dict
    close_char = '}'
    if isinstance(values, list):
        # list
        open_char = '['
        close_char = ']'
    elif isinstance(values, tuple):
        # tuple
        open_char = '('
        close_char = ')'
    
    strings = []
    _data_nest_level += 1
    indent_string = _get_data_indent_string()

    string = _get_type_name(values, len(values))
    string += open_char

    element_index = 0
    line_breaked = False
    string_backup = string
    for element in values:
        if element_index >= _collection_limit:
            string += _limit_string
            break

        value_strings = []
        if isinstance(values, dict):
            # dictionary
            value_strings = _to_strings_keyvalue(element, values[element], force_reflection, output_private, output_method)
        else:
            # list, set, frozenset or tuple
            value_strings = _to_strings('', element, force_reflection, output_private, output_method)

        if not line_breaked and len(value_strings) > 1:
            # multi line element strings
            strings.append(string)
            string = indent_string
            line_breaked = True

        string_backup2 = string

        value_index = 0
        for value_string in value_strings:
            if value_index == 0:
                string += value_string
            else:
                strings.append(string)
                string = value_string

            if not line_breaked and len(string) > _maximum_data_output_width:
                if len(strings) == 0:
                    # first line break
                    strings.append(string_backup)
                    right_string = string[len(string_backup):]
                    string = indent_string
                    string += right_string
                else:
                    strings.append(string_backup2)
                    string = indent_string
                    string += value_string

            value_index += 1

        if element_index < len(values) - 1:
            string += ', '
        line_breaked = False
        element_index += 1

    _data_nest_level -= 1
    if not line_breaked and len(strings) > 0:
        strings.append(string)
        string = _get_data_indent_string()
    string += close_char
    strings.append(string)

    return strings

def _to_strings_keyvalue(key: object, value: object,
        force_reflection: bool,
        output_private: bool,
        output_method: bool) -> list:
    global _data_nest_level

    strings = []
    string = ''
    key_strings = _to_strings('', key, force_reflection, output_private, output_method)
    value_strings = _to_strings('', value, force_reflection, output_private, output_method)

    # key
    indent_string = _get_data_indent_string()
    index = 0
    for key_string in key_strings:
        string += key_string
        if index < len(key_strings) - 1:
            # not last
            strings.append(string)
            string = indent_string
        index += 1

    string += _key_value_separator

    # value
    _data_nest_level += 1
    indent_string = _get_data_indent_string()
    index = 0
    for value_string in value_strings:
        string += value_string
        if index < len(value_strings) - 1:
            # not last
            strings.append(string)
            string = indent_string
        index += 1
    _data_nest_level -= 1

    strings.append(string)
    return strings

def _get_type_name(value: object, count: int = -1) -> str:
    type_name = '('
    type_name += _get_simple_type_name(type(value), 0)

    if count >= _minimum_output_count:
        type_name += ' ' + _count_format.format(count)
    type_name += ')'
    return type_name

def _get_simple_type_name(value_type: type, nest: int) -> str:
    type_name = str(value_type) if nest == 0 else value_type.__name__
    if type_name.startswith("<class '"):
        type_name = type_name[8:]
    elif type_name.startswith("<enum '"):
        type_name = 'enum ' + type_name[7:]
    if type_name.endswith("'>"):
        type_name = type_name[:-2]

    base_names = list(
        map(lambda base: _get_simple_type_name(base, nest + 1),
        filter(lambda base: base != object,
            value_type.__bases__)))

    if len(base_names) > 0:
        type_name += '('
        type_name += ', '.join(base_names)
        type_name += ')'

    return type_name

def _has_str_repr_method(value: object) -> (bool, bool):
    try:
        members = inspect.getmembers(value, lambda v: inspect.ismethod(v))
        return (
            len([member for member in members if member[0] == '__str__']) != 0,
            len([member for member in members if member[0] == '__repr__']) != 0
        )
    except:
        return False

def print(name: str, value: object = _DO_NOT_OUTPUT, *,
        force_reflection: bool = False,
        output_private: bool = False,
        output_method: bool = False) -> None:
    '''
    Outputs the name and value.

    Args:
        name: The name of the value (simply output message if the value is omitted)
        value: The value to output if not omitted
        force_reflection: If true, uses reflection even if __str__ method is defined
        output_private: Outputs private member if true
        output_method: Outputs method if true

    The following is in Japanese.
    
    名前と値を出力します。

    引数:
        name: 出力する名前 (valueが省略されている場合は、単に出力するメッセージ)
        value: 出力する値 (省略されていなければ)
        force_reflection: Trueなら __str__ メソッドが定義されていてもリフレクションを使用する
        output_private: Trueならプライベートメンバーも出力する
        output_method: Trueならメソッドも出力する
    '''
    global _data_nest_level
    global _last_print_strings
    global _reflected_objects

    if not _is_enabled: return

    _data_nest_level = 0
    _reflected_objects.clear()

    indent_string = _get_indent_string()
    if value is _DO_NOT_OUTPUT:
        _logger.print(indent_string + name)
    else:
        last_print_lines = len(_last_print_strings)
        _last_print_strings = _to_strings(name, value, force_reflection, output_private, output_method)

        if last_print_lines > 0 and (last_print_lines > 1 or len(_last_print_strings)) > 1:
            _logger.print(indent_string)

        for string in _last_print_strings:
            _logger.print(indent_string + string)

class _DebugTrace(object):
    '''
    Outputs a entering log when initializing
    and outputs an leaving log when deleting.

    The following is in Japanese.

　  初期化時に開始ログを出力し、削除時に終了ログを出力します。
    '''
    __slots__ = ['name', 'filename', 'lineno', 'enter_time']
    
    def __init__(self, invoker: object):
        global _last_print_strings

        if not _is_enabled: return

        if isinstance(invoker, type(None)):
            self.name = ''
        else:
            self.name = type(invoker).__name__
            if self.name == 'type':
                self.name = invoker.__name__
            self.name += '.'

        try:
            raise RuntimeError
        except RuntimeError:
            frame_summary = traceback.extract_stack(limit=3)[0]
            self.name += frame_summary.name
            self.filename = os.path.basename(frame_summary.filename)
            self.lineno = frame_summary.lineno

        indent_string = _get_indent_string()
        if _code_nest_level < _previous_nest_level:
            _logger.print(indent_string)

        _logger.print(indent_string +
            _enter_string + ' ' +
            _enter_format.format(self.name, self.filename, self.lineno)
        )
        _up_nest()
        _last_print_strings = []

        self.enter_time = datetime.datetime.now()

    def __del__(self):
        if not _is_enabled: return

        time = datetime.datetime.now() - self.enter_time
        _down_nest()
        _logger.print(_get_indent_string() +
            _leave_string + ' ' +
            _leave_format.format(self.name, self.filename, self.lineno, time)
        )

def enter(invoker: object=None):
    '''
    By calling this method when entering an execution block such as a function or method,
    outputs a entering log.
    Store the return value in some variable (such as _).
    Outputs a leaving log when leaving the scope of this variable.

    Args
        invoker: The object or class that invoked this method.
    
    Returns:
        An inner class object.

    The following is in Japanese.

    関数やメソッドなどの実行ブロックに入る際にこのメソッドを呼び出す事で、開始のログを出力します。
    戻り値は何かの変数(例えば _)に格納してください。この変数のスコープを出る際に終了のログを出力します。

    引数:
        invoker: このメソッドを呼び出したオブジェクトまたはクラス。
    
    戻り値:
        内部クラスのオブジェクト。
    '''
    return _DebugTrace(invoker)

if _is_enabled:
    from debugtrace import version
    print('DebugTrace-python ' + version.VERSION + ' -> ' + str(_logger))
    print('')
