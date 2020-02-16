
from . import tools
from . import helpers


__all__ = ('tables', 'sculpt')


tables = {}


def table(new, name, *args):

    """
    Create the structure and its respective table.
    """

    cls = new.__getattr__(name)

    tables[cls] = tools.Table(*args)

    return cls


def sculpt(new, *assets):

    """
    Create structures and link them to handling instructions.

    .. code-block:: py

        sculpt(
            New(),
            (
                'Item',
                {
                    Key(1, 'name'): field(str),
                    Key(1, 'broken'): field(bool)
                }
            ),
            (
                'User',
                {
                    Key(0, 'id'): field(int),
                    Key(1, 'name'): field(str),
                    Key(2, 'invetory'): field(Array, Item)
                }
            )
        )
    """

    for asset in assets:

        yield table(new, *asset)
