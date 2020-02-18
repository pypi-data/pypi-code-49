class YeahYeahContext:
    """Core yeahyeah context object. This gets passed to all yeahyeah_plugins on init() and to any method call

    """

    def __init__(self, settings_path):
        """

        Parameters
        ----------
        settings_path: Pathlike
            Path to the folder where any context can be stored
        """
        self.settings_path = settings_path
