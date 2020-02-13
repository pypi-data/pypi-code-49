import codecs
from io import StringIO
from pathlib import Path
import colorama
colorama.init()
from colorama import Fore, Back, Style
import click
import csv
import io


def echo_error(message=None, file=None, nl=True, err=True, color=None):
    if message:
        message = f"{Fore.RED}{message}{Fore.RESET}"
    click.echo(message=message, file=file, nl=nl, err=err, color=color)


def echo_warning(message=None, file=None, nl=True, err=True, color=None):
    if message:
        message = f"{Fore.YELLOW}{message}{Fore.RESET}"
    click.echo(message=message, file=file, nl=nl, err=err, color=color)


def get_file_utf8_encoding(file_path: Path):
    first_bytes = min(32, file_path.stat().st_size)
    with file_path.open('rb') as f:
        raw = f.read(first_bytes)
    if raw.startswith(codecs.BOM_UTF8):
        return 'utf-8-sig'
    else:
        return 'utf-8'


def dict2csv(d: dict) -> str:
    csvio: StringIO = io.StringIO(newline='')
    writer = csv.DictWriter(csvio, fieldnames=list(d[next(iter(d))].keys()))
    writer.writeheader()
    for key, item in d.items():
        writer.writerow(item)
    return_value = csvio.getvalue()
    csvio.close()
    return return_value


def csv2dict(csv_file, key_name):
    reader = csv.DictReader(csv_file)
    result = {}
    for d in reader:
        result[d.get(key_name)] = d
    return result
