import json
import os
import time
from functools import wraps
from math import floor
from selenium.common.exceptions import NoSuchElementException
# from pyseleniumjs import E2EJS
from selenium.common.exceptions import JavascriptException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tractordriver.WebElement import Element


#
# class Element(WebElement):
#     def __init__(self, parent):
#         super(Element, self).__init__(parent, id_=None, w3c=False)
#
#     def __repr__(self):
#         return '<{0.__module__}.{0.__name__} (session="{1}", element="{2}")>'.format(
#             type(self), self._parent.session_id, self._id)


class AngularNotFoundException(WebDriverException):
    """An exception raised if angular.js could not be found on a web page."""


def angular_wait_required(wrapped):
    @wraps(wrapped)
    def wait_for_angular(driver, *args, **kwargs):
        driver.wait_for_angular()
        return wrapped(driver, *args, **kwargs)

    return wait_for_angular


class By(By):
    MODEL = "model name"
    BINDING = "Binding"
    BUTTON_TEXT = "Button text"
    PARTIAL_BUTTON_TEXT = "Partial button text"
    REPEATER_ROWS = 'repeater_rows'


class TractorDriver(object):

    def __init__(self, *args, **kwargs):
        super(TractorDriver, self).__init__()
        self._web_element_cls = Element
        file_source = os.path.join(os.path.dirname(__file__), 'clientsidescripts.js')
        with open(file_source) as f:
            js_script = f.read()
            f.close()
        # self._web_element_cls.js = E2EJS
        self._exports = json.loads(self.execute_script(js_script + """return JSON.stringify(exports);"""))
        self.__dict__.update(self._exports)

    # @staticmethod
    def explicity_wait_for_visible(self, element, timeout=60):
        wait = WebDriverWait(self, timeout=timeout)
        result = wait.until(EC.visibility_of_element_located(element))
        # element = wait.until(EC.presence_of_element_located(element))
        return result

    def wait_for_clickable(self, element, timeout=5):
        wait = WebDriverWait(self, timeout=timeout)
        element = wait.until(EC.element_to_be_clickable(element))
        return element

    def wait_for(self, wait_type, element, timeout=5):
        """
        :param wait_type: method
        :param timeout: int
        :param element: Element
        """
        wait = WebDriverWait(self, timeout)
        element = wait.until(wait_type(element))
        return element

    def find_element(self, by=By.ID, value=None, auto_wait=True, timeout=20):
        """
        :param auto_wait: bool
        :param timeout: int
        :param wait_method: object
        :type by: By
        :type value: str
        """
        if by is By.MODEL:
            element = self.find_element_by_model(value)
        elif by is By.BINDING:
            element = self.find_element_by_binding(value)
        elif by is By.BUTTON_TEXT:
            element = self.find_element_by_button_text(value)
        elif by is By.PARTIAL_BUTTON_TEXT:
            element = self.find_element_by_partial_button_text(value)
        elif by is By.REPEATER_ROWS:
            element = self.find_all_repeater_rows(value)
        else:
            element = super().find_element(by=by, value=value)
        if isinstance(element, (list,)):
            for elem in element:
                elem.selector = value
        else:
            element.selector = value
        if auto_wait:
            if not isinstance(element, (list,)):
                element.scroll_into_view()
                element.wait_visible(timeout=timeout, error=True)
        return element

    def find_elements(self, by=By.ID, value=None, auto_wait=True, timeout=20):
        """
        :param auto_wait: bool
        :param timeout: int
        :param wait_method: object
        :type by: By
        :type value: str
        """
        if by is By.MODEL:
            self.find_elements_by_model(value)
        elif by is By.BINDING:
            elements = self.find_elements_by_binding(value)
        elif by is By.BUTTON_TEXT:
            elements = self.find_elements_by_button_text(value)
        elif by is By.PARTIAL_BUTTON_TEXT:
            elements = self.find_elements_by_partial_button_text(value)
        elif by is By.REPEATER_ROWS:
            elements = self.find_all_repeater_rows(value)
        else:
            elements = super().find_elements(by=by, value=value)

        if isinstance(elements, (list,)):
            for elem in elements:
                elem.selector = value
        else:
            elements.selector = value
        if auto_wait:
            if not isinstance(elements, (list,)):
                # element.scroll_into_view()
                elements.wait_visible(timeout=timeout, error=True)
        return elements

    def _run_script(self, script, *args, **kwargs):
        _async = kwargs.pop('_async', False)
        new_args = tuple(['true' if x is True else x for x in list(args)]) if True in args else args
        if _async:
            return self.execute_async_script(script, *new_args, **kwargs), self._web_element_cls
        else:
            return self.execute_script(script, *new_args, **kwargs)

    def wait_for_angular(self):
        return self._run_script(self.waitForAngular, 'body', _async=True)

    @angular_wait_required
    def find_elements_by_model(self, model):
        return self._run_script(self.findByModel, model, _async=False)

    @angular_wait_required
    def find_element_by_model(self, model):
        return self.find_elements_by_model(model)[0]

    @angular_wait_required
    def find_elements_by_binding(self, bindings):
        return self._run_script(self.findBindings, bindings)

    @angular_wait_required
    def find_element_by_binding(self, binding):
        return self.find_elements_by_binding(binding)[0]

    @angular_wait_required
    def find_elements_by_option(self, options):
        return self._run_script(self.findByOptions, options)

    @angular_wait_required
    def find_element_by_option_value(self, option, value, show_first=True):
        opts = self.find_elements_by_option(option)
        results = []
        for item in opts:
            if value in item.get_text():
                results.append(item)
        if not len(results):
            raise NoSuchElementException(f"could not find element by option {option} and value {value}")
        return results[0] if show_first else results

    @angular_wait_required
    def find_element_by_option(self, option):
        elements = self.find_elements_by_option(option)
        if len(elements) == 1:
            return elements[0]
        else:
            raise NoSuchElementException(f" {len(elements)} elements found with \"{option}\" option value. ")

    @angular_wait_required
    def find_elements_by_button_text(self, button_text):
        return self._run_script(self.findByButtonText, button_text)

    @angular_wait_required
    def find_element_by_button_text(self, button_text):
        elements = self.find_elements_by_button_text(button_text)
        if len(elements) == 1:
            return elements[0]
        else:
            raise NoSuchElementException(f" {len(elements)} elements found with \"{button_text}\" button text. ")

    @angular_wait_required
    def find_elements_by_partial_button_text(self, partial_button_text):
        return self._run_script(self.findByPartialButtonText, partial_button_text)

    @angular_wait_required
    def find_element_by_partial_button_text(self, partial_button_text):
        return self.find_elements_by_partial_button_text(partial_button_text)[0]

    @angular_wait_required
    def find_element_by_repeater_rows(self, repeater_rows, using=None):
        return self._run_script(self.findRepeaterRows, repeater_rows, using)

    @angular_wait_required
    def find_all_repeater_rows(self, repeater_rows):
        return self._run_script(self.findAllRepeaterRows, repeater_rows)

    @angular_wait_required
    def find_all_repeater_rows_by_value(self, repeater_rows, value, exact_match=False):
        elements = []
        items = self.find_all_repeater_rows(repeater_rows)
        for item in items:
            if exact_match:
                if item.get_text() == value:
                    elements.append(item)
            else:
                if value in item.get_text():
                    elements.append(item)
        if not len(elements):
            raise NoSuchElementException(f'Could not found any element by {repeater_rows} repeater and {value} value')
        return elements

    @angular_wait_required
    def find_repeater_row_by_value(self, repeater_rows, value, exact_match=False):
        """
        :type repeater_rows: str
        :type value: str
        :type exact_match: bool
        """
        items = self.find_all_repeater_rows_by_value(repeater_rows, value, exact_match=exact_match)
        if len(items) != 1:
            raise NoSuchElementException(
                f"Expected to find one item with {repeater_rows} repeater and {value} value but multiple items have "
                f"been found")
        return items[0]

    @angular_wait_required
    def find_all_repeater_column(self, repeater_column):
        return self._run_script(self.findRepeaterColumn, repeater_column)

    def repeater_match(self):
        return self._run_script(self.repeaterMatch)

    @angular_wait_required
    def find_element_by_css_containing_text(self, css_containing_text):
        return self._run_script(self.findByCssContainingText, css_containing_text)

    def _test_for_angular(self, timeout=10):
        return self._run_script(self.testForAngular, floor(timeout / 1000))[0]

    def reload(self):
        url = self.execute_script('return window.location.href')
        self.get(url)

    @angular_wait_required
    def set_location(self, url):
        return self._run_script(self.setLocation, 'body', url)

    def _location_equals(self, location):
        result = self.execute_script('return window.location.href')
        return result == location

    # @property
    # @angular_wait_required
    # def current_url(self):
    #     return self.current_url

    @property
    @angular_wait_required
    def current_location(self):
        return self.execute_script('return window.location.href')

    @property
    @angular_wait_required
    def page_source(self):
        return self.page_source

    # TODO: fix issue catching exception
    def is_angular_page(self, timeout=10):

        # test_result = self._test_for_angular()
        # print(test_result)
        # angular_on_page = test_result[0]
        # if not angular_on_page:
        #     message = test_result[1]
        #     raise AngularNotFoundException(
        #         'Angular could not be found on page: {}:'
        #         ' {}'.format(self.current_url, message)
        #     )
        try:
            self._test_for_angular(timeout)
        except JavascriptException:
            return False
        return True

    def wait_and_click(self, element, timeout=10):
        wait = WebDriverWait(self, timeout)
        element = wait.until(EC.element_to_be_clickable(element))
        element.click()
        return element

    def exit(self, safe_exit=False):
        """
        Safely exit instance of webdriver.

        :param safe_exit: Disable any possible alert or confirmation popup windows.
        :type safe_exit: bool
        """
        if safe_exit:
            self.execute_script('delete window.alert; delete window.confirm')
        try:
            self.browser.stop_client()
        except (WebDriverException, AttributeError):
            self.logger.warning('Could not close remote driver')
        finally:
            self.quit()

    # TODO: Add browser logs to the Aluure report
    def browser_logs(self, name=None, path=None):
        """
        Dumps browser logs to local directory.

        :Warning: `self.js.console_logger` must be executed to store logs.
        :param name: Name log file dropped to disk, will default to timestamp if not specified.
        :type name: string
        :param path: Path to drop console log in.
        :type path: string
        :return: string
        """
        if path and not os.path.exists(path):
            os.mkdir(path)
        try:
            timestamp = str(int(time.time()))
            log_path = '%sconsole.%s.json' % (path, ('%s.%s' % (name, timestamp)) if \
                name else timestamp)
            with open(log_path, 'a', encoding='utf-8') as logfile:
                logfile.write(self.console_dump())
            return log_path
        except WebDriverException:
            self.logger.critical('Browser logger object not found, could not return any logs.')

    def screen_shot(self, prefix=None, path=None):
        """
        Takes a screen shot and saves it specified path.

        :param prefix: Prefix for screenshot.
        :type prefix: string
        :param path: Path to drop screen shot in.
        :type path: string
        :return: string
        """
        file_location = os.path.join(
            path if path else './', (prefix + '_' if prefix else '') + str(time.time()) + '.png')
        self.browser.get_screenshot_as_file(filename=file_location)
        return file_location

    @classmethod
    def wait(cls, timeout=1, condition=None, reverse=False, throw_error=False):
        """
        Assisted delays between browser and main thread.

        :param timeout: Time in seconds to wait.
        :type timeout: int
        :param condition: (callable) Wait 1 to timeout seconds until condition met.
        :param reverse: Will wait for the condition to evaluate to False instead of True.
        :param throw_error: Will throw error raised by condition at end of timeout.
        :type throw_error: bool
        :return: bool
        """
        if callable(condition):
            if not isinstance(timeout, int) or timeout < 1:
                raise ValueError('Timeout must be an integer or float greater than or equal to 1')
            error = None
            for _ in range(timeout):
                try:
                    if reverse:
                        if not condition():
                            return False
                    else:
                        if condition():
                            return True
                except Exception as exc:  # pylint: disable=broad-except
                    if throw_error:
                        error = exc
                time.sleep(1)
            if error and throw_error:
                raise error  # pylint: disable=raising-bad-type
            return reverse
        else:
            time.sleep(timeout)
            return True

    def console_logger(self):
        """
        :Description: Override browser console for log and error store.
        :Source: https://github.com/neetVeritas/pyselenium-js/issues/9#issuecomment-304284471
        :Warning: This will only enable console logging per session.
        """
        self.execute_script(
            'var _0x4f63=["\x24\x63\x6F\x6E\x73\x6F\x6C\x65","\x24\x6C\x6F\x67\x73","\x24\x65\x72\x72\x6F\x72\x73","\x24\x77\x61\x72\x6E\x69\x6E\x67\x73","\x61\x73\x73\x65\x72\x74","\x63\x6C\x65\x61\x72","\x67\x72\x6F\x75\x70","\x67\x72\x6F\x75\x70\x43\x6F\x6C\x6C\x61\x70\x73\x65\x64","\x67\x72\x6F\x75\x70\x45\x6E\x64","\x69\x6E\x66\x6F","\x74\x61\x62\x6C\x65","\x74\x69\x6D\x65","\x74\x69\x6D\x65\x45\x6E\x64","\x6C\x6F\x67","\x70\x72\x6F\x74\x6F\x74\x79\x70\x65","\x70\x75\x73\x68","\x65\x72\x72\x6F\x72","\x65\x78\x63\x65\x70\x74\x69\x6F\x6E","\x74\x72\x61\x63\x65","\x77\x61\x72\x6E","\x64\x75\x6D\x70","\x73\x74\x72\x69\x6E\x67\x69\x66\x79","\x24","\x61\x6A\x61\x78\x45\x72\x72\x6F\x72","\x75\x72\x6C","\x74\x79\x70\x65","\x73\x74\x61\x74\x75\x73","\x72\x65\x73\x70\x6F\x6E\x73\x65\x54\x65\x78\x74","\x63\x6F\x6E\x73\x6F\x6C\x65"];function Logger(){this[_0x4f63[0]]= console,this[_0x4f63[1]]= [],this[_0x4f63[2]]= [],this[_0x4f63[3]]= [],this[_0x4f63[4]]= this[_0x4f63[0]][_0x4f63[4]],this[_0x4f63[5]]= this[_0x4f63[0]][_0x4f63[5]],this[_0x4f63[6]]= this[_0x4f63[0]][_0x4f63[6]],this[_0x4f63[7]]= this[_0x4f63[0]][_0x4f63[7]],this[_0x4f63[8]]= this[_0x4f63[0]][_0x4f63[8]],this[_0x4f63[9]]= this[_0x4f63[0]][_0x4f63[9]],this[_0x4f63[10]]= this[_0x4f63[0]][_0x4f63[10]],this[_0x4f63[11]]= this[_0x4f63[0]][_0x4f63[11]],this[_0x4f63[12]]= this[_0x4f63[0]][_0x4f63[12]]}Logger[_0x4f63[14]][_0x4f63[13]]= function(){this[_0x4f63[1]][_0x4f63[15]](arguments[0]),this[_0x4f63[0]][_0x4f63[13]](arguments[0])},Logger[_0x4f63[14]][_0x4f63[16]]= function(){this[_0x4f63[2]][_0x4f63[15]](arguments[0]),this[_0x4f63[0]][_0x4f63[16]](arguments[0])},Logger[_0x4f63[14]][_0x4f63[17]]= function(){this[_0x4f63[2]][_0x4f63[15]](arguments[0]),this[_0x4f63[0]][_0x4f63[17]](arguments[0])},Logger[_0x4f63[14]][_0x4f63[18]]= function(){this[_0x4f63[2]][_0x4f63[15]](arguments[0]),this[_0x4f63[0]][_0x4f63[18]](arguments[0])},Logger[_0x4f63[14]][_0x4f63[19]]= function(){this[_0x4f63[3]][_0x4f63[15]](arguments[0]),this[_0x4f63[0]][_0x4f63[19]](arguments[0])},Logger[_0x4f63[14]][_0x4f63[20]]= function(){return JSON[_0x4f63[21]]({logs:this[_0x4f63[1]],errors:this[_0x4f63[2]],warnings:this[_0x4f63[3]]})},(window[_0x4f63[22]]&& $(document)&& $(document)[_0x4f63[23]]?!0:!1)&& $(document)[_0x4f63[23]](function(){console[_0x4f63[16]]({location:arguments[2][_0x4f63[24]],method:arguments[2][_0x4f63[25]],status:arguments[1][_0x4f63[26]],error:arguments[3],response:arguments[1][_0x4f63[27]]})}),window[_0x4f63[28]]=  new Logger')

    def console_dump(self):
        """
        :Description: Return console logs as stringified JSON structure.
        :Warning: This will only work once `console_logger` is executed.
        :return: string
        """
        return self.execute_script('return console.dump()')
