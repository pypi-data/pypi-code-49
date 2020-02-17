import numpy as np
import time
import traceback
from logger_config import logger

class TapHandler:
    __TAP_TO_IGNORE__ = 2
    __MAX_PREMA_SENSORS__ = 4
    counter = 0

    def __init__(self, di, test, num_of_mirrors=1, ip='10.1.1.112'):
        self.is_done = False
        self.num_of_mirrors = num_of_mirrors
        self.di = di
        self.int_power = int(di.get_dp("IntPower"))
        self.test = test
        if self.test == "CALIBRATION":
            self.buf_size = 1
        else:
            self.buf_size = 2

        # for debug prints
        self.last_callback = time.time()
        self.current_callback = time.time()
        self.timeout = 3  # 3 seconds
        self.ip = ip

        self._count = np.zeros([self.buf_size], dtype=np.int32)
        self.__NUM_OF_BUFFERS__ = self.buf_size

        # Sense size should contain 1 cycle
        self._sense_cycle_size = int(di.get_dp('DriveSize') * (2 ** self.int_power))

        # To concatenate the data
        self._sense_buff = np.zeros([num_of_mirrors, self.__MAX_PREMA_SENSORS__, self._sense_cycle_size,
                                     self.__NUM_OF_BUFFERS__], np.uint16)
        # TO accumulate the current taps
        self.tap_buffer = np.zeros([num_of_mirrors, (di.get_empty_dp('sense0')).shape[0],
                                    (di.get_empty_dp('sense0')).shape[1]], np.uint16)

        self._buffer_index = 0  # starting to fill the buffer from this index
        self.is_buf_locked = np.zeros(self.buf_size, dtype=bool)
        self.is_buffer_full = np.zeros(self.buf_size, dtype=bool)

        self.frame_index = 0
        self.tap_index = 0
        self.wrong_frame = 0  # ignore first tap

        self._sense_default_len = len(di.get_empty_dp('sense0')[0])
        self.num_of_subframes = int(np.ceil(self._sense_cycle_size / self._sense_default_len))
        self.last_subframe_len = self._sense_cycle_size % self._sense_default_len
        logger.info(f"table_size:{self._sense_cycle_size}, sense_len:{self._sense_default_len}, num_of_subframes {self.num_of_subframes}")

        self.is_stop_request = False

        # Register event
        self.is_registered = False
        self.register()

    def reset_counter(self, index=-1, reset_tap_index =False):
        '''
        Resetting one of the indexes or Both of the double buffer
        :param index:
        :return:
        '''

        if index == 0 or index == 1:
            self._count[index] = 0
        else:
            # reset all of the counters
            self._count[:] = 0

        if reset_tap_index:
            self.frame_index = 0
            self.tap_index = 0

    def set_cycle_size(self, int_power):
        self._sense_cycle_size = int(self.di.get_dp('DriveSize') * (2 ** int_power))

    @property
    def cycle_size(self):
        return self._sense_cycle_size

    @property
    def check_buffer(self):
        logger.info(f"buffer in index {self._buffer_index} is {self.is_buffer_full[self._buffer_index]}")
        return self.is_buffer_full[self._buffer_index]

    async def get_buffer(self):
        '''
        If the buffer index is 1 meaning buffer is full at o index and the opposite
        :return: sense_buff
        '''
        i = self._buffer_index 
        # i = (self._buffer_index + 1) % self.buf_size
        # Waiting for this buffer to be full ( if full the count is set to 0 )
        # while self._count[i] != 0:
        #     time.sleep(0.05)
        #     # TODO: ask Maxim
        if not self.is_buffer_full[i]:
            return False, -1

        # Locking the buffer not to be inserted in the middle
        self.is_buf_locked[i] = True

        # Extracting the buffer
        ret = self._sense_buff[:, :, :, i]
        self.is_buffer_full[i] = False

        # Releasing the buffer
        self.is_buf_locked[i] = False

        logger.debug(f'get_buffer[{i}]:: returning the buffer')
        return True, ret
        # return 1, ret

    def set_ignore_taps(self):
        self.__TAP_TO_IGNORE__ = 2

    # def set_stop_request(self, val):
    #     self.is_stop_request = val
    #     self.frame_index = 0
    #     self.tap_index = 0

    def clear_buffer_full(self):
        self.is_buffer_full[self._buffer_index] = False

    def set_wrong_frame(self, msg):
        logger.warning(msg)
        self.wrong_frame = self.frame_index

    def callback(self, handler, count):
        '''
        Filling the double buffer in turns
        After one buffer is full we set the boolean array buffer_full to True and start filling the other one
        :param handler:
        :param count:
        :return:
        '''

        logger.debug(f"{[self.ip]} Tap callback Start")

        # if self.test == "ENDURANCE" and self.__TAP_TO_IGNORE__ > 0:
        #     logger.debug(f"self.__TAP_TO_IGNORE__: {self.__TAP_TO_IGNORE__}")
        #     self.__TAP_TO_IGNORE__ -= 1
        #     return

        # if self.is_stop_request:
        #     logger.info(f"{[self.ip]}[Tap callback] during stop request, ignore these taps")
        #     return

        if self.test == "CALIBRATION" and self.is_done:
            return

        try:
            # in case the interrupt accrues while we grab the buffer
            while self.is_buf_locked[self._buffer_index]:
                logger.warning(f"Buffer is blocked waiting 3 ms")
                time.sleep(3 / 1000)  # sleep of 3 ms

            # debug for the "CALIBRATION" test
            if self.test == "CALIBRATION" and self._count[0] % 250 == 0:
                logger.debug(f'taps collected so far: {self._count[0]} out of {self._sense_cycle_size}')

            # Get tap event and fill buffer with sense data
            names = self.di.get_taps_callback_dps(handler, count)

            last_frame_index = self.frame_index
            last_tap_index = self.tap_index

            if "frameCnt" in names:
                self.frame_index = self.di.get_dp("frameCnt")
                logger.debug(f"{[self.ip]}[callback] frame_index {self.frame_index}")
            else:
                self.set_wrong_frame("frameCnt tap is missing")

            if "tapCnt" in names:
                self.tap_index = self.di.get_dp("tapCnt")
                logger.debug(f"{[self.ip]}[callback] tapCnt {self.tap_index}")
            else:
                self.set_wrong_frame("tapCnt tap is missing")

            for i in range(self.num_of_mirrors):
                if f"sense{i}" in names:
                    sense = self.di.get_dp(f"sense{i}")
                    self.tap_buffer[i, :, :] = sense
                else:
                    self.set_wrong_frame(f"sense{i} is missing")

            if self.frame_index < last_frame_index:
                # raise Exception(f"{[self.ip]}[callback] bad frame index: {last_frame_index}->{self.frame_index}")
                self.set_wrong_frame(f"{[self.ip]}[callback] bad frame index: {last_frame_index}->{self.frame_index}")


            if self.tap_index > self.num_of_subframes:
                self.set_wrong_frame(f"{[self.ip]}[callback] tapCnt > {self.num_of_subframes} ({self.tap_index}), at frame {self.frame_index}")

            if last_frame_index == self.frame_index:
                if self.tap_index != last_tap_index + 1:
                    self.set_wrong_frame(f"{[self.ip]}[callback] bad tap index: {last_tap_index}->{self.tap_index}"
                                         f" at frame {self.frame_index}")

            elif self.tap_index != 0 or last_tap_index != 3:
                self.set_wrong_frame(f"{[self.ip]}[callback] missed taps: {last_tap_index}->{self.tap_index}"
                                     f" from frame {last_frame_index}->{self.frame_index}")

            if self.frame_index == self.wrong_frame:
                logger.warning(f"skip frame {self.frame_index}")
                self.reset_counter(self._buffer_index)
                return

            # If cycle size is smaller than len, use cycle size
            size = min(self._sense_cycle_size, self._sense_default_len)

            # Blocking this buffer index until we finish to fill it
            self.is_buf_locked[self._buffer_index] = True

            cur_count = self._count[self._buffer_index]

            # Last accumulation
            if cur_count + (self.tap_buffer[0]).shape[1] > self._sense_cycle_size:
                last_size = self._sense_cycle_size - cur_count

                if last_size != self.last_subframe_len:
                    logger.error(f'wrong accumulation {last_size} != {self.last_subframe_len}')

                self._sense_buff[:, :, cur_count:, self._buffer_index] \
                    = self.tap_buffer[:, :, :last_size]

                # Setting the buffer flag to true
                self.is_buffer_full[self._buffer_index] = True

                logger.debug(f'taps collected so far[{self._buffer_index}]: {self._count[self._buffer_index]+last_size}'
                             f' out of {self._sense_cycle_size}')

                # Resetting the buffer counter of the full one
                self.reset_counter(self._buffer_index)

                # Switching the buffer index to fill the next one
                # to get 0/1 only or just 1 in Calibration
                self._buffer_index = (self._buffer_index + 1) % self.buf_size

                # for the CALIBRATION test
                self.is_done = True

            # First accumulation 0:1023
            else:
                if cur_count != (size * self.tap_index):
                    logger.error(f"Wrong accumulation {cur_count} != {size * self.tap_index}")

                cur_size = cur_count+size
                self._sense_buff[:, :, cur_count:cur_size, self._buffer_index] = \
                    self.tap_buffer[:, :, :size]

                self._count[self._buffer_index] += size
                logger.debug(f'taps collected so far[{self._buffer_index}]: {self._count[self._buffer_index]} '
                             f'out of {self._sense_cycle_size}')

            # Release the buffer
            self.is_buf_locked[self._buffer_index] = False

            logger.debug(f"{[self.ip]} Tap callback Done")

        except Exception as e:
            self.reset_counter(self._buffer_index) # todo is it ok for all cases
            self.wrong_frame = self.frame_index
            logger.info(f'{[self.ip]} TapHandler: failed executing callback. reason: {e}')
            logger.info(f' names: {names}')
            logger.info(f'traceback: {traceback._cause_message}')
            traceback.print_exc()
            # raise Exception(f'TapHandler: failed executing callback. reason: {e}')

    def register(self):
        if not self.is_registered:
            self.di.register_taps_callback(self.callback)
            logger.info(f"{[self.ip]} Tap callback register")
            self.is_registered = True
        else:
            logger.info(f"{[self.ip]} Tap callback is already registered")

    def unregister(self):
        if self.is_registered:
            self.di.unregister_taps_callback()
            logger.info(f"{[self.ip]} Tap callback unregister")
            self.is_registered = False
        else:
            logger.info(f"{[self.ip]} Tap callback is already unregistered")

    def del_di(self):
        self.di = None

    # def __del__(self):
    #     logger.info("## TapHandler destructor ##")
    #     self.unregister()



