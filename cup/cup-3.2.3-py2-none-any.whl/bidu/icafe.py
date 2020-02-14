#!/usr/bin/env python
# -*- coding: utf-8 -*
# #############################################################
#
#  Copyright (c) Baidu.com, Inc. All Rights Reserved
#
# #############################################################
"""
:authors:
    Guannan Ma maguannan @mythmgn
:description:
    For interacting with icafe spaces and cards.

"""
from __future__ import print_function
import json

from cup import log
from cup.thirdp import requests

ICAFE_API_URL = 'http://icafe.baidu.com/api/v2'
ICAFE_API_DEBUG_URL = 'http://icafebeta.baidu.com/api/v2'
# api_entry=icafe_debug

__all__ = ['ICafe']

class ICafe(object):
    """
    icafe things
    """
    def __init__(self, space_name, username, virtual_pass):
        """
        :space_name:
            space name in icafe
        :username:
            prefix of your email address.  E.g., maguannan  ,
            then the username is maguannan
        :virtual_pass:
            get your virtual pass from http://icafe.baidu.com/users/virtual
        """
        self._func_map = {
            'create': '{0}/space/{1}/issue/new'
        }
        self._username = username
        self._pass = virtual_pass
        self._spaceid = space_name

    # pylint: disable=R0913
    # need so mancy params
    def create_issue(self, title, detail, owner, emailto, card_type='Bug'):
        """
        return (200, response.json()) for success

        :title:
            title of the issue card
        :detail:
            content of the issue
        :owner:
            shoule be the username of your email addrs.
            E.g. maguannan for maguannan
        :emailto:
            list with emails. E.g.
                ['maguannan ', 'file-qa '],
        :card_type:
            'Bug' by default.
        """
        create_fmt = self._func_map['create']
        api_url = create_fmt.format(ICAFE_API_URL, self._spaceid)
        i_headers = {'Content-Type': 'application/json'}
        values = {
            'username': self._username,
            'password': self._pass,
            'issues': [
                {
                    'title': title,
                    'detail': detail,
                    'type': card_type,
                    'fields': {
                        '负责人': owner,
                        '流程状态': '新建'
                    },
                    'notifyEmails': emailto,
                    'creator': owner
                }
            ]
        }
        data = json.dumps(values)
        response = requests.post(
            api_url, data=data, headers=i_headers, timeout=5
        )
        if any([
            response.status_code != 200,
            'status' not in response.json(),
            response.json()['status'] != 200
        ]):
            log.warn(
                'failed to create icafe card, msg:{0}'.format(
                    response.json()
                )
            )
            return (response.status_code, response.json())
        else:
            log.info('succeed to create icafe card')
            return (response.status_code, response.json())


if __name__ == '__main__':
    pass
    # cafe = ICafe('baixin-qa', 'maguannan', '*********')
    # print(cafe.create_issue(
    #     title='test auto log issue no:02',
    #     detail='test as it is',
    #     owner='maguannan',
    #     emailto=['maguannan '],
    #     card_type='Dailybuild问题'
    # ))

# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
