#! /usr/bin/env python3
import itertools
import pathlib
from typing import Dict, Any, Sequence, Tuple

from ._base import Hardware

__all__ = ["ContinuousHardware"]


class ContinuousHardware(Hardware):
    _kind: str = "continuous-hardware"

    def __init__(
        self, name: str, config: Dict[str, Any], config_filepath: pathlib.Path
    ):
        super().__init__(name, config, config_filepath)
        self._out_of_limits = config.get("out_of_limits", "error")

    def get_limits(self) -> Sequence[Tuple[float, float]]:
        return self._limits

    def in_limits(self, position: float) -> bool:
        for l, r in self._limits:
            if l <= position <= r or r <= position <= l:
                return True
        return False

    def set_position(self, position: float) -> None:
        if not self.in_limits(position):
            if self._out_of_limits == "closest":
                closest = float("inf")
                for bound in itertools.chain(self._limits):
                    if abs(bound - position) < abs(closest - position):
                        closest = bound
                position = closest
            elif self._out_of_limits == "ignore":
                return
            else:
                raise ValueError(f"{position} not in ranges {self._limits}")
        super().set_position(position)

    def get_state(self) -> Dict[str, Any]:
        state = super().get_state()
        state["limits"] = self._limits
        return state

    def _load_state(self, state: Dict[str, Any]) -> None:
        super()._load_state(state)
        self._limits = state.get("limits", [(float("-inf"), float("inf"))])


if __name__ == "__main__":
    ContinuousHardware.main()
