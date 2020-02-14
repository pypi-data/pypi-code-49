"""
A module responsible for parsing saved World of Warcraft item data per account.

This module currently only makes use of the user data from the vanilla patch  
1.12 World of Warcraft (WoW) addon called `Possessions`_. WoW addons and saved 
data are written in the Lua language. Therefore, this module uses a third-party 
Lua expression parser (`slpp`_) to get data into Python. The data is flattened 
and reformatted for higher level processing by users of this module.

.. _Possessions: https://github.com/Road-block/Possessions
.. _slpp: https://github.com/SirAnthony/slpp

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
import os
import re
from collections import abc
from collections import namedtuple

from . slpp import slpp

from . utils._i18n import n_
from . utils import _path


CONTAINER_NAME = {
    0: 'inventory',  # bag: the backpack - your intial 16 slots container
    -1: 'bank',
    -2: 'player',
    -3: 'mail',
    1: 'bag01',
    2: 'bag02',
    3: 'bag03',
    4: 'bag04',
    5: 'bag05',  # bank: bag
    6: 'bag06',  # bank: bag
    7: 'bag07',  # bank: bag
    8: 'bag08',  # bank: bag
    9: 'bag09',  # bank: bag
    10: 'bag10',  # bank: bag
}
"""Mapping from raw container index to container name."""

ITEM_INDEX = {
    'item_id': 0,
    'item_name': 1,
    'item_icon': 2,
    'item_quantity': 3,
    'item_rarity': 4,
}
"""Reverse mapping from item property to raw item index."""

ITEM_RARITY = {
    -1: '',
    0: '0-Poor',
    1: '1-Common',
    2: '2-Uncommon',
    3: '3-Rare',
    4: '4-Epic',
    5: '5-Legendary',
    6: '6-Artifact',
}
"""Mapping from raw item rarity to rarity name."""

POSSESSIONS_VAR = r'^\s*PossessionsData = '
"""Matching pattern for unneeded variable assignment in the Lua text input."""


ItemRecord = namedtuple(
    'ItemRecord', [
        n_('realm'), n_('character'), n_('faction'), n_('gold'), 
        n_('container'), n_('slot_id'), n_('item_id'), n_('item_name'), 
        n_('item_icon'), n_('item_quantity'), n_('item_rarity')])
"""Data type capturing the raw item data from the Possessions addon."""


def check_possessions(wowpath):
    """Checks for the existence of Possessions addon data files.

    Args:
        wowpath (str): path to WoW folder.

    Returns:
        bool: True if files found, False otherwise.
    """
    results = find_possessions(wowpath)
    empty = object()
    return next(results, empty) is not empty


def find_possessions(wowpath):
    """Returns the path information for the Possessions addon raw data files.
    
    Args:
        wowpath (str): path to WoW folder.
    
    Returns:
        :obj:`types.GeneratorType` of :obj:`str`: paths matching Possessions 
        addon data files.
    """
    results = _path.gen_find_file(
        'Possessions.lua',
        os.path.join(wowpath, 'WTF', 'Account'))
    return results


def gen_itemrecord(account_data):
    """Yields item data for output.
    
    Args:
        account_data (dict): converted item data for all characters.
    
    Yields:
        :obj:`ItemRecord`: individual item information.
    """
    filter_for_realms(account_data)
    for realm, characters in sorted(account_data.items()):
        for character, attributes in sorted(characters.items()):
            containers = attributes['items']
            for container_id, container in sorted(containers.items()):
                container_name = CONTAINER_NAME[container_id]
                for slot_id, item in sorted(container.items()):
                    record = ItemRecord(
                        realm,
                        character,
                        attributes['faction'],
                        int(attributes['money']),
                        container_name,
                        int(slot_id),
                        int(item.get(ITEM_INDEX['item_id'], -1)),
                        item.get(ITEM_INDEX['item_name'], ''),
                        item.get(ITEM_INDEX['item_icon'], ''),
                        int(item.get(ITEM_INDEX['item_quantity'], 0)),
                        ITEM_RARITY[item.get(ITEM_INDEX['item_rarity'], -1)])
                    yield record


def filter_for_realms(account_data):
    """Filters out non-realm, non-item information from the raw data.
    
    Args: 
        account_data (dict): Possessions addon data which includes non-item data
    """
    if 'config' in account_data:
        del account_data['config']
    return None


def read(filename):
    """Reads a data file containing a Lua expression and returns item data.
    
    Args:
        filename (str): data file containing a Lua expression.

    Returns:
        :obj:`types.GeneratorType`: generator of :obj:`ItemRecord` item
        information.
    """
    with open(filename, 'rt', encoding='utf_8') as lua_file:
        lua_data = lua_file.read()
    account_data = lua_to_python(lua_data)
    assert isinstance(account_data, abc.Mapping)
    return gen_itemrecord(account_data)


def lua_to_python(lua_data):
    """Translates Lua data to a Python expression and evaluates it.
    
    Item data in the Possessions data file is in this format::
    
        PossessionsData = {
            ["Kronos"] = {
                ["harrypotter"] = {
                    ["items"] = {
                        [1] = {
                            [1] = {
                                [1] = "Thorium Lockbox",
                                [2] = "Interface\\Icons\\INV_Misc_OrnateBox",
                                [3] = 1,
                                [4] = 2,
                                [0] = "5759",
                            },
                            ...
    
    The 'PossessionsData = ' portion, indicating the start of a Lua statement 
    of a variable assignment, is not required and would cause an error. Only the
    right hand side of the assignment, i.e. the Lua expression is needed. This
    function translates the Lua input into a Python expression, evaluates it
    and so produces Python item data in its 'raw' format.
    
    Args:
        lua_data (str): text containing a Lua statement.

    Returns:
        dict: item data in raw format.
    """
    lua_expression = lua_statement_to_expression(lua_data)
    lua = slpp.SLPP()
    python_data = lua.decode(lua_expression)
    return python_data


def lua_statement_to_expression(lua_statement):
    """Converts the Lua text to a Lua expression.
    
    Args:
        lua_statement (str): Lua statement containing a single known variable
            assignment.
        
    Returns:
        str: text containing a Lua expression.
    """
    lua_expression = re.sub(POSSESSIONS_VAR, '', lua_statement)
    return lua_expression
