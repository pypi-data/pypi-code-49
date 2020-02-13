import re


def find_match(start, end, S, IGNORECASE=True):
    """find the string between `start` and `end` of `S`
    and ignore case
    """
    START = re.search(start, S, re.IGNORECASE).span()[1]
    END = re.search(end, S, re.IGNORECASE).span()[0]
    return S[START:END]

def replace(repl, string, count=1):
    """replace `repl` from `string` count times"""
    strinfo = re.compile(repl, string)
    return strinfo.sub(repl, string, count)
