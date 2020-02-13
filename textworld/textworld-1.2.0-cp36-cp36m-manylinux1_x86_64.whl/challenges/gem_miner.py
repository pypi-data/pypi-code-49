# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.


"""
.. _gem_miner:

Gem Miner
=========

In this type of games, the layout of the world is guaranteed to contain
at least one cycle when the number of rooms is greater or equal to four.
Each room may contain one or several gems that can be mined. To get
points, the player has to bring back the gems to the starting location
and put them in a chest.

Variants
--------
 - Limited capacity in the player's inventory.
 - Gems have color according to their value (points).
 - The gems are all simply laying on the floor (no "mining").
 - The player has to find a pickaxe before being able to mine.

Difficulties
------------
 - Number of rooms.
 - Distractor objects.

TODO
----
- Have a "cavern" themed grammar.
"""

from typing import Optional

import numpy as np
from numpy.random import RandomState

import textworld
from textworld.generator.graph_networks import reverse_direction

from textworld.utils import encode_seeds
from textworld.generator.game import GameOptions

from textworld.challenges.utils import get_seeds_for_game_generation


def _make_map(nb_rooms: int, rng: RandomState):
    map_ = textworld.generator.make_map(nb_rooms, rng=rng, possible_door_states=None)
    return map_


def make_game_from_level(level: int, options: Optional[GameOptions] = None) -> textworld.Game:
    """ Make a Gem Miner game of the desired difficulty level.

    Arguments:
        level: Difficulty level (see notes).
        options:
            For customizing the game generation (see
            :py:class:`textworld.GameOptions <textworld.generator.game.GameOptions>`
            for the list of available options).

    Returns:
        Generated game.

    Notes:
        Difficulty levels are defined as follows:
        TODO
    """
    n_distractors = (level // 100)
    quest_length = level % 100
    n_rooms = (n_distractors + 1) * quest_length
    distractor_mode = "random" if n_distractors > 2 else "simple"
    return make_game(distractor_mode, n_rooms, quest_length, options)


def make_game(mode: str, n_rooms: int, quest_length: int,
              options: Optional[GameOptions] = None) -> textworld.Game:
    """ Make a Gem Miner game.

    Arguments:
        mode: Mode for the game where

              * `'simple'`: the distractor rooms are only placed orthogonaly
                to the chain. This means moving off the optimal path leads
                immediately to a dead end.
              * `'random'`: the distractor rooms are randomly place along the
                chain. This means a player can wander for a while before
                reaching a dead end.
        n_rooms: Number of rooms in the game.
        quest_length: Number of rooms in the chain. This also represents the
                      number of commands for the optimal policy.
        options:
            For customizing the game generation (see
            :py:class:`textworld.GameOptions <textworld.generator.game.GameOptions>`
            for the list of available options).

    Returns:
        Generated game.
    """
    nb_rooms = 4
    gem_values = [1, 1, 1, 1]
    nb_gems = len(gem_values)
    limited_inventory = False
    start_with_pickaxe = False
    gems_on_the_floor = True

    if mode == "simple" and float(n_rooms) / quest_length > 4:
        msg = ("Total number of rooms must be less than 4 * `quest_length` "
               "when distractor mode is 'simple'.")
        raise ValueError(msg)

    # Deal with any missing random seeds.
    seeds = get_seeds_for_game_generation(seeds)

    metadata = {}  # Collect infos for reproducibility.
    metadata["desc"] = "Coin Collector"
    metadata["mode"] = mode
    metadata["seeds"] = seeds
    metadata["world_size"] = n_rooms
    metadata["quest_length"] = quest_length
    metadata["grammar_flags"] = grammar_flags

    rng_map = np.random.RandomState(seeds['seed_map'])
    rng_grammar = np.random.RandomState(seeds['seed_grammar'])

    #map_ = _make_map(nb_rooms, rng_map)
    M = textworld.GameMaker()
    rooms = M.make_map(nb_rooms, rng_map)

    # Generate map.
    M = textworld.GameMaker()
    M.grammar = textworld.generator.make_grammar(flags=grammar_flags, rng=rng_grammar)

    rooms = []
    walkthrough = []
    for i in range(quest_length):
        r = M.new_room()
        if i >= 1:
            # Connect it to the previous rooms.
            free_exits = [k for k, v in rooms[-1].exits.items() if v.dest is None]
            src_exit = rng_map.choice(free_exits)
            dest_exit = reverse_direction(src_exit)
            M.connect(rooms[-1].exits[src_exit], r.exits[dest_exit])
            walkthrough.append("go {}".format(src_exit))

        rooms.append(r)

    M.set_player(rooms[0])

    # Add object the player has to pick up.
    obj = M.new(type="o", name="coin")
    rooms[-1].add(obj)

    # Add distractor rooms, if needed.
    chain_of_rooms = list(rooms)
    while len(rooms) < n_rooms:
        if mode == "random":
            src = rng_map.choice(rooms)
        else:
            # Add one distractor room per room along the chain.
            src = chain_of_rooms[len(rooms) % len(chain_of_rooms)]

        free_exits = [k for k, v in src.exits.items() if v.dest is None]
        if len(free_exits) == 0:
            continue

        dest = M.new_room()
        src_exit = rng_map.choice(free_exits)
        dest_exit = reverse_direction(src_exit)
        M.connect(src.exits[src_exit], dest.exits[dest_exit])
        rooms.append(dest)

    # Generate the quest thats by collecting the coin.
    walkthrough.append("take coin")
    # TODO: avoid compiling the game at all (i.e. use the inference engine).
    M.set_quest_from_commands(walkthrough)

    game = M.build()
    game.metadata = metadata
    mode_choice = 0 if mode == "simple" else 1
    uuid = "tw-coin_collector-{specs}-{flags}-{seeds}"
    uuid = uuid.format(specs=encode_seeds((mode_choice, n_rooms, quest_length)),
                       flags=encode_flags(grammar_flags),
                       seeds=encode_seeds([seeds[k] for k in sorted(seeds)]))
    game.metadata["uuid"] = uuid
    return game
