# -*- coding: utf-8 -*-
class IHE(object):
    status = 'Global status.'

    __status = {
        'messages': {
            0: 'S: WA.IHE      {f:>20} : status {c}, {m}',
            1: 'E: WA.IHE      {f:>20} : status {c}: {m}',
            2: 'W: WA.IHE      {f:>20} : status {c}: {m}',
        },
        'code': 0,
        'message': '',
        'is_print': True
    }

    __conf = {
        'file': '',
        'path': '',
        'data': {}
    }

    def __init__(self, workspace, is_status, **kwargs):
        print('IHE.__init__()')
        # super(IHE, self).__init__(workspace, is_status, **kwargs)

        # Class self.__status['is_print']
        self.__status['is_print'] = is_status

        # Class self.__conf['path']
        self.__conf['path'] = workspace

    def download(self):
        print('IHE.download()')
