class AerieException(Exception):
    ...


class DoesNotExist(AerieException):
    ...


class MultipleResults(AerieException):
    ...


class ImproperlyConfigured(AerieException):
    ...
