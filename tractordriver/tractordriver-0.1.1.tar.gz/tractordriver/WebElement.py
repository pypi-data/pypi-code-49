import json
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, InvalidElementStateException
from selenium.webdriver.support.wait import WebDriverWait
from six import string_types
from selenium.webdriver.remote.webelement import WebElement
import uuid
import re
from selenium.webdriver.common.action_chains import ActionChains

from tractordriver.resource import Resource


class Element(WebElement):
    def js_click(self):
        """
        :Description: Execute the `click` event on the target element.
        :param element: Element for browser instance to target.
        :type element: WebElement
        """
        self._parent.execute_script('arguments[0].click()', self)
        return self

    @classmethod
    def __type2js(cls, value):
        """
        :Description: Convert python value to executable javascript value by type.
        :param value: Value to transform.
        :type value: None, bool, int, float, string
        :return: string
        """
        if value is None:
            return 'null'
        elif isinstance(value, bool):
            return 'false' if not value else 'true'
        elif isinstance(value, (int, float)):
            return '%s' % value
        elif isinstance(value, dict):
            return json.dumps(dict)
        return '"%s"' % value

    @classmethod
    def __type2python(cls, value):
        """
        :Description: Convert javascript value to python value by type.
        :param value: Value to transform.
        :type value: None, bool, int, float, string
        :return: None, bool, int, float, string
        """
        if isinstance(value, string_types):
            if value is 'null':
                return None
            elif value in ('true', 'false'):
                return False if value == 'false' else True
            elif value.replace('.', '', 1).isdigit():
                return eval(value)
            elif value.startswith('{') and value.endswidth('}'):
                try:
                    return json.loads(value)
                except ValueError:
                    return value
        return value

    def js_wait(self, condition, interval, *args):
        """
        :Description: Create an interval in vm.window, will clear interval after condition met.
        :param condition: Condition in javascript to pass to interval.
        :example: '$el.innerText == "cheesecake"'
        :example: '$el[0].disabled && $el[1].disabled'
        :type condition: string
        :param interval: Time in milliseconds to execute interval.
        :type interval: int or float
        :param *args: WebElement or selector of condition element.
        :type *args: tuple
        :return: string
        """
        hid = lambda: '$' + str(uuid.uuid1())[:8]
        handle = hid()
        if len(args):
            element_handle = hid()
            self._parent.execute_script(
                'window["{}"] = [];'.format(element_handle)
            )  # create element container in window scope
            for el in args:
                if isinstance(el, string_types):
                    # assume selector
                    self._parent.execute_script('window["{}"].push({});'.format(
                        element_handle, 'function() { return document.querySelector("%s") }' % el))
                else:
                    # assume web element
                    self._parent.execute_script(
                        'window["{}"].push(arguments[0]);'.format(element_handle), el)
            if len(args) == 1:
                condition = condition.replace('$el', 'window["{}"][0]{}'.format(
                    element_handle, '()' if isinstance(args[0], string_types) else ''))
            else:
                regex = r'(\$el\[([0-9]{0,3})\])'
                results = re.findall(regex, condition)  # [('$el[0]', '0'), ('$el[1]', '1'), ...]
                for result in results:
                    pos = eval(result[1])
                    if pos + 1 <= len(args):
                        condition = condition.replace(result[0], 'window["{}"][{}]{}'.format(
                            element_handle, pos, '()' if isinstance(args[pos], string_types) else ''))

            self._parent.execute_script(
                'window["%s"]=window.setInterval(function(){if(%s){ \
                (window.clearInterval(window["%s"])||true)&&(window["%s"]=-1); \
                delete window["%s"];}}, %s)' % (handle, condition, handle, handle, \
                                                element_handle, interval))  # create interval
        else:
            self._parent.execute_script(
                'window["%s"]=window.setInterval(function(){if(%s){ \
                (window.clearInterval(window["%s"])||true)&&(window["%s"]=-1);}}, %s)' % (
                    handle, condition, handle, handle, interval))  # create interval

        return handle

    def wait_status(self, handle):
        """
        :Description: Check the status of browser wait.
        :param handle: Interval handle returned from `self.wait`.
        :type handle: string
        :return: bool
        """
        return self._parent.execute_script('return window["%s"] == -1' % handle)

    def is_enabled(self):
        """
        Used to check at least one element is available and all are enabled.

        :return: bool
        """

        if self.get_property('disabled'):
            return False
        return True

    def is_disabled(self):
        """
        Used to check at least one element is available and all are disabled.

        :return: bool
        """
        if not self.get_property('disabled'):
            return False
        return True

    def is_visible(self):
        """
        :Description: Get's the visibility of the provided target element.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :return: bool
        """
        return bool(self._parent.execute_script(
            'return !!(arguments[0].offsetWidth || arguments[0].offsetHeight || \
            arguments[0].getBoundingClientRect().height || \
            arguments[0].getBoundingClientRect().width) && \
            (arguments[0].style.visibility == "" || arguments[0].style.visibility == "visible") && \
            (arguments[0].style.opacity ? arguments[0].style.opacity > 0 : true);',
            self))

    def click(self):
        """
        :Description: Execute the `click` event on the target element.
        :param element: Element for browser instance to target.
        :type element: WebElement
        """
        actions = ActionChains(self._parent)
        actions.move_to_element(self).perform()
        super(Element, self).click()
        return self

    def submit(self):
        super(Element, self).submit()
        return self

    def clear(self):
        super(Element, self).clear()
        return self

    def send_keys(self, *value):
        super(Element, self).send_keys(*value)
        return self

    def dbl_click(self):
        """
        :Description: Execute the `dbclick` event on the target element.
        :param element: Element for browser instance to target.
        :type element: WebElement
        """
        self._parent.execute_script(
            'var e = document.createEvent("mouseEvent"); \
            e.initEvent("dblclick", true, true); \
            arguments[0].dispatchEvent(e);', self)
        return self

    def select(self):
        """
        :Description: Sets the attribute `selected` to true and triggers `change` event.
        :param element: Element for browser instance to target.
        :type element: WebElement
        """
        self._parent.execute_script(
            'arguments[0].selected = "selected"; \
             arguments[0].dispatchEvent(new Event("change"));', self)

        return self

    def deselect(self):
        """
        :Description: Sets the attribute `selected` to null and triggers `change` event.
        :param element: Element for browser instance to target.
        :type element: WebElement
        """
        self._parent.execute_script(
            'arguments[0].selected = null; \
             arguments[0].dispatchEvent(new Event("change"));', self)

        return self

    def get_attribute(self, attribute, convert_type=True):
        """
        :Description: Return the given attribute of the target element.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :param attribute: Attribute of target element to return.
        :type attribute: string
        :param convert_type: If enabled, will return pythonic type.
        :type convert_type: bool
        :return: None, bool, int, float, string
        """
        attribute = self._parent.execute_script(
            'return arguments[0].getAttribute("%s");' % attribute, self)

        return self.__type2python(attribute) if convert_type else attribute

    def set_attribute(self, attribute, value):
        """
        :Description: Modify the given attribute of the target element.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :param attribute: Attribute of target element to modify.
        :type attribute: string
        :param value: Value of target element's attribute to modify.
        :type value: None, bool, int, float, string
        """
        self._parent.execute_script('arguments[0].setAttribute("%s", %s);' % (
            attribute, self.__type2js(value=value)), self)
        return self

    def remove_attribute(self, attribute):
        """
        :Description: Remove the given attribute from the target element.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :param attribute: Attribute of target element to remove.
        :type attribute: string
        """
        self._parent.execute_script('arguments[0].removeAttribute("%s");' % attribute, self)
        return self

    def get_property(self, prop):
        """
        :Description: Return the given attribute of the target element.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :param prop: Property of target element to return.
        :type prop: string
        :return: None, bool, int, float, string
        """
        return self._parent.execute_script('return arguments[0]["%s"];' % prop, self)

    def set_property(self, prop, value):
        """
        :Description: Modify the given attribute of the target element.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :param prop: Property of target element to modify.
        :type prop: string
        :param value: Value of target element's property to modify.
        :type value: None, bool, int float, string
        """
        self._parent.execute_script(
            'arguments[0]["%s"] = %s' % (prop, self.__type2js(value=value)), self)

        return self

    def get_value(self):
        """
        :Description: Return the value of the given element.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :return: string
        """
        return self.get_property(prop='value')

    def get_text(self):
        """
        :Description: Return the text content between the tags of the given element.
        :Info: Helpful for reading text from elements that do not support the `value` property.
        :param element: Element for browser instance to target.
        :return: string
        """
        return self.get_property(prop='innerText')

    def get_raw_text(self):
        """
        :Description: Return the text content between the tags of the given element.
        :Info: Helpful for reading text from elements that do not support the `value` property.
        :Warning: This will return the raw text content of the DOM's child scope.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :return: string
        """
        return self.get_property(prop='innerHTML')

    def trigger_event(self, event, event_type=None, options=None):
        """
        :Description: Trigger specified event of the given element.
        :param element: Element for browser instance to target.
        :type element: WebElement, (WebElement, ...)
        :param event: Event to trigger from target element.
        :type event: string, (string, ...)
        :param event_type: Event type.
        :type event_type: string
        :example: 'KeyboardEvent'
        :param options: Event options.
        :example: { 'bubbles': True, 'cancelable': False }
        :type options: dict
        """
        if not isinstance(self, (tuple, list)):
            element = [self]
        if not isinstance(event, (tuple, list)):
            event = [event]
        for el in element:
            for e in event:
                self._parent.execute_script(
                    'e = new %s("%s"); ops = %s; if (ops) {for(key in ops) { \
                        Object.defineProperty(e, key, { value: ops[key], configurable: true }) \
                    }} arguments[0].dispatchEvent(e)' % (
                        event_type if event_type else 'Event',
                        e, json.dumps(options) if options else 'undefined'
                    ), el)

    def scroll_into_view(self):
        """
        :Description: Scroll the target element into view.
        :Warning: This method relies on JQuery.
        :param element: Element for browser instance to target.
        :type element: WebElement
        """
        self._parent.execute_script('arguments[0].scrollIntoView(true);', self)
        return self

    @property
    def get_scrolling_offsets(self):
        """
        :Description: Returns the page scrolling x and y offsets.
        :return: dict
        """
        return {
            'x': self._parent.execute_script('return window.pageXOffset'),
            'y': self._parent.execute_script('return window.pageYOffset')
        }

    def ng_enable_debugging(self):
        """
        :Description: Enables angular debugging on given webpage.
        :Warning: This will only work for angular.js 1.x.
        """
        self._parent.execute_script('angular.reloadWithDebugInfo()')
        return self

    def ng_get_text(self):
        """
        :Description: Will return the DOM's value, if not found will default to `innerHTML`.
        :Warning: This will only work for angular.js 1.x.
        :Warning: This will only work for angular elements.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :return: string
        """
        return self._parent.execute_script('return angular.element(arguments[0]).text();', self)

    def ng_set_text(self, text):
        """
        :Description: Will set a DOM's value, if not found will default to `innerHTML`.
        :Warning: This will only work for angular.js 1.x.
        :Warning: This will only work for angular elements.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :param text: Text used for related operation.
        :type text: string
        """
        self._parent.execute_script('angular.element(arguments[0]).text("%s");' % text, self)

    def ng_toggle_class(self, target):
        """
        :Description: Toggle DOM class.
        :Warning: This will only work for angular.js 1.x.
        :Warning: This will only work for angular elements.
        :param element: Element for browser instance to target.
        :param target: Class to toggle.
        """
        self._parent.execute_script(
            'angular.element(arguments[0]).toggleClass("%s");' % target, self)
        return self

    def ng_trigger_event_handler(self, event):
        """
        :Description: Trigger angular event handler of element.
        :Warning: This will only work for angular.js 1.x.
        :Warning: This will only work for angular elements.
        :param element: Element for browser instance to target.
        :param event: Event to trigger.
        """
        self._parent.execute_script(
            'angular.element(arguments[0]).triggerHandler("%s");' % event, self)
        return self

    @staticmethod
    def __d2b_notation(prop):
        """
        :Description: Transform javascript dot notation to bracket notation.
        :param prop: Property to transform.
        :type prop: string
        :example: 'messages.total' >> someObject['messages']['total']
        :return: string
        """
        results = re.compile('[[$a-zA-Z]{0,}.').findall(prop)
        for i in range(0, len(results)):
            results[i] = ("['%s']" % results[i]).replace('.', '')
        return ''.join(results)

    @classmethod
    def __serialize_params(cls, params):
        param_str = ''
        for param in params:
            param_str += '%s,' % cls.__type2js(value=param)
        if param_str.endswith(','):
            param_str = param_str.replace(param_str[-1], '')
        return param_str

    def ng_get_scope_property(self, element, prop):
        """
        :Description: Will return value of property of element's scope.
        :Warning: This will only work for angular.js 1.x.
        :Warning: Requires angular debugging to be enabled.
        :param element: Element for browser instance to target.
        :param prop: Property of element's angular scope to target.
        :type prop: string
        :example: 'messages.total'
        :return: string
        """
        return self._parent.execute_script(
            'return angular.element(arguments[0]).scope()%s;' % self.__d2b_notation(
                prop=prop
            ), element)

    def ng_set_scope_property(self, element, prop, value):
        """
        :Description: Will set value of property of angular element's scope.
        :Warning: This will only work for angular.js 1.x.
        :Warning: Requires angular debugging to be enabled.
        :param element: Element for browser instance to target.
        :param prop: Property of element's angular scope to target.
        :type prop: string
        :example: 'messages.total'
        :param value: Value to specify to angular element's scope's property.
        :type value: None, bool, int, float, string
        """
        self._parent.execute_script(
            'angular.element(arguments[0]).scope()%s = %s;' % (
                self.__d2b_notation(prop=prop), self.__type2js(value=value)
            ), element)
        return self

    def ng_call_scope_function(self, func, params='', return_out=False):
        """
        :Description: Will execute scope function with provided parameters.
        :Warning: This will only work for angular.js 1.x.
        :Warning: Requires angular debugging to be enabled.
        :param element: Element for browser instance to target.
        :param func: Function to execute from angular element scope.
        :type func: string
        :param params: String (naked) args, or list of parameters to pass to target function.
        :type params: string, tuple, list
        :param return_out: Return output of function call otherwise None
        :type return_out: bool
        """
        if isinstance(params, string_types):
            param_str = params
        elif isinstance(params, (tuple, list)):
            param_str = self.__serialize_params(params)
        else:
            raise ValueError('Invalid type specified for function parameters')
        exec_str = 'angular.element(arguments[0]).scope().%s(%s);' % (func, param_str)
        if return_out:
            return self.__type2python(
                self._parent.execute_script('return {}'.format(exec_str), self))
        else:
            self._parent.execute_script(exec_str, self)

    def ng_get_ctrl_property(self, prop):
        """
        :Description: Will return value of property of element's controller.
        :Warning: This will only work for angular.js 1.x.
        :Warning: Requires angular debugging to be enabled.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :param prop: Property of element's angular controller to target.
        :type prop: string
        :example: 'messages.total'
        :return: string
        """
        return self._parent.execute_script(
            'return angular.element(arguments[0]).controller()%s;' % self.__d2b_notation(prop=prop),
            self)

    def ng_set_ctrl_property(self, prop, value):
        """
        :Description: Will set value of property of element's controller.
        :Warning: This will only work for angular.js 1.x.
        :Warning: Requires angular debugging to be enabled.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :param prop: Property of element's angular scope to target.
        :type prop: string
        :example: 'messages.total'
        :param value: Value to specify to angular element's controller's property.
        :type value: None, bool, int, float, string
        """
        self._parent.execute_script(
            'angular.element(arguments[0]).controller()%s = %s;' % (
                self.__d2b_notation(prop=prop), self.__type2js(value=value)
            ), self)

    def ng_call_ctrl_function(self, func, params='', return_out=False):
        """
        :Description: Will execute controller function with provided parameters.
        :Warning: This will only work for angular.js 1.x.
        :Warning: Requires angular debugging to be enabled.
        :param element: Element for browser instance to target.
        :param func: Function to execute from angular element controller.
        :type func: string
        :param params: String (naked) args, or list of parameters to pass to target function.
        :type params: string, tuple, list
        :param return_out: Return output of function call otherwise None
        :type return_out: bool
        """
        if isinstance(params, string_types):
            param_str = params
        elif isinstance(params, (tuple, list)):
            param_str = self.__serialize_params(params)
        else:
            raise ValueError('Invalid type specified for function parameters')
        exec_str = 'angular.element(arguments[0]).controller().%s(%s);' % (func, param_str)
        if return_out:
            return self.__type2python(
                self._parent.execute_script('return {}'.format(exec_str), self))
        else:
            self._parent.execute_script(exec_str, self)

    def ng2_get_component_property(self, prop):
        """
        :Description: Will get value of property of element's component instance.
        :Warning: This will only work for Angular components.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :param prop: Property of element's component to target.
        :type prop: string
        :example: 'messages.total'
        :return: string
        """
        return self._parent.execute_script(
            'return ng.probe(arguments[0]).componentInstance%s;' % self.__d2b_notation(prop=prop),
            self)

    def ng2_set_component_property(self, prop, value):
        """
        :Description: Will set value of property of element's component instance.
        :Warning: This will only work for Angular components.
        :param element: Element for browser instance to target.
        :type element: WebElement
        :param prop: Property of element's component to target.
        :type prop: string
        :example: 'messages.total'
        :param value: Value to specify to component's property.
        :type value: None, bool, int, float, string
        """
        self._parent.execute_script(
            'ng.probe(arguments[0]).componentInstance%s = %s;' % (
                self.__d2b_notation(prop=prop), self.__type2js(value=value)), self)

        return self

    def ng2_call_component_function(self, func, params='', return_out=False):
        """
        :Description: Will execute the component instance function with provided parameters.
        :Warning: This will only work for Angular components.
        :param element: Element for browser instance to target.
        :param func: Function to execute from component instance.
        :type func: string
        :param params: String (naked) args, or list of parameters to pass to target function.
        :type params: string, tuple, list
        :param return_out: Return output of function call otherwise None
        :type return_out: bool
        """
        if isinstance(params, string_types):
            param_str = params
        elif isinstance(params, (tuple, list)):
            param_str = self.__serialize_params(params)
        else:
            raise ValueError('Invalid type specified for function parameters')
        exec_str = 'ng.probe(arguments[0]).componentInstance.%s(%s);' % (func, param_str)
        if return_out:
            return self.__type2python(
                self._parent.execute_script('return {}'.format(exec_str), self))
        else:
            self._parent.execute_script(exec_str, self)

    # def fmt(self, **kwargs):
    #     """
    #     Used to format selectors.
    #
    #     :return: Elements
    #     """
    #     self._selector = self.selector
    #     self.selector = Template(self.selector).safe_substitute(**kwargs)
    #     return self

    def mousedown(self):
        """
        Dispatches a mousedown event on the given element.

        :return: Element, None
        """
        # pragma: no cover
        # ignoring from coverage, assume covered in scroll_to and trigger_event
        if self:
            self.scroll_into_view()
            self.trigger_event(self, 'mousedown', 'MouseEvent')
            return self
        return None

    def wait_for(self, timeout, available=True, error=None):
        """
        Wait for a given element to become available.

        :param timeout: Time in seconds to wait for element.
        :type timeout: int
        :available: Used to check whether element is available or not available.
        :type available: bool
        :param error: Error message, if passed will raise NoSuchElementException.
        :type error: string, bool
        :return: Element, None
        """
        check = Checks(self)
        if not self._parent.wait(timeout=timeout, condition=check.available \
                if available else check.not_available):

            if error:
                raise NoSuchElementException(error if isinstance(error, string_types) else \
                                                 'Element by selector "{}" was {}' \
                                             .format(self.selector, 'not found' if available else 'found'))
            return None

        return self

    def wait_village(self, timeout=30):
        while not self.is_visible() and timeout > 0:
            time.sleep(1)
            timeout -= 1
        return self

    def wait_visible(self, timeout=10, error=None):
        """
        Wait for given element to be visible.

        :param timeout: Time in seconds to wait for element.
        :type timeout: int
        :param error: Raise ElementNotVisibleException on failure.
        :type error: bool, string
        :return: Element, None
        """
        if not self._parent.wait(timeout=timeout, condition=self.is_visible):
            if error:
                raise ElementNotVisibleException(error if isinstance(error, string_types) \
                                                     else f'Element by selector "{self.selector}"\
                                                      not found or is not visible')
            return None

        return self

    def wait_invisible(self, timeout, error=None):
        """
        Wait for given element to be invisible.

        :param timeout: Time in seconds to wait for element.
        :type timeout: int
        :param error: Raise InvalidElementStateException on failure.
        :type error: bool, string
        :return: Element, None
        """

        if not self._parent.wait(timeout=timeout, condition=not self.is_visible):
            if error:
                raise InvalidElementStateException(error if isinstance(error, string_types) else \
                                                       'Element by selector "{}" not found or is visible'.format(
                                                           self.selector))
            return None

        return self

    def wait_enabled(self, timeout, error=None):
        """
        Wait for given element to be enabled.

        :param timeout: Time in seconds to wait for element.
        :type timeout: int
        :param error: Raise InvalidElementStateException on failure.
        :type error: bool, string
        :return: Element, None
        """
        check = Checks(self)

        if not self._parent.wait(timeout=timeout, condition=check.enabled):
            if error:
                raise InvalidElementStateException(error if isinstance(error, string_types) else \
                                                       'Element by selector "{}" not found or is disabled'.format(
                                                           self.selector))
            return None

        return self

    def wait_disabled(self, timeout, error=None):
        """
        Wait for given element to be disabled.

        :param timeout: Time in seconds to wait for element.
        :type timeout: int
        :param error: Raise InvalidElementStateException on failure.
        :type error: bool, string
        :return: Element, None
        """
        check = Checks(self)
        if not self._parent.wait(timeout=timeout, condition=check.disabled):
            if error:
                raise InvalidElementStateException(error if isinstance(error, string_types) else \
                                                       'Element by selector "{}" not found or is enabled'.format(
                                                           self.selector))
            return None

        return self

    def wait_js(self, condition, interval):
        """
        Wait for element by javascript condition.

        :param condition: Javascript condition to execute.
        :type condition: string
        :param interval: Interval to check condition by in ms.
        :type interval: int
        :return: Element, None
        """
        self.wait_handle = self.wait(condition, interval, self.selector)
        return self

    def switch_to(self):
        """
        Switch into an iframe element context.

        :return: Element, None
        """
        found = self
        if found:
            self._parent.switch_to.frame(found)
            return self
        return None

    def wait_presense_of_element(self, timeout=20):
        wait = WebDriverWait(self, timeout)
        element = wait.until(EC.presence_of_element_located(self))
        return element


class Checks(Resource):
    """
    Base resource for multiple element checks.

    :param elements: Elements instance to reference.
    :type element: Elements
    """

    def __init__(self, elements, value=''):

        self.elements = elements
        self.validate()
        self.value = value

        try:
            self.elements = iter(elements)
        except TypeError:
            self.elements = [self.elements]

    def visible(self):
        """
        Used to check at least one element is available and all are visible.

        :return: bool
        """
        found = self
        return found and self.is_visible(found)

    def invisible(self):
        """
        Used to check at least one element is available and all are invisible.

        :return: bool
        """
        found = self.elements if self.elements else None
        if found:
            for element in found:
                if element.is_visible():
                    return False
            return True

    def is_enabled(self):
        """
        Used to check at least one element is available and all are enabled.

        :return: bool
        """
        found = self.elements
        if not len(found):  # pylint: disable=len-as-condition
            return False
        for element in found:
            if self.elements.get_property(element, 'disabled'):
                return False
        return True

    def is_disabled(self):
        """
        Used to check at least one element is available and all are disabled.

        :return: bool
        """
        found = self.elements
        if not len(found):  # pylint: disable=len-as-condition
            return False
        for element in found:
            if not self.elements.get_property(element, 'disabled'):
                return False
        return True

    # meta = {'required_fields': [('elements', Element)]}
