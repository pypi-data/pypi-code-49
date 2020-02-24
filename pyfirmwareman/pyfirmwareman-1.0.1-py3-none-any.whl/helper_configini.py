import click
from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text, HTML

from shared import bindings


import configparser
from pyfirmwaremandef import CONST__CONFIG_F_NAME


def prompt_and_update_config_option(section_name, option_name, prompt_question, default_val="" ):


    config_value = get_config(section_name, option_name, default_val)
    prompt_value = prompt(prompt_question, key_bindings=bindings, default=config_value)

    if (prompt_value != config_value):
        set_config(section_name, option_name, prompt_value)

    return prompt_value


def get_config(section_name, option_name, default_val=""):
    config = configparser.ConfigParser()
    config.read(CONST__CONFIG_F_NAME)

    if not config.has_section(section_name):  # .has_option(section, option)
        config.add_section(section_name)

    if not config.has_option(section_name, option_name):
        config[section_name][option_name] = default_val
        with open(CONST__CONFIG_F_NAME, 'w+') as configfile:
            config.write(configfile)

    # Ask userfor targetbaudrate
    config_value = config[section_name][option_name]
    return config_value


def set_config(section_name,option_name, config_val):
    config = configparser.ConfigParser()
    config.read(CONST__CONFIG_F_NAME)

    config[section_name][option_name] = config_val
    with open(CONST__CONFIG_F_NAME, 'w+') as configfile:
        config.write(configfile)


