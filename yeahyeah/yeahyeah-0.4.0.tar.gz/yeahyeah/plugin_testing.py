"""Test resources for plugin developers.
"""
from click.testing import CliRunner


class MockContextCliRunner(CliRunner):
    """a click.testing.CliRunner that always passes a mocked context to any call, making sure any operations
    on current dir are done in a temp folder"""

    def __init__(self, *args, mock_context, **kwargs):

        super().__init__(*args, **kwargs)
        self.mock_context = mock_context

    def invoke(
        self,
        cli,
        args=None,
        input=None,
        env=None,
        catch_exceptions=True,
        color=False,
        mix_stderr=False,
        **extra
    ):
        return super().invoke(
            cli,
            args,
            input,
            env,
            catch_exceptions,
            color,
            mix_stderr,
            obj=self.mock_context,
        )


class YeahYeahCommandLineParserRunner(MockContextCliRunner):
    """A click runner that always injects a YeahYeahContext instance into the context
    """

    def __init__(self, *args, mock_context, **kwargs):
        """

        Parameters
        ----------
        mock_context: YeahYeahContext
        """
        super().__init__(*args, mock_context=mock_context, **kwargs)