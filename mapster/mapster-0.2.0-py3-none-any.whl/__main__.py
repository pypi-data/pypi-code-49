import sys
import re
from datetime import date

import click
import toml
from pathlib import Path
import requests

from mapster.tools import get_file_utf8_encoding, echo_error, echo_warning, dict2csv, csv2dict
from . import __version__

SYS_ERROR = 1
SYS_OK = 0

MAIN_MAPSTER_URL = "http://igrek.amzp.pl/"


class Mapster(object):
    def __init__(self, user_name, user_password):
        self._user_name = user_name
        self._user_password = user_password
        self._session: requests.Session = None

    def add_map(self, data):
        if not self._session:
            self._login()
        r = self._session.post(f"{MAIN_MAPSTER_URL}dupa_maps_editsend.php", data=data)
        r.raise_for_status()
        return r.text


    def _login(self):
        if not self._user_name:
            self._user_name = click.prompt('User name')
        if not self._user_password:
            self._user_password = click.prompt('User password')
        self._session = requests.Session()
        r = self._session.post(f"{MAIN_MAPSTER_URL}login.php",
                                   data={'u': self._user_name, 'p': self._user_password, 'cmd': 'login'})
        r.raise_for_status()
        # click.echo(f"{r.content}, {r}")
        # click.echo(f"Cookie: {self._session.cookies.get('mapsterdata', None)}")
        if "Zaloguj" in r.text:
            raise requests.exceptions.HTTPError("Unauthorized")


pass_mapster = click.make_pass_decorator(Mapster)


@click.group()
@click.option('--user-name', envvar='MAPSTER_USERNAME', default='', help='User name')
@click.option('--user-password', envvar='MAPSTER_PASSWORD', default='', help='User password')
@click.version_option(__version__)
@click.pass_context
def cli(ctx, user_name, user_password):
    """Mapster

    To manage maps.

    """
    ctx.obj = Mapster(user_name, user_password)


@cli.group()
def maps():
    """Edit maps"""


@maps.command('create_params_file')
@click.argument('config_file',  required=True, type=click.File('r'))
@click.option('-o', '--output-params-csv-file', type=click.File('wb'), help='File name of output params CSV file.')
@pass_mapster
def maps_create_params_file(mapster: Mapster, output_params_csv_file, config_file):
    """Creates params CSV file from maps set config file"""
    sys.exit(create_csv_params_file(mapster, config_file, output_params_csv_file))


@maps.command('add')
@click.argument('params_csv_file', required=True, type=click.File('r'))
@pass_mapster
def maps_add(mapster: Mapster, params_csv_file):
    """Add maps from parameters in CSV file"""
    sys.exit(add_maps_from_params_csv_file(mapster, params_csv_file))


def add_maps_from_params_csv_file(mapster: Mapster, params_csv_file):
    try:
        maps_params = csv2dict(params_csv_file, key_name='file_img')
    except Exception as e:
        echo_error(f"ERROR: Loading params file. {str(e)}")
        return SYS_ERROR

    for idx, (key, map_param) in enumerate(maps_params.items()):
        try:
            response_txt = mapster.add_map(map_param)
            # click.echo(map_param)
        except Exception as e:
            echo_error(f"ERROR: Creating map for {key} with data: {map_param}. {str(e)}")
        else:
            click.echo(f"Map for {key} created at Mapster.")

    return SYS_OK


def create_csv_params_file(mapster: Mapster, config_file, params_csv_file):
    config = toml.load(config_file)
    config_path: Path = Path(config_file.name).parent
    map_images_list_filename: Path = Path(config_path, config.pop('list', ''))
    if not map_images_list_filename.exists():
        echo_error(f"ERROR: File with list of map images not exists or not set in configuration file.")
        return SYS_ERROR
    else:
        filename_pattern = config.pop('filename_pattern', '')
        p = re.compile(filename_pattern)
        #   click.echo(filename_pattern)
        try:
            encoding = get_file_utf8_encoding(map_images_list_filename)
            maps_configs = {}
            with map_images_list_filename.open("r", encoding=encoding) as f:
                for image_filename in f:
                    image_filename = image_filename.strip()
                    if not image_filename:
                        continue
                    maps_configs[image_filename] = None
                    # click.echo(image_filename)
                    m = p.search(image_filename)
                    if not m:
                        echo_error(f"ERROR: File name: {image_filename} do not match filename_pattern !")
                        continue
                    #   click.echo(f"{m.groupdict()}")
                    map_godlo = config.get('map_godlo', '').format(**m.groupdict())
                    map_title = config.get('map_title', '').format(**m.groupdict())
                    map_date = config.get('map_date', '').format(**m.groupdict())
                    lib_call_no = config.get('lib_call_no', '').format(**m.groupdict())
                    # click.echo(f"{map_godlo}")
                    # mapster.login()
                    maps_configs[image_filename] = {'file_img': image_filename, **config}
                    maps_configs[image_filename]['map_godlo'] = map_godlo
                    maps_configs[image_filename]['map_title'] = map_title.replace('_', ' ')
                    maps_configs[image_filename]['map_date'] = map_date
                    maps_configs[image_filename]['lib_call_no'] = lib_call_no
                    #
                    maps_configs[image_filename]['map_fileaddeddate'] = date.today().strftime('%Y-%m-%d')
                    maps_configs[image_filename]['id'] = 'new'
                    maps_configs[image_filename]['type'] = 0

                    # maps_configs[image_filename]['image_filename'] = image_filename
                    # click.echo(f"{image_filename}: {maps_configs[image_filename]}")
            if None in maps_configs.values():
                echo_warning(f"Params file was't created because of errors. Please check, fix and run again.")
                return SYS_ERROR
            # click.echo(f"{maps_configs.keys()}")
            csv_strings = dict2csv(maps_configs)
            if params_csv_file:
                params_csv_file.write(csv_strings.encode())
            else:
                click.echo(csv_strings)
            return SYS_OK
        except Exception as e:
            echo_error(f"ERROR: {e}")
            import traceback
            traceback.print_exc()
            return SYS_ERROR


if __name__ == '__main__':
    cli()
