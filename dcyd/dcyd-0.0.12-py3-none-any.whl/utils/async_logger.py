import os
import logging

from google.cloud import logging as gc_logging

import dcyd.utils.constants as constants


def async_logger():
    '''Create asyncronous logger.
    This code came from: https://medium.com/google-cloud/python-and-stackdriver-logging-2ade460c90e3
    '''
    client = gc_logging.Client.from_service_account_json(
        os.environ[constants.DCYD_CONFIG_ENV_VAR]
    )

    # Custom formatter returns a structure, than a string
    class CustomFormatter(logging.Formatter):
        def format(self, record):
            logmsg = super(CustomFormatter, self).format(record)
            return {
                'msg': logmsg,
                'payload': record.args
            }

    # Setup handler explicitly -- different labels
    handler = client.get_default_handler()
    handler.setFormatter(CustomFormatter())

    # Setup logger explicitly with this handler                                     
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger
