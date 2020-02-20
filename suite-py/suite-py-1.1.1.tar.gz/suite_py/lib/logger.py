# -*- encoding: utf-8 -*-
from termcolor import colored

from suite_py.lib.singleton import Singleton


class Logger(metaclass=Singleton):
    def __init__(self):
        pass

    def info(self, message):
        print(colored(message, "green"))

    def warning(self, message):
        print(colored(message, "yellow"))

    def error(self, message):
        print(colored(message, "red"))
