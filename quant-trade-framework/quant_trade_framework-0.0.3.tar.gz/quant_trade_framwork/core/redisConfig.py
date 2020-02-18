from quant_trade_framwork.data.database import redisTools
from logConfig import logger
from datetime import datetime

class RuntimeConfig:
    prefix_daq_symbols = "daq_symbols:"
    prefix_symbols = "symbols"
    prefix_valid_trade_day = "trade_days"
    prefix_symbol_valid_trade_time = "symbols_trade_timespan"

    def __init__(self):
        self.redis_obj = redisTools('182.151.7.177', passwd='qyG0usOb')
        self.redis_instance = None
        self.checkRedisConnected()
        return

    def getRedisInstance(self):
        self.redis_instance = self.redis_obj.getRedisInstance()
        return

    def checkRedisConnected(self):
        if self.redis_instance is None or not self.redis_instance.ping():
            self.getRedisInstance()
        return

    def get_symbols(self):
        try:
            self.checkRedisConnected()
            temp = self.redis_instance.hgetall(self.prefix_daq_symbols)
            temp_list = []
            for k,v in temp.items():
                temp_list.append(k.decode('utf-8'))
        except BaseException as e:
            logger.error(str(e))
        return temp_list

    def set_symbols(self,symbol_list):
        if len(symbol_list) > 0:
            try:
                self.checkRedisConnected()
                for item in symbol_list:
                    self.redis_instance.hset(self.prefix_daq_symbols, item, item)
            except BaseException as e:
                logger.error(str(e))
        return

    def set_valid_trade_days(self,days):
        if len(days) > 0:
            try:
                self.checkRedisConnected()
                for day in days:
                    self.redis_instance.hset(self.prefix_valid_trade_day, day.strftime('%Y-%m-%d'), day.strftime('%Y-%m-%d'))
            except BaseException as e:
                logger.error(str(e))
        return

    def get_valid_trade_days(self,query_str):
        result = []
        try:
            self.checkRedisConnected()
            temp = self.redis_instance.hscan_iter(self.prefix_valid_trade_day, match = query_str + "*")
            for item in temp:
                result.append(item[0].decode('utf-8'))
        except BaseException as e:
            logger.error(str(e))
        return result

    def check_day_is_valid_trade_day(self,date_str):
        result = False
        try:
            self.checkRedisConnected()
            if date_str is not None and date_str:
                temp = self.redis_instance.hget(self.prefix_valid_trade_day, date_str)
            if temp is not None and temp.decode('utf-8'):
                result = True
        except BaseException as e:
            logger.error(str(e))
        return result

    def set_symbols_valid_trade_timespan(self,symbol,timespan_list):
        data = []
        if symbol is not None and symbol and timespan_list is not None \
                and len(timespan_list) > 0 and len(timespan_list) % 2 == 0:
            for time_item in timespan_list:
                temp = datetime.strptime(time_item,'%H:%M:%S')
                data_item = temp.time().hour + (temp.time().minute/60.0)
                data.append(str(data_item))

            try:
                temp = ","
                temp = temp.join(data)
                self.checkRedisConnected()
                self.redis_instance.hset(self.prefix_symbol_valid_trade_time, symbol,
                                         temp)
            except BaseException as e:
                logger.error(str(e))
        return

    def check_valid_trade_timespan(self,symbol,time_str):
        result = False
        if symbol is not None and symbol and time_str:
            try:
                self.checkRedisConnected()
                temp = datetime.strptime(time_str, '%H:%M:%S')
                input_time = temp.hour + (temp.minute/60.0)
                temp = self.redis_instance.hget(self.prefix_symbol_valid_trade_time, symbol)
                if temp is not None:
                    temp = temp.decode('utf-8')
                    temp_list = temp.split(',')
                    temp_len = int(len(temp_list)/2)
                    for index in range(0,temp_len):
                        if input_time >= float(temp_list[2 * index]) and input_time <= float(temp_list[2 * index +1]):
                            result = True
                            break
            except BaseException as e:
                logger.error(str(e))
        return result
