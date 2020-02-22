"""harper exceptions."""


class Error(Exception):
    """Base class for harper errors."""

    def __init__(self, *args, **kwargs):
        pass


class InvalidWaveFileError(Error):
    """Throw an error when we encounter a badly formatted wavfile."""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
