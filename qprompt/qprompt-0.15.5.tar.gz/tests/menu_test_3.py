"""Check for show_menu() functionality."""

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

from qprompt import MenuEntry, show_menu

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(unittest.TestCase):

    def setUp(test):
        test.entries = []
        test.entries.append(MenuEntry("1", "foo", None, None, None))
        test.entries.append(MenuEntry("2", "bar", None, None, None))

    def test_menu_1(test):
        setinput("1")
        result = show_menu(test.entries)
        test.assertEqual("1", result)

    def test_menu_2(test):
        setinput("1")
        result = show_menu(test.entries, returns="desc")
        test.assertEqual("foo", result)

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()
