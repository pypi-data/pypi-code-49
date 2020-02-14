import yaml
from yaml.error import YAMLError
import os
from yaml import FullLoader, dump

import_key = 'import'


def load(steam):
    try:
        r_steam = _make_import_steam(steam)
        data = _load(r_steam)
        if data.get(import_key):
            data.pop(import_key)
        return data
    except YAMLError as e:
        raise e


def _load(steam):
    return yaml.load(steam, Loader=FullLoader)


def _find_import_tag(path):
    base_path = os.getcwd()
    file_path = os.path.join(base_path, path)
    if os.path.exists(file_path):
        with open(file_path, encoding='utf8') as f:
            return f.read()
    return


def _make_import_steam(steam: str):
    if steam.startswith(import_key):
        steam_list = steam.split('\n')
        import_steam = [steam_list[0]]
        steam_list.pop(0)
        for idx, item in enumerate(steam_list):

            if '-' in item:

                import_steam.append(item)
            else:
                break

        import_val = _load('\n'.join(import_steam)).get(import_key)
        if isinstance(import_val, str):
            a_steam = _find_import_tag(import_val)
            a_steam = _make_import_steam(a_steam)
            steam = a_steam + steam
        elif isinstance(import_val, list):
            a_steams = []
            for val in import_val:
                a_steam = _find_import_tag(val)
                a_steam = _make_import_steam(a_steam)
                if a_steam:
                    a_steams.append(a_steam)
            if a_steams:
                steam = '\n'.join(a_steams) + '\n' + steam

        return steam
    else:
        return steam
