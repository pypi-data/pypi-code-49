# -*- coding: utf-8 -*-
"""

    Получение информации о том, в каком коммите мы сейчас находимся

"""
# встроенные модули
import subprocess


def get_git_revision_hash(cmd: str = 'git rev-parse HEAD',
                          encoding: str = 'utf-8') -> str:
    """Получить хеш текущего коммита.

    Обращается к системе и получает данные о том,
    какой коммит сейчас является головным для данного репозитория. Исполнение зависит от
    параметров системы и настроек окружения.

    :param cmd: команда для исполнения подпроцессом

    :param encoding: из какой кодировки произвести конвертацию
    (стандартная кодировка терминала на Windows - cp866)

    Пример вывода:
        'aa4d5ef11973828a18425c369e0fdde5fd45c11d'
    """
    pipe = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True
    )
    stdout, stderr = pipe.communicate()
    response = stdout.decode(encoding)

    if response.replace('"', '').replace("'", '').startswith(('git', 'fatal')):
        response = 'unknown'
    else:
        # есть риск получить сюда очень большой блок текста в виде
        # стандартного ответа гита на ввод незнакомой команды
        response = response[:41].strip()

    return response


def get_git_revision_hash_short(cmd: str = 'git rev-parse --short HEAD',
                                encoding: str = 'utf-8') -> str:
    """Получить укороченный хеш текущего коммита.

    :param cmd: команда для исполнения подпроцессом

    :param encoding: из какой кодировки произвести конвертацию
    (стандартная кодировка терминала на Windows - cp866)

    Пример вывода:
        'aa4d5ef'
    """
    return get_git_revision_hash(cmd, encoding)
