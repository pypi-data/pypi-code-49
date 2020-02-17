import asyncio
import numpy as np
import math
import time
import matplotlib.pyplot as plt

from innopy.api import DeviceInterface, DeviceType, logger_init
from innolab_utils.run_board_api.TapHandler import TapHandler

from logger_config import logger


class RunBoardApi:
    __MAX_NUM_OF_MIRRORS__ = 4

    def __init__(self, config, num_of_mirrors=1, outpath=None):
        '''
        Connect to board and sets board parameters.
        Sens tap is enabled by default
        :param config: contains all the configurations of the device
        :param num_of_mirrors: number of mirror activated
        '''

        self.tap_handler = None
        self.di = None
        self.outpath = outpath
        self.num_of_mirrors = num_of_mirrors
        self.ip = config.ip
        # set api logger
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        log_filename = f"api_logs/{self.ip}_{date}.txt"
        logger_init(log_filename, 0)

        # Configure the test of the run board and transfer it to the Tap Handler
        self.test = config.main_config.test

        if num_of_mirrors > self.__MAX_NUM_OF_MIRRORS__:
            raise Exception(f"num_of_mirrors '{num_of_mirrors}' exceed max value '{self.__MAX_NUM_OF_MIRRORS__}'")

        # BSample parameters defaults
        if config.Model.Type == "B":
            self.b2 = config.Model.BSample.b
            self.a2 = config.Model.BSample.a
            self.a_led = config.Model.BSample.a_led
            self.b_led = config.Model.BSample.b_led
        # CSample parameters defaults
        else:
            self.b2 = config.Model.CSample.b
            self.a2 = config.Model.CSample.a
            self.a_led = config.Model.CSample.a_led
            self.b_led = config.Model.CSample.b_led

        # board parameters initialization sequence
        self.di = DeviceInterface(ip=self.ip, password="200andbeyond", login_level=2)

        self.di.set_dp("DriveSize", config.MEMsRunBoard.table_size)
        self.di.set_dp("BuffersAfterStop", config.MEMsRunBoard.BuffersAfterStop)
        self.di.set_dp("SamplingRate", float(config.MEMsRunBoard.rate))
        self.di.set_dp("ZeroCode", int(config.MEMsRunBoard.zero_daq))
        self.di.set_dp("MaxPulse", float(config.MEMsRunBoard.trigger_pulse_width) * np.ones(4, np.float32))

        if config.Model.Type == "B":
            self.di.set_dp("LEDDrive", float(config.MEMsRunBoard.led_drive))
        else:
            led_dac = np.uint16(
                (1000 * float(config.MEMsRunBoard.led_drive) * self.a_led + self.b_led) * (2 ** 16 - 1) / 2.5)
            self.di.set_dp("LEDDriveDAC", led_dac)

        self.stop()
        self.di.set_dp("SSTime", float(config.MEMsRunBoard.raster_SSTime))
        self.di.set_dp("IntPower", int(config.MEMsRunBoard.raster_int_power))

        self.drive_size = config.MEMsRunBoard.table_size
        self.sense_cycle_size = 0

    @property
    def cycle_size(self):
        '''

        :return:
        '''
        return self.tap_handler.cycle_size

    @property
    def tap_count(self):
        return self.tap_handler.count

    async def module_temp(self):
        '''
        Getting the temperature from the Module_sample
        :return:
        '''
        self.di.set_dp("ReadTempInterval", 0.5)  # turn On the temperature sampling
        await asyncio.sleep(2)
        temp = self.di.get_dp("Temperature")
        self.di.set_dp("ReadTempInterval", -1.0)  # turn Off the temperature sampling
        return temp

    @property
    def spaceship_temp(self):
        '''
        Getting the temperature from the spaceship
        :return:
        '''
        return self.di.get_dp("spaceship_temp")

    @property
    def eeprom(self):
        '''
        Returns all data in Eporm as object (parsed)
        :return:
        '''
        return self.di.get_dp("eeprom")

    @property
    def spaceship_humidity(self):
        '''

        :return:
        '''
        return self.di.get_dp("spaceship_humidity")

    @property
    def tap_size(self):
        return self.tap_handler.sense_buff_size

    def start(self):
        '''
        starts drive and sampling ( for 1 mirror or hole spaceship ? )
        :return:
        '''
        self.di.set_dp("SampleActive", int(True))

    # async def stop(self):
    def stop(self):
        '''
        stops drive and sampling ( for 1 mirror or hole spaceship ? )
        :return:
        '''
        self.di.set_dp("SampleActive", int(False))
        # todo temp in comment, need to update embedded version
        # Letting the device stop properly
        # while self.di.get_dp("active") != 0:
        #     await asyncio.sleep(0.01)

    def init_tap_handler(self):
        self.tap_handler = TapHandler(self.di, self.test, self.num_of_mirrors, self.ip)
        # reset counter of the tap handler
        self.tap_handler.reset_counter()

    def set_tap_size(self, size):
        self.tap_handler.set_cycle_size(size)

    async def del_tap_handler(self):
        if self.tap_handler:
            logger.info("del_tap_handler : Start")  # todo temp
            self.tap_handler.unregister()
            # self.tap_handler.reset_counter(reset_tap_index=True)
            await asyncio.sleep(1) # wait for all callbacks
            self.tap_handler.del_di()
            self.tap_handler = None
            logger.info("del_tap_handler : Done")

    # def continue_tap_handler(self):
    #     # self.ignore_first_taps()
    #     self.tap_handler.reset_counter(reset_tap_index=True)
    #     self.tap_handler.register()
    #
    # def stop_tap_handler(self):
    #     self.tap_handler.unregister()
    #     self.tap_handler.reset_counter(reset_tap_index=True)
    #     # self.clear_tap_buffer()

    def set_drive_volt(self, volts):
        '''
        Setting the drive. drive size
        :param volts: volts is a numpy array in size NxM, where N(default=4) is the number of dac per mirror
        :return:
        '''
        dword = self.di.get_empty_dp("DriveTable")

        # converting the Volts to DACWords
        for i, vals in enumerate(volts):
            for j, v in enumerate(vals):
                dword[i][j] = math.floor((v - self.b2) * (2 ** 16 - 1) / (self.a2 * 2.5))
        self.set_drive_dword(dword)

    def set_drive_dword(self, dword):
        '''
        Setting the drive. drive size
        :param dword: dword is a numpy array in size NxM, where N(default=4) is the number of dac per mirror
        :return:
        '''
        dp = self.di.get_empty_dp("DriveTable")
        if dp.shape == dword.shape:
            self.di.set_dp("DriveTable", np.array(dword, np.uint16))
        else:
            raise Exception(f'The Drive table is not in the correct shape, {dp.shape()} != {dword.shape()}')

    def check_error(self):
        '''
        @todo close interface with System. pulling? event(tap)?
        Checking if one of the mirrors has an error
        :return:
        '''
        raise NotImplemented()

    def check_warning(self):
        '''
        @todo close interface with System. pulling? event(tap)?
        Checking if one of the mirrors has an error
        :return:
        '''
        raise NotImplemented()

    def tap_start(self, name):
        self.di.set_tap_activation_state(name, True)

    def tap_stop(self, name):
        self.di.set_tap_activation_state(name, False)

    def set_ss_time(self, val):
        self.di.set_dp("SSTime", val)

    def set_int_power(self, val):
        self.di.set_dp("IntPower", val)

    def set_dp(self, name, val, set_to_flash=False):
        self.di.set_dp(name, val, set_param=set_to_flash)

    def get_dp(self, name):
        return self.di.get_dp(name)

    def get_empty_dp(self, name):
        return self.di.get_empty_dp(name)

    def get_aux_cycle(self):
        return self.tap_handler.get_aux_buffer()

    def get_cycle(self):
        # waiting until all the buffer is full
        while not self.tap_handler.check_buffer:
            time.sleep(0.05)

        return self.tap_handler.get_buffer()

    def ignore_first_taps(self):
        self.tap_handler.set_ignore_taps()

    def clear_tap_buffer(self):
        self.tap_handler.clear_buffer_full()

    async def get_async_cycle(self):
        # waiting until all the buffer is full
        valid, data = await self.tap_handler.get_buffer()
        while not valid:
            await asyncio.sleep(0.05)
            valid, data = await self.tap_handler.get_buffer()
        return data

    async def reset(self, wait_after_reset=True):
        try:
            self.di.set_dp("reset", 1)
            if wait_after_reset:
                await asyncio.sleep(10)
        except Exception as e:
            logger.error(f"[{self.ip}][RunBoardApi: reset] error during reset {e}")

    def __del__(self):
        logger.info("RunboardApi destructor Start")
        # if self.tap_handler: todo needed?
        #     self.del_tap_handler()
        self.di = None
        logger.info("RunboardApi destructor Done")
    # #     self.tap_handler.unregister()

