#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com> and
#                            Matthew Wall
#
#    See the file LICENSE.txt for your full rights.
#
"""Utilities for managing the config file"""

import logging
import sys
import stat
import platform
from pkg_resources import resource_string

import nimbuscfg
from nimbuscfg import *
from nimbuscfg.prompts import *
from nimbuscfg.stanzas import *


class ConfigEngine(object):

    def run(self, options):
        print "Configuring nimbus for %s - %s" % (platform.system(), platform.release())

        try:
            config_dict = read_config()
        except SyntaxError as e:
            sys.exit("Syntax error in configuration file: %s" % e)
        except IOError as e:
            sys.exit("Unable to open configuration file: %s" % e)

        self.modify_config(config_dict)

        reorder_to_ref(config_dict)

        self.save_config(config_dict)
        self.configure_debian_startup()

    def configure_debian_startup(self):
        init_script = resource_string(__name__, 'init.d/nimbus.debian')
        with open("/etc/init.d/nimbus", 'w') as _file:
            _file.write(init_script)
            os.chmod("/etc/init.d/nimbus", stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IXOTH)

    def modify_config(self, config_dict):
        """Modify the configuration dictionary according to any command
        line options. Give the user a chance too.
        """

        if 'Station' not in config_dict:
            config_dict['Station'] = {}
            config_dict.comments['Station'] = " "

        info = prompt_for_info()
        driver_dict = prompt_for_driver()
        driver_name = driver_dict.get('driver_name')
        driver_settings = prompt_for_driver_settings(driver_name)
        weather_services = prompt_for_weather_services()

        config_dict.update(weather_services)
        config_dict['Station'].update(info)
        config_dict['Station']['station_type'] = driver_name

        orig_stanza_text = None

        # if a previous stanza exists for this driver, grab it
        if driver_name in config_dict:
            orig_stanza = configobj.ConfigObj(interpolation=False)
            orig_stanza[driver_name] = config_dict[driver_name]
            orig_stanza_text = '\n'.join(orig_stanza.write())

        if orig_stanza_text:
            stanza_text = orig_stanza_text
        else:
            stanza_text = config_stanzas[driver_name]

        stanza = configobj.ConfigObj(stanza_text.splitlines())

        # Insert the stanza in the configuration dictionary:
        config_dict[driver_name] = stanza[driver_name]
        config_dict.comments[driver_name] = " "

        reorder_sections(config_dict, driver_name, 'Station', after=True)

        for k in driver_settings:
            config_dict[driver_name][k] = driver_settings[k]

    def save_config(self, config_dict):
        """Save the config file, backing up as necessary."""

        config_path = os.path.join(nimbuscfg._config_dir, nimbuscfg._config_file)

        if not os.path.exists(nimbuscfg._config_dir):
            os.makedirs(nimbuscfg._config_dir)

        with open(config_path, 'w') as fd:
            config_dict.write(fd)

        logging.info("Saved configuration to %s" % config_path)
