
from .version import __version__
from .Structure import Structure
from .Database import Database

db = database = Database.make_standard()
