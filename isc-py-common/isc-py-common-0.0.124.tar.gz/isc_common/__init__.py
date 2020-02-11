import logging
import os

logger = logging.getLogger(__name__)


def getAttr(o, name, default=None):
    if o is None:
        return default
    return o[name] if name in o else default


def setAttr(o, name, value):
    o[name] = value
    return o


def delAttr(o, name):
    if name in o:
        del o[name]
        return True
    else:
        return False


def isEmptyDict(dictionary):
    for element in dictionary:
        if element:
            return True
        return False


def delete_drive_leter(path):
    path = path.replace(os.path.sep, os.path.altsep)
    if path.find(':') != -1:
        path = (path.split(':')[1]).replace(os.path.sep, os.path.altsep)
        path = ''.join(path)

    if path.startswith(os.altsep):
        return path[1:]
    return path


def get_drive_leter(path):
    path = path.replace(os.path.sep, os.path.altsep)
    if path.find(':') != -1:
        return f"{(path.split(':')[0])}:"
    return None


def replace_alt_set(path):
    return path.replace(os.altsep, os.sep).replace(f'{os.sep}{os.sep}', os.sep)

def replace_sep(path):
    return path.replace(os.sep, os.altsep)


def del_last_not_digit(str):
    res = ''
    flag = False
    for ch in reversed(str):
        if flag or ch.isdigit():
            res += ch
            flag = True

    return res[::-1]


def str_to_bool(s):
    if s in ['True', 'true']:
        return True
    elif s in ['False', 'false']:
        return False
    else:
        raise ValueError(f'{s} is not a good boolean string')


def bool_to_jsBool(value):
    if value == True:
        return "true"
    return "false"

class StackElementNotExist(Exception):
    def __init__(self, *args, **kwargs):  # real signature unknown
        super().__init__('Соответствие не найдено.')

class MultipleStackElement(Exception):
    def __init__(self, *args, **kwargs):  # real signature unknown
        super().__init__('Не однозначный выбор.')

class Stack:

    def __init__(self):
        self.stack = []

    def top(self):
        if len(self.stack) < 1:
            return None
        return self.stack[len(self.stack) - 1]

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def find(self, function):
        return [item for item in self.stack if function(item)]

    def find_one(self, function):
        res = self.find(function=function)
        if len(res) == 0:
            raise StackElementNotExist()
        elif len(res) > 1:
            raise MultipleStackElement()

        return res[0]

    def __str__(self):
        return "\n" + ', '.join([str(item.id) for item in self.stack])
