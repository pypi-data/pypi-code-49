# Copyright (C) 2019 Shiela Buitizon | Joshua Kim Rivera

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from AppiumLibrary import VERSION
from AppiumLibrary import (
    _LoggingKeywords,
    _RunOnFailureKeywords,
    _ElementKeywords,
    _ScreenshotKeywords,
    _ApplicationManagementKeywords,
    _WaitingKeywords,
    _TouchKeywords,
    _KeyeventKeywords,
    _AndroidUtilsKeywords,
)

__version__ = '0.4a1'


class _ApplicationManagementExtendedKeywords(_ApplicationManagementKeywords):

    def __init__(self):
        super().__init__()

    def switch_window(self, window):
        """ Change focus to another window (Web context only).
            *AppiumExtensionLibrary Only Keyword*.
        """
        self._current_application().switch_to.window(window)

    def close_window(self):
        """ Closes the current window (Web context only).
            *AppiumExtensionLibrary Only Keyword*.
        """
        self._current_application().close()

    def get_current_window_handle(self):
        """ Retrieves the current window handle (Web context only).
            Returns the window handle as string.
            *AppiumExtensionLibrary Only Keyword*.
        """
        return self._current_application().current_window_handle

    def get_window_handles(self):
        """ Retrieves the list of all window handles available to \
            the session (Web context only).
            Returns a list if there are more than one window active.
            *AppiumExtensionLibrary Only Keyword*.
        """
        return self._current_application().window_handles

    def get_title(self):
        """ Get the current page title (Web context only).
            *AppiumExtensionLibrary Only Keyword*.
        """
        return self._current_application().title

    def get_location(self):
        """ Retrieve the URL of the current page (Web context only).
            *AppiumExtensionLibrary Only Keyword*.
        """
        return self._current_application().current_url()

    def reload_page(self):
        """ Refreshes the current page. (Web context only).
            *AppiumExtensionLibrary Only Keyword*.
        """
        self._current_application().refresh()

    def get_cookies(self):
        """ Retrieves all cookies visible to the current page \
            (Web context only).
            *AppiumExtensionLibrary Only Keyword*.
        """
        return self._current_application().get_cookies

    def add_cookie(self, **kwargs):
        """Set a cookie (Web context only).
           Arguments should be given like the example:
           NOTE: ``name`` and ``value`` arguments are required, \
               ``path``, ``domain``, ``expiry`` and ``secure`` \
                   are optional.
           | Set Cookie   | name=_cookieName   | value=someValue |
           | Set Cookie   | name=_cookieName   | value=someValue \
               | path=some/path | domain=.cookie.com |
           *AppiumExtensionLibrary Only Keyword*.
        """
        try:
            self._current_application().add_cookie(kwargs)
        except Exception as err:
            raise err

    def delete_cookie(self, cookieName):
        """ Delete the cookie with the given name (Web context only).
            *AppiumExtensionLibrary Only Keyword*.
        """
        try:
            self._current_application().delete_cookie(cookieName)
        except Exception as err:
            raise err

    def delete_all_cookies(self):
        """ Delete the cookie with the given name (Web context only).
            *AppiumExtensionLibrary Only Keyword*.
        """
        self._current_application().delete_all_cookies()


class AppiumExtensionLibrary(
    _LoggingKeywords,
    _RunOnFailureKeywords,
    _ElementKeywords,
    _ScreenshotKeywords,
    _ApplicationManagementExtendedKeywords,
    _WaitingKeywords,
    _TouchKeywords,
    _KeyeventKeywords,
    _AndroidUtilsKeywords,
):
    """AppiumExtensionLibrary is a Mobile App testing \
        library for Robot Framework.

    = Locating or specifying elements =

    All keywords in AppiumLibrary that need to find an \
        element on the page
    take an argument, either a ``locator`` or a \
        ``webelement``. ``locator``
    is a string that describes how to locate an element \
        using a syntax
    specifying different location strategies. \
        ``webelement`` is a variable that
    holds a WebElement instance, which is a representation \
        of the element.

    == Using locators ==

    By default, when a locator is provided, it is matched \
        against the key attributes
    of the particular element type. For iOS and Android, \
        key attribute is ``id`` for
    all elements and locating elements is easy using just \
        the ``id``. For example:

    | Click Element    id=my_element

    New in AppiumLibrary 1.4, ``id`` and ``xpath`` are not \
        required to be specified,
    however ``xpath`` should start with ``//`` else just use ``xpath`` locator as explained below.

    For example:

    | Click Element    my_element
    | Wait Until Page Contains Element    //*[@type="android.widget.EditText"]


    Appium additionally supports some of the [https://w3c.github.io/webdriver/webdriver-spec.html|Mobile JSON Wire Protocol] locator strategies.
    It is also possible to specify the approach AppiumLibrary should take
    to find an element by specifying a lookup strategy with a locator
    prefix. Supported strategies are:

    | *Strategy*        | *Example*                                                      | *Description*                     | *Note*                      |
    | identifier        | Click Element `|` identifier=my_element                        | Matches by @id attribute          |                             |
    | id                | Click Element `|` id=my_element                                | Matches by @resource-id attribute |                             |
    | accessibility_id  | Click Element `|` accessibility_id=button3                     | Accessibility options utilize.    |                             |
    | xpath             | Click Element `|` xpath=//UIATableView/UIATableCell/UIAButton  | Matches with arbitrary XPath      |                             |
    | class             | Click Element `|` class=UIAPickerWheel                         | Matches by class                  |                             |
    | android           | Click Element `|` android=UiSelector().description('Apps')     | Matches by Android UI Automator   |                             |
    | ios               | Click Element `|` ios=.buttons().withName('Apps')              | Matches by iOS UI Automation      |                             |
    | nsp               | Click Element `|` nsp=name=="login"                            | Matches by iOSNsPredicate         | Check PR: #196              |
    | css               | Click Element `|` css=.green_button                            | Matches by css in webview         |                             |
    | name              | Click Element `|` name=my_element                              | Matches by @name attribute        | *Only valid* for Selendroid |

    == Using webelements ==

    Starting with version 1.4 of the AppiumLibrary, one can pass an argument
    that contains a WebElement instead of a string locator. To get a WebElement,
    use the new `Get WebElements` or `Get WebElement` keyword.

    For example:
    | @{elements}    Get Webelements    class=UIAButton
    | Click Element    @{elements}[2]

    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self, timeout=5, run_on_failure='Capture Page Screenshot'):
        """AppiumExtensionLibrary can be imported with optional arguments.

        ``timeout`` is the default timeout used to wait for all waiting actions.
        It can be later set with `Set Appium Timeout`.

        ``run_on_failure`` specifies the name of a keyword (from any available
        libraries) to execute when a AppiumLibrary keyword fails.

        By default `Capture Page Screenshot` will be used to take a screenshot of the current page.
        Using the value `No Operation` will disable this feature altogether. See
        `Register Keyword To Run On Failure` keyword for more information about this
        functionality.

        Examples:
        | Library | AppiumExtensionLibrary | 10 | # Sets default timeout to 10 seconds                                                                             |
        | Library | AppiumExtensionLibrary | timeout=10 | run_on_failure=No Operation | # Sets default timeout to 10 seconds and does nothing on failure           |
        """
        for base in AppiumExtensionLibrary.__bases__:
            base.__init__(self)
        self.set_appium_timeout(timeout)
        self.register_keyword_to_run_on_failure(run_on_failure)
