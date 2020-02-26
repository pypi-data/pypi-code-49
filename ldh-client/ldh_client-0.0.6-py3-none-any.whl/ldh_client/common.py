#!/usr/bin/env python3
# Copyright 2017-2020 Purism SPC
# SPDX-License-Identifier: AGPL-3.0-or-later

import ldh_client
import re

from getpass import getpass

# define strings that use defaults
ADDRESS_PROMPT = "Enter your " + str(ldh_client.DEFAULT["HOST_LABEL"]) + " address: "
PASSPHRASE_PROMPT = "Enter your passphrase: "


class LdhCredential(object):
    """User credentials for an LDH account."""

    def __init__(self, user, host, passphrase):
        self.user = user
        self.host = host
        self.passphrase = passphrase

    def __str__(self):
        return self.address + " : '" + self.passphrase + "'"

    @property
    def address(self):
        return self.user + "@" + self.host


class LdhError(Exception):
    """Base class for LDH-related errors."""

    def __init__(self, message):
        self.message = message


def prompt_for_credentials():
    """Prompts the user until they enter valid credentials. Returns a valid LdhCredential."""

    valid_address = False

    while not valid_address:
        address = input(ADDRESS_PROMPT)
        regex = r"^[A-Za-z][A-Za-z0-9]*@[A-Za-z0-9]+(\.[A-Za-z0-9]+)+$"
        if not re.match(regex, address):
            print(address + " is not a valid email address.")
        else:
            valid_address = True

    (user, host) = address.split("@")
    passphrase = getpass(PASSPHRASE_PROMPT)

    return LdhCredential(user, host, passphrase)
