class SuperwiseRequestFormatError(RuntimeError):
    """
        Request Format error class:
    """

    def __init__(self, message):
        super().__init__(self, message)


class SuperwiseConnectionError(RuntimeError):
    """
        Connection error class:
        superwise connection error
    """

    def __init__(self, message):
        super().__init__(self, message)


class SuperwiseENVError(RuntimeError):
    """
        ENV error class:
        superwise connection error
    """

    def __init__(self, message):
        super().__init__(self, message)


class SuperwiseDataError(RuntimeError):
    """
        Data getting from client error
        superwise Data error
    """

    def __init__(self, message):
        super().__init__(self, message)


class SuperwiseTraceError(RuntimeError):
    """
        Trace service exception handler
        superwise trace service error
    """

    def __init__(self, message):
        super().__init__(self, message)
