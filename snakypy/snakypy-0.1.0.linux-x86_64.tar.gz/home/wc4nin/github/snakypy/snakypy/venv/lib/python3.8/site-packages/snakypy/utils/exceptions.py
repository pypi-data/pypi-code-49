class NotSupportWindows(Exception):
    """
    A simple exception to show an unsupported error on Windows system.
    """

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return repr(self.text)
