"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import yaml
from . import const


class backup_system:
    def __init__(self, path):
        print(const.TTY_YML_TRY % (path))
        if path is None or path == '':
            self.path = 'config.yml'
        else:
            self.path = path
        with open(self.path, 'r') as stream:
            try:
                self.data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(const.TTY_YML_FAILED)
                print(exc)
