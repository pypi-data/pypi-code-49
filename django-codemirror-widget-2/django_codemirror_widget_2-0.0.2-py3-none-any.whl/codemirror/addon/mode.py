from .base import BaseModeAddon


class LoadmodeAddon(BaseModeAddon):
    file = 'loadmode'


class MultiplexAddon(BaseModeAddon):
    file = 'multiplex'


class MultiplexTestAddon(BaseModeAddon):
    file = 'multiplex_test'


class OverlayAddon(BaseModeAddon):
    file = 'overlay'
