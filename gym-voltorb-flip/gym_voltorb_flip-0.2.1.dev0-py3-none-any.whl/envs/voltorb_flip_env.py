import sys

import gym
import numpy as np
from gym import spaces
from gym.utils import colorize
from six import StringIO
from voltorb_flip.game import CellState, GameState, UnableToFlipException, VoltorbFlip

COVERED_CHARACTER = "?"
MARKED_CHARACTER = "M"


class VoltorbFlipEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.game = VoltorbFlip()

        self.action_space = spaces.Tuple(
            [
                spaces.Discrete(self.game.CLASSIC_BOARD_SIZE),
                spaces.Discrete(self.game.CLASSIC_BOARD_SIZE),
            ]
        )

        self.board_space = spaces.Box(
            low=-1,
            high=3,
            shape=(self.game.CLASSIC_BOARD_SIZE, self.game.CLASSIC_BOARD_SIZE),
            dtype=np.uint8,
        )

        self.bombs_vertical = spaces.Box(
            low=0, high=5, shape=(self.game.CLASSIC_BOARD_SIZE,), dtype=np.uint8
        )
        self.bombs_horizontal = spaces.Box(
            low=0, high=5, shape=(self.game.CLASSIC_BOARD_SIZE,), dtype=np.uint8
        )
        self.points_vertical = spaces.Box(
            low=0, high=243, shape=(self.game.CLASSIC_BOARD_SIZE,), dtype=np.uint8
        )
        self.points_horizontal = spaces.Box(
            low=0, high=243, shape=(self.game.CLASSIC_BOARD_SIZE,), dtype=np.uint8
        )
        self.level = spaces.Discrete(8)

        self.observation_space = spaces.Tuple(
            [
                self.board_space,
                self.bombs_horizontal,
                self.bombs_vertical,
                self.points_horizontal,
                self.points_vertical,
                self.level,
            ]
        )

    def reset(self):
        self.game = VoltorbFlip()
        return self._encoded_state()

    def step(self, action):
        if not self.action_space.contains(action):
            raise ValueError(
                f"action {str(action)} is not part of the environment's action space"
            )
        row, column = action
        reward = 0
        done = False
        info = dict()

        try:
            self.game.flip(row, column)
            reward = self.game.board[row][column]
        except UnableToFlipException:
            reward = 0

        if self.game.state == GameState.IN_PROGRESS:
            done = False
        elif self.game.state == GameState.WON:
            if self.game.level == self.game.MAX_LEVEL:
                done = True
            self.game.bump_level()
            reward = 100
        else:
            done = True

        return self._encoded_state(), reward, done, info

    def render(self, mode="human"):
        outfile = StringIO() if mode == "ansi" else sys.stdout
        outfile.write("\n".join(self._get_board()))

    def _encoded_state(self):
        mask = np.array(env.game.cell_states)
        board = np.array(env.game.board)
        return (
            np.where(mask == CellState.COVERED, -1, board),
            np.array(self.game.horizontal_bombs),
            np.array(self.game.vertical_bombs),
            np.array(self.game.horizontal_points),
            np.array(self.game.vertical_points),
            self.game.level,
        )

    def _get_board(self):
        game = self.game
        game_string = []
        headers_row = "      ".join(
            [str(column + 1) for column in range(game.CLASSIC_BOARD_SIZE)]
        )
        game_string.append(" " * 6 + headers_row)
        for row in range(game.CLASSIC_BOARD_SIZE):
            row_str = ""
            current_row_label = chr(ord("a") + row)
            row_str = row_str + f"{current_row_label:>3}"
            for column in range(game.CLASSIC_BOARD_SIZE):
                value = _get_cell_value(column, game, row)
                row_str = row_str + f" [ {value} ] "
            row_str = (
                row_str
                + f" {_get_summary(game.horizontal_points[row], game.horizontal_bombs[row])}"
            )
            game_string.append(row_str)
        ver_stats_row = "    ".join(
            [
                _get_summary(game.vertical_points[column], game.vertical_bombs[column])
                for column in range(game.CLASSIC_BOARD_SIZE)
            ]
        )
        game_string.append(" " * 5 + ver_stats_row)
        game_string = [string.ljust(45, " ") for string in game_string]
        return game_string


def _get_cell_value(column, game, row):
    cell_state = game.cell_states[row][column]
    value = colorize(game.board[row][column], "cyan", bold=True)
    if cell_state == CellState.COVERED:
        value = COVERED_CHARACTER
    elif cell_state != CellState.UNCOVERED:
        value = MARKED_CHARACTER
    return value


def _get_summary(points, bombs):
    return (
        colorize(points, "green", bold=True) + "/" + colorize(bombs, "red", bold=True)
    )
