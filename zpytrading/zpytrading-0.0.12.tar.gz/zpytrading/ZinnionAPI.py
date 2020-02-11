import sys
import logging
import zmq
import ctypes
import os
import signal
import pandas


class ZinnionAPI(object):
    def __init__(self):
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(
            format=format, level=logging.INFO, datefmt="%H:%M:%S")

        logging.info("Python ZTrading    : Version: 0.0.12")

        logging.info("Python ZTrading    : Starting threads")

        if sys.platform == "linux" or sys.platform == "linux2":
            # linux
            logging.info("Python ZTrading    : Plataform: Linux")
        elif sys.platform == "darwin":
            # OS X
            logging.info("Python ZTrading    : Plataform: OS X")
            sys.exit()
        elif sys.platform == "win32":
            # Windows...
            logging.info("Python ZTrading    : sys.platform not supported")
            sys.exit()

        if os.getenv("TOKEN") is not None:
            logging.info("Python ZTrading    : Please set your TOKEN")
            sys.exit()

        if os.getenv("USER_ID") is not None:
            logging.info("Python ZTrading    : Please set your USER_ID")
            sys.exit()

        if 'ZTRADING_LIB' in os.environ:
            self.ztrading_lib = ctypes.cdll.LoadLibrary(
                os.environ['ZTRADING_LIB'])
        else:
            logging.error(
                "Python ZTrading    : Please export ZTRADING_LIB, for more details go to: https://github.com/Zinnion/zpytrading/wiki")
            sys.exit()

        if 'SIMULATION' in os.environ:
            self.simulation = os.environ.get('SIMULATION').lower() == 'true'
        else:
            self.simulation = False

        if 'DEBUG' in os.environ:
            self.debug = os.environ.get('DEBUG').lower() == 'true'
        else:
            self.debug = False

        logging.info("Python ZTrading    : API startup")
        self.ztrading_lib.init_ztrading.restype = ctypes.c_int
        if self.ztrading_lib.init_ztrading() == 1:
            os.kill(os.getpid(), signal.SIGUSR1)

    def add_streaming(self, streaming_config):
        self.ztrading_lib.add_streaming.restype = ctypes.c_bool
        if self.ztrading_lib.add_streaming(bytes(streaming_config, 'utf-8')) == False:
            os.kill(os.getpid(), signal.SIGUSR1)

    def add_indicator(self, indicator_config):
        self.ztrading_lib.add_indicator.restype = ctypes.c_bool
        if self.ztrading_lib.add_indicator(bytes(indicator_config, 'utf-8')) == False:
            os.kill(os.getpid(), signal.SIGUSR1)

    def get_history_candles(self, bart_ype, venue, product, step, num_candles, begin, end):
        self.ztrading_lib.get_history_candles.restype = ctypes.c_char_p
        data = self.ztrading_lib.get_history_candles(
            bytes(bart_ype, 'utf-8'), bytes(venue, 'utf-8'), bytes(product, 'utf-8'), step, num_candles, bytes(begin, 'utf-8'), bytes(end, 'utf-8'))
        pd = pandas.read_json(data)
        return pd

    def get_history_trades(self, venue, product, begin, end):
        self.ztrading_lib.get_history_trades.restype = ctypes.c_char_p
        data = self.ztrading_lib.get_history_trades(
            bytes(venue, 'utf-8'), bytes(product, 'utf-8'), bytes(begin, 'utf-8'), bytes(end, 'utf-8'))
        pd = pandas.read_json(data)
        return pd

    def get_indicator(self, input_config):
        self.ztrading_lib.get_indicator.restype = ctypes.c_char_p
        data = self.ztrading_lib.get_indicator(
            bytes(input_config, 'utf-8'), self.debug)
        pd = pandas.read_json(data)
        if pd.empty:
            return pandas.DataFrame()
        return pd

    def get_candlestick_buffer(self, venue, product, candle_type, timeframe):
        self.ztrading_lib.get_candlestick_buffer.restype = ctypes.c_char_p
        data = self.ztrading_lib.get_candlestick_buffer(
            bytes(venue, 'utf-8'), bytes(product, 'utf-8'), bytes(candle_type, 'utf-8'), timeframe)
        pd = pandas.read_json(data)
        if pd.empty:
            return pandas.DataFrame()
        return pd

    def get_counter(self):
        self.ztrading_lib.get_counter.restype = ctypes.c_int
        data = self.ztrading_lib.get_counter()
        print(data)

    def hand_data(self, callback, json):
        callback(self, json)

    def start_streaming(self, callback):
        logging.info("Python ZTrading    : Stream startup")
        # Prepare our context and publisher
        context = zmq.Context()
        subscriber = context.socket(zmq.SUB)

        if 'ZTRADING_STREAM_ADDR' in os.environ:
            subscriber.connect(os.environ['ZTRADING_STREAM_ADDR'])
        else:
            subscriber.connect("tcp://localhost:5555")

        subscriber.setsockopt(zmq.SUBSCRIBE, b"")

        if self.simulation == True:
            logging.info("Python ZTrading    : SIMULATION MODE")
            self.ztrading_lib.simulation_msg.restype = ctypes.c_bool
            if self.ztrading_lib.simulation_msg(bytes("next::client", 'utf-8')) == False:
                print("Problem requesting more data from simulation.")

        while True:
            # Read envelope with address
            msg = subscriber.recv_json()
            # Request next message if we are in simulation mode
            if self.simulation == True:
                if 'trade' in msg:
                    self.ztrading_lib.simulation_msg.restype = ctypes.c_bool
                    if self.ztrading_lib.simulation_msg(bytes("next::client", 'utf-8')) == False:
                        print("Problem requesting more data from simulation.")

            # Handle the data received
            self.hand_data(callback, msg)

        # We never get here but clean up anyhow
        subscriber.close()
        context.term()
