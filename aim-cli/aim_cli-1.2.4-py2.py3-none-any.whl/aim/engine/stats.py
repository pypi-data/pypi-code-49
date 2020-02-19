import time
import psutil
import functools
from pprint import pprint
import threading

from aim.engine.types import Singleton
from aim.sdk.artifacts.stats import Stats


class Profiler(metaclass=Singleton):
    # Available aggregate functions
    AGG_MODE_AVG = 'average'
    AGG_MODE_MIN = 'min'
    AGG_MODE_MAX = 'max'
    AGG_MODE_DIFF = 'diff'
    AGG_MODES = (AGG_MODE_AVG, AGG_MODE_MIN, AGG_MODE_MAX, AGG_MODE_DIFF)
    AGG_DEFAULT = AGG_MODE_AVG

    STAT_INTERVAL_MIN = 5
    STAT_INTERVAL_MAX = 500

    stat_interval = 10
    cycles_agg_amount = 10
    cycle_index = 0
    cycles = []

    curr_cycle_keys = []
    curr_cycle_tracked_keys = []
    curr_cycle = {}
    cycle_write_lock = False

    _initialized = False
    _thread = None
    _shutdown = False
    _process = None

    @classmethod
    def aggregate(cls, items, mode):
        if mode == cls.AGG_MODE_MAX:
            return max(items)
        elif mode == cls.AGG_MODE_MIN:
            return min(items)
        elif mode == cls.AGG_MODE_AVG:
            return sum(items) / len(items)
        elif mode == cls.AGG_MODE_DIFF:
            return max(items) - min(items)

    @classmethod
    def aggregate_items(cls, stat_items, agg_mode=''):
        if not stat_items:
            return {}

        if not agg_mode:
            agg_mode = cls.AGG_MODE_AVG

        keys = list(stat_items[0].keys())
        aggregated_stat = {}
        for k in keys:
            items_arr = []
            for s in stat_items:
                items_arr.append(s[k])
            if k == 'time':
                aggregated_stat[k] = cls.aggregate(items_arr, cls.AGG_MODE_DIFF)
            else:
                aggregated_stat[k] = cls.aggregate(items_arr, agg_mode)

        return aggregated_stat
    
    def __init__(self, cycles_agg_amount, stat_interval):
        if not self._initialized:
            # Initialize Profiler
            self._initialized = True
            self.cycles_agg_amount = cycles_agg_amount
            self.stat_interval = stat_interval
            try:
                self._process = psutil.Process()
            except:
                self._process = None

            # Start thread to collect stats at interval
            stat_collector = threading.Thread(target=self._stat_collector,
                                              daemon=True)
            stat_collector.start()
            self._stat_collector_thread = stat_collector

    def track(self, key):
        # Check if cycle is done and append it to the cycles storage
        if key in self.curr_cycle_keys and key == self.curr_cycle_keys[0]:
            self.cycle_write_lock = True

            agg_cycle = {}
            for k in list(self.curr_cycle.keys()):
                agg_cycle[k] = self.aggregate_items(self.curr_cycle[k],
                                                    self.AGG_MODE_AVG)
            self.cycles.append(agg_cycle)
            self.cycle_index += 1
            self.curr_cycle_keys = []
            self.curr_cycle = {}

            # Is full
            if self.cycle_index == self.cycles_agg_amount:
                Stats('system', self.cycles[0])
                # TODO agg cycles and log output
                self.cycle_index = 0
                self.cycles = []
            exit()

            self.cycle_write_lock = False

        # Add value with None, to ignore first stat item for precision
        self.curr_cycle[key] = [None]
        self.curr_cycle_tracked_keys.append(key)
        self.curr_cycle_keys.append(key)

    def cycle(self, key):
        # Append to storage
        self.curr_cycle_tracked_keys.remove(key)

    def _stat_collector(self):
        while True:
            if self._shutdown:
                break

            time_counter = 0
            while time_counter < self.stat_interval:
                time.sleep(self.STAT_INTERVAL_MIN / 1000)
                time_counter += self.STAT_INTERVAL_MIN
                if self._shutdown:
                    break

            if self.cycle_write_lock:
                continue

            stat_time = round(time.time() * self.stat_interval)
            stat_time /= self.stat_interval

            stats = self.stats()
            for k in self.curr_cycle_tracked_keys:
                if len(self.curr_cycle[k]) and self.curr_cycle[k][0] is None:
                    self.curr_cycle[k].pop()
                else:
                    self.curr_cycle[k].append(stats)

    def stats(self):
        # Collect system statistics
        memory_usage = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')
        system_stats = {
            'cpu': self._process.cpu_percent(0.0),
            'time': time.perf_counter(),
            'disk_used': disk_usage.used / 1024 / 1024,
            'p_memory_rss': self._process.memory_info().rss / 1024 / 1024,
            'p_memory_percent': self._process.memory_percent(),
            'memory_used': memory_usage.used / 1024 / 1024,
            'memory_percent': (memory_usage.used * 100) / memory_usage.total,
        }

        return system_stats


def stats():
    # Collect system statistics
    memory_usage = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    system_stats = {
        'cpu': psutil.cpu_percent(),
        'memory_used': memory_usage.used / 1024 / 1024,
        'memory_percent': (memory_usage.total * memory_usage.used) / 100,
        'disk_total': disk_usage.total / 1024 / 1024,
        'disk_free': disk_usage.free / 1024 / 1024,
    }

    # Collect GPU statistics
    gpu_stats = []
    try:
        import pynvml
        pynvml.nvmlInit()

        for i in range(pynvml.nvmlDeviceGetCount()):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)

            util = pynvml.nvmlDeviceGetUtilizationRates(handle)
            memory = pynvml.nvmlDeviceGetMemoryInfo(handle)
            temp = pynvml.nvmlDeviceGetTemperature(handle,
                                                   pynvml.NVML_TEMPERATURE_GPU)

            power_watts = pynvml.nvmlDeviceGetPowerUsage(handle) / 1000
            power_cap = pynvml.nvmlDeviceGetEnforcedPowerLimit(handle)
            power_cap_watts = power_cap / 1000
            power_usage = power_watts / power_cap_watts * 100

            gpu_stats[i] = {
                'gpu': util.gpu,
                'memory_total': memory.total,
                'memory_free': memory.total - memory.used,
                'power_watts': power_watts,
                'power_percent': power_usage,
                'temp': temp,
            }
    except Exception:
        pass

    # Collect current process statistics
    process_stats = {}
    try:
        p = psutil.Process()
        process_stats = {
            'memory_rss': p.memory_info().rss / 1024 / 1024,
            'memory_percent': p.memory_percent(),
        }
    except Exception:
        pass

    return system_stats, gpu_stats, process_stats
