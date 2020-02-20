import argparse
import configparser
import logging
from pathlib import Path
from sys import stdout

from . import exp_strategy
from .vivado_ip_export import export_ip

DEFAULT_PART = "xc7k160tfbg484-1"
DEFAULT_STANDARD = "c++11"


def parse_includes(include_str, ini_path):
    preprocessed = [Path(s.strip()) for s in include_str.split(',')]
    final = []
    for p in preprocessed:
        if p.is_absolute():
            final.append(p)
        else:
            absolute = (ini_path / p).resolve()
            final.append(absolute)
    return final


def parse_defines(defines_str):
    defines_list = defines_str.split(',')
    defines = {}
    for d in defines_list:
        if '=' in d:
            d = d.split('=')
            defines[d[0].strip()] = d[1].strip()
        else:
            defines[d.strip()] = 1
    return defines


def run_metaexp(name, config, config_path, ip_export):
    comp_path = config['comp_path']
    comp_name = config['top_level_comp']
    clock_period = int(config['period'])
    part = config['part'] if 'part' in config else DEFAULT_PART
    standard = config['standard'] if 'standard' in config else DEFAULT_STANDARD
    includes = parse_includes(config['includes'], config_path) if 'includes' in config else []
    defines = parse_defines(config['defines']) if 'defines' in config else {}
    keep_env = bool(config['keep_env']) if 'keep_env' in config else False
    handler = exp_strategy.csv_handler('{}.csv'.format(name.strip()))
    ip_lib = config['ip_lib'] if 'ip_lib' in config else comp_name
    version = config['ip_version'] if 'ip_version' in config else '1.0'
    descr = config['ip_descr'] if 'ip_descr' in config else comp_name
    if not ip_export:
        exp_strategy.minimize_latency(
            comp_path,
            comp_name,
            name,
            clock_period,
            part,
            standard,
            includes,
            defines,
            [handler],
            keep_env
        )
    else:
        export_ip(comp_path, comp_name, name, clock_period, part, standard, ip_lib, version, descr, includes, defines,
                  keep_env)

def handle_args(args):
    ini_file = Path(args.exp_file).resolve()
    if (not ini_file.exists()) or (not ini_file.is_file()):
        raise FileNotFoundError('File {} does not exists or is not a regular '
                                'file'.format(ini_file))
    config = configparser.ConfigParser()
    config.read(ini_file)
    logger = logging.getLogger('vrs_log')
    handler = logging.StreamHandler(stdout)
    log_level = logging.DEBUG if args.debug else logging.INFO
    logger.setLevel(log_level)
    handler.setLevel(log_level)
    logger.addHandler(handler)
    ip_export = args.command == "export"
    for s in config.sections():
        run_metaexp(s, config[s], ini_file.parent, ip_export)


def main():
    parser = argparse.ArgumentParser(description="Perform synthesis and"
                                                 "implementation of vivado HLS components")
    parser.add_argument("--debug", "-d", action="store_true", help="Activate "
                                                                   "debug output")
    parser.add_argument("command", choices=["impl", "export"], help="which command to run")
    parser.add_argument("exp_file", help="Experiment description ini file")

    args = parser.parse_args()
    handle_args(args)


if __name__ == "__main__":
    main()
