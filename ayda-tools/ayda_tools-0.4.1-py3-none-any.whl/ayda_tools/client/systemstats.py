from gpuinfo import GPUInfo
import psutil as ps
import multiprocessing as mp
from time import sleep
from time import time


class SysStats:
    def __init__(
        self,
        gpu_usage,
        gpu_mem,
        cpu_usage,
        cpu_freq,
        mem_tot,
        mem_usage,
        measuremnet_time=None,
    ):
        self.gpu_usage = gpu_usage
        self.gpu_mem = gpu_mem
        self.cpu_usage = cpu_usage
        self.cpu_freq = cpu_freq
        self.mem_tot = mem_tot
        self.mem_usage = mem_usage
        self.timestamp = measuremnet_time
        if self.timestamp is None:
            self.timestamp = time()

    def __add__(self, other):
        g_u = [i + j for i, j in zip(self.gpu_usage, other.gpu_usage)]
        g_m = [i + j for i, j in zip(self.gpu_mem, other.gpu_mem)]
        c_u = self.cpu_usage + other.cpu_usage
        c_f = self.cpu_freq + other.cpu_freq
        m_u = self.mem_usage + other.mem_usage
        m_t = self.mem_tot + other.mem_tot
        t = self.timestamp + other.timestamp
        return self.__class__(g_u, g_m, c_u, c_f, m_t, m_u, t)

    def __truediv__(self, other):

        g_u = [i / other for i in self.gpu_usage]
        g_m = [i / other for i in self.gpu_mem]
        c_u = self.cpu_usage / other
        c_f = self.cpu_freq / other
        m_u = self.mem_usage / other
        m_t = self.mem_tot / other
        t = self.timestamp / other
        return self.__class__(g_u, g_m, c_u, c_f, m_t, m_u, t)

    def to_dict(self):
        return {
            "gpu": {"usage": self.gpu_usage, "memory": self.gpu_mem},
            "cpu": {"usage": self.cpu_usage, "freq": self.cpu_freq},
            "mem": {"total": self.mem_tot, "usage": self.mem_usage},
            "timestamp": self.timestamp,
        }


def get_sys_info():
    gpu = GPUInfo.gpu_usage()
    cpu_usage = ps.cpu_percent()
    cpu_freq = ps.cpu_freq()[0]
    mem = ps.virtual_memory()
    return SysStats(gpu[0], gpu[1], cpu_usage, cpu_freq, mem[0], mem[3])


class SystemMonitor:
    def __init__(self, measure_interval_secs: float = 0.5):
        self.measure_interval_secs = measure_interval_secs
        self.stopped = mp.Value("b", False)
        self.queue = mp.Queue()
        self.process = mp.Process(target=self._run)

    def pull_collected_stats(self):
        i = 0
        if self.queue.empty():
            return None
        stats = None
        while not self.queue.empty():
            if stats is None:
                stats = self.queue.get()
            else:
                stats = stats + self.queue.get()
            i += 1
        stats = stats / i
        return stats.to_dict()

    def _run(self):
        while not self.stopped.value:
            stats = get_sys_info()
            self.queue.put(stats)
            sleep(self.measure_interval_secs)

    def start(self):
        self.process = mp.Process(target=self._run)
        self.stopped.value = False
        self.process.start()

    def stop(self):
        self.stopped.value = True
        if self.process.is_alive():
            self.process.join()

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
