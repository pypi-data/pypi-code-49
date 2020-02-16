import pyvisa
import logging

logger = logging.getLogger(__name__)


class Stabilock4040:
    def __init__(self, address):
        self.address = address
        self.rm = pyvisa.ResourceManager()
        try:
            logger.info(f"Connecting to instrument address: {self.address}")
            self.inst = self.rm.open_resource(
                self.address
            )  # type:pyvisa.resources.GPIBInstrument
        except Exception as e:
            print(f"Error connecting to instrument: {e}")
            raise

        self.inst.read_termination = "\r\n"
        self.inst.timeout = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.inst.close()
        self.rm.close()

    def _write_command(self, message: str):
        self.inst.write(message)

    def _query_command(self, message: str) -> str:
        return self.inst.query(message).strip()

    def beep(self, beep_count: int):
        self._write_command(f"PP{beep_count}")

    @property
    def signal_generator_level(self):
        return self._query_command("P4")

    @signal_generator_level.setter
    def signal_generator_level(self, level):
        # Set RF output level in dBm
        self._write_command(f"IN AP {level} DM")

    def signal_generator_on(self):
        self._write_command("LE ON")

    def signal_generator_off(self):
        self._write_command("LE OF")

    @property
    def frequency(self):
        return self._query_command("P1")

    @frequency.setter
    def frequency(self, frequency):
        self._write_command(f"FR {frequency} MH")

    def one_khz_mod_on(self):
        self._write_command("MK ON")

    def one_khz_mod_off(self):
        self._write_command("MK OF")

    @property
    def am_mod_depth(self):
        return self._query_command("P5")

    @am_mod_depth.setter
    def am_mod_depth(self, mod_depth):
        self._write_command(f"MM {mod_depth} %")

    @property
    def dc_voltage(self):
        self._write_command("VD")
        return self._query_command("M6 P6")

    @property
    def dc_current(self):
        self._write_command("AD")
        return self._query_command("M6 P6")

    def selfcheck(self):
        self._write_command("ON 49 1")  # Enable end of measurement service request
        self._write_command("ON 31")  # Start selfcheck routine
        self.inst.wait_for_srq(40000)  # Wait for SRQ
        print(self.inst.read())  # Read the response
        self._write_command("OF 49")  # Reset service request function

        # todo: Add check of return from test set and evaluate to return pass/fail to caller

    @property
    def measure_af_level(self):
        self._write_command("AC VA")
        return self._query_command("M6 P6")

    @property
    def measure_af_distortion(self):
        self._write_command("AC DI")
        return self._query_command("M6 P6")
