
"""Application constants.

These constants are provided for re-usability and
consistency across the application's modules and classes.

.. code-block:: python
    :caption: Available constants

    SWLOOKUP        SWLookup program name.
    SWLING          SWLing reporting application name.
    SWLOOKUP_LOGO   SWLookup application ASCII art logo.
    SWLING_LOGO     SWLing application ASCII art logo.
    FORMATTERS      Dictionary of ANSI escape codes.

"""

# SWLookup program name
SWLOOKUP = 'SWLookup'

# SWLing program name
SWLING = 'SWLing'

# SWLookup application logo
SWLOOKUP_LOGO = r"""
    ______       __   __                __
   / ___/ |     / /  / /   ____  ____  / /____  ______
   \__ \| | /| / /  / /   / __ \/ __ \/ //_/ / / / __ \
  ___/ /| |/ |/ /  / /___/ /_/ / /_/ / ,< / /_/ / /_/ /
 /____/ |__/|__/  /_____/\____/\____/_/|_|\__,_/ .___/
                                              /_/"""

# SWLing application logo
SWLING_LOGO = r"""
    ______       ____    _
   / ___/ |     / / /   (_)___  ____ _
   \__ \| | /| / / /   / / __ \/ __ `/
  ___/ /| |/ |/ / /___/ / / / / /_/ /
 /____/ |__/|__/_____/_/_/ /_/\__, /
                             /____/
"""

# A dictionary with ANSI escape codes used in format substitutions.
FORMATTERS = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'orange': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'lightgrey': '\033[37m',
    'darkgrey': '\033[90m',
    'lightred': '\033[91m',
    'lightgreen': '\033[92m',
    'yellow': '\033[93m',
    'lightblue': '\033[94m',
    'pink': '\033[95m',
    'lightcyan': '\033[96m',
    'reset': "\033[0m",
    'bold': '\033[1m',
    'italic': '\033[3m',
    'underline': '\033[4m'
}
