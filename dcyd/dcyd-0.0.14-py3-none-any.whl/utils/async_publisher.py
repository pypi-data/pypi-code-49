import os

from google.cloud import pubsub_v1

import dcyd.utils.constants as constants


def async_publisher():
    '''Create asyncronous publisher.'''
    return pubsub_v1.PublisherClient.from_service_account_json(
        os.environ[constants.DCYD_CONFIG_ENV_VAR]
    )
