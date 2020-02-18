import click


class CliContextState:
    """
    CLI Context State
    """

    def __init__(self, quite_mode=False):
        """
        Args:
            quite_mode (bool): Run in quite mode
        """
        self.quite_mode = quite_mode


pass_state = click.make_pass_decorator(CliContextState, ensure=True)  # pylint: disable=invalid-name
