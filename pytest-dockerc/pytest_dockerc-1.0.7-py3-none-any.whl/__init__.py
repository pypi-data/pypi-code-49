import time


class Wait:
    """ Wait until helper to wait for a trigger state
    """

    def __init__(self, freq=0.2, timeout=10, ignored_exns=None):
        self.freq = freq
        self.timeout = timeout
        self.ignored_exns = tuple(ignored_exns) if ignored_exns else tuple()

    def __call__(self, trigger):
        end = time.time() + self.timeout

        while time.time() < end:
            try:
                res = trigger()
                return res
            except self.ignored_exns as exn:
                res = exn
            time.sleep(self.freq)
        raise StopIteration(str(res))


class Context:
    """ Context class with containers helpers
    """

    def __init__(self, dockerc):
        self.dockerc = dockerc

    def wait_for_running_state(self):
        NotImplemented
