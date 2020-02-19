import os


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


def isEmptyDict(dictionary):
    for element in dictionary:
        if element:
            return True
        return False


def delete_drive_leter(path: object) -> object:
    path = path.replace(os.path.sep, os.path.altsep)
    if path.find(':') != -1:
        path = (path.split(':')[1]).replace(os.path.sep, os.path.altsep)
        path = ''.join(path)

        if path.startswith(os.altsep):
            return path[1:]
        return path
    else:
        if path.startswith(os.altsep):
            return path[1:]
        return path

def get_drive_leter(path: object) -> str:
    path = path.replace(os.path.sep, os.path.altsep)
    if path.find(':') != -1:
        return f"{(path.split(':')[0])}:"
    return None
