"""
A module for creating user-friendly views of WoW account item data.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
import re
from collections import namedtuple
from operator import itemgetter

from . account import AccountItemRecord as RawViewRecord
from . utils._i18n import n_
from . utils._iterable import multisort_by_attribute


CONTAINER_LOCATION = {
    'inventory': 'bags',
    'bank': 'bank',
    'player': 'player',
    'mail': 'mail',
    'bag01': 'bags',
    'bag02': 'bags',
    'bag03': 'bags',
    'bag04': 'bags',
    'bag05': 'bank',  # bank: bag
    'bag06': 'bank',  # bank: bag
    'bag07': 'bank',  # bank: bag
    'bag08': 'bank',  # bank: bag
    'bag09': 'bank',  # bank: bag
    'bag10': 'bank',  # bank: bag
}
"""Mapping from container to generalized location."""

DATAVIEWS = (
    'character', 'location', 'mail', 'item', 'worn', 'gold', 'factiongold', 
    'raw')
"""List of available dataviews."""

EQUIPPED_SLOT_NAME = {
    1: '01-Head',
    2: '02-Neck',
    3: '03-Shoulders',
    4: '04-Back',
    5: '05-Chest',
    6: '06-Shirt',
    7: '07-Tabard',
    8: '08-Wrist',
    9: '09-Hands',
    10: '10-Waist',
    11: '11-Legs',
    12: '12-Feet',
    13: '13-Ring1',
    14: '14-Ring2',
    15: '15-Trinket1',
    16: '16-Trinket2',
    17: '17-Main Hand',
    18: '18-Off Hand',
    19: '19-Ranged',
    20: '20-Ammo',
}
"""Mapping from raw slot id of an equipped slot to slot name"""

ITEM_LINK_FORMAT = {
    'id': '{}',
    'twinhead': 'https://vanilla-twinhead.twinstar.cz/?item={}',
    'wowhead': 'https://classic.wowhead.com/item={}',
    'classicdb': 'https://classicdb.ch/?item={}',
}
"""Mapping from item link format to the link representation."""

PRESENTATION_FORMATS = {
    'gold': {'gold', 'factiongold'},
    'numerical': {'item_quantity', 'gold', 'factiongold', 'item_id', 'slot_id'},
    'url': {'item_link'}
}
"""Mapping from presentation format to set of Possessions data fields."""

CharacterViewRecord = namedtuple(
    'CharacterViewRecord', [
        n_('realm'), n_('account'), n_('faction'), n_('character'), 
        n_('item_name'), n_('item_rarity'), n_('item_quantity'), 
        n_('item_link')])
"""Data type for the 'character' dataview."""

LocationViewRecord = namedtuple(
    'LocationViewRecord', [
        n_('realm'), n_('account'), n_('faction'), n_('character'), 
        n_('item_name'), n_('item_rarity'), n_('item_quantity'), n_('location'), 
        n_('item_link')])
"""Data type for the 'location' dataview."""

MailViewRecord = namedtuple(
    'MailViewRecord', [
        n_('realm'), n_('account'), n_('faction'), n_('character'), 
        n_('item_name'), n_('item_quantity'), n_('location')])
"""Data type for the 'mail' dataview."""

ItemViewRecord = namedtuple(
    'ItemViewRecord', [
        n_('realm'), n_('item_name'), n_('item_rarity'), n_('item_quantity'), 
        n_('max'), n_('item_link')])
"""Data type for the 'item' dataview."""

WornViewRecord = namedtuple(
    'WornViewRecord', [
        n_('realm'), n_('account'), n_('faction'), n_('character'), n_('slot'), 
        n_('item_name'), n_('item_rarity'), n_('item_link')])
"""Data type for the 'worn' dataview."""

GoldViewRecord = namedtuple(
    'GoldViewRecord', [
        n_('realm'), n_('account'), n_('faction'), n_('character'), n_('gold')])
"""Data type for the 'gold' dataview."""

FactionGoldViewRecord = namedtuple(
    'FactionGoldViewRecord', [n_('realm'), n_('faction'), n_('gold')])
"""Data type for the 'factiongold' dataview."""


class DataViewFactory(object):
    """Factory for DataView objects based on view name."""
    def __init__(self):
        """Initializes the factory class with a dispatch table.
        
        The dispatch table maps view names to view generator functions and the
        view fields.
        """
        self.Attributes = namedtuple(
            'Attributes', ['header_fields', 'data_gen'])
        self._table = {
            'character': self.Attributes(
                CharacterViewRecord._fields, gen_view_character),
            'location': self.Attributes(
                LocationViewRecord._fields, gen_view_location),
            'mail': self.Attributes(
                MailViewRecord._fields, gen_view_mail),
            'item': self.Attributes(
                ItemViewRecord._fields, gen_view_item),
            'worn': self.Attributes(
                WornViewRecord._fields, gen_view_worn),
            'gold': self.Attributes(
                GoldViewRecord._fields, gen_view_gold),
            'factiongold': self.Attributes(
                FactionGoldViewRecord._fields, gen_view_factiongold),
            'raw': self.Attributes(
                RawViewRecord._fields, gen_view_raw),
        }

    def dispatch(self, view_name, input_data, args):
        """Returns a Dataview object based on view name.
        
        Args:
            view_name (str): view name.
            input_data (:obj:`types.GeneratorType`): raw input data generator.
            args (:obj:`argparse.Namespace`): program arguments.
        
        Returns:
            DataView: dataview object.
        """
        view_type = self._table[view_name]
        return DataView(
            view_type.header_fields, view_type.data_gen(input_data, args))


class DataView(object):
    """Represents a dataview type.
    
    Attributes:
        header (tuple): tuple of strings listing the view field names.
        data (:obj:`types.GeneratorType`): view data generator.
    """
    def __init__(self, header, data):
        self.header = header
        self.data = data

    def __iter__(self):
        return self.data


class ItemHolders(object):
    """Utility class identifying the character with max. count for an item.
    
    Attributes:
        holders (dict): dicionary with character name key, item quantity value.
    """
    def __init__(self, holder, quantity):
        self.holders = {holder: quantity}

    def update(self, holder, quantity):
        """Updates the item count for a given character name.
        
        Args:
            holder (str): character name.
            quantity (int): item count.
        """
        if holder in self.holders:
            self.holders[holder] += quantity
        else:
            self.holders[holder] = quantity

    def max(self):
        """Returns the maximum item count and associated character name."""
        return max(zip(self.holders.values(), self.holders.keys()))


def query_dataview(input_data, args):
    """Creates and queries a dataview.
    
    Args:
        input_data (:obj:`types.GeneratorType`): raw input data generator.
        args (:obj:`argparse.Namespace`): program arguments.
        
    Return:
        :obj:`types.GeneratorType`: filtered view data based on a query.
    """
    view = create_view(input_data, args)
    return search(view, args.search)


def create_view(input_data, args, called_view=None):
    """Creates a dataview from raw input data.
    
    Args:
        input_data (:obj:`types.GeneratorType`): raw input data generator.
        args (:obj:`argparse.Namespace`): program arguments.
        
    Return:
        DataView: dataview object.
    """
    factory = DataViewFactory()
    if called_view in DATAVIEWS:
        return factory.dispatch(called_view, input_data, args)
    if args.view in DATAVIEWS:
        return factory.dispatch(args.view, input_data, args)
    return factory.dispatch('character', input_data, args)


def gen_view_character(input_data, args):
    """Yields data for a 'character' dataview.
    
    Args:
        input_data (:obj:`types.GeneratorType`): raw input data generator.
        args (:obj:`argparse.Namespace`): program arguments.

    Yields:
        :obj:`CharacterViewRecord`: 'character' view data.
    """
    aggregate = {}
    for raw_row in input_data:
        row = RawViewRecord(*raw_row)
        if row.container == 'mail' and not args.include_mail:
            continue
        # Creates a "group-by" data structure based on composite key of a dict
        key = '='.join(
            [row.realm, row.account, row.faction, row.character, row.item_name])
        if key in aggregate:
            aggregate[key][0] = aggregate[key][0] or row.item_rarity
            aggregate[key][1] += row.item_quantity
            aggregate[key][2] = aggregate[key][2] or row.item_id
        else:
            aggregate[key] = [row.item_rarity, row.item_quantity, row.item_id]

    for key, value in sorted(aggregate.items()):
        (realm, account, faction, character, item_name) = key.split('=')
        yield CharacterViewRecord(
            realm, 
            account,
            faction,
            character, 
            item_name, 
            value[0],  # item_rarity
            value[1],  # item_quantity
            format_item_link(value[2], args.db),  # item_link
        )


def gen_view_location(input_data, args, only_mail=False):
    """Yields data for a 'location' dataview.
    
    Args:
        input_data (:obj:`types.GeneratorType`): raw input data generator.
        args (:obj:`argparse.Namespace`): program arguments.

    Yields:
        :obj:`LocationViewRecord`: 'location' view data.
    """
    aggregate = {}
    for raw_row in input_data:
        row = RawViewRecord(*raw_row)
        if only_mail and row.container != 'mail':
            continue
        location = CONTAINER_LOCATION[row.container]
        # Creates a "group-by" data structure based on composite key of a dict
        key = '='.join(
            [
                row.realm, row.account, row.faction, row.character, 
                row.item_name, location
            ])
        if key in aggregate:
            aggregate[key][0] = aggregate[key][0] or row.item_rarity
            aggregate[key][1] += row.item_quantity
            aggregate[key][2] = aggregate[key][2] or row.item_id
        else:
            aggregate[key] = [row.item_rarity, row.item_quantity, row.item_id]

    results = []
    for key, value in aggregate.items():
        (
            realm, account, faction, character, item_name, 
            location) = key.split('=')
        results.append(
            LocationViewRecord(
                realm, 
                account,
                faction,
                character, 
                item_name, 
                value[0],  # item_rarity
                value[1],  # item_quantity
                location,
                format_item_link(value[2], args.db)))  # item_link

    multisort_by_attribute(
        results, 
        (
            ('realm', False), ('account', False), ('faction', False), 
            ('character', False), ('item_name', False), 
            ('item_quantity', True)))
    for row in results:
        yield row


def gen_view_mail(input_data, args):
    """Yields data for a 'mail' dataview.
    
    Args:
        input_data (:obj:`types.GeneratorType`): raw input data generator.
        args (:obj:`argparse.Namespace`): program arguments.

    Yields:
        :obj:`MailViewRecord`: 'mail' view data.
    """
    aggregate = {}
    for raw_row in input_data:
        row = RawViewRecord(*raw_row)
        if row.container != 'mail':
            continue
        location = CONTAINER_LOCATION[row.container]
        # Creates a "group-by" data structure based on composite key of a dict
        key = '='.join(
            [
                row.realm, row.account, row.faction, row.character, 
                row.item_name, location
            ])
        if key not in aggregate:
            aggregate[key] = 0
        aggregate[key] += row.item_quantity

    results = []
    for key, value in aggregate.items():
        (realm, account, faction, character, item_name, 
            location) = key.split('=')
        results.append(
            MailViewRecord(
                realm, 
                account,
                faction,
                character, 
                item_name, 
                value,  # item_quantity
                location))

    multisort_by_attribute(
        results, 
        (
            ('realm', False), ('account', False), ('faction', False), 
            ('character', False), ('item_name', False), 
            ('item_quantity', True)))
    for row in results:
        yield row


def gen_view_item(input_data, args):
    """Yields data for an 'item' dataview.
    
    Args:
        input_data (:obj:`types.GeneratorType`): raw input data generator.
        args (:obj:`argparse.Namespace`): program arguments.

    Yields:
        :obj:`ItemViewRecord`: 'Item' view data.
    """
    aggregate = {}
    for raw_row in input_data:
        row = RawViewRecord(*raw_row)
        if row.container == 'mail' and not args.include_mail:
            continue
        # Only interested in stored items (not equipped)
        if row.container == 'player':
            continue
        item_key = '='.join(
            [row.realm, row.item_name, row.item_rarity, str(row.item_id)])
        character_key = '='.join([row.account, row.character])
        if item_key in aggregate:
            entry = aggregate[item_key]
            entry['total'] += row.item_quantity
            entry['holders'].update(character_key, row.item_quantity)
        else:
            aggregate[item_key] = { 
                'total': row.item_quantity,
                'holders': ItemHolders(character_key, row.item_quantity)}

    for item_key, value in sorted(aggregate.items()):
        (realm, item_name, item_rarity, item_id_str) = item_key.split('=')
        item_id = int(item_id_str)
        max_quantity, max = value['holders'].max()
        (account, character) = max.split('=')
        yield ItemViewRecord(
            realm,
            item_name,
            item_rarity,
            value['total'],
            '{} - {} ({})'.format(character, account, max_quantity),
            format_item_link(item_id, args.db)
        )


def gen_view_worn(input_data, args):
    """Yields data for a 'worn' dataview.
    
    Args:
        input_data (:obj:`types.GeneratorType`): raw input data generator.
        args (:obj:`argparse.Namespace`): program arguments.

    Yields:
        :obj:`WornViewRecord`: 'worn' view data.
    """
    aggregate = {}
    results = []
    for raw_row in input_data:
        row = RawViewRecord(*raw_row)
        # Only interested in player equipped items
        if row.container != 'player':
            continue
        rarity_value = 0
        if row.item_rarity:
            rarity_value = int(row.item_rarity[0])
        # Creates a "group-by" data structure based on composite key of a dict
        key = '='.join([row.realm, row.character])
        if key in aggregate:
            aggregate[key] += rarity_value
        else:
            aggregate[key] = rarity_value
        results.append(
            WornViewRecord(
                row.realm,
                row.account,
                row.faction,
                row.character,
                EQUIPPED_SLOT_NAME.get(
                    row.slot_id, '{}-Unknown'.format(row.slot_id)),
                row.item_name,
                row.item_rarity,
                format_item_link(row.item_id, args.db))
        )

    def sort_by_totalrarity(row):
        key = '='.join([row.realm, row.character])
        return aggregate[key]

    multisort_by_attribute(
        results, 
        (
            ('realm', False), ('faction', False), ('character', False), 
            ('slot', False)))
    results.sort(key=sort_by_totalrarity, reverse=True)
    for row in results:
        yield row


def format_item_link(item_id, db_name):
    """Formats an item id as an item link based on a format name.
    
    Args:
        item_id (int): item id.
        db_name (str): format name.

    Returns:
        string: item link.
    """
    if item_id > 0:
        return ITEM_LINK_FORMAT[db_name].format(str(item_id))
    return ''


def gen_view_gold(input_data, args):
    """Yields data for a 'gold' dataview.
    
    Args:
        input_data (:obj:`types.GeneratorType`): raw input data generator.
        args (:obj:`argparse.Namespace`): program arguments.

    Yields:
        :obj:`GoldViewRecord`: 'gold' view data.
    """
    aggregate = {}
    for raw_row in input_data:
        row = RawViewRecord(*raw_row)

        # Creates a "group-by" data structure based on composite key of a dict
        key = '='.join([row.realm, row.account, row.faction, row.character])
        if key not in aggregate:
            # The gold is the same for every item row on a character
            aggregate[key] = row.gold 

    for key, value in sorted(
            aggregate.items(), key=itemgetter(1), reverse=True):
        (realm, account, faction, character) = key.split('=')
        yield GoldViewRecord(
            realm, 
            account,
            faction,
            character, 
            value,
        )


def gen_view_factiongold(input_data, args):
    """Yields data for a 'factiongold' dataview.
    
    Args:
        input_data (:obj:`types.GeneratorType`): raw input data generator.
        args (:obj:`argparse.Namespace`): program arguments.

    Yields:
        :obj:`FactionGoldViewRecord`: 'factiongold' view data.
    """
    aggregate = {}
    seen = {}
    for raw_row in input_data:
        row = RawViewRecord(*raw_row)
        # Creates a "group-by" data structure based on composite key of a dict
        groupby_key = '='.join([row.realm, row.faction])
        character_key = '='.join([row.realm, row.character])
        if groupby_key in aggregate:
            # The gold is the same for every item row on a character
            if character_key not in seen:
                aggregate[groupby_key] += row.gold
                seen[character_key] = True
        else:
            aggregate[groupby_key] = row.gold
            seen[character_key] = True

    for key, value in sorted(
            aggregate.items(), key=itemgetter(1), reverse=True):
        (realm, faction) = key.split('=')
        yield FactionGoldViewRecord(
            realm, 
            faction,
            value,
        )


def gen_view_raw(input_data, args):
    """Yields data for a 'raw' dataview.
    
    Args:
        input_data (:obj:`types.GeneratorType`): raw input data generator.
        args (:obj:`argparse.Namespace`): program arguments.

    Yields:
        :obj:`RawViewRecord`: 'raw' view data.
    """
    return input_data


def search(input_data, pattern):
    """Searches nested data for a pattern returning a list of matches.
    
    Args:
        input_data: generator for list of tuples or a sequence of tuples.
        pattern (str): regular expression pattern.
        
    Yield:
        tuple: data row of fields.
    """
    for row in input_data:
        for item in row:
            if re.search(pattern, str(item), re.IGNORECASE):
                yield row
                break
