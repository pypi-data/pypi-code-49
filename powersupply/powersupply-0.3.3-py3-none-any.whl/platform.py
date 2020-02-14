import glob
import os


class Platform:
    def process(self, ps):
        return ps

    def read_sysfs(self, path):
        with open(path) as handle:
            return int(handle.read().strip())

    def read_sysfs_str(self, path):
        with open(path) as handle:
            return handle.read().strip()

    def find_iio_device(self, name):
        if not os.path.isdir('/sys/bus/iio'):
            return None
        for path in glob.glob('/sys/bus/iio/devices/iio*'):
            compat_file = os.path.join(path, 'of_node/compatible')
            if not os.path.isfile(compat_file):
                continue
            with open(compat_file) as handle:
                compatible = handle.read().strip()

            if name in compatible:
                return path


class AXP803(Platform):
    def __init__(self):
        """
        in_current1 is the current going IN the battery while charging
        in_current2 is the current going OUT the battery while discharging
        """
        self.axp_adc = self.find_iio_device('axp813-adc')
        self.current1 = os.path.join(self.axp_adc, 'in_current1_raw')
        self.current2 = os.path.join(self.axp_adc, 'in_current2_raw')

    def process(self, ps):
        current1 = self.read_sysfs(self.current1)
        current2 = self.read_sysfs(self.current2)
        if current1 > current2:
            ps.battery_current = current1 / 1000.0
        else:
            ps.battery_current = current2 / 1000.0

        return ps
