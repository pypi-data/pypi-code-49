import click
from .context_state import CliContextState


def quite_mode_option(func):
    """
    Add quite mode flag to context state

    Args:
        func:
    """
    def callback(ctx, _, value):
        state = ctx.ensure_object(CliContextState)
        state.quite_mode = value
        return value
    return click.option('-q', '--quite', default=False, is_flag=True, required=False, help='Run in quite mode.',
                        expose_value=False, callback=callback)(func)


def common_options(func):
    """
    Adds common options used by multiple CLI commands

    Args:
        func:
    """
    func = quite_mode_option(func)
    return func
