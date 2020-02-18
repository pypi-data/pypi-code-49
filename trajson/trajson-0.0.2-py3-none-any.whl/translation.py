import json
from os import path
import click #muss installiert werden
import requests as req

__author__ = "Ismael Traoré"
__version__ = "0.0.2"

yandexAPIkey = 'trnsl.1.1.20200211T105049Z.b79a2a613b6b77cd.0a27d6ccd0c1568df588f93c461cdbdbded191da'

@click.group()
def cli():
    """Translate JSON files"""
    pass

@cli.command('trans',short_help="Translating JSON file")
@click.argument('lang')
@click.option('--source',default='de.json',help='Source json file',
              show_default=True)
def trans(lang, source, key=yandexAPIkey):
    try:
        """Translating words from Json file"""
        with open(source) as source_json:
            print('Translating...')
            words_data = json.load(source_json)
            for value in words_data:
                word = words_data[value]
                response = req.post(f"https://translate.yandex.net/api/"
                                    f"v1.5/tr.json/translate?lang={source[:2]}-{lang}&key="
                                    f"{key}&text={word}")
                trans_json = response.json()
                words_data[value] = trans_json['text'][0]

            # saving new {lang}.json file
            with open(f"{lang}.json", 'w') as new_json:
                json.dump(words_data, new_json, ensure_ascii=False, indent=4)
        print(f"Saved new JSOn as {lang}.json in",path.abspath(f'{lang}.json'))

    except Exception as e:
        print(f"Failure occured:\n{type(e)}\n{e}")

@cli.command('codes',short_help='Get language codes')
def codes(key=yandexAPIkey):
    try:
        """Show available language codes"""
        response = req.post(f"https://translate.yandex.net/api/"
                            f"v1.5/tr.json/getLangs?key={key}&ui=de")
        trans_json = response.json()
        count = 0
        strings = ""
        print("Available languages Codes:\n")
        # structure output
        for keys, val in trans_json['langs'].items():
            count += 1
            space = 20 - len(val) - len(keys) - 2
            strings = strings + f'{keys} = {val + space * " "}'
            if count == 4:
                print(strings + '\t')
                count = 0
                strings = ""
    except Exception as e:
        print(f"Failure occured:\n{type(e)}\n{e}")

if __name__ == '__main__':
    cli()