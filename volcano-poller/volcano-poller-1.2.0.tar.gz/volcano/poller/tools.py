#!/usr/bin/python3

def search(it, cb):
    for x in it:
        if cb(x):
            return x
    return None


def unique_name(prefix, cb):
    ctr = 1
    name = '{}{}'.format(prefix, ctr)
    while not cb(name):
        ctr += 1
        name = '{}{}'.format(prefix, ctr)
    return name
