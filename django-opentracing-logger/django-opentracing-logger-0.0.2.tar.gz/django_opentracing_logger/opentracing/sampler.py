"""choose whether to report or not."""


class NoopSampler:
    def __init__(self):
        pass

    def sample(self):
        return False


class AlwaysSampler:
    def __init__(self):
        pass

    def sample(self):
        return True
