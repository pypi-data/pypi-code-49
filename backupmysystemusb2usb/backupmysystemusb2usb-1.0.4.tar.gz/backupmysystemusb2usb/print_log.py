"""
    This software is a part of backupmysystemusb2usb and its functionality is
    to backup one usb key to another usb with the same space disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
from __future__ import print_function


class print_log:
    def __init__(self, log_file):
        self.log_file = log_file

    def add_log(self, message):
        """
        Print to the console and to the temporary file
        """
        self.__add(message, True)

    def add_log_end(self, message):
        """
        Print with end
        """
        self.__add(message, False)

    def __add(self, message, switch):
        """
        Print with end or not
        """
        if switch:
            print(message)
        else:
            print(message, end='')
        try:
            log = open(self.log_file, 'a')
            log.write(message)
            if switch:
                log.write('\n')
            log.close()
        except IOError:
            pass
