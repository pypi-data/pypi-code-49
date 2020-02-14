import asyncio
import threading
import time
from functools import partial

from background_task_manager.runner import run_all_until_done

from hardware_communicator.controller.usb import SerialDevice
from hardware_communicator.message_interpreter.binary_interpreter import StartKeyDataEndInterpreter
import numpy as np


def put_device_property_receive_function(name):
    def f(target, data):
        target.set_device_property(name, data)

    return f


class TOY18_UVVIS_Backend(SerialDevice):
    POSSIBLE_BAUD_RATES = [115200]
    name = "TOY18_UVVIS"
    BANDWIDTH_MIN = 4
    BANDWIDTH_MAX = 10

    def __init__(self, port=None, auto_port=False):

        super().__init__(port=port, auto_port=auto_port, interpreter=StartKeyDataEndInterpreter("#", 10, []),
                         background_sleep_time=0.1)
        self.measure_task = None

        for key, data in self.available_querys.items():
            receive_size = data.get("receive_size", 0)
            max_receive_size = data.get("max_receive_size", receive_size)
            send_size = data.get("send_size", 0)
            receive_function = data.get("receive_function")
            receive_dtype = data.get("receive_dtype")
            self.interpreter.add_query(
                name=key,
                key=data["key"],
                send_size=send_size,
                receive_size=receive_size,
                max_receive_size=max_receive_size,
                receive_function=receive_function,
                receive_dtype=receive_dtype,
            )

        self.add_connection_check(self.connection_check)
        self._full_report_callback = None
        self._receive_full_spectrum_callback = None
        self.register_background_task(self.hold_connection, minimum_call_delay=3)

    def on_connect(self):
        self.beep(200)

    def hold_connection(self):
        if self.connected:
            self.write_to_port(self.interpreter.prepare_query("CMD_HOLD_COMMUNICATION"))

    async def connection_check(self):
        flag_names = [
            "QST_DETECTOR_NAME",
            "QST_HARDWARE_VERSION",
            "QST_MODEL_NAME",
            "QST_WAVELENGTH_RANGE",
            "QST_WAVELENGTH_SCAN",
            "QST_BAND_WIDTH",
        ]
        self._checkflags = {n: False for n in flag_names}
        keys = list(self._checkflags.keys())
        for key in keys:
            self.write_to_port(self.interpreter.prepare_query(key))

        start_t = time.time()
        while time.time() - start_t < 10 and not all(
                [self._checkflags[k] for k in keys]
        ):
            await asyncio.sleep(0.01)


        return all([self._checkflags[k] for k in keys])

    def set_check_and_property(self, value, checkflag, prop_name):
        put_device_property_receive_function(prop_name)(self, value)
        self._checkflags[checkflag] = True


    def request_informations(self):
        for req in [
            "QST_DETECTOR_NAME",
            "QST_HARDWARE_VERSION",
            "QST_MODEL_NAME",
            "QST_FIRMWARE_VERSION",
            "QST_SERIAL_NUMBER",
            "QST_D2_LAMP_IDF",
            "QST_D2_LAMP_AGE",
            "QST_DEVICE_RUN_TIME",
            "QST_STATUS_CHECKSUM",
            "QST_LAMPS_STATE",
        ]:
            self.write_to_port(self.interpreter.prepare_query(req))

        def print_config():
            from pprint import pprint
            pprint(self.config.data)

        self.run_once(print_config, delay=2)

    def validate_cs(self, byte_data, cs_hex_string):
        cs = int(cs_hex_string.decode(), 16)
        raw_cs = sum([x for x in byte_data])
        if cs == raw_cs:
            return True
        else:
            self.logger.error(
                f"Wrong Checsum for recive_status (raw:{byte_data},cs:{cs},raw_cs:{raw_cs})"
            )
            return False

    def turn_off(self):
        self.stop_measurment()
        self.switch_lamp(False)

    def recive_status(self, raw, checksum):
        if checksum:
            raw, cs = raw.split(":")
            # cs = int(cs,16)
            # raw_cs = sum([ord(x) for x in raw])

            if not self.validate_cs(raw.encode(), cs.encode()):
                return

        d = bin(int(raw[:2], 16))[2:]
        d = "".join(["0" for i in range(8 - len(d))]) + d
        d = [bool(int(x)) for x in d]
        self.set_device_status(
            "base_status",
            [
                self.DEVICE_STATES[x]["state_name"]
                for x, b in enumerate(d)
                if b and x in self.DEVICE_STATES
            ],
        )

        d = bin(int(raw[2:4], 16))[2:]
        d = "".join(["0" for i in range(8 - len(d))]) + d
        d = [bool(int(x)) for x in d]
        self.set_device_status(
            "lamp_error",
            [
                self.DEVICE_COMPATIBLE_ERRORS["ERR0"][x]
                for x, b in enumerate(d)
                if b and x in self.DEVICE_COMPATIBLE_ERRORS["ERR0"]
            ],
        )

        d = bin(int(raw[4:6], 16))[2:]
        d = "".join(["0" for i in range(8 - len(d))]) + d
        d = [bool(int(x)) for x in d]
        self.set_device_status(
            "lamp_error",
            [
                self.DEVICE_COMPATIBLE_ERRORS["ERR1"][x]
                for x, b in enumerate(d)
                if b and x in self.DEVICE_COMPATIBLE_ERRORS["ERR1"]
            ],
        )

        d = bin(int(raw[6:8], 16))[2:]
        d = "".join(["0" for i in range(8 - len(d))]) + d
        d = [bool(int(x)) for x in d]
        self.set_device_status(
            "lamp_error",
            [
                self.DEVICE_COMPATIBLE_ERRORS["ERR2"][x]
                for x, b in enumerate(d)
                if b and x in self.DEVICE_COMPATIBLE_ERRORS["ERR2"]
            ],
        )

        d = bin(int(raw[8:10], 16))[2:]
        d = "".join(["0" for i in range(8 - len(d))]) + d
        d = [bool(int(x)) for x in d]
        self.set_device_status(
            "lamp_error",
            [
                self.DEVICE_COMPATIBLE_ERRORS["ERR3"][x]
                for x, b in enumerate(d)
                if b and x in self.DEVICE_COMPATIBLE_ERRORS["ERR3"]
            ],
        )

    def beep_interval(self, interval):
        def play_interval():
            for i, ms in enumerate(interval):
                if i % 2 == 0:
                    self.beep(ms)
                time.sleep(ms / 1000)
                # await asyncio.sleep()

        self.run_task(play_interval)

    def autozero(self):
        self.write_to_port(self.interpreter.prepare_query("CMD_AUTOZERO_STATE"))

    def beep(self, ms=1):
        def beep_line():
            ms_remaining = ms
            sleep_delay = 0.03
            while ms_remaining >= 200:
                self.write_to_port(self.interpreter.prepare_query("CMD_BEEP", data="3"))
                ms_remaining -= 200
                time.sleep(0.2 - sleep_delay)
            while ms_remaining >= 50:
                self.write_to_port(self.interpreter.prepare_query("CMD_BEEP", data="2"))
                ms_remaining -= 50
                time.sleep(0.05 - sleep_delay)
            while ms_remaining > 0:
                self.write_to_port(self.interpreter.prepare_query("CMD_BEEP", data="1"))
                ms_remaining -= 2
        threading.Thread(target=beep_line).start()

    def switch_lamp(self, on):
        self.write_to_port(
            self.interpreter.prepare_query("CMD_LAMPS_STATE", data="T" if on else "F")
        )

    def request_full_report(self, callback=None):
        self._full_report_callback = callback
        self.write_to_port(self.interpreter.prepare_query("QST_DEVICE_REPORT"))

    def get_full_report_callback(self):
        print(self._full_report_callback)
        if self._full_report_callback:
            return self._full_report_callback
        else:
            return self.logger.info

    DEVICE_STATES = {
        0x00: {
            "state_name": "IDLE",
            "description": "Idle equipment, lamp(s) is turned off",
        },
        0x01: {"state_name": "LAMP IGNITION", "description": "Lamp(s) initializations"},
        0x02: {
            "state_name": "MEAS",
            "description": "State of measuring, lamp(s) is turned on",
        },
        0x03: {
            "state_name": "AUTOZERO",
            "description": "Running of automatic zeroing, the lamp(s) may briefly go off",
        },
        0x04: {
            "state_name": "SCAN ABS",
            "description": "Scan of absorbance, lamp(s) is turned on",
        },
        0x05: {
            "state_name": "SCAN ITS",
            "description": "Scan of intensity, lamp(s) is turned on",
        },
        0x06: {
            "state_name": "USER CALIB",
            "description": "User calibration mode, lamp(s) is turned on",
        },
        0x07: {
            "state_name": "SELF TEST",
            "description": "Start up and self test of unit, lamp(s) is turned off",
        },
        0x09: {
            "state_name": "SCAN ABS SUBSCR",
            "description": "Subscription scan of absorbance, lamp(s) is turned on",
        },
    }

    DEVICE_COMPATIBLE_ERRORS = {
        "ERR0": {
            0: "Bad block of ignition voltage generator, disconnected D2 lamp or bad D2 lamp (SELF TEST)",
            1: "Bad power supply of lamp heater voltage in (SELF TEST)",
            2: "Bad power supply of lamp anodic voltage in (SELF TEST)",
            3: "Bad power supply of detector analog or digital voltage (SELF TEST)",
            4: "4th cycle of lamp ignition fails (LAMP IGNITION)",
            5: "D2 lamp spontaneously douse (other states)",
            6: "D2 lamp ignition fails after short douse (AUTOZERO)",
            7: "",
        },
        "ERR1": {
            0: "",
            1: "Bad identification of light peak caused by low light intensity (AUTOZERO)",
            2: "Bad identification of light peak caused by unworkable light intensity (AUTOZERO)",
            3: "Low light intensity was found on some photo elements of CCD sensor (AUTOZERO)",
            4: "Required wavelength is out of range of CCD sensor (other states)",
            5: "",
            6: "",
            7: "Spontaneously failure on analog or digital power supply (other states) ",
        },
        "ERR2": {
            0: "Error during calibration of intensity caused by low base signal (USER CALIB)",
            1: "Error during calibration of intensity caused by ADC overflow or underflow (USER CALIB)",
            2: "Error during calibration of absorbance, error of under flow, over flow (USER CALIB)",
            3: "Error during calibration of absorbance, low or negative base absorbance (USER CALIB)",
            4: "Error during calibration of absorbance, calibration coefficient is low (USER CALIB)",
            5: "Error during calibration of absorbance, calibration coefficient is high (USER CALIB)",
            6: "Error or base offset of unit, bad CCD sensor, monochromator is open (SELF TEST)",
            7: "",
        },
        "ERR3": {
            0: "TG lamp is not working or lamp spontaneously douse (other states)",
            1: "Any fan is not working or any fan is disconnected or mechanical blocked (other states)",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "Occurrence of any error that is not listed in this list ",
        },
    }

    def set_spectral_range(self, start, end, force=True):
        print("_______\n",self.config,self.get_device_property("WAVELENGTH_RANGE"))
        start = max(self.get_device_property("WAVELENGTH_RANGE")[0], start)
        end = min(self.get_device_property("WAVELENGTH_RANGE")[1], end)
        if (
                self.get_device_property("WAVELENGTH_SCAN")[0] != start
                or self.get_device_property("WAVELENGTH_SCAN")[1] != end
                or force
        ):
            self.write_to_port(
                self.interpreter.prepare_query(
                    "CMD_WAVELENGTH_SCAN",
                    data=f"X{str(start).zfill(3)}Y{str(end).zfill(3)}",
                )
            )

    def set_bandwidth(self, bandwidth, force=True):
        bandwidth = min(max(bandwidth, self.BANDWIDTH_MIN), self.BANDWIDTH_MAX)
        if self.get_device_property("BAND_WIDTH") != bandwidth or force:
            self.write_to_port(
                self.interpreter.prepare_query(
                    "CMD_BAND_WIDTH", data=str(bandwidth).zfill(2)
                )
            )

    def get_full_spectrum(
            self, start_nm=0, end_nm=1200, bandwidth=4, callback=None, force_parameter=True
    ):
        print(self.config)
        self.switch_lamp(True)
        assert start_nm <= end_nm
        self.set_spectral_range(start_nm, end_nm, force=force_parameter)
        self.set_bandwidth(bandwidth, force=force_parameter)
        self.write_to_port(self.interpreter.prepare_query("QST_SCAN_ABSORBANCE"))
        self._full_report_callback = callback

    def receive_full_spectrum(self, data):
        i1 = data.index(b":")
        i2 = data.index(b":", i1 + 1)
        pre = data[:i1]
        post = data[i2 + 1:]
        items = data[i1 + 1: i2]
        if not self.validate_cs(b"".join(items), b"".join(post[:6])):
            return

        start = int(b"".join(pre[1:4]), 16)
        end = int(b"".join(pre[5:8]), 16)
        n_chars = int(b"".join(pre[9:10]), 16)

        items = [items[x: x + n_chars] for x in range(0, len(items), n_chars)]
        num_items = []
        for item in items:
            b = bin(int(b"".join(item), 16))[2:].zfill(24)
            ufe, ofe = bool(int(b[0])), bool(int(b[1]))
            if ufe or ofe:
                v = np.nan
            else:
                v = (int(b[3:], 2) * 0.01) * (-1 if int(b[2]) else 1)
            num_items.append(v)

        x = np.arange(start=start, stop=end + 1)
        y = np.array(num_items)
        if self._full_report_callback:
            try:
                self._full_report_callback(x, y)
            except:
                pass
        self._full_report_callback = None

    def start_continuous_get_full_spectrum(
            self, delay=2, start_nm=0, end_nm=1200, bandwidth=4, callback=None
    ):
        self.stop_measurment()
        self.get_full_spectrum(
            start_nm=start_nm, end_nm=end_nm, bandwidth=bandwidth, force_parameter=True
        )
        self.measure_task = self.register_background_task(
            partial(
                self.get_full_spectrum,
                start_nm=start_nm,
                end_nm=end_nm,
                bandwidth=bandwidth,
                force_parameter=False,
                callback=callback,
            ),
            minimum_call_delay=delay,
        )

    def stop_measurment(self):
        if self.measure_task is not None:
            self.stop_task(self.measure_task)

    available_querys = {
        #    Queries for get basic information about the device
        "QST_DETECTOR_NAME": {
            "key": "DTr",
            "description": "Query returns name of device (detector) ",
            "receive_size": 0,
            "max_receive_size": 16,
            "receive_function": lambda target, value: target.set_check_and_property(
                value, "QST_DETECTOR_NAME", "DETECTOR_NAME"
            ),
            "receive_dtype": str,
        },
        "QST_HARDWARE_VERSION": {
            "key": "HWr",
            "description": "Query returns hardware version of electronics ",
            "receive_size": 3,
            "receive_function": lambda target, value: target.set_check_and_property(
                value, "QST_HARDWARE_VERSION", "HARDWARE_VERSION"
            ),
            "receive_dtype": str,
        },
        "QST_MODEL_NAME": {
            "key": "MDr",
            "description": "Query returns of model name ",
            "receive_size": 4,
            "receive_function": lambda target, value: target.set_check_and_property(
                value, "QST_MODEL_NAME", "MODEL_NAME"
            ),
            "receive_dtype": str,
        },
        "QST_FIRMWARE_VERSION": {
            "key": "SWr",
            "description": "Query returns of firmware version ",
            "receive_size": 3,
            "receive_function": lambda target, value: target.set_check_and_property(
                value, "QST_FIRMWARE_VERSION", "FIRMWARE_VERSION"
            ),
            "receive_dtype": str,
        },
        "QST_SERIAL_NUMBER": {
            "key": "SNr",
            "description": "Query returns of serial number ",
            "receive_size": 7,
            "receive_function": lambda target, value: target.set_check_and_property(
                value, "QST_SERIAL_NUMBER", "SERIAL_NUMBER"
            ),
            "receive_dtype": str,
        },
        #  Queries /commands for get extended information about the device
        "QST_D2_LAMP_IDF": {
            "key": "LNr",
            "description": "Query returns of D2 lamp unique identification number ",
            "receive_size": 14,
            "receive_function": lambda target, value: target.set_check_and_property(
                value, "QST_D2_LAMP_IDF", "D2_LAMP_IDF"
            ),
            "receive_dtype": str,
        },
        "QST_D2_LAMP_AGE": {
            "key": "LLr",
            "description": "Query returns of D2 lamp index and age time ",
            "receive_size": 10,
            "receive_function": lambda target, value: target.set_check_and_property(
                value, "QST_D2_LAMP_AGE", "D2_LAMP_AGE"
            ),
            "receive_dtype": str,
        },
        "QST_DEVICE_RUN_TIME": {
            "key": "RTr",
            "description": "Query returns of device run time ",
            "receive_size": 8,
            "receive_function": lambda target, value: target.set_check_and_property(
                int(value, 16), "QST_DEVICE_RUN_TIME", "DEVICE_RUN_TIME"
            ),
            "receive_dtype": str,
        },
        "QST_STATUS": {
            "key": "STr",
            "description": "Query returns status of device ",
            "receive_size": 10,
            "receive_function": lambda target, value: target.recive_status(
                value, False
            ),
            "receive_dtype": str,
        },
        "QST_STATUS_CHECKSUM": {
            "key": "SXr",
            "description": "Query returns status of device with checksum ",
            "receive_size": 15,
            "receive_function": lambda target, value: target.recive_status(value, True),
            "receive_dtype": str,
        },
        "QST_STATUS_ENH": {
            "key": "SYr",
            "description": "Query returns enhanced status of device with checksum ",
        },
        "CMD_STATUS_ENH_SC_START": {
            "key": "SYs",
            "description": "Command starts of enhanced status subscription ",
        },
        "QST_DIPS_STATE": {
            "key": "BSr",
            "description": "Query returns dip switches state (on PCB) Queries / commands for device control ",
        },
        "QST_DISABLE_TIMEOUT_RMT": {
            "key": "DHr",
            "description": "Query returns state of disable timeout for remote control ",
        },
        "CMD_DISABLE_TIMEOUT_RMT": {
            "key": "DHw",
            "description": "Command for disable timeout of remote control mode ",
        },
        "CMD_HOLD_COMMUNICATION": {
            "key": "HCw",
            "receive_size": 1,
            "description": "Command for refresh timer of remote control mode ",
        },
        "CMD_BREAK_ERRORS": {
            "key": "BEw",
            "description": "Command reset device errors bytes EB0 to EB7 ",
        },
        "QST_LAMPS_STATE": {
            "key": "LPr",
            "description": "Query returns state of Lamp(s)",
            "receive_size": 1,
            "receive_function": lambda target, value: target.set_device_status(
                "LAMPS_STATE", value
            ),
            "receive_dtype": str,
        },
        "CMD_LAMPS_STATE": {
            "key": "LPw",
            "description": "Command for set ON / OFF Lamp(s) state ",
            "receive_size": 1,
            "send_size": 1,
            "receive_function": lambda target, value: value,
            "receive_dtype": str,
        },
        "QST_AUTOZERO_STATE": {
            "key": "ZRr",
            "description": "Query returns Autozero state ",
        },
        "CMD_AUTOZERO_STATE": {
            "key": "ZRw",
            "description": "Command for invoke Autozero ",
            "receive_size": 1,
            "max_receive_size": 4,
            "receive_dtype": str,
        },
        "CMD_BEEP": {
            "key": "SGw",
            "description": "Command for generating sound ",
            "send_size": 1,
        },
        "QST_IO_STATE": {
            "key": "FSr",
            "description": "Query returns state of external interface (I/O flags) ",
        },
        "CMD_IO_STATE": {
            "key": "FSw",
            "description": "Command set external interface digital outputs (I/O flags) ",
        },
        # Queries / commands for read / set parameters
        "QST_WAVELENGTH_RANGE": {
            "key": "WRr",
            "description": "Query returns acceptable wavelength range ",
            "receive_function": lambda target, value: target.set_check_and_property(
                [int(x) for x in value[1:].split("U")],
                "QST_WAVELENGTH_RANGE",
                "WAVELENGTH_RANGE",
            ),
            "receive_size": 8,
            "receive_dtype": str,
        },
        "QST_WAVELENGTH_CHANNELS": {
            "key": "WLr",
            "description": "Query returns channels wavelength ",
        },
        "CMD_WAVELENGTH_CHANNELS": {
            "key": "WLw",
            "description": "Command set channels wavelength ",
        },
        "QST_WAVELENGTH_SCAN": {
            "key": "WSr",
            "description": "Query returns wavelengths range for scan ",
            "receive_size": 8,
            "receive_function": lambda target, value: target.set_check_and_property(
                [int(x) for x in value[1:].split("Y")],
                "QST_WAVELENGTH_SCAN",
                "WAVELENGTH_SCAN",
            ),
            "receive_dtype": str,
        },
        "CMD_WAVELENGTH_SCAN": {
            "key": "WSw",
            "description": "Command set wavelengths range for scan ",
            "send_size": 8,
            "receive_size": 3,
            "max_receive_size": 8,
            "receive_function": lambda target, value: put_device_property_receive_function(
                "WAVELENGTH_SCAN"
            )(
                target, [int(x) for x in value[1:].split("Y")]
            ),
            "receive_dtype": str,
        },
        "QST_BAND_WIDTH": {
            "key": "BWr",
            "description": "Query returns Band width ",
            "receive_size": 2,
            "receive_function": lambda target, value: target.set_check_and_property(
                int(value), "QST_BAND_WIDTH", "BAND_WIDTH"
            ),
            "receive_dtype": str,
        },
        "CMD_BAND_WIDTH": {
            "key": "BWw",
            "description": "Command set Band width",
            "receive_size": 2,
            "send_size": 2,
            "receive_function": lambda target, value: target.set_check_and_property(
                int(value), "QST_BAND_WIDTH", "BAND_WIDTH"
            ),
            "receive_dtype": str,
        },
        "QST_HALF_WIDTH": {
            "key": "HFr",
            "description": "Query returns Half width level ",
        },
        "CMD_HALF_WIDTH": {
            "key": "HFw",
            "description": "Command set Half width level ",
        },
        "QST_SUBSCRIPTION_FREQ": {
            "key": "SFr",
            "description": "Query returns subscription frequency ",
        },
        "CMD_SUBSCRIPTION_FREQ": {
            "key": "SFw",
            "description": "Command set subscription frequency ",
        },
        "QST_TIME_CONSTANT": {
            "key": "TCr",
            "description": "Query returns time constant ",
        },
        "CMD_TIME_CONSTANT": {
            "key": "TCw",
            "description": "Command set time constant ",
        },
        "QST_MATH_FUNCTION": {
            "key": "ODr",
            "description": "Query returns mathematical function code (channel D) ",
        },
        "CMD_MATH_FUNCTION": {
            "key": "ODw",
            "description": "Command set mathematical function code (channel D) ",
        },
        "QST_MATH_THRESHOLD": {
            "key": "OTr",
            "description": "Query returns threshold for mathematical function A / B ",
        },
        "CMD_MATH_THRESHOLD": {
            "key": "OTw",
            "description": "Command set threshold for mathematical function A / B ",
        },
        "QST_AUTO_LAMP_IGNITION": {
            "key": "ALr",
            "description": "Query returns lamps auto start function  ",
        },
        "CMD_AUTO_LAMP_IGNITION": {
            "key": "ALw",
            "description": "Command set lamps auto start function state ",
        },
        "QST_BEEP_MASK": {"key": "BMr", "description": "Query returns beep mask code "},
        "CMD_BEEP_MASK": {"key": "BMw", "description": "Command set beep mask code "},
        "QST_NEGATIVE_RANGE": {
            "key": "NRr",
            "description": "Query returns negative absorbance range level ",
        },
        "CMD_NEGATIVE_RANGE": {
            "key": "NRw",
            "description": "Command set negative absorbance range level ",
        },
        "QST_LEAKS_MODE": {
            "key": "LMr",
            "description": "Query returns leakage sensor mode ",
        },
        "CMD_LEAKS_MODE": {
            "key": "LMw",
            "description": "Command set leakage sensor mode ",
        },
        "QST_DISPLAY_SETTINGS": {
            "key": "DSr",
            "description": "Query returns display settings ",
        },
        "CMD_DISPLAY_SETTINGS": {
            "key": "DSw",
            "description": "Command for display settings ",
        },
        "QST_REMOTE_KEYLOCK": {
            "key": "RKr",
            "description": "Query returns remote keylock level ",
        },
        "CMD_REMOTE_KEYLOCK": {
            "key": "RKw",
            "description": "Command set remote keylock level ",
        },
        "QST_BAUD_RATE_SELECTION": {
            "key": "BRr",
            "description": "Query returns baud rate selection code ",
        },
        "CMD_BAUD_RATE_SELECTION": {
            "key": "BRw",
            "description": "Command set baud rate selection code ",
        },
        "QST_NET_SETTINGS": {
            "key": "NSr",
            "description": "Query returns net settings ",
        },
        "CMD_NET_SETTINGS": {"key": "NSw", "description": "Command for net settings "},
        "QST_ANAOUT_RANGE": {
            "key": "AGr",
            "description": "Query returns analog outputs range ",
        },
        "CMD_ANAOUT_RANGE": {
            "key": "AGw",
            "description": "Command set analog outputs range ",
        },
        "QST_ANAOUT_OFFSET": {
            "key": "AOr",
            "description": "Query returns analog outputs offset ",
        },
        "CMD_ANAOUT_OFFSET": {
            "key": "AOw",
            "description": "Command set analog outputs offset ",
        },
        "QST_IO_CONFIGURATION": {
            "key": "FGr",
            "description": "Query returns external interface configuration ",
        },
        "CMD_IO_CONFIGURATION": {
            "key": "FGw",
            "description": "Command set external interface configuration ",
        },
        "QST_DOUT_THRESHOLDS": {
            "key": "FTr",
            "description": "Query returns digital outputs thresholds ",
        },
        "CMD_DOUT_THRESHOLDS": {
            "key": "FTw",
            "description": "Command set digital outputs thresholds ",
        },
        "QST_CSA_TP1_RESOLUTION": {
            "key": "SRr",
            "description": "Query returns continual scan type 1 format / resolution ",
        },
        "CMD_CSA_TP1_RESOLUTION": {
            "key": "SRw",
            "description": "Command set continual scan type 1 format / resolution Queries for read measurement results ",
        },
        "QST_ABSORBANCE": {"key": "ABr", "description": "Query returns absorbance "},
        "QST_ABSORBANCE_CHK": {
            "key": "AXr",
            "description": "Query returns absorbance with checksum ",
        },
        "QST_INTENSITY": {"key": "ITr", "description": "Query returns intensity "},
        "QST_INTENSITY_CHK": {
            "key": "IXr",
            "description": "Query returns intensity with checksum ",
        },
        "QST_SCAN_ABSORBANCE": {
            "key": "SAr",
            "description": "Query returns scan of absorbance ",
            "receive_size": 30,
            "max_receive_size": 3640,
            "receive_function": lambda target, value: target.receive_full_spectrum(
                value
            ),
        },
        "QST_SCAN_INTENSITY": {
            "key": "SIr",
            "description": "Query returns scan of intensity ",
        },
        #  Queries / commands for measurement results subscription
        "CMD_ABSORBANCE_SC_START": {
            "key": "ABs",
            "description": "Command starts of absorbance subscription ",
        },
        "CMD_ABSORBANCE_SC_STOP": {
            "key": "ABu",
            "description": "Command stops of absorbance subscription ",
        },
        "CMD_ABSORBANCE_CHK_SC_START": {
            "key": "AXs",
            "description": "Command starts of absorbance with checksum subscription ",
        },
        "CMD_ABSORBANCE_CHK_SC_STOP": {
            "key": "AXu",
            "description": "Command stops of absorbance with checksum subscription ",
        },
        "CMD_INTENSITY_SC_START": {
            "key": "ITs",
            "description": "Command starts of intensity subscription ",
        },
        "CMD_INTENSITY_SC_STOP": {
            "key": "ITu",
            "description": "Command stops of intensity subscription ",
        },
        "CMD_INTENSITY_CHK_SC_START": {
            "key": "IXs",
            "description": "Command starts of intensity with checksum subscription ",
        },
        "CMD_INTENSITY_CHK_SC_STOP": {
            "key": "IXu",
            "description": "Command stops of intensity with checksum subscription ",
        },
        "CMD_CSA_TP1_START": {
            "key": "SAs",
            "description": "Command starts continual scan of absorbance, type 1 ",
            "receive_size": 0,
            "max_receive_size": 835,
        },
        "CMD_CSA_TP1_STOP": {
            "key": "SAu",
            "description": "Command stops continual scan of absorbance, type 1 ",
        },
        "CMD_CSA_TP2_START": {
            "key": "SZs",
            "description": "Command starts continual scan of absorbance, type 2 ",
        },
        "QST_MANAGE_SUBSCRIPTIONS": {
            "key": "MSr",
            "description": "Query returns state of subscriptions ",
        },
        "CMD_MANAGE_SUBSCRIPTIONS": {
            "key": "MSw",
            "description": "Command set state of subscriptions ",
        },
        # Queries / commands for user calibrations
        "QST_UCAL_PARAMETERS": {
            "key": "CPr",
            "description": "Query returns user calibration response parameters ",
        },
        "CMD_UCAL_PARAMETERS": {
            "key": "CPw",
            "description": "Command set user calibration response parameters ",
        },
        "QST_UCAL_STATE": {
            "key": "MUr",
            "description": "Query returns state of user calibration mode ",
        },
        "CMD_UCAL_STATE": {
            "key": "MUw",
            "description": "Command for set ON / OFF user calibration mode ",
        },
        "QST_UCAL_AUTOZERO": {
            "key": "CZr",
            "description": "Query returns user calibration Autozero state ",
        },
        "CMD_UCAL_AUTOZERO": {
            "key": "CZw",
            "description": "Command for invoke user calibration Autozero ",
        },
        "CMD_UCAL_ABSORBANCE_PAR": {
            "key": "CAw",
            "description": "Command for absorbance calibration according parameters ",
        },
        "CMD_UCAL_ABSORBANCE_STD": {
            "key": "CSw",
            "description": "Command for absorbance calibration to standard value ",
        },
        "CMD_UCAL_ABSORBANCE_STORE": {
            "key": "RAw",
            "description": "Command for store absorbance calibration constants ",
        },
        "CMD_UCAL_INTENSITY": {
            "key": "CIw",
            "description": "Command for intensity calibration to 100 % ",
        },
        "CMD_UCAL_INTENSITY_STORE": {
            "key": "RIw",
            "description": "Command for store intensity calibration constants ",
        },
        "CMD_UCAL_D2_REPLACE": {
            "key": "CHw",
            "description": "Command for increment D2 lamp ix and clearing age time Queries for diagnostics ",
        },
        "QST_DEVICE_REPORT": {
            "key": "CRr",
            "description": "Command for read textual report ",
            "receive_size": 4900,
            "max_receive_size": 5400,
            "receive_function": lambda target, value: target.get_full_report_callback()(
                value
            ),
            "receive_dtype": str,
        },
    }


import matplotlib.pyplot as plt

plt_start = None

x_data = None
reg_data = []
times = []


def print_spectra_callback(x, y):
    global plt_start, reg_data, x_data, times
    if plt_start is None:
        plt_start = time.time()
    if x_data is None:
        x_data = x

    reg_data.append(y)
    times.append(time.time() - plt_start)

    X, Y = np.meshgrid(x_data, times)
    Z = np.array(reg_data)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z)
    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    ax.set_zlabel("Z Label")
    plt.show(block=False)
    plt.close(fig)


def main():
    import logging
    from data_recorder import TimeSeriesDataRecorder
    # set_asyncio(True)
    logging.basicConfig(level=logging.DEBUG)
    t18 = TOY18_UVVIS_Backend()
    recorder = TimeSeriesDataRecorder()
    recorder.min_nm = np.inf
    recorder.max_nm = -np.inf

    def recorder_recive_spec(x, y):
        recorder.data_point(**dict(zip([f"nm_{xi}" for xi in x], y)))
        recorder.min_nm = min(recorder.min_nm, *x)
        recorder.max_nm = max(recorder.max_nm, *x)
        array = recorder.as_array(as_delta=True)
        plt.imshow(
            array[1:],
            interpolation="nearest",
            aspect="auto",
            extent=[array[0].min(), array[0].max(), recorder.max_nm, recorder.min_nm],
        )
        plt.xlabel("time [s]")
        plt.ylabel("wavelength [nm]")
        plt.colorbar()
        plt.savefig("spec.png")
        plt.close()


    asyncio.get_event_loop().run_until_complete(t18.find_port(excluded_ports=["COM1", "COM4"]))


    print(t18.config)
    if t18.connected:
        # t18.request_full_report(lambda v:print(len(v),"\n",v.replace(";",";\n")))

        t18.request_informations()
        t18.beep()

        t18.start_continuous_get_full_spectrum(delay=1, callback=recorder_recive_spec)

    def autostop():
        time.sleep(5)
        t18.stop_measurment()
        t18.stop()
        print("DONE")

    import threading

    threading.Thread(target=autostop).start()

    run_all_until_done()


if __name__ == "__main__":
    main()
