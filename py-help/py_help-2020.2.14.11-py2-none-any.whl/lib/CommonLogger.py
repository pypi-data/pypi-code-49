# -*- coding: utf-8 -*-
import re
import copy
import os
import sys  # reload()之前必须要引入模块
import logbook
import traceback
import threading
import better_exceptions
from logbook import lookup_level
from logbook import CRITICAL, ERROR, WARNING, NOTICE, INFO, DEBUG, TRACE, NOTSET
from logbook.more import ColorizedStderrHandler
from logbook.handlers import Handler
from .path_helper import PathHelper
from collections import deque


def from_utf8(string):
    try:
        return string.decode('utf-8')
    except AttributeError:
        return string


def to_utf8(string):
    try:
        if sys.version_info < (3, 0):
            return string.encode('utf-8')
        else:
            return string
    except AttributeError:
        return to_utf8(str(string))
    except UnicodeDecodeError:
        try:
            return to_utf8(unicode(string, 'utf-8'))
        except UnicodeDecodeError:
            return string


class BufferHandler(Handler):
    """缓存到一个buffer的处理器
    """
    log_buf_level_match = {
        DEBUG: 'DEBUG',
        TRACE: 'DEBUG',
        NOTICE: 'DEBUG',
        INFO: 'INFO',
        WARNING: 'WARN',
        ERROR: 'ERROR',
        CRITICAL: 'FATAL',
    }

    def __init__(self, *args, **kwargs):
        buffer_arg = kwargs.get('buffer')
        del kwargs['buffer']
        Handler.__init__(self, *args, **kwargs)
        self.buffered_records = buffer_arg

    def rollover(self):
        self.buffered_records.clear()

    def pop_application(self):
        Handler.pop_application(self)
        self.rollover()

    def pop_thread(self):
        Handler.pop_thread(self)
        self.rollover()

    def pop_greenlet(self):
        Handler.pop_greenlet(self)
        self.rollover()

    def emit(self, record):
        one_log = {'level': self.log_buf_level_match.get(record.level, 0), 'message': self.format(record)}
        self.buffered_records.append(one_log)


class CommonLogger(logbook.Logger):
    """
    所有的日志都通过这个类进行输出
    """

    loggers = {}
    handlers = {
        'all': [
        ],
    }
    buffers = {}
    handlers_init = False
    handlers_init_mark = False
    log_cfg = [
        {
            'name': 'default',
            'file_regex': '.*',
            'out_file': 'default.log',
            'log_level': 'info',
            'stderr_log_level': 'info',
            'stderr_log': False,
            'buffer_log_level': 'info',
            'buffer_size': 1024,
            'buffer_log': False,
        },
        {
            'name': 'py_help_log',
            'file_regex': '.*py_help.*',
            'out_file': 'py_help.log',
            'log_level': 'debug',
            'stderr_log_level': 'debug',
            'stderr_log': True,
            'buffer_log_level': 'info',
            'buffer_size': 1024,
            'buffer_log': False,
        },
    ]
    log_path = None
    log_cfg_init = False
    log_lock = threading.Lock()

    @classmethod
    def set_log_path(cls, log_path):
        cls.log_path = log_path

    @classmethod
    def set_log_level(cls, cfg_name, level):
        for index, cfg in enumerate(cls.log_cfg):
            if cfg['name'] == cfg_name:
                cfg['log_level'] = level

    @classmethod
    def add_log_cfg(cls, log_cfg):
        cls._load_project_log_cfg()
        cls.log_cfg.append(log_cfg)
        cls.__handlers_init(True, False)
        pass

    @staticmethod
    def common_log_format(record, handler):
        if record.calling_frame:
            log_frame = getattr(handler, 'log_frame')
            if log_frame is None:
                log_frame = 2
            target_frame = record.calling_frame.f_back
            for cnt in range(log_frame):
                target_frame = target_frame.f_back
            file_name = target_frame.f_code.co_filename
            func_name = target_frame.f_code.co_name
            file_line = target_frame.f_lineno
        else:
            file_name = "not support fname"
            func_name = ''
            file_line = "0"

        log = "[{time}][{level}][pid:{pid}][th:{thread}] \"{file}:{line}\"[{func}]: {msg}".format(
            level=record.level_name[0],
            msg=to_utf8(record.message),
            thread=record.thread,
            pid=os.getpid(),
            file=file_name,
            func=func_name,
            line=file_line,
            time=record.time,
        )

        if record.formatted_exception:
            log += "\n" + record.formatted_exception
        return log

    @classmethod
    def get_log_path(cls):
        if cls.log_path is None:
            cls.log_path = PathHelper.get_project_log()
        if not os.path.exists(cls.log_path):
            os.makedirs(cls.log_path)
        return cls.log_path

    @classmethod
    def _get_buffer(cls, name, max_len=1024):
        if cls.buffers.get(name) is None:
            cls.buffers[name] = {
                'name': name,
                'buffer': deque(maxlen=max_len)
            }
        return cls.buffers[name]

    @classmethod
    def get_buffer_data(cls, name):
        ret_data = []
        if cls.buffers.get(name) is not None:
            buffer_data = cls._get_buffer(name)
            ret_data.extend(buffer_data.get('buffer'))
        else:
            if name == 'all':
                for (buf_name, buffer_data) in cls.buffers.items():
                    ret_data.extend(buffer_data.get('buffer'))
        return ret_data

    @classmethod
    def _parse_level(cls, level_str):
        level_str = level_str.upper()
        if 'WARN' in level_str:
            return 'WARNING'
        if 'INF' in level_str:
            return 'INFO'
        if 'ERR' in level_str:
            return 'ERROR'
        return level_str

    @classmethod
    def _load_project_log_cfg(cls):
        if not cls.log_cfg_init:
            from .cfg_loader import CfgLoader
            cls.log_cfg_init = True
            log_cfg = CfgLoader.get_project_cfg('log.yml')
            if log_cfg:
                the_log_cfg = log_cfg.get('log_cfg')
                if the_log_cfg is None:
                    the_log_cfg = log_cfg.get('cfg')
                if the_log_cfg is None:
                    the_log_cfg = log_cfg.get('conf')
                if the_log_cfg is None:
                    sys.stderr.write("log_config(log.yml) format is error\n")
                    return
                if log_cfg.get('reset_cfg'):
                    cls.log_cfg = []
                for one_cfg in the_log_cfg:
                    cls.log_cfg.append(one_cfg)

    @classmethod
    def __handlers_init(cls, force=False, is_load_cfg=True):
        if force or not cls.handlers_init:
            cls.handlers_init_mark = False
            with cls.log_lock:
                if cls.handlers_init_mark:
                    return
                cls.handlers_init_mark = True
                if sys.version_info < (3, 0):
                    reload(sys)
                    sys.setdefaultencoding('utf-8')
                logbook.set_datetime_format("local")
                if is_load_cfg:
                    cls._load_project_log_cfg()

                for cfg in cls.log_cfg:
                    cfg_name = cfg.get('name')
                    one_handle_arr = cls.handlers.get(cfg_name)
                    if one_handle_arr is None:
                        cls.handlers[cfg_name] = []
                        # print("init handler {} {}".format(cfg_name, cfg))
                        if cfg.get('stderr_log'):
                            # bubble 意思是要不要传递到下一个handler处理,如果是false就不传递,这里必须是true的,否则下一个handler会失效
                            cls.handlers[cfg_name].append(
                                ColorizedStderrHandler(bubble=True,
                                                       level=cls._parse_level(cfg.get('stderr_log_level', 'INFO'))))
                        if cfg.get('buffer_log'):
                            # bubble 意思是要不要传递到下一个handler处理,如果是false就不传递,这里必须是true的,否则下一个handler会失效
                            the_buffer = cls._get_buffer(cfg_name, cfg.get('buffer_size', 1024))
                            cls.handlers[cfg_name].append(
                                BufferHandler(bubble=True, level=cls._parse_level(cfg.get('buffer_log_level', 'INFO')),
                                              buffer=the_buffer.get('buffer')))
                        if cfg.get('out_file', None) is not None:
                            # print("out file {} {} ".format(cls.get_log_path(), cfg.get('out_file', None)))
                            # bubble 意思是要不要传递到下一个handler处理,如果是false就不传递,这里必须是true的,否则下一个handler会失效
                            cls.handlers[cfg_name].append(logbook.TimedRotatingFileHandler(
                                os.path.join(cls.get_log_path(), cfg.get("out_file")),
                                date_format='%Y-%m-%d', encoding="utf-8", backup_count=3,
                                bubble=True))
                for handler_name, handlers in cls.handlers.items():
                    for one_handle in handlers:
                        # print("init {} handler format {}".format(handler_name, one_handle))
                        one_handle.formatter = cls.common_log_format
                cls.handlers_init = True
                cls.loggers.clear()

    @classmethod
    def get_logger(cls, name=__file__, log_frame=2):
        cls.__handlers_init()
        if cls.loggers.get(name, None) is None:
            cls.loggers[name] = CommonLogger(name)
            # 其他的handlers就用正则来匹配
            for cfg in cls.log_cfg:
                cfg_name = cfg['name']
                the_reg = re.compile(cfg['file_regex'], re.I)
                if the_reg.match(name):
                    cls.loggers[name].level = lookup_level(cls._parse_level(cfg['log_level']))
                    # 这里是必须要删掉的，因为需要顺序靠后的顶掉顺序考前的
                    del (cls.loggers[name].handlers[:])
                    for one_handle in cls.handlers[cfg_name]:
                        the_handler = one_handle
                        the_handler.log_frame = log_frame
                        # print("append  logger {} handler:{}".format(name, the_handler))
                        cls.loggers[name].handlers.append(the_handler)
            # all里面的 handlers 就是都要的handlers吧
            for one_handle in cls.handlers['all']:
                cls.loggers[name].handlers.append(one_handle)
        return cls.loggers.get(name)

    def process_record(self, record):
        logbook.Logger.process_record(self, record)
        record.extra['cwd'] = os.getcwd()


def __log_msg(msg, level, es, frame_level=2):
    default_exc_msg = ''
    frame = sys._getframe(frame_level)
    code = frame.f_code
    # print("the fname::{}".format(code.co_filename))
    logger = CommonLogger.get_logger(code.co_filename, frame_level)
    try:
        # print("====file{} oh handlers:{}=======".format(code.co_filename, logger.handlers))
        if es is not None:
            default_exc_msg = traceback.format_exc()
            e_type, value, e_traceback = sys.exc_info()
            msg += "\n" + better_exceptions.format_exception(e_type, value, e_traceback)
        eval("logger.{level}(msg)".format(level=level))
    except Exception as aes:
        try:
            eval("logger.{level}(msg)".format(level=level))
            new_trace_msg = traceback.format_exc()
            logger.error(new_trace_msg)
        except Exception as fuck_ex:
            logger.error("怎么都写不下来消息==>{}".format(fuck_ex))


def set_log_path(log_path):
    CommonLogger.set_log_path(log_path)


def debug(msg, es=None, frame=2):
    __log_msg(msg, "debug", es, frame)


def info(msg, es=None, frame=2):
    __log_msg(msg, "info", es, frame)


def warn(msg, es=None, frame=2):
    __log_msg(msg, "warning", es, frame)


def error(msg, es=None, frame=2):
    __log_msg(msg, "error", es, frame)


def get_buffer_data(name='all'):
    return CommonLogger.get_buffer_data(name)


def print_ex(ex):
    result = ''
    e_type = None
    value = None
    try:
        if ex is not None:
            e_type, value, e_traceback = sys.exc_info()
            result += "\n" + better_exceptions.format_exception(e_type, value, e_traceback)
    except Exception as aes:
        result += "\nprint_ex format_err: {}".format(aes)
        if ex is not None:
            result += "\norig ex: {},{}".format(e_type, value)
    return result


add_log_cfg = CommonLogger.add_log_cfg
set_log_level = CommonLogger.set_log_level
