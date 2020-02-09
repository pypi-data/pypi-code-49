import os
import asyncio
import logging.config

from signal import SIG_IGN, SIGINT, SIGTERM, Signals
from signal import signal as signal_func

from typing import List, Dict, Type, Callable, Awaitable

from macrobase_driver.driver import MacrobaseDriver
from macrobase_driver.config import CommonConfig, AppConfig
from macrobase_driver.hook import HookHandler
from macrobase_driver.logging import get_logging_config

from .config import AiopikaDriverConfig
from .hook import AiopikaHookNames
from .result import AiopikaResult, AiopikaResultAction
from .method import Method
from .router import Router, HeaderMethodRouter
from .serializers import deserialize
from .exceptions import AiopikaException, DeserializeFailedException, ContentTypeNotSupportedException,\
    ResultDeliveryFailedException, MethodNotFoundException

import uvloop
from aio_pika import connect_robust, Connection, IncomingMessage, Channel, Queue

from structlog import get_logger

log = get_logger('AiopikaDriver')


class AiopikaDriver(MacrobaseDriver):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.name is None:
            self.name = 'Aiopika Driver'

        self._connection = None
        self._channel: Channel = None
        self._queue: Queue = None

        self._hooks: Dict[AiopikaHookNames, List[HookHandler]] = {}
        self._methods: Dict[str, Method] = {}

        self._router: Router = None
        self.router_cls: Type[Router] = HeaderMethodRouter

    @property
    def config(self) -> CommonConfig[AppConfig, AiopikaDriverConfig]:
        return self._config

    def add_hook(self, name: AiopikaHookNames, handler):
        if name not in self._hooks:
            self._hooks[name] = []

        self._hooks[name].append(HookHandler(self, handler))

    def add_method(self, method: Method):
        self._methods[method.identifier] = method

    def add_methods(self, methods: List[Method]):
        self._methods.update({method.identifier: method for method in methods})

    async def process_message(self, message: IncomingMessage, *args, **kwargs):
        async with message.process(ignore_processed=self.config.driver.ignore_processed):
            log.info(f'Message <IncomingMessage correlation_id: {message.correlation_id}> received')

            await self._process_message(message)

    async def _process_message(self, message: IncomingMessage):
        try:
            result = await self._get_method_result(message, self._router.route(message))
        except MethodNotFoundException as e:
            log.debug(f'Ignore unknown method')
            result = AiopikaResult(action=AiopikaResultAction.nack, requeue=self.config.driver.requeue_unknown)
            await self._process_result(message, result, ignore_reply=True)
            return
        except Exception as e:
            requeue = e.requeue if isinstance(e, AiopikaException) else self.config.driver.requeue_if_failed

            log.error(e)
            result = AiopikaResult(action=AiopikaResultAction.nack, requeue=requeue)
            await self._process_result(message, result, ignore_reply=True)
            return

        await self._process_result(message, result, ignore_reply=False)

    async def _get_method_result(self, message: IncomingMessage, method: Method):
        data = message.body

        try:
            if message.content_type is not None and len(message.content_type) != 0:
                data = deserialize(message.body, message.content_type)
        except ContentTypeNotSupportedException as e:
            pass

        return await method.handler(self, message, data=data, identifier=method.identifier)

    async def _process_result(self, message: IncomingMessage, result: AiopikaResult, ignore_reply: bool = False):
        if result.requeue:
            await asyncio.sleep(self.config.driver.requeue_delay)

        if result.action == AiopikaResultAction.ack:
            await message.ack(multiple=result.multiple)
        elif result.action == AiopikaResultAction.nack:
            await message.nack(multiple=result.multiple, requeue=result.requeue)
        elif result.action == AiopikaResultAction.reject:
            await message.reject(requeue=result.requeue)

        if ignore_reply:
            return

        if message.reply_to is not None and len(message.reply_to) != 0:
            try:
                result_message = result.get_response_message()

                await self._channel.default_exchange.publish(
                    result_message,
                    routing_key=message.reply_to
                )
            except Exception as e:
                raise ResultDeliveryFailedException

    async def _prepare(self):
        log.debug(f'Router <{self.router_cls.__name__}> initialize')
        self._router = self.router_cls(self._methods)

        self._logging_config = get_logging_config(self.config.app)
        logging.config.dictConfig(self._logging_config)

    async def _consume(self) -> Connection:
        host            = self.config.driver.rabbitmq.host
        port            = self.config.driver.rabbitmq.port
        user            = self.config.driver.rabbitmq.user
        password        = self.config.driver.rabbitmq.password
        virtual_host    = self.config.driver.rabbitmq.vhost
        queue           = self.config.driver.queue.name

        log.info(f'<Aiopika worker: {os.getpid()}> Connect to {host}:{port}/{virtual_host} ({user}:******)')
        self._connection = await connect_robust(
            host=host,
            port=port,
            login=user,
            password=password,
            virtualhost=virtual_host,

            loop=self.loop
        )

        self._channel = await self._connection.channel()

        self._queue = await self._channel.declare_queue(
            queue,
            durable=self.config.driver.queue.durable,
            auto_delete=self.config.driver.queue.auto_delete
        )

        await self._queue.consume(self.process_message)

        return self._connection

    def _run_single_mode(self, run_multiple: bool = False, *args, **kwargs):
        uvloop.install()

        pid = os.getpid()
        log.info(f'<Aiopika worker: {pid}> Starting worker')

        await_func = self.loop.run_until_complete

        await_func(self._call_hooks(AiopikaHookNames.before_server_start.value))

        connection: Connection = None

        try:
            connection = await_func(self._consume())

            # Ignore SIGINT when run_multiple
            if run_multiple:
                signal_func(SIGINT, SIG_IGN)

            # Register signals for graceful termination
            _singals = (SIGTERM,) if run_multiple else (SIGINT, SIGTERM)
            for _signal in _singals:
                try:
                    def fu():
                        print('stop')
                        self.loop.stop()

                    self.loop.add_signal_handler(_signal, self.loop.stop)
                except NotImplementedError:
                    log.warning(
                        "AiopikaDriver tried to use loop.add_signal_handler "
                        "but it is not implemented on this platform."
                    )

            self.loop.run_forever()
        except BaseException as e:
            log.error(e)

            if self._connection is not None:
                await_func(connection.close())
        finally:
            if self._connection is not None:
                await_func(self._connection.close())
            log.info(f'<Aiopika worker: {pid}> Stopping worker')

            await_func(self._call_hooks(AiopikaHookNames.after_server_stop.value))
            self.loop.close()

    def _run_multiple_mode(self, workers: int, *args, **kwargs):
        import multiprocessing

        log.debug(self.config.driver.logo)

        processes = []

        def sig_handler(signal, frame):
            log.info("Received signal %s. Shutting down.", Signals(signal).name)
            for process in processes:
                os.kill(process.pid, SIGTERM)

        signal_func(SIGINT, lambda s, f: sig_handler(s, f))
        signal_func(SIGTERM, lambda s, f: sig_handler(s, f))

        for _ in range(workers):
            p = multiprocessing.Process(
                target=self._run_single_mode,
                daemon=True,
                kwargs={
                    'run_multiple': True,
                }
            )
            p.start()

            processes.append(p)

        for process in processes:
            process.join()

        # the above processes will block this until they're stopped
        for process in processes:
            process.terminate()

    def run(self, *args, **kwargs):
        super().run(*args, **kwargs)

        log.debug(self.config.driver.logo)

        self.loop.run_until_complete(self._prepare())

        if self.config.driver.workers == 1:
            self._run_single_mode(*args, **kwargs)
        else:
            self._run_multiple_mode(self.config.driver.workers, *args, **kwargs)
