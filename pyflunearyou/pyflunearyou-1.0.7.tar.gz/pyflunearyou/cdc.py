"""Define endpoints related to CDC reports."""
from copy import deepcopy
import logging
from typing import Callable, Coroutine, Dict

from aiocache import cached

from .helpers import get_nearest_by_numeric_key
from .report import Report

_LOGGER = logging.getLogger(__name__)

STATUS_MAP: Dict[int, str] = {
    1: "No Data",
    2: "Minimal",
    3: "Low",
    4: "Moderate",
    5: "High",
    99: "None",
}


def adjust_status(info: dict) -> dict:
    """Apply status mapping to a raw API result."""
    modified_info: dict = deepcopy(info)
    modified_info.update(
        {
            "level": get_nearest_by_numeric_key(STATUS_MAP, int(info["level"])),
            "level2": STATUS_MAP[99]
            if info["level2"] is None
            else get_nearest_by_numeric_key(STATUS_MAP, int(info["level2"])),
        }
    )

    return modified_info


class CdcReport(Report):
    """Define a CDC report object."""

    def __init__(self, request: Callable[..., Coroutine], cache_seconds: int) -> None:
        """Initialize."""
        super().__init__(request, cache_seconds)
        self.raw_cdc_data: Callable[..., Coroutine] = cached(ttl=self._cache_seconds)(
            self._raw_cdc_data
        )

    async def _raw_cdc_data(self) -> dict:
        """Return the raw CDC data."""
        return await self._request("get", "map/cdc")

    async def status_by_coordinates(self, latitude: float, longitude: float) -> dict:
        """Return the CDC status for the provided latitude/longitude."""
        cdc_data: dict = await self.raw_cdc_data()
        nearest: dict = await self.nearest_by_coordinates(latitude, longitude)
        return adjust_status(cdc_data[nearest["state"]["name"]])

    async def status_by_state(self, state: str) -> dict:
        """Return the CDC status for the specified state."""
        data: dict = await self.raw_cdc_data()

        try:
            info: dict = next((v for k, v in data.items() if state in k))
        except StopIteration:
            return {}

        return adjust_status(info)
