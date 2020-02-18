#! /usr/bin/env python3

__all__ = ["Sensor"]


import asyncio
import pathlib
from typing import Dict, Any, Sequence, Union, Tuple
from ._daemon import Base

ChannelType = Dict[str, Tuple[str, Tuple[int, ...]]]
# TODO: add array type
MeasureType = Dict[str, Union[float]]


class Sensor(Base):
    _kind = "base-sensor"

    def __init__(
        self, name: str, config: Dict[str, Any], config_filepath: pathlib.Path
    ):
        super().__init__(name, config, config_filepath)
        self._measured: MeasureType = dict()  # values must be numbers or arrays
        self.channels: ChannelType = dict()  # values must be list [units, shape]
        self.measurement_id = 0

    def measure(self, loop: bool = False) -> int:
        """Start a measurement, optionally looping.

        Sensor will remain busy until measurement completes.

        Parameters
        ----------
        loop: bool, optional
            Toggle looping behavior. Default False.

        See Also
        --------
        stop_looping
        """
        self.looping = loop
        if not self._busy:
            self._busy = True
            self._loop.create_task(self._runner(loop=loop))
        return self.measurement_id

    def get_channels(self) -> ChannelType:
        """Get current channel information."""
        return self.channels

    def get_measured(self) -> MeasureType:
        """Get most recently measured values."""
        return self._measured

    async def _measure(self) -> MeasureType:
        """Do measurement, filling _measured dictionary.

        Returns dictionary with keys channel names, values numbers or arrays.
        """
        return {}

    async def _runner(self, loop: bool) -> None:
        """Handle execution of _measure, including looping and setting of measurement_id."""
        while True:
            self._measured = await self._measure()
            assert self._measured.keys() == self.channels.keys()
            self._measured["measurement_id"] = self.measurement_id
            if not self.looping:
                self._busy = False
                self.measurement_id += 1
                break
            await asyncio.sleep(0)

    def stop_looping(self) -> None:
        """Stop looping."""
        self.looping = False


if __name__ == "__main__":
    Sensor.main()
