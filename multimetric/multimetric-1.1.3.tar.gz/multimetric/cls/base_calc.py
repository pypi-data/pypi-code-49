class MetricBaseCalc():

    def __init__(self, args, **kwargs):
        self._metrics = {}

    def get_results(self, metrics):
        """
        This alters the originally passed metrics by calculated ones
        """
        return metrics
