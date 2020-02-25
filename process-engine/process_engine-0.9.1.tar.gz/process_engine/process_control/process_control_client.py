
import asyncio
import logging 

from ..core import base_client
from .start_callback_type import StartCallbackType

logger = logging.getLogger(__name__)

class ProcessControlClient(base_client.BaseClient):

    def __init__(self, url, session=None, identity=None):
        super(ProcessControlClient, self).__init__(url, session, identity)

    async def __start_process_instance(self, process_model_id, **options):
        start_callback_type = options.get('start_callback', StartCallbackType.ON_PROCESSINSTANCE_CREATED)

        path = f"/api/consumer/v1/process_models/{process_model_id}/start?startCallbackType={int(start_callback_type)}"

        logger.info(f"start process with uri '{path}'")

        result = await self.do_post(path, {})

        return result

    async def __start_process_instance_by_start_event(self, process_model_id, start_event_id, end_event_id, **options):
        start_callback_type = options.get('start_callback', StartCallbackType.ON_PROCESSINSTANCE_CREATED)

        path = f"/api/consumer/v1/process_models/{process_model_id}/start?start_callback_type={int(start_callback_type)}&start_event_id={start_event_id}"

        if end_event_id is not None:
            path = f"{path}&end_event_id={end_event_id}"

        logger.info(f"start process with uri '{path}'")

        result = await self.do_post(path, {})

        return result

    def start_process_instance(self, process_model_id, start_event_id=None, end_event_id=None, **options):

        async def run_loop(process_model_id, start_event_id, **options):
            result = None
            
            if start_event_id is not None:
                result = await self.__start_process_instance_by_start_event(process_model_id, start_event_id, end_event_id, **options)
            else:
                result = await self.__start_process_instance(process_model_id, **options)

            await self.close()

            return result

        logger.info(f"Connection to process engine at url '{self._url}'.")
        logger.info(f"Starting process instance process_model_id '{process_model_id}' and start_event_id '{start_event_id}'.")

        loop = asyncio.get_event_loop()

        task = run_loop(process_model_id, start_event_id, **options)
        result = loop.run_until_complete(task)

        loop.close()

        return result