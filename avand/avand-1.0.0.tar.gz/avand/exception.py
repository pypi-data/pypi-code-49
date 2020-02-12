from pod_base import PodException


class AvandException(PodException):
    __slots__ = ("reference_id", "error_code")

    def __init__(self, **kwargs):
        super(AvandException, self).__init__(**kwargs)
        self.reference_id = kwargs.get("referenceId", None)
        self.error_code = kwargs.get("errorCode", None)
