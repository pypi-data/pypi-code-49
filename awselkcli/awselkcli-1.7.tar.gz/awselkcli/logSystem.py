import logging
import sys
import os
import datetime
from logging import Handler
from awselkcli.elk import ELK

FORMATTER = logging.Formatter(fmt='%(asctime)s %(name)s %(levelname)s %(message)s',
                              datefmt='%d/%m/%Y_%I:%M:%S-%p')


class ELKHandler(Handler):
    def __init__(self, name, host, region):
        super().__init__()
        self.name = name
        self.elk = ELK(host=host, region=region)

    def emit(self, record):
        add_ons = {
            "@timestamp": datetime.datetime.now().isoformat()
        }
        log_info = {**record.__dict__, **add_ons}

        self.elk.logger(index="log",
                        body=log_info)


def init_elk_logger(name, host=None, region=None, elk=True, stdout=True, file=True, tmpfolder='/tmp/', formatter=FORMATTER,
                    level=logging.DEBUG):
    logger = logging.getLogger(name)

    if elk:
        elk_handler = ELKHandler(
            name=name,
            host=host,
            region=region
        )
        logger.addHandler(elk_handler)

    if stdout:
        stdout_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stdout_handler)

    if file:
        filename = '{}_{}.log'.format(name, datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S'))
        fh = logging.FileHandler(os.path.join(tmpfolder, filename))
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    logger.setLevel(level)

    return logger
