""" Module with the interface to interact with Kraken websocket API.
https://www.kraken.com/features/websocket-api
"""
import asyncio
from collections import namedtuple, defaultdict
from contextlib import suppress
import copy
import json
import logging
import time
import websockets


logger = logging.getLogger(__name__)


def _cast_datasets(datasets):
    """ Ensure cast of datasets."""
    return [(str(pair), int(interval)) for pair, interval in datasets]


class KrakenWs:
    """ Interface to handle Kraken ws.

    ::

        kraken = await KrakenWs.create(callback)
        # or
        # kraken = KrakenWs(callback)
        # await kraken.start()

        await kraken.subscribe([("XBT/EUR", 1)]) # start subscription for interval 1 minute
        # → await callback("XBT/EUR",  # pair
        #                  1,  # interval
        #                  1568315100,  # open timestamp
        #                  8000.0,  # open price
        #                  8001.0,  # high price
        #                  7999.0,  # low price
        #                  8000.0,  # close price
        #                  15)  # volume
        await kraken.subscribe([("ETH/EUR", 1)]) # new subscription, doesn't stop the previsous one

        await kraken.unsubscribe([("XBT/EUR", 1), ("ETH/EUR", 1)]) # end of subscriptions

        await kraken.close() # shutdown → close ws

    """

    def __init__(self, callback, url="wss://ws.kraken.com"):
        """
        :param callback: coroutine call on new candle. Arguments are
            coroutine(pair: str, o: float, h: float, l: float, c: float, v: float, interval: int)
        :param str url: Kraken ws endpoint
        """
        logger.debug(f"connect to {url}")
        self.callback = callback
        self.url = url
        self._stream = None

    @classmethod
    async def create(cls, callback, url="wss://ws.kraken.com"):
        kraken = cls(callback, url)
        await kraken.start()
        logger.debug("KrakenWs instance created and started")
        return kraken

    async def start(self):
        logger.debug("starting...")
        self._stream = await Stream.create(self.url, self.callback)

    def subscribe(self, datasets):
        """ Stream datasets.

        :param list((str,int)) datasets: list of (pair name, interval), interval is a time
            period in minute
        """
        cast = _cast_datasets(datasets)
        logger.debug(f"subscribe to {cast}")
        self._stream.subscribe(cast)

    def unsubscribe(self, datasets):
        """ Stop streams.

        :param list((str,int)) datasets: list of (pair name, interval), interval is a time
            period in minute
        """
        cast = _cast_datasets(datasets)
        logger.debug(f"unsubscribe to {cast}")
        self._stream.unsubscribe(cast)

    @property
    def datasets(self):
        """ Datasets currently streamed.

        :returns: List of pair name, interval
        :rtype: list((str,int))
        """
        if self._stream is None:
            return []
        return list(self._stream.datasets)

    async def close(self):
        """ Stop all streams. """
        logger.info("Shutdown kraken ws.")
        if self._stream is not None:
            await self._stream.close()


class Stream:
    """ Manage a socket and datasets. """

    def __init__(self, url, callback):
        self.url = url
        self.callback = callback
        self._datasets_to_add = set()
        self._datasets_to_remove = set()
        self._ws = None
        self._worker_task = None
        self._read_task = None
        self._watchdog_task = None
        self._builders = {}
        self._read_is_over = asyncio.Event()

    @classmethod
    async def create(cls, url, callback):
        """ Start to subscribe using ws. """
        stream = cls(url, callback)
        await stream.start()
        logger.debug("Stream instance created and started")
        return stream

    @property
    def datasets(self):
        """ All datasets currently streamed. """
        return set(self._builders.keys()
                   ).union(self._datasets_to_add
                           ).difference(self._datasets_to_remove)

    async def start(self):
        """  Bring up the stream. """
        await self._connect()
        self._worker_task = asyncio.ensure_future(self.worker())
        self._watchdog_task = asyncio.ensure_future(self.watchdog())
        await self._start_read()

    async def _connect(self):
        """ Acquire websocket connection. """
        logger.debug(f"connect to {self.url}")
        self._ws = await websockets.connect(self.url)

    async def _close_connection(self):
        """ Stop socket connection. """
        logger.debug(f"close connection")
        if self._ws is not None:
            await self._ws.close()

    async def _start_read(self):
        """ Get ready to receive message from the ws. """
        start_event = asyncio.Event()
        self._read_task = asyncio.ensure_future(self._read(start_event))
        await start_event.wait()

    async def _send(self, data):
        """ Send a command to the server.

        :param dict data:
        """
        logger.info(f"→ {data}")
        await self._ws.send(json.dumps(data))

    def subscribe(self, datasets):
        """ Make a new subscription.

        :param list((str,int)) datasets: list of (pair name, interval), interval is a time
            period in minutes
        """
        for dataset in datasets:
            self._datasets_to_add.add(dataset)

    def unsubscribe(self, datasets):
        """ Unsubscribe to datasets.

        :param list((str,int)) datasets: list of (pair name, interval), interval is a time
            period in minutes
        """
        for dataset in datasets:
            self._datasets_to_remove.add(dataset)

    async def close(self):
        """ Stop to subscribe. """
        logger.debug(f"close stream")

        async def close_task(task):
            if task is not None:
                task.cancel()
                with suppress(asyncio.CancelledError):
                    await task

        await close_task(self._watchdog_task)
        await close_task(self._worker_task)
        await self._close_connection()
        if self._read_task is not None:
            with suppress(websockets.exceptions.ConnectionClosedError):
                await self._read_task

    async def watchdog(self):
        """ Task handling ws deconnection. """
        while True:
            await self._read_is_over.wait()
            self._read_is_over.clear()
            logger.warning("reset ws connection.")
            try:
                await self._reconnect()
            except:
                logger.exception("fail to reconnect")
                self._read_is_over.set()
            finally:
                await asyncio.sleep(1)

    async def _reconnect(self):
        """ Clean connection and start new subsriptions to current datasets. """
        logger.debug(f"reconnect")
        await self._close_connection()
        await self._connect()
        await self._start_read()
        await self._subscribe(self.datasets)

    async def _read(self, start_event):
        """ Background task that handle incoming data from the ws.

        :raises: websockets.exceptions.ConnectionClosed when subscription is over

        ::

            [823,
              ['1568266025.580083',
               '1568266080.000000',
               '0.00009900',
               '0.00009900',
               '0.00009900',
               '0.00009900',
               '0.00009900',
               '568.44750717',
               1],
              'ohlc-1',
              'XTZ/XBT']
        """
        start_event.set()
        logger.info("ready to receive data from Kraken.")
        async for message in self._ws:
            logger.debug(f"← {message}")
            try:
                await self._process_new_msg(message)
            except:
                logger.exception(f"fail to process {message}")

        self._read_is_over.set()

    async def _process_new_msg(self, message):
        """ Process incoming messages from the kraken.

        :param str message: data from kraken ws.
        """
        msg = json.loads(message)
        if isinstance(msg, dict):
            if msg.get("status") == "error":
                # message is an error message...
                logger.error(msg)
            return
        try:
            _, data, interval_type, pair = msg
            _, interval = interval_type.split('-')
            interval = int(interval)
        except ValueError:
            logger.debug(f"message ignored: {message}")
        else:
            # message is ohlc data...
            builder = self._get_ohlc_buidler(pair, interval)
            builder.new_data(data)

    async def _subscribe(self, datasets):
        """ Perfom subscribe command.

        :param list((str,int)) datasets: list of (pair name, interval), interval is a time
            period in minutes
        """
        intervals = self._group_pairs_by_interval(datasets)
        for interval, pairs in intervals.items():
            for pair in pairs:
                self._get_ohlc_buidler(pair, interval)
            await self._send({
                "event": "subscribe",
                "pair": pairs,
                "subscription": {
                    "name": "ohlc",
                    "interval": interval
                }
            })

    async def _unsubscribe(self, datasets):
        """ Perfom unsubscribe command.

        :param list((str,int)) datasets: list of (pair name, interval), interval is a time
            period in minutes
        """
        intervals = self._group_pairs_by_interval(datasets)
        for interval, pairs in intervals.items():
            await self._send({
                "event": "unsubscribe",
                "pair": pairs,
                "subscription": {
                    "name": "ohlc",
                    "interval": interval
                }
            })
            for pair in pairs:
                self._del_ohlc_builder(pair, interval)

    async def _manage_subscriptions(self):
        """ Reset subsciptions to kraken server if necessary to get less than
        20 subsciptions commands (limit from Kraken Server).
        """
        await self._unsubscribe(self._datasets_to_remove)
        self._datasets_to_remove = set()
        if self._datasets_to_add:
            to_unsubscribe = self._builders.keys()
            to_add = self._datasets_to_add.union(to_unsubscribe)
            await self._unsubscribe(to_unsubscribe)
            await self._subscribe(to_add)
            self._datasets_to_add = set()

    async def worker(self):
        """ Periodically run and trigger callback with closed candles builded.
        """
        def is_new_candle(dataset, timestamp):
            _, interval = dataset
            return timestamp % (interval * 60) == 0

        while True:
            await self._manage_subscriptions()
            await self._sleep_until_next_interval()
            timestamp = int(time.time())
            timestamp -= timestamp % 60
            await asyncio.gather(*[
                self._trigger_callback(timestamp, dataset, builder)
                for dataset, builder in self._builders.items()
                if is_new_candle(dataset, timestamp)
            ])
            if timestamp % 21600 == 0:
                # reset subscriptions every 6 hours
                await self._reconnect()

    async def _trigger_callback(self, timestamp, dataset, builder):
        pair, interval = dataset
        ohlc = builder.get_ohlc(timestamp - interval * 60)
        if ohlc is None:
            return
        logger.info(f"new candle ({pair}, {interval}, *{ohlc})")
        try:
            await self.callback(pair, interval, *ohlc)
        except:
            logger.exception("error with callback processing "
                             f"({pair}, {interval}, *{ohlc})")

    def _get_ohlc_buidler(self, pair, interval):
        """
        :param str pair:
        :param int interval:
        :rtype: OhlcBuilder
        """
        try:
            return self._builders[(pair, interval)]
        except KeyError:
            pass

        builder = OhlcBuilder(interval)
        self._builders[(pair, interval)] = builder
        return builder

    def _del_ohlc_builder(self, pair, interval):
        """
        :param str pair:
        :param int interval:
        """
        try:
            del self._builders[(pair, interval)]
        except KeyError:
            pass

    @staticmethod
    def _group_pairs_by_interval(datasets):
        """ Helper to format a dataset. """
        intervals = defaultdict(list)
        for pair, interval in datasets:
            intervals[interval].append(pair)
        return intervals

    @staticmethod
    async def _sleep_until_next_interval():
        """ Sleep until next UT interval.
        Precision is 10ms max after the exact date according to the system.
        """
        now = int(time.time() * 100)
        to_sleep = (6000 - (now % 6000)) / 100
        await asyncio.sleep(to_sleep)


Candle = namedtuple("Candle", "t, o, h, l, c, v")


class OhlcBuilder:
    """ Build closed candle for a market from Kraken data. """

    def __init__(self, interval):
        """
        :param int interval: in minute
        """
        self.interval_sec = interval * 60
        self.candle = None  # current candle
        self._next_candle_tmp = self.next_timestamp()
        self.last_candle = None  # latest closed candles

    def next_timestamp(self):
        """ Start time of the next candle. """
        now = int(time.time())
        return now - (now % self.interval_sec) + self.interval_sec

    def new_data(self, data):
        """ Build current candle with data received from the websocket.

        :param data: part of message of the kraken msg that contain market data.
        """
        try:
            tmp, end_tmp, o, h, l, c, _, v, _ = data
        except ValueError:
            logger.debug(f"data ignored: {data}")
            return

        tmp = float(tmp)
        end_tmp = int(float(end_tmp))

        timestamp = end_tmp - self.interval_sec
        candle = Candle(timestamp, float(o), float(h), float(l), float(c), float(v))

        if candle.t >= self._next_candle_tmp:
            self._next_candle_tmp = self.next_timestamp()
            self.last_candle = copy.deepcopy(self.candle or candle)
            self.candle = candle

        self.candle = candle
        logger.debug(f"current candle (ut:{self.interval_sec}):{self.candle}")

    def get_ohlc(self, timestamp):
        """ Get closed candle that start at the given timestamp.

        :param int timestamp:
        :returns: dump of the candle or None
        """
        # we do not have data yet
        if self.candle is None:
            return None

        # the latest close candle match the timestamp
        if self.last_candle is not None and timestamp == self.last_candle.t:
            return self._dump_to_ohlc(self.last_candle)

        # last data receiv is the most up to date.
        if timestamp - self.candle.t <= self.interval_sec:
            return self._dump_to_ohlc(self.candle)

        # no activity
        if timestamp - self.candle.t > self.interval_sec:
            close = self.candle.c
            return [timestamp, close, close, close, close, 0]

        return None

    @staticmethod
    def _dump_to_ohlc(candle):
        return [candle.t, candle.o, candle.h, candle.l, candle.c, candle.v]
