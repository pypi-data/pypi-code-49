"""Test the Account object."""
#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

from ocean_keeper.account import Account
from tests.resources.helper_functions import get_resource_path


def test_create_account():
    account = Account('0x213123123', 'pass', encrypted_key='0190209129092101920')
    assert isinstance(account, Account)
    assert account.address == '0x213123123'
    assert account.password == 'pass'
    assert account.key == '0190209129092101920'

    account = Account('0x213123123', 'pass', private_key='0190209129092101920')
    assert isinstance(account, Account)
    assert account.address == '0x213123123'
    assert account.password is None
    assert account.key == '0190209129092101920'

    address = '0x00bd138abd70e2f00903268f3db08f2d25677c9e'
    key_file = get_resource_path('data', 'publisher_key_file.json')
    with open(key_file) as f:
        encrypted_key = f.read()
    account = Account(address, 'pass', key_file=key_file)
    assert account.key_file == str(key_file)
    assert account.key == encrypted_key

    account = Account(address, 'pass', key_file=key_file,
                      encrypted_key='encrypted_key')
    assert account.key == 'encrypted_key'

    account = Account(address, 'pass', key_file=key_file,
                      encrypted_key=encrypted_key, private_key='privatekey')
    assert account.key == 'privatekey'
