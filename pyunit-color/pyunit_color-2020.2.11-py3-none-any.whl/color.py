#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/2/11 13:30
# @Author: Jtyoui@qq.com
from colorama import init, Fore, Back, Style

init(autoreset=True)


class FontColor:

    @staticmethod
    def red(s):
        """红色"""
        return Fore.RED + str(s)

    @staticmethod
    def green(s):
        """绿色"""
        return Fore.GREEN + str(s)

    @staticmethod
    def yellow(s):
        """黄色"""
        return Fore.YELLOW + str(s)

    @staticmethod
    def blue(s):
        """蓝色"""
        return Fore.BLUE + str(s)

    @staticmethod
    def magenta(s):
        """洋红色"""
        return Fore.MAGENTA + str(s)

    @staticmethod
    def cyan(s):
        """青色"""
        return Fore.CYAN + str(s)

    @staticmethod
    def white(s):
        """白色"""
        return Fore.WHITE + str(s)

    @staticmethod
    def black(s):
        """黑色"""
        return Fore.BLACK + str(s)

    @staticmethod
    def warning(s):
        """警告色"""
        return Style.BRIGHT + Fore.BLACK + Back.YELLOW + "WARNING: " + str(s)

    @staticmethod
    def error(s):
        """错误色"""
        return Style.BRIGHT + Fore.RED + Back.CYAN + "ERROR: " + str(s)

    @staticmethod
    def success(s):
        """成功色"""
        return Style.BRIGHT + Fore.BLACK + Back.GREEN + "SUCCESS: " + str(s)
