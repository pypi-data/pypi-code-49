import logging


class Config:
    """ global config """
    host = 'localhost'  # redis host
    port = 6379  # redis port
    db = 0  # redis db
    password = None  # redis password
    concurrency = 100  # Max concurrency for worker
    max_retry = 3  # max retry for each request
    blocks = 1  # block amount for bloom filter
    worker_log = True  # enable worker download log
    cache_error_request = True

    def set_config_from_dict(self, options):
        assert isinstance(options, dict), 'options must be dict'
        for k, v in options.items():
            setattr(self, k, v)


config = Config()
