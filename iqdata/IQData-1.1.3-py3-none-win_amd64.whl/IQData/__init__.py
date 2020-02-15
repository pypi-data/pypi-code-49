from .apis import register_to_locales
from IQData.version import __version__

__all__ = ["__version__"]

register_to_locales(locals(), __all__)

del register_to_locales
