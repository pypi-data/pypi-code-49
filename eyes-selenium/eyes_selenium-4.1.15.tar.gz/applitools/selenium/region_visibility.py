from abc import abstractmethod

from applitools.common import Point, logger
from applitools.common.utils import ABC
from applitools.core import PositionProvider


class RegionVisibilityStrategy(ABC):
    """
    Encapsulates implementations for providing region visibility during
    check_region.
    """

    @abstractmethod
    def return_to_original_position(self, position_provider):
        # type: (PositionProvider) -> None
        pass

    @abstractmethod
    def move_to_region(self, position_provider, location):
        # type: (PositionProvider, Point) -> None
        pass


class NopRegionVisibilityStrategy(RegionVisibilityStrategy):
    def move_to_region(self, position_provider, location):
        logger.debug("Ignored (no op).")

    def return_to_original_position(self, position_provider):
        logger.debug("Ignored (no op).")


class MoveToRegionVisibilityStrategy(RegionVisibilityStrategy):
    VISIBILITY_OFFSET = 100  # pixels
    _position_memento = None

    def move_to_region(self, position_provider, location):
        # type: (PositionProvider, Point) -> None
        self._position_memento = position_provider.get_state()
        # We set the location to "almost" the location we were asked. This is because
        # sometimes, moving the browser  to the specific pixel where the
        # element begins, causes the element to be slightly out of the viewport.
        location = location - self.VISIBILITY_OFFSET
        location.x = 0 if location.x < 0 else location.x
        location.y = 0 if location.y < 0 else location.y
        position_provider.set_position(location)

    def return_to_original_position(self, position_provider):
        if self._position_memento:
            position_provider.restore_state(self._position_memento)
