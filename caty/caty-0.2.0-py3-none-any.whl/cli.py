from functools import partial
from pathlib import Path
from os.path import isfile, expanduser
from argparse import ArgumentParser, RawTextHelpFormatter


def read_json(path):
    from json import load
    with open(path) as fo:
        data = load(fo)
    return data


def read_csv(path):
    from csv import DictReader
    with open(path) as fo:
        data = list(DictReader(fo))
    return data


def read_ini(path):
    from configparser import ConfigParser
    conf = ConfigParser()
    conf.read(path)
    data = {s:dict(conf.items(s)) for s in conf.sections()}
    return data


def read_toml(path):
    from toml import load
    data = load(path)
    return data


def read_yaml(path):
    from yaml import safe_load as load
    with open(path) as fo:
        data = load(fo)
    return data


def read_txt(path):
    for line in open(path):
        yield line.rstrip()


def dump_txt(data):
    from nicely import Printer
    readers = dict(
        json = read_json,
        ini = read_ini,
        toml = read_toml,
        yml = read_yaml,
        yaml = read_yaml,
    )
    for ext in readers:
        confil = expanduser(f'~/caty.{ext}')
        if isfile(confil):
            conf = readers[ext](confil)
            break
    else:
        conf = {}
    Printer(**conf).print(data)


def dump_bin(lines):
    for line in lines:
        print(line)


def get_handlers():
    from binview import dumper as read_bin
    return dict(
        json = (read_json, dump_txt),
        ini = (read_ini, dump_txt),
        csv = (read_csv, dump_txt),
        toml = (read_toml, dump_txt),
        yml = (read_yaml, dump_txt),
        yaml = (read_yaml, dump_txt),
        txt = (read_txt, dump_bin),
        hex = (partial(read_bin, fmt='hex'), dump_bin),
        oct = (partial(read_bin, fmt='oct'), dump_bin),
        dec = (partial(read_bin, fmt='dec'), dump_bin),
        bin = (partial(read_bin, fmt='bin'), dump_bin),
    )


def main():
    ''' Dump the file given as arg.
    '''
    handlers = get_handlers()
    desc = f'''
{main.__doc__}
Supported Formats are :
    {", ".join(sorted(handlers.keys()))}.
    '''
    parser = ArgumentParser(
        description = desc,
        formatter_class = RawTextHelpFormatter,
    )
    parser.add_argument(
        'file',
        help='File to be dumped.'
    )
    parser.add_argument(
        '--format',
        help='''
File format.
Overrule the ext.
May be one of the supported format.
        '''
    )
    args = parser.parse_args()
    path = Path(args.file)
    ext = args.format or path.suffix[1:]
    reader, dumper = handlers.get(ext,  handlers['hex'])
    try:
        data = reader(path)
        dumper(data)
    except Exception as x:
        print(x)

