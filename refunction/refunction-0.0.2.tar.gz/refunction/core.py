"""
core.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""


class Refunction:
    """
    Refunction creates a new function from an existing function with specific arguments now set as parameters.

    Examples
    --------
    1. When we're expecting a result

    >>>from refunction import Refunction
    >>>import numpy as np

    >>>f = Refunction(np.histogram, bins=10)
    >>>x = np.random.rand(100)
    >>>x_hist = f(x)

    2. When we just want to execute the function (no result)

    >>>from refunction import Refunction
    >>>import matplotlib.pyplot as plt
    >>>import numpy as np

    >>>def plot(x, y):
    >>>    plt.figure()
    >>>    plt.plot(x, y)
    >>>    plt.show()

    >>>x = np.random.rand(100)
    >>>y = np.random.rand(100)
    >>>f = Refunction(plot, x, y)
    >>>f.execute()
    """

    # Initialize instance of Refunction class
    def __init__(self, function, *args, **kwargs):
        """

        Parameters
        ----------
        function : callable
            Function to turn into new parametrized function.
        """

        self.function = function
        self.args = args
        self.kwargs = kwargs

    # Allows us to use Refunction instance as a function
    def __call__(self, *args, **kwargs):
        # Process args
        args = self._process_args(args)

        # Run the function
        return self.function(*args, **kwargs, **self.kwargs)

    # Process positional arguments
    def _process_args(self, args):
        # Send warning if we've specified positional arguments at class declaration and call
        if self.args is not None and args is not None:
            Warning('appending new args to first position')
            args += self.args

        # If we've only specified positional arguments at class declaration, use those
        elif self.args is not None:
            args = self.args

        # Return
        return args

    # Execute the function without returning anything
    def execute(self, *args, **kwargs):
        # Process args
        args = self._process_args(args)

        # Run the function
        self.function(*args, **kwargs, **self.kwargs)
