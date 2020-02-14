#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import json
from functools import wraps
from random import randint
from .common import logger
from .common import format_stacks


def tracer(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        log_id = randint(0, 100000)
        start_time = time.time()

        def _time():
            # return '%0.4f' % (time.time() - start_time)
            return '%sms' % int((time.time() - start_time) * 1000)

        def _log(lines):
            lines = ['', '<<< trace_%s <<<<<<<<<<<' % log_id] + ['    %s' % line for line in lines] + ['>>> trace_%s >>>>>>>>>>>' % log_id, '']
            logger.info('\n'.join(lines))

        def _json(result, header=' ' * 4):
            if isinstance(result, dict):
                return '\n'.join('%s%s' % (header, i) for i in json.dumps(result, indent=4).splitlines())
            else:
                try:
                    assert isinstance(result, str)
                    return '\n'.join('%s%s' % (header, i) for i in json.dumps(json.loads(result), indent=4).splitlines())

                except Exception:
                    return result

        if len(args) >= 3 and hasattr(args[1], 'method') and hasattr(args[1], 'path') and hasattr(args[2], 'dict'):
            mode = 'DJANGO_HANDLER'
        else:
            mode = ''

        def _log_input():
            if mode == 'DJANGO_HANDLER':
                return '%s:%s %s' % (args[1].method, args[1].path, args[2].dict())
            else:
                return '<----< %s %s' % (' '.join(str(i) for i in args), ' '.join('%s:%s' % (k, v) for k, v in kwargs.items()))

        def _log_output():
            if mode == 'DJANGO_HANDLER':
                return '%s %s -> %s' % (_time(), result.status_code, _json(result.content.decode('utf-8')))
            else:
                return '>----> %s' % _json(result)
        _log([
            _log_input()
        ])
        try:
            result = fn(*args, **kwargs)
        except Exception:
            _log([
                _log_input(),
            ] + list(format_stacks()))
            raise
        else:
            _log([
                _log_input(),
                _log_output(),
            ])
            return result
    return wrapper
