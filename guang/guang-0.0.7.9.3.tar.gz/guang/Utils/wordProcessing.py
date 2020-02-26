import re

def find_match(start, end, S, flag=0):
    """find the string between `start` and `end` of `S`
    flag=0 defaults, means no special specification
    flag options:
        re.I    IGNORECASE， 忽略大小写的匹配模式
        re.M    MULTILINE，多行模式, 改变 ^ 和 $ 的行为
        re.S  　DOTALL，此模式下 '.' 的匹配不受限制，可匹配任何字符，包括换行符，也就是默认是不能匹配换行符
        re.X    VERBOSE，冗余模式， 此模式忽略正则表达式中的空白和#号的注释
    """
    try:
        START = re.search(start, S, flags=flag).span()[1]
        END = re.search(end, S, flags=flag).span()[0]
        return S[START:END]
    except:
        print('Do not match anything.')
        return None

def find_match2(pattern, S, flag=0):
    res = re.search(pattern, S, flags=flag)
    return res.group()


def replace(string, beRepl, repl, count=1):
    """replace `beRepl` to 'repl' from `string` count times.
    if count=0, relplace all."""
    pattern = re.compile(beRepl)
    return pattern.sub(repl, string, count)
