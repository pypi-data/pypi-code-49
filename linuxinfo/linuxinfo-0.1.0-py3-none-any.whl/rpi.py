#!/usr/bin/env python

from collections import namedtuple
import re
from .helpers import read
from ast import literal_eval


"""
https://www.raspberrypi.org/documentation/hardware/raspberrypi/revision-codes/README.md
uuuuuuuuFMMMCCCCPPPPTTTTTTTTRRRR

Note: As of the 4.9 kernel, all Pis report BCM2835, even those with BCM2836,
BCM2837 and BCM2711 processors. You should not use this string to detect the
processor. Decode the revision code using the information below, or cat
/sys/firmware/devicetree/base/model
"""

RPiInfo = namedtuple("RPiInfo", "type processor memory revision manufacturer flag")

def revision(n):
    return 0b1111 & n

def name(n):
    rpi = {
        0x0: "A",
        0x1: "B",
        0x2: "A+",
        0x3: "B+",
        0x4: "2B",
        0x5: "Alpha (early prototype)",
        0x6: "CM1",
        0x8: "3B",
        0x9: "Zero",
        0xa: "CM3",
        0xc: "Zero W",
        0xd: "3B+",
        0xe: "3A+",
        0xf: "Internal use only",
        0x10: "CM3+",
        0x11: "4B"
    }
    val = 0b11111111 & (n >> 4)
    return rpi[val]

def processor(n):
    p = {
        0: "BCM2835",
        1: "BCM2836",
        2: "BCM2837",
        3: "BCM2711"
    }
    val = 0b1111 & (n >> 12)
    return p[val]

def manufacturer(n):
    m = {
        0: "Sony UK",
        1: "Egoman",
        2: "Embest",
        3: "Sony Japan",
        4: "Embest",
        5: "Stadium"
    }
    val = 0b1111 & (n >> 16)
    return m[val]

def memory(n):
    m = {
        0: "256MB",
        1: "512MB",
        2: "1GB",
        3: "2GB",
        4: "4GB"
    }
    val = 0b111 & (n >> 20)
    return m[val]

def flag(n):
    f = {
        1: "new-style revision",
        0: "old-style revision"
    }
    val = 0b1 & (n >> 23)
    return f[val]

def decode(n):
    return RPiInfo(
        name(n),
        processor(n),
        memory(n),
        revision(n),
        manufacturer(n),
        flag(n)
    )

def find(key, info):
    match = re.search('^{}\s+:\s+(\w+)$'.format(key), info, flags=(re.MULTILINE | re.IGNORECASE))
    if match is None:
        return None
    return match.group(1)


def pi_info():
    cpuinfo = read('/proc/cpuinfo')
    # print(">> ", cpuinfo)
    if cpuinfo is None:
        return None

    n = find("Revision", cpuinfo)
    if n is None:
        return None

    # need to convert the text string to an integer to process it
    n = literal_eval("0x" + n)

    if n is None:
        return None

    return decode(n)
