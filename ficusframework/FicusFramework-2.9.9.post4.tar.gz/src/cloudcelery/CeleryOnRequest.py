import logging

from celery.result import AsyncResult

from api.model.ResultVO import ResultVO, FAIL_CODE
from cloudcelery import celery
from schedule import TriggerActor
from munch import Munch
import json

log = logging.getLogger('Ficus')


@celery.task(name='tasks.on_request', bind=True, max_retries=2, default_retry_delay=1 * 6)
def on_request(self, protocol):
    """
    从celery接收协议
    :param self:
    :param protocol:
    :return:
    """
    log.info(f"从celery中获取到任务:{protocol}")

    body = Munch(json.loads(protocol))

    result: ResultVO = TriggerActor.handle_trigger(body, True)  # ResultVO

    if result.code == FAIL_CODE:
        # 让celery的任务也置失败
        raise RuntimeError(result.msg)

    return {'status': True, 'data': result.to_dict()}
