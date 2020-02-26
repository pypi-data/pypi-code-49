from __future__ import print_function

import os
import string
import secrets


def get_wordlist_path():
    wordlist = os.path.join(os.path.dirname(__file__), "english.txt")

    if not os.path.isfile(wordlist):
        raise Exception("Could not find wordlist")

    return wordlist


def gen_wordlist(length=4, separator="."):
    with open(get_wordlist_path(), "r", encoding="utf-8") as f:
        wordlist = [w.strip() for w in f.readlines()]

    return separator.join(secrets.choice(wordlist) for _ in range(length))


def gen_string(length=16):
    return "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))


def cli():
    print(gen_wordlist(), end="")


if __name__ == "__main__":
    cli()
