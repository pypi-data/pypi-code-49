# -*- coding: utf-8 -*-
class Template(object):
    status = 'Global status.'

    __status = {}
    __conf = {}

    def __init__(self, status, config, **kwargs):
        print('Template.__init__()')
        # super(IHE, self).__init__(status, config, **kwargs)

        # Class self.__status < Download.__status
        self.__status = status

        # Class self.__conf <- Download.__conf
        self.__conf = config

    def download(self):
        from pprint import pprint
        print('Template.download()')
        print('\n=> Template.__status')
        pprint(self.__status)
        print('\n=> Template.__conf.time')
        pprint(self.__conf['time'])
        print('\n=> Template.__conf.log')
        pprint(self.__conf['log'])
        print('\n=> Template.__conf.path')
        pprint(self.__conf['path'])
        print('\n=> Template.__conf.account')
        pprint(self.__conf['account'])
        print('\n=> Template.__conf.product')
        pprint(self.__conf['product'])
        print('\n=> Template.__conf.template')
        pprint(self.__conf['template'])
