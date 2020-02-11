#!/usr/bin/env python3
"""Generate doctest files from AtCoder"""

import argparse
import logging
import os
from urllib import parse

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)


def get_body(url: str, output=False):
    """Parse task page."""

    # TODO: content < 20
    # https://abc100.contest.atcoder.jp/
    if "atcoder.jp" not in url:
        contest = url[:-2]
        url = f"https://atcoder.jp/contests/{contest}/tasks/{url}"

    r = requests.get(url)
    r.raise_for_status()

    bs = BeautifulSoup(r.text, features="html.parser")

    description = bs.find("span", class_="lang-ja") or bs.find(
        "div", id="task-statement"
    )

    body = bs.title.text + "\n" + url + "\n"
    for s in description.find_all("pre"):
        body += s.text

    logging.info(body)

    if output:
        _output(url, body)


def _output(url: str, body: str):
    main_statement = """
def main():
    pass


if __name__ == "__main__":
    main()
"""

    _body = f'"""{body}"""\n\n' + main_statement

    contests, tasks = parse.urlparse(url).path.split("/")[2::2]

    if not os.path.isdir(contests):
        try:
            os.mkdir(contests)
        except IOError:
            raise

    filename = f"{contests}/{tasks}.py"
    if os.path.exists(filename):
        logging.error("The file was not created. File already exists.")
        exit()

    with open(filename, "w", encoding="utf-8") as f:
        logging.info(f"{filename} was created.")
        f.write(_body)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--output", action="store_true")

    args = parser.parse_args()

    get_body(args.url, args.output)


if __name__ == "__main__":
    main()
