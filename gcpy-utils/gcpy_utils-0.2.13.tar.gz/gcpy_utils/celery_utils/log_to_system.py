# coding:utf-8
__author__ = "zhou"
# create by zhou on 2019/7/28
import redis
import json
import time
import logging


conn = redis.Redis('10.101.30.210', 8889)


def log_to_system(module, task_id, task_name, content, level='INFO'):
    try:
        assert len(task_id) > 0
        content = content[-10240:]  # 一次日志长度最大10kb
        assert level in ('INFO', "ERROR", 'WARN', 'DEBUG')
        key = 'task_log_%s_%s' % (module, task_id)
        data = {'content': content, 'timestamp': time.time(), 'level': level, 'module': module, 'task_name': task_name}
        data = json.dumps(data)
        _log_num = conn.lpush(key, data)
        if _log_num > 1000 and _log_num % 20 == 0:
            conn.ltrim(key, 0, 1000)
        conn.expire(key, 86400*31)
        conn.set('celery_task_recent_log_id_%s' % task_id, data, 86400*31)
        conn.sadd('celery_logs', module)
        if _log_num == 1:
            _ = conn.lpush('celery_logs_%s' % module, task_id)
            if _ > 5000 and _ % 20 == 0:
                conn.ltrim('celery_logs_%s' % module, 0, 5000)
            _1 = conn.lpush('celery_logs_%s_task_name_%s' % (module, task_name), task_id)
            conn.sadd('celery_logs_%s_shortcuts' % module, task_name)
            if _1 > 5000 and _1 % 20 == 0:
                conn.ltrim('celery_logs_%s_task_name_%s' % (module, task_name), 0, 5000)
    except:
        pass
    return True


class CustomHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            msg = self.format(record)
            data = {}
            data['task_id'] = record.__dict__['task_id']
            data['task_name'] = record.__dict__['task_name']
            data['levelname'] = record.__dict__['levelname']
            data['message'] = record.__dict__['message']
            for i, j in record.__dict__.items():
                if type(i) in (str, unicode) and type(j) in (str, unicode, int):
                    data[i] = j
            if data['message'].startswith('Received task:'):
                _ = data['message'].find('[')
                assert _
                data['task_name'] = data['message'][15:_]
                data['task_id'] = data['message'][_+1:-3]
            assert data['task_id'] != '???' and data['task_id']
            assert data['task_name'] != '???' and data['task_name']
            level = 'WARN' if data['levelname'] == 'WARNING' else data['levelname']
            log_to_system(_module_name, data['task_id'], data['task_name'], data['message'], level)
        except:
            pass


from celery.app.log import TaskFormatter


def _setup_celery_logger(logger, *args, **kwargs):
    handler = CustomHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(TaskFormatter('%(message)s'))
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)


def logger_patch(module_name):
    global _module_name
    _module_name = module_name
    from celery.signals import after_setup_logger, after_setup_task_logger, setup_logging
    after_setup_task_logger.connect(_setup_celery_logger)
    after_setup_logger.connect(_setup_celery_logger)


if __name__ == '__main__':
    print log_to_system('test', '100043243242', 'test.test','fdafdafdsafdasfdsafdsafdsa')
    #pass