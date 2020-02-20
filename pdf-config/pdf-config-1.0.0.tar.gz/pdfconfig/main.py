import logging
import os

import fire
import yaml

from .composer import PdfFileComposer
from .utils import get_output_filename

log = logging.getLogger()


def merge_documents(config_filename: str, output_filename: (str, None) = None, overwrite: bool = False,
                    log_level: str = 'INFO') -> None:
    """
    Merges PDF documents using a YAML configuration file.

    :param config_filename: Configuration file path.
    :param output_filename: Optional: Output file name and path. If not specified, uses the name and path of the
     config file with the extension changed to ``.pdf``.
    :param overwrite: By default, an existing output file is not overwritten. Change to ``True`` for overwriting any
     existing files.
    :param log_level: Detail level of output messages. Default is ``INFO``.
    """
    logging.basicConfig(format='%(levelname)s:%(message)s', level=log_level)
    log.info("Reading config from %s", config_filename)
    with open(config_filename, 'rb') as cfg_file:
        config = yaml.safe_load(cfg_file)
    if not output_filename:
        output_filename = get_output_filename(config_filename)
    if os.path.isfile(output_filename) and not overwrite:
        raise FileExistsError("The output file is already present.", output_filename)
    cp = PdfFileComposer(config['contents'], config['metadata'], config['paths'])
    cp.write(output_filename)


def run():
    fire.Fire(merge_documents)


if __name__ == '__main__':
    run()
