import json

from stackifyapm.conf import setup_stackifyapm_logging
from stackifyapm.transport.base import BaseTransport


class DefaultTransport(BaseTransport):
    """
    Default Transport handles logging of transaction data into a log file
    """
    def __init__(self, client):
        self.logging = setup_stackifyapm_logging(client)

    def send_all(self):
        # nothing to do in here since we do log transaction immediately once done
        pass

    def log_transaction(self, transaction):
        # log transaction immediately
        self.logging.debug(json.dumps(transaction.to_dict()))
