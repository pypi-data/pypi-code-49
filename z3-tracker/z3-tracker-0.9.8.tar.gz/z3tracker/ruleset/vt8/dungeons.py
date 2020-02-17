'''
Dungeons
'''

__all__ = 'LOCATIONS',


LOCATIONS = {
    'Castle Dungeons': {
        'type': 'drop', 'map': 'light', 'coord': (332, 290),
        'keypools': [],
        'link': {
            "Zelda's Treasure": []}
    },
    'East Palace': {
        'type': 'dungeon', 'map': 'light', 'coord': (636, 251),
        'keypools': [],
        'link': {}
    },
    'Desert Palace': {
        'type': 'dungeon', 'map': 'light', 'coord': (49, 528),
        'keypools': [
            {'type': 'small', 'settings': (), 'keys': 1,
             'chests': ('Desert Palace Map', 'Desert Palace Small Key')},
            {'type': 'big', 'settings': (),
             'chests': (
                 'Desert Palace Compass', 'Desert Palace Big Key',
                 'Desert Palace Map', 'Desert Palace Small Key')}],
        'link': {}
    },
    'Mountain Tower': {
        'type': 'dungeon', 'map': 'light', 'coord': (372, 14),
        'keypools': [
            {'type': 'small', 'settings': (), 'keys': 1,
             'chests': ('Mountain Tower Small Key', 'Mountain Tower Map')},
            {'type': 'big', 'settings': (),
             'chests': (
                 'Mountain Tower Small Key', 'Mountain Tower Map',
                 'Mountain Tower Big Key')}],
        'link': {}
    },
    'Castle Tower': {
        'type': 'dungeon', 'map': 'light', 'coord': (332, 244),
        'keypools': [
            {'type': 'small', 'settings': (), 'keys': 1,
             'chests': ('Castle Tower First Chest',)},
            {'type': 'small', 'settings': (), 'keys': 1,
             'chests': (
                 'Castle Tower First Chest', 'Castle Tower Seconds Chest')}],
        'link': {}
    },
    'Dark Palace': {
        'type': 'dungeon', 'map': 'dark', 'coord': (629, 241),
        'keypools': [
            {'type': 'small', 'settings': (), 'keys': 4,
             'chests': (
                 'Dark Palace First Key', 'Dark Palace Key With A View',
                 'Dark Palace Map', 'Dark Palace Big Key',
                 'Dark Palace Stalfos Key', 'Dark Palace Targetting Chest')},
            {'type': 'small', 'settings': (), 'keys': 2,
             'chests': (
                 'Dark Palace First Key', 'Dark Palace Key With A View',
                 'Dark Palace Map', 'Dark Palace Big Key',
                 'Dark Palace Stalfos Key', 'Dark Palace Targetting Chest',
                 'Dark Palace Treasury Left Chest',
                 'Dark Palace Treasury Right Chest','Dark Palace Compass')}],
        'link': {}
    },
    'Swamp Palace': {
        'type': 'dungeon', 'map': 'dark', 'coord': (304, 600),
        'keypools': [
            {'type': 'small', 'settings': (), 'keys': 1,
             'chests': ('Swamp Palace Key',)}],
        'link': {}
    },
    'Skull Woods': {
        'type': 'dungeon', 'map': 'dark', 'coord': (20, 22),
        'keypools': [],
        'link': {}
    },
    "Thieves' Town": {
        'type': 'dungeon', 'map': 'dark', 'coord': (77, 301),
        'keypools': [],
        'link': {}
    },
    'Ice Palace': {
        'type': 'dungeon', 'map': 'dark', 'coord': (523, 552),
        'keypools': [],
        'link': {}
    },
    'Misery Mire': {
        'type': 'dungeon', 'map': 'dark', 'coord': (43, 532),
        'keypools': [],
        'link': {}
    },
    'Turtle Rock': {
        'type': 'dungeon', 'map': 'dark', 'coord': (618, 33),
        'keypools': [
            {'type': 'small', 'settings': ('open',), 'keys': 1,
             'chests': (
                 'Turtle Rock Compass', 'Turtle Rock Map',
                 'Turtle Rock Map Key')},
            {'type': 'small', 'settings': ('open',), 'keys': 1,
             'chests': (
                 'Turtle Rock Compass', 'Turtle Rock Map',
                 'Turtle Rock Map Key', 'Turtle Rock Chain Chomp Key')},
            {'type': 'small', 'settings': ('open',), 'keys': 1,
             'chests': (
                 'Turtle Rock Compass', 'Turtle Rock Map',
                 'Turtle Rock Map Key', 'Turtle Rock Chain Chomp Key',
                 'Turtle Rock Big Key', 'Turtle Rock Treasure',
                 'Turtle Rock Switch Key')},
            {'type': 'small', 'settings': ('open',), 'keys': 1,
             'chests': (
                 'Turtle Rock Compass', 'Turtle Rock Map',
                 'Turtle Rock Map Key', 'Turtle Rock Chain Chomp Key',
                 'Turtle Rock Big Key', 'Turtle Rock Treasure',
                 'Turtle Rock Switch Key', 'Turtle Rock Treasury Chest 1',
                 'Turtle Rock Treasury Chest 2', 'Turtle Rock Treasury Chest 3',
                 'Turtle Rock Treasury Chest 4')},
            {'type': 'big', 'settings': ('open',),
             'chests': (
                 'Turtle Rock Compass', 'Turtle Rock Map',
                 'Turtle Rock Map Key', 'Turtle Rock Chain Chomp Key',
                 'Turtle Rock Big Key')}],
        'link': {}
    },
    "Ganon's Tower": {
        'type': 'dungeon', 'map': 'dark', 'coord': (367, 14),
        'keypools': [
            {'type': 'small', 'settings': (), 'keys': 2,
             'chests': (
                 "Ganon's Tower Torch Key",
                 "Ganon's Tower Stalfos Room Chest 1",
                 "Ganon's Tower Stalfos Room Chest 2",
                 "Ganon's Tower Stalfos Room Chest 3",
                 "Ganon's Tower Stalfos Room Chest 4",
                 "Ganon's Tower Trap Chest 1", "Ganon's Tower Trap Chest 2",
                 "Ganon's Tower Tile Room")},
            {'type': 'small', 'settings': (), 'keys': 1,
             'chests': (
                 "Ganon's Tower Torch Key",
                 "Ganon's Tower Stalfos Room Chest 1",
                 "Ganon's Tower Stalfos Room Chest 2",
                 "Ganon's Tower Stalfos Room Chest 3",
                 "Ganon's Tower Stalfos Room Chest 4",
                 "Ganon's Tower Map", "Ganon's Tower Trap Chest 1",
                 "Ganon's Tower Trap Chest 2", "Ganon's Tower Tile Room")},
            {'type': 'small', 'settings': (), 'keys': 1,
             'chests': (
                 "Ganon's Tower Torch Key",
                 "Ganon's Tower Stalfos Room Chest 1",
                 "Ganon's Tower Stalfos Room Chest 2",
                 "Ganon's Tower Stalfos Room Chest 3",
                 "Ganon's Tower Stalfos Room Chest 4",
                 "Ganon's Tower Map", "Ganon's Tower Winder Room Key",
                 "Ganon's Tower Trap Chest 1", "Ganon's Tower Trap Chest 2",
                 "Ganon's Tower Tile Room")}],
        'link': {}
    },
}
