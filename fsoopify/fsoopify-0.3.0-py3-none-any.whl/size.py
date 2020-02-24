# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
# a formatable size for file info
# ----------

UNIT_BYTES = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB')
UNIT_BYTES_LEN = len(UNIT_BYTES)

class Size(int):
    '''
    a formatable size for file info
    '''
    def __str__(self):
        '''
        example: `10000000` => `9.537 MB`
        '''
        level = 0
        size = int(self)
        while size > 1024 and level < UNIT_BYTES_LEN:
            size /= 1024
            level += 1
        return '%.3f %s' % (size, UNIT_BYTES[level])
