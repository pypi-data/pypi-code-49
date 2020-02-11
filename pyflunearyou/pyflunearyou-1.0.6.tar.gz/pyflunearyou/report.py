"""Define a generic report object."""
import logging
from typing import Callable, Coroutine

from aiocache import cached

from .helpers.geo import get_nearest_by_coordinates

_LOGGER: logging.Logger = logging.getLogger(__name__)


class Report:  # pylint: disable=too-few-public-methods
    """Define a generic report object."""

    def __init__(self, request: Callable[..., Coroutine], cache_seconds: int) -> None:
        """Initialize."""
        self._cache_seconds: int = cache_seconds
        self._request: Callable[..., Coroutine] = request

        self.user_reports: Callable[..., Coroutine] = cached(
            ttl=self._cache_seconds, key="local_data"
        )(self._raw_user_report_data)
        self.state_data: Callable[..., Coroutine] = cached(
            ttl=self._cache_seconds, key="state_data"
        )(self._raw_state_data)

    async def _raw_user_report_data(self) -> list:
        """Return user report data (if accompanied by latitude/longitude)."""
        data: dict = await self._request("get", "map/markers")
        return [
            location
            for location in data
            if location["latitude"] and location["longitude"]
        ]

    async def _raw_state_data(self) -> list:
        """Return a list of states."""
        data: dict = await self._request("get", "states")
        return [location for location in data if location["name"] != "United States"]

    async def nearest_by_coordinates(self, latitude: float, longitude: float) -> dict:
        """Get the nearest report (with local and state info) to a lat/lon."""
        # Since user data is more granular than state or CDC data, find the
        # user report whose coordinates are closest to the provided
        # coordinates:
        nearest_user_report: dict = get_nearest_by_coordinates(
            await self.user_reports(), "latitude", "longitude", latitude, longitude
        )

        nearest_state: str

        try:
            # If the user report corresponds to a known state in
            # flunearyou.org's database, we can safely assume that's the
            # correct state:
            nearest_state = next(
                (
                    state
                    for state in await self.state_data()
                    if state["place_id"] == nearest_user_report["contained_by"]
                )
            )
        except StopIteration:
            # If a place ID doesn't exist (e.g., ZIP Code 98012 doesn't have a
            # place ID), calculate the nearest state by measuring the distance
            # from the provided latitude/longitude to flunearyou.org's
            # latitude/longitude that defines each state:
            nearest_state = get_nearest_by_coordinates(
                await self.state_data(), "lat", "lon", latitude, longitude
            )

        return {"local": nearest_user_report, "state": nearest_state}
