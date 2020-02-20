__all__ = ("VERSION")

__version__ = '1.8.3'
name = "stackify-python-apm"


VERSION = __version__


from stackifyapm.base import Client  # noqa
from stackifyapm.conf import setup_logging  # noqa
from stackifyapm.instrumentation.control import instrument  # noqa
from stackifyapm.instrumentation.control import uninstrument  # noqa
from stackifyapm.traces import CaptureSpan  # noqa
from stackifyapm.traces import set_transaction_context  # noqa
from stackifyapm.traces import set_transaction_name  # noqa
