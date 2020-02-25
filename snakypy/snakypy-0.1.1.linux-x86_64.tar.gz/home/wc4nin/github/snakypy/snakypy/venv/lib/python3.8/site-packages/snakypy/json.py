import json
from os.path import exists


def read(file_path):
    """
    Function that reads JSON configuration file and returns data.

    >>> import snakypy
    >>> file = '/tmp/file.json'
    >>> snakypy.json.read(file)

    Arguments:
        **file_path {str}** -- You must receive the full/absolute file path.

    Returns:
        [dict] -- If the file is found it will return a dictionary
    """

    try:
        with open(file_path) as f:
            data = json.load(f)
        return data
    except FileNotFoundError as err:
        raise FileNotFoundError(f'>>> File not found {err}')
    except Exception:
        raise Exception(f'>>> There was an error reading the file: {file_path}')


def create(dictionary, file_path, force=False):
    """
    Create a JSON file through a dictionary.

    >>> import snakypy
    >>> dic = {'msg': 'Hello, Snakypy!'}
    >>> snakypy.json.create(dic, '/tmp/file.json')
    >>> snakypy.json.create(dic, '/tmp/file.json', force=True)

    Arguments:
        **dictionary {dict}** -- [description]

        **file_path {str}** -- You must receive the full/absolute file path.

    Keyword Arguments:
        **force {bool}** -- Use the True option if you want to overwrite the existing file. \
                            (default: {False})

    Returns:
        **[bool]** -- If everything went well, it will return True.
    """
    from os.path import splitext

    if splitext(file_path)[1] != '.json':
        raise Exception('The JSON file extension was not explicit.')
    if not force and exists(file_path):
        raise FileExistsError(f'>>> The file {file_path} already exists, use force=True.')
    else:
        try:
            if type(dictionary) is dict:
                with open(file_path, 'w') as f:
                    json.dump(dictionary, f, indent=4, separators=(',', ': '))
                    return True
            return False
        except Exception as err:
            raise Exception(f'>>> There was an error creating the file. {err}')


def update(file_path, content: dict):
    """
    Function to update json file. The "snakypy.json.read" function depends on
    reading a json file.

    >>> import snakypy
    >>> data = snakypy.json.read('/tmp/file.json')
    >>> data['msg'] = 'Olá, Snakypy!'
    >>> snakypy.json.update('/tmp/file.json', data)

    Arguments:
        **file_path {str}** -- You must receive the full/absolute file path.

        **content {dict}** -- You should receive a dictionary with the updated data \
                              already.
    Returns:
        **[bool]** -- If everything went well, it will return True.
    """
    try:
        if type(content) is dict:
            with open(file_path, 'w') as f:
                json.dump(content, f, indent=2, separators=(',', ': '))
            return True
        return False
    except Exception as err:
        msg = f'>>> Something unexpected happened while updating {file_path}'
        raise Exception(msg, err)


__all__ = ['read', 'create']
