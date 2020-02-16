#!/usr/bin/env python
# -*- coding: utf-8 -*-
from blessings import Terminal
import click
import json
import logging
import os
import sys

import yaml

term = Terminal()

LOG = logging.getLogger(__name__)


def link(url, name):
    """Print clickabl link on supporting terminals."""
    return "\033]8;;{}\033\\{}\033]8;;\033\\".format(url, name)


class Config(dict):
    """Config."""

    def __init__(self):
        self.update(self.load_config("~/.gertty.yaml"))

    def load_config(self, config_file):
        config_file = os.path.expanduser(config_file)
        with open(config_file, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                LOG.error(exc)
                sys.exit(2)


class Tender(object):
    def __init__(self):
        self.cfg = Config()

    def header(self):
        msg = ""
        return term.on_bright_black(msg)


def parsed(result):
    result.raise_for_status()

    if hasattr(result, "text") and result.text[:4] == ")]}'":
        return json.loads(result.text[5:])
    else:
        print("ERROR: %s " % (result.result_code))
        sys.exit(1)


@click.command()
@click.option("--debug", "-d", default=False, help="Debug mode", is_flag=True)
def main(debug):
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)-8s %(message)s")
    handler.setFormatter(formatter)
    LOG.addHandler(handler)

    if debug:
        LOG.setLevel(level=logging.DEBUG)

    tender = Tender()
    print(tender.header())
    cnt = 0
    print(term.bright_black("-- %d changes listed" % cnt))


if __name__ == "__main__":

    main()
