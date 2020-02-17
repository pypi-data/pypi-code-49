# -*- coding: utf-8 -*-

"""Console script for yeahyeah
# usage:

$ pip install --editable .
$ eval "$(_YEAHYEAH_COMPLETE=source yeahyeah)"
$ eval "$(_JJ_COMPLETE=source jj)"
$ yeahyeah

"""

import click

from yeahyeah.config import CORE_CONFIG_PATH
from yeahyeah.core import YeahYeah
from yeahyeah.persistence import YeahYeahPersistenceException

jj = YeahYeah(configuration_path=CORE_CONFIG_PATH)

try:
    settings = jj.get_settings()
except YeahYeahPersistenceException as e:
    click.echo(f'Error: Could not read settings file. Please'
               f' check {jj.settings_file_path}. Original error: {e}')
    raise

else:
    for class_ref in settings.plugin_paths:
        jj.add_plugin(class_ref)

yeahyeah = jj.root_cli  # base click command line entry point