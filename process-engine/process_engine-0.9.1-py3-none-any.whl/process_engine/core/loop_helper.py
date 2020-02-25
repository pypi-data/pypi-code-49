import asyncio
import logging
import signal

logger = logging.getLogger(__name__)

_DEFAULT_DELAY = 1

class LoopHelper:
    
    # TODO: mm - remove kwargs with better readable params
    def __init__(self, loop=asyncio.get_event_loop(), **kwargs):
        self._loop = loop
        self._tasks = []

        self.on_shutdown = kwargs.get('on_shutdown', self.__internal_on_shutdown)

    def create_task(self, task_callback):
        task = self._loop.create_task(task_callback())
        self._tasks.append(task)

    def register_delayed_task(self, task_func, **options):
        logger.info(f"create delayed tasks with options ({options}).")
        task = self._loop.create_task(self.__create_delayed_task(task_func, **options))
        self._tasks.append(task)

        return task

    def unregister_delayed_task(self, delayed_task, msg=""):
        return self.__unregister_task(delayed_task, msg)

    async def __create_delayed_task(self, task_func, **options):
        async def _worker(delay):
            try:
                await asyncio.sleep(delay)

                if asyncio.iscoroutinefunction(task_func):
                    logger.debug("running delayed job (async)")
                    await task_func()
                else:
                    logger.debug("running delayed job (sync)")
                    task_func()
                    
            except asyncio.CancelledError as ce:
                logger.debug(f"Cancel the task {ce}")


        delay = options.get('delay', _DEFAULT_DELAY)
        return await _worker(delay)

    def register_background_task(self, task_func, **options):
        logger.info(f"create background worker with options ({options}).")
        task = self._loop.create_task(self.__create_background_task(task_func, **options))
        self._tasks.append(task)
        return task

    def unregister_background_task(self, background_task, msg=""):
        return self.__unregister_task(background_task, msg)

    def __unregister_task(self, task, msg):
        can_unregister = True

        if self._tasks.index(task) >= 0:
            logger.info(f"cancel and unregister task: {msg}")
            self._tasks.remove(task)

            try:
                task.cancel()
                logger.info(f"cancelled task: {msg}")
            except asyncio.CancelledError as ce:
                logger.error(f"__unregister_task: {ce}")
                pass
        else:
            logger.warning("did'nt found task to unregister")
            can_unregister = False

        return can_unregister

    async def __create_background_task(self, task_func, **options):
        async def _task(delay):
            running = True

            while running:
                try:
                    if with_delay:
                        logger.debug(f"background worker delay for {delay}")
                        await asyncio.sleep(delay)
                    
                    if asyncio.iscoroutinefunction(task_func):
                        logger.debug("running background job (async)")
                        await task_func() 
                    else:
                        logger.debug("running background job (sync)")
                        task_func()

                except asyncio.CancelledError:
                    running = False

        delay = options.get('delay', _DEFAULT_DELAY)
        with_delay = True if delay > 0 else False

        return await _task(delay)

    def start(self):
        logger.info("Starting event loop.")
        try:
            self.__register_shutdown()
            self._loop.run_forever()
        except KeyboardInterrupt:
            self._loop.close()

    def stop(self):
        logger.info("Stopping event loop.")
        for task in self._tasks:
            try:
                task.cancel()
            except Exception as e:
                logger.warning(f"Task stopped with exception {e}")

        self._loop.stop()

    async def __internal_on_shutdown(self):
        logger.debug('only internal on_shutdown called')
        await asyncio.sleep(0)

    def __register_shutdown(self):
        async def shutdown(sig):
            logger.info(f"Received exit signal {sig.name}...")

            await self.on_shutdown()

            self.stop()

        signal_handler = lambda sig: asyncio.create_task(shutdown(sig))
        signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT, signal.SIGQUIT)

        for s in signals:
            self._loop.add_signal_handler(s, signal_handler, s)
