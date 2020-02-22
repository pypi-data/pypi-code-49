from enum import Enum

from voltorb_flip import levels


class CellState(Enum):
    UNCOVERED = -1
    MARKED_0 = 0
    MARKED_1 = 1
    MARKED_2 = 2
    MARKED_3 = 3
    COVERED = 4


class GameState(Enum):
    IN_PROGRESS = 1
    LOST = 2
    WON = 3


class UnableToFlipException(Exception):
    def __init__(self, *args, cell_state):
        super().__init__(args)
        self.cell_state = cell_state


class GameOverException(Exception):
    def __init__(self, *args, state):
        super().__init__(args)
        self.state = state


class VoltorbFlip:  # pylint: disable=too-many-instance-attributes

    MAX_LEVEL = 8
    MIN_LEVEL = 1
    CLASSIC_BOARD_SIZE = 5

    def __init__(self):
        self.level = 1
        self.accumulated_score = 0

        self.current_score = None
        self.state = None
        self.board = None
        self.horizontal_points = None
        self.horizontal_bombs = None
        self.vertical_points = None
        self.vertical_bombs = None
        self.cell_states = None
        self.maximum_points = None

        self.reset_level()

    def reset_level(self):
        self.current_score = 1
        self.state = GameState.IN_PROGRESS
        self.board = levels.generate_board(self.level)
        self.cell_states = VoltorbFlip._generate_states(
            VoltorbFlip.CLASSIC_BOARD_SIZE, VoltorbFlip.CLASSIC_BOARD_SIZE
        )
        (
            self.horizontal_points,
            self.horizontal_bombs,
            self.vertical_points,
            self.vertical_bombs,
        ) = VoltorbFlip._calculate_borders(self.board)
        self.maximum_points = VoltorbFlip._calculate_winning_score(self.board)

    def bump_level(self):
        self.level = min(self.level + 1, VoltorbFlip.MAX_LEVEL)
        self.accumulated_score += self.current_score
        self.reset_level()

    def remove_level(self):
        self.level = max(self.level - 1, VoltorbFlip.MIN_LEVEL)
        self.accumulated_score = max(self.accumulated_score - self.current_score, 0)
        self.reset_level()

    def flip(self, row, column):
        if self.state != GameState.IN_PROGRESS:
            raise GameOverException(state=self.state)

        if self.cell_states[row][column] != CellState.COVERED:
            raise UnableToFlipException(cell_state=self.cell_states[row][column])

        self._change_cell_state(row, column, CellState.UNCOVERED)
        self.current_score *= self.board[row][column]

        self._win_or_lose()

    def mark(self, row, column, cell_state):
        self._change_cell_state(row, column, cell_state)

    def unmark(self, row, column):
        self._change_cell_state(row, column, CellState.COVERED)

    @staticmethod
    def _generate_states(width, height):
        return [[CellState.COVERED for _ in range(width)] for _ in range(height)]

    @staticmethod
    def _calculate_borders(board):
        height = len(board)
        width = len(board[0])

        horizontal_points = [sum(arr) for arr in board]
        horizontal_bombs = [0 for _ in range(height)]
        for row, arr in enumerate(board):
            for value in arr:
                if value == 0:
                    horizontal_bombs[row] += 1

        vertical_points = [0 for _ in range(width)]
        vertical_bombs = [0 for _ in range(width)]
        for i in range(width):
            for j in range(height):
                vertical_points[i] += board[j][i]
                if board[i][j] == 0:
                    vertical_bombs[j] += 1

        return horizontal_points, horizontal_bombs, vertical_points, vertical_bombs

    @staticmethod
    def _calculate_winning_score(board):
        score = 1
        for row in board:
            for number in row:
                score *= 1 if number == 0 else number
        return score

    def _win_or_lose(self):
        if self.current_score == self.maximum_points:
            self.state = GameState.WON
        elif self.current_score == 0:
            self.state = GameState.LOST

    def _change_cell_state(self, row, column, new_state):
        if self.cell_states[row][column] == CellState.UNCOVERED:
            return
        self.cell_states[row][column] = new_state
