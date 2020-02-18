from time import monotonic as time, sleep
from multiprocessing import Value

from simpy.core import EmptySchedule, Environment, Infinity


class SyncedFloat:
    """ holds a float value which can be shared between threads and used as a factor for a casymda ChangeableFactorRealtimeEnvironment """

    def __init__(self, synced: Value):
        """can be instanciated via factory class method"""
        self.synced: Value = synced

    def __truediv__(self, other):
        return self.synced.value / other

    def __rtruediv__(self, other):
        return other / self.synced.value

    def __mul__(self, other):
        return other * self.synced.value

    def __rmul__(self, other):
        return self.__mul__(other)

    def set_value(self, value: float) -> float:
        self.synced.value = value
        return self.synced.value

    @classmethod
    def _create_factor_instance(cls, factor=1.0) -> "SyncedFloat":
        value = Value("d", factor)
        return SyncedFloat(value)


class ChangeableFactorRealtimeEnvironment(Environment):
    """Realtime environment without strict-mode, but with possibility to set the factor dynamically"""

    def __init__(self, initial_time=0, factor=SyncedFloat._create_factor_instance()):
        """ factor can be obtained via 'get_factor_instance' classmethod.
            also works when factor is """
        self.factor: SyncedFloat = factor
        super().__init__(initial_time)

    def step(self):
        """ modified step function without strict-mode but working with changing factors"""
        evt_time = self.peek()

        if evt_time is Infinity:
            raise EmptySchedule()

        sleep_time = (evt_time - self.now) * self.factor

        if sleep_time > 0.01:
            sleep(sleep_time)

        return Environment.step(self)

    @classmethod
    def create_factor_instance(cls, factor=1.0) -> SyncedFloat:
        """ forwards to SyncedFloat factory method """
        return SyncedFloat._create_factor_instance(factor=factor)
