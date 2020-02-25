#=============================================================================================
class Singleton(type):
    
    _instances = {}
    
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super().__call__(*args, **kwargs)
        return self._instances[self]

#=============================================================================================
class SingletonViejo:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `I` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    """

    #------------------------------------------------------------------------------------------
    def __init__(self, decorated):
        self._decorated = decorated

    #------------------------------------------------------------------------------------------
    def I(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    #------------------------------------------------------------------------------------------
    def __call__(self):
        raise TypeError('Singletons must be accessed through `I()`.')

    #------------------------------------------------------------------------------------------
    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
    