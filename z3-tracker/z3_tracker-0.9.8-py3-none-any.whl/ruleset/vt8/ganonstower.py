'''
Ganon's Tower
'''

__all__ = 'LOCATIONS',


LOCATIONS = {
    "Ganon's Tower Entrance (I)": {
        'type': 'interior',
        'link': {
            'Castle Tower Entrance (E)': [('settings', 'inverted')],
            "Ganon's Tower Entrance (E)": [('nosettings', 'inverted')],
            "Ganon's Tower Lobby": [('and', [
                ('or', [
                    ('settings', 'placement_advanced'),
                    ('and', [
                        ('or', [
                            ('settings', 'swordless'),
                            ('item', 'mastersword')]),
                        ('or', [
                            ('item', 'bottle'), ('item', 'bluemail')])])]),
                ('rabbitbarrier', None)])]}
    },
    "Ganon's Tower Lobby": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Entrance (I)": [],
            "Ganon's Tower Torch Key Room": [],
            "Ganon's Tower Trap Room": [],
            "Ganon's Tower Ascent 1": [('bigkey', "Ganon's Tower")]}
    },

    "Ganon's Tower Torch Key Room": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Lobby": [],
            "Ganon's Tower Trap Room": [('smallkey', "Ganon's Tower")],
            "Ganon's Tower Torch Key": [('item', 'pegasus')],
            "Ganon's Tower Moving Bumper Key": []}
    },
    "Ganon's Tower Torch Key": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Torch Key Room": []}
    },
    "Ganon's Tower Moving Bumper Key": {
        'type': 'dungeonkey', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Torch Key Room": [],
            "Ganon's Tower Pit Room": [('item', 'hammer')]}
    },
    "Ganon's Tower Pit Room": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Moving Bumper Key": [('item', 'hookshot')],
            "Ganon's Tower Stalfos Room": [('item', 'hookshot')],
            "Ganon's Tower Map Room": [
                ('item', 'hookshot'), ('item', 'pegasus')]}
    },
    "Ganon's Tower Stalfos Room": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Pit Room": [
                ('item', 'hookshot'), ('item', 'pegasus')],
            "Ganon's Tower Stalfos Room Chest 1": [],
            "Ganon's Tower Stalfos Room Chest 2": [],
            "Ganon's Tower Stalfos Room Chest 3": [],
            "Ganon's Tower Stalfos Room Chest 4": []}
    },
    "Ganon's Tower Stalfos Room Chest 1": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Stalfos Room": []}
    },
    "Ganon's Tower Stalfos Room Chest 2": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Stalfos Room": []}
    },
    "Ganon's Tower Stalfos Room Chest 3": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Stalfos Room": []}
    },
    "Ganon's Tower Stalfos Room Chest 4": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Stalfos Room": []}
    },
    "Ganon's Tower Map Room": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Pit Room": [('item', 'hookshot')],
            "Ganon's Tower Map": [('smallkey', "Ganon's Tower")],
            "Ganon's Tower Double Switch": []}
    },
    "Ganon's Tower Map": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Map Room": []}
    },
    "Ganon's Tower Double Switch": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Map Room": [],
            "Ganon's Tower Switch Key": [],
            "Ganon's Tower Winder Room": [('smallkey', "Ganon's Tower")]}
    },
    "Ganon's Tower Switch Key": {
        'type': 'dungeonkey', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Double Switch": []}
    },
    "Ganon's Tower Winder Room": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Winder Room Key": [('item', 'hookshot')]}
    },
    "Ganon's Tower Winder Room Key": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Teleport Maze": [('smallkey', "Ganon's Tower")]}
    },
    "Ganon's Tower Teleport Maze": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Secret Treasure": [('item', 'bombs')],
            "Ganon's Tower Convergence": []}
    },
    "Ganon's Tower Secret Treasure": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Secret Chest 1": [],
            "Ganon's Tower Secret Chest 2": [],
            "Ganon's Tower Secret Chest 3": [],
            "Ganon's Tower Secret Chest 4": [],
            "Ganon's Tower Convergence": []}
    },
    "Ganon's Tower Secret Chest 1": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Secret Treasure": []}
    },
    "Ganon's Tower Secret Chest 2": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Secret Treasure": []}
    },
    "Ganon's Tower Secret Chest 3": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Secret Treasure": []}
    },
    "Ganon's Tower Secret Chest 4": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Secret Treasure": []}
    },

    "Ganon's Tower Trap Room": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Lobby": [],
            "Ganon's Tower Torch Key Room": [('smallkey', "Ganon's Tower")],
            "Ganon's Tower Trap Chest 1": [],
            "Ganon's Tower Trap Chest 2": [],
            "Ganon's Tower Tile Room": [('item', 'somaria')]}
    },
    "Ganon's Tower Trap Chest 1": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Trap Room": []}
    },
    "Ganon's Tower Trap Chest 2": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Trap Room": []}
    },
    "Ganon's Tower Tile Room": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Trap Room": [],
            "Ganon's Tower Torch Race": [('smallkey', "Ganon's Tower")]}
    },
    "Ganon's Tower Torch Race": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Tile Room": [],
            "Ganon's Tower Compass Room": [('item', 'firerod')]}
    },
    "Ganon's Tower Compass Room": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Torch Race": [],
            "Ganon's Tower Compass Chest 1": [],
            "Ganon's Tower Compass Chest 2": [],
            "Ganon's Tower Compass Chest 3": [],
            "Ganon's Tower Compass Chest 4": [],
            "Ganon's Tower Obstacle Course Key": []}
    },
    "Ganon's Tower Compass Chest 1": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Compass Room": []}
    },
    "Ganon's Tower Compass Chest 2": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Compass Room": []}
    },
    "Ganon's Tower Compass Chest 3": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Compass Room": []}
    },
    "Ganon's Tower Compass Chest 4": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Compass Room": []}
    },
    "Ganon's Tower Obstacle Course Key": {
        'type': 'dungeonkey', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Convergence": [('smallkey', "Ganon's Tower")]}
    },

    "Ganon's Tower Convergence": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Anti-Fairy Room": [],
            "Ganon's Tower Treasure Room": []}
    },
    "Ganon's Tower Anti-Fairy Room": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Convergence": [],
            "Ganon's Tower Armos On Ice": [('item', 'bombs')]}
    },
    "Ganon's Tower Armos On Ice": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Big Key Room": [],
            "Ganon's Tower Treasure Room": []}
    },
    "Ganon's Tower Big Key Room": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Armos On Ice": [],
            "Ganon's Tower Big Key": [],
            "Ganon's Tower Big Key Chest Left": [],
            "Ganon's Tower Big Key Chest Right": []}
    },
    "Ganon's Tower Big Key": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Big Key Room": []}
    },
    "Ganon's Tower Big Key Chest Left": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Big Key Room": []}
    },
    "Ganon's Tower Big Key Chest Right": {
        'type': 'dungeonchest', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Big Key Room": []}
    },
    "Ganon's Tower Treasure Room": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Treasure": [('bigkey', "Ganon's Tower")],
            "Ganon's Tower Convergence": [],
            "Ganon's Tower Torch Key Room": []}
    },
    "Ganon's Tower Treasure": {
        'type': 'dungeonchest_nokey', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Treasure Room": []}
    },

    "Ganon's Tower Ascent 1": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Lobby": [],
            "Ganon's Tower Ascent 2": [
                ('item', 'bow'), ('settings', 'enemiser')]}
    },
    "Ganon's Tower Ascent 2": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Ascent 1": [
                ('item', 'bow'), ('settings', 'enemiser')],
            "Ganon's Tower Ascent 3": [
                ('item', 'lantern'), ('item', 'firerod')]}
    },
    "Ganon's Tower Ascent 3": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Ascent 2": [],
            "Ganon's Tower Helmasaur Key": [],
            "Ganon's Tower Helmasaur Chest 1": [],
            "Ganon's Tower Helmasaur Chest 2": [],
            "Ganon's Tower Ascent 4": [('smallkey', "Ganon's Tower")]}
    },
    "Ganon's Tower Helmasaur Key": {
        'type': 'dungeonkey', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Ascent 3": []}
    },
    "Ganon's Tower Helmasaur Chest 1": {
        'type': 'dungeonchest_nokey', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Ascent 3": []}
    },
    "Ganon's Tower Helmasaur Chest 2": {
        'type': 'dungeonchest_nokey', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Ascent 3": []}
    },
    "Ganon's Tower Ascent 4": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Ascent 3": [],
            "Ganon's Tower Rabbit Beam Chest": [],
            "Ganon's Tower Ascent 5": [('smallkey', "Ganon's Tower")]}
    },
    "Ganon's Tower Rabbit Beam Chest": {
        'type': 'dungeonchest_nokey', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Ascent 4": []}
    },
    "Ganon's Tower Ascent 5": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Ascent 4": [],
            "Ganon's Tower Ascent 6": [('item', 'hookshot')]}
    },
    "Ganon's Tower Ascent 6": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Last Chest": [],
            "Ganon's Tower Boss": []}
    },
    "Ganon's Tower Last Chest": {
        'type': 'dungeonchest_nokey', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Ascent 6": []}
    },
    "Ganon's Tower Boss": {
        'type': 'dungeonboss', "dungeon": "Ganon's Tower",
        'link': {
            "Ganon's Tower Boss Item": [
                ('item', 'sword'),
                ('and', [
                    ('settings', 'swordless'), ('item', 'hammer')]),
                ('item', 'bugnet')]}
    },
    "Ganon's Tower Boss Item": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            "Ganon's Tower Reward": []}
    },
    "Ganon's Tower Reward": {
        'type': 'area', 'dungeon': "Ganon's Tower",
        'link': {
            'Pyramid': [('nosettings', 'inverted')],
            'Castle Walls': [('settings', 'inverted')]}
    },
}
