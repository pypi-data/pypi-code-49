#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
auth.py


Created by Swen Vermeul on Feb 26th 2018
Copyright (c) 2018 ETH Zuerich All rights reserved.
"""

import os
import pwd
import re

from jupyterhub.auth import LocalAuthenticator
from tornado import gen
from traitlets import Unicode, Bool

from pybis.pybis import Openbis



class OpenbisAuthenticator(LocalAuthenticator):
    server_url = Unicode(
        config=True,
        help='URL of openBIS server to contact'
    )

    verify_certificates = Bool(
        config=True,
        default_value=True,
        help='Should certificates be verified? Normally True, but maybe False for debugging.'
    )

    valid_username_regex = Unicode(
        r'^[a-z][.a-z0-9_-]*$',
        config=True,
        help="""Regex to use to validate usernames before sending to openBIS."""
    )


    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        password = data['password']

        # Protect against invalid usernames as well as LDAP injection attacks
        if not re.match(self.valid_username_regex, username):
            self.log.warn('Invalid username')
            return None

        # No empty passwords!
        if password is None or password.strip() == '':
            self.log.warn('Empty password')
            return None


        openbis = Openbis(self.server_url, verify_certificates=self.verify_certificates)
        try:
            # authenticate against openBIS and store the token (if possible)
            openbis.login(username, password)
            # creating user if not found on the system, custom logic
            if self.create_system_users:
                try:
                    user = pwd.getpwnam(username)
                except KeyError:
                    self.create_user(username)
            #
            return {
                "name": username,
                "auth_state": {
                    "token": openbis.token,
                    "url": openbis.url,
                }
            }
        except ValueError as err:
            self.log.warn(str(err))
            return None


    @gen.coroutine
    def pre_spawn_start(self, user, spawner):
        """Pass openbis token to spawner via environment variable"""
        auth_state = yield user.get_auth_state()
        if not auth_state:
            # auth_state not enabled
            return

        # Write the openBIS token to the users' environment variables
        spawner.environment['OPENBIS_URL'] = auth_state['url']  
        spawner.environment['OPENBIS_TOKEN'] = auth_state['token']  


    def get_new_uid_for_home(self, os_home):
        id_sequence = 999; # Linux uids start at 1000
        for file in next(os.walk(os_home))[1]:
            home_info = os.stat(os_home + file)
            if home_info.st_uid > id_sequence:
                id_sequence = home_info.st_uid
            if home_info.st_gid > id_sequence:
                id_sequence = home_info.st_gid
        if id_sequence is None:
            return None
        else:
            return { "uid" : id_sequence + 1 }

    def create_user(self, username):
        os_home = "/home/" # Default CentOS home as used at the ETHZ
        home = os_home + username
        useradd = "useradd " + username
        if os.path.exists(home): # If the home exists
            home_info = os.stat(home)
            home_uid = home_info.st_uid
            useradd = useradd + " --uid " + str(home_uid) + " -G jupyterhub"
        elif os.path.exists(os_home):
            new_uid = self.get_new_uid_for_home(os_home)
            if new_uid is not None:
                useradd = useradd + " --uid " + str(new_uid["uid"]) + " -G jupyterhub"
        os.system(useradd)
