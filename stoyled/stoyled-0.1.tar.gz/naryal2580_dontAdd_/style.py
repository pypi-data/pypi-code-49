from sys import exit
from datetime import datetime
import ctypes
from platform import system as osType


if osType() == 'Windows':
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


bold    = '\033[1m'
dim     = '\033[2m'
italic  = '\033[3m'
uline   = '\033[4m'
blink   = '\033[5m'
normal  = '\033[6m'
invert  = '\033[7m'
hidden  = '\033[8m'
strike  = '\033[9m'

red    = '\033[31m'
green  = '\033[32m'
yellow = '\033[33m'
blue   = '\033[34m'
purple = '\033[35m'
cyan   = '\033[36m'

red_l    = '\033[91m'
green_l  = '\033[92m'
yellow_l = '\033[93m'
blue_l   = '\033[94m'
purple_l = '\033[95m'
cyan_l   = '\033[96m'
white    = '\033[97m'

rst = '\033[0m'


def fetchTime():
    now = datetime.now()
    dd = str(now.day)
    mm = str(now.month)
    yyyy = str(now.year)
    HH = str(now.hour)
    MM = str(now.minute)
    SS = str(now.second)
    return dd, mm, yyyy, HH, MM, SS


def fetchFormattedTime():
    now = fetchTime()
    now = now[0]+'.'+now[1]+'.'+now[2]+' '+now[3]+':'+now[4]+':'+now[5]
    return now


def info(text, color=True):
    if color:
        if len(text.split(' -> ')) != 2:
            return '{}[{}*{}] {}{}{}'.format(rst+white,
                                             rst+bold+cyan,
                                             rst+white,
                                             rst+blue_l,
                                             text,
                                             rst)
        else:
            text = text.split(' -> ')
            return '{}[{}*{}]{} {}: {}{}{}'.format(rst+white,
                                                   rst+bold+cyan,
                                                   rst+white,
                                                   rst+blue_l,
                                                   text[0],
                                                   rst+cyan+italic,
                                                   text[1],
                                                   rst)
    else:
        if len(text.split(' -> ')) != 2:
            return '[*] {}'.format(text)
        else:
            text = text.split(' -> ')
            return '[*] {}: {}'.format(text[0], text[1])


def warn(text, color=True):
    if color:
        if len(text.split(' -> ')) != 2:
            return '{}[{}!{}] {}{}{}'.format(rst+white,
                                             rst+bold+yellow_l,
                                             rst+white,
                                             rst+yellow,
                                             text,
                                             rst)
        else:
            text = text.split(' -> ')
            return '{}[{}!{}]{} {}: {}{}{}'.format(rst+white,
                                                   rst+bold+yellow_l,
                                                   rst+white,
                                                   rst+yellow,
                                                   text[0],
                                                   rst+yellow_l+italic,
                                                   text[1],
                                                   rst)
    else:
        if len(text.split(' -> ')) != 2:
            return '[!] {}'.format(text)
        else:
            text = text.split(' -> ')
            return '[!] {}: {}'.format(text[0], text[1])


def good(text, color=True):
    if color:
        if len(text.split(' -> ')) != 2:
            return '{}[{}+{}] {}{}{}'.format(rst+white,
                                             rst+bold+green_l,
                                             rst+white,
                                             rst+green,
                                             text,
                                             rst)
        else:
            text = text.split(' -> ')
            return '{}[{}+{}]{} {}: {}{}{}'.format(rst+white,
                                                   rst+bold+green_l,
                                                   rst+white,
                                                   rst+green,
                                                   text[0],
                                                   rst+green_l+italic,
                                                   text[1],
                                                   rst)
    else:
        if len(text.split(' -> ')) != 2:
            return '[+] {}'.format(text)
        else:
            text = text.split(' -> ')
            return '[+] {}: {}'.format(text[0], text[1])


def bad(text, color=True):
    if color:
        if len(text.split(' -> ')) != 2:
            return '{}[{}-{}] {}{}{}'.format(rst+white,
                                             rst+bold+red_l,
                                             rst+white,
                                             rst+red,
                                             text,
                                             rst)
        else:
            text = text.split(' -> ')
            return '{}[{}-{}]{} {}: {}{}{}'.format(rst+white,
                                                   rst+bold+red_l,
                                                   rst+white,
                                                   rst+red,
                                                   text[0],
                                                   rst+red_l+italic,
                                                   text[1],
                                                   rst)
    else:
        if len(text.split(' -> ')) != 2:
            return '[-] {}'.format(text)
        else:
            text = text.split(' -> ')
            return '[-] {}: {}'.format(text[0], text[1])


def cls():
    print('\033[H\033[J', end='')


def printTakenInput(value, prompt='Prompt', color=True):
    if color:
        x = '{}[{}<{}]{} {}: {}{}{}'.\
          format(rst+white, rst+bold+purple_l, rst+white, rst+purple_l, prompt,
                 rst+italic, value, rst)
    else:
        x = '[<] {}: {}'.format(prompt, value)
    print(x)


def coolInput(prompt='Prompt', color=True):
    try:
        if color:
            prompt = '{}[{}<{}]{} {}: {}'.\
                       format(rst+white, bold+purple_l, rst+white,
                              rst+purple_l, prompt, rst+white+italic)
        else:
            prompt = '[<] {}: '.format(prompt)
        _input = input(prompt)
        if color:
            print('\033[0m', end='')
        return _input
    except KeyboardInterrupt:
        print('\b\b'+'Null'+rst)
        print(bad('Exitting, because recived an Interruption from Keyboard.'))
        coolExit(0)
    except EOFError:
        print('Null'+rst)
        print(bad('Terminating via EOF, actually EOL.'))
        coolExit(0)


def coolExit(exitCode=0, color=True):
    now = fetchFormattedTime()
    print(info('Halted [at] {}'.format(now), color))
    exit(exitCode)
