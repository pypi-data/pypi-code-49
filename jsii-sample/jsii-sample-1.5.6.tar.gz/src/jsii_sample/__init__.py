"""
# aws-delivlib-sample

Sample project for [aws-delivlib](https://github.com/awslabs/aws-delivlib).
"""
import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty
__jsii_assembly__ = jsii.JSIIAssembly.load("jsii-sample", "1.5.6", __name__, "jsii-sample@1.5.6.jsii.tgz")
class HelloJsii(metaclass=jsii.JSIIMeta, jsii_type="jsii-sample.HelloJsii"):
    """This guy knows how to say hello, in multiple langauges."""
    def __init__(self, *, goodbye_message: typing.Optional[str]=None) -> None:
        """
        :param props: -
        :param goodbye_message: The message to emit when saying goodbye. Default: "Goodbye"
        """
        props = HelloJsiiProps(goodbye_message=goodbye_message)

        jsii.create(HelloJsii, self, [props])

    @jsii.member(jsii_name="sayGoodbye")
    def say_goodbye(self, times: typing.Optional[jsii.Number]=None) -> str:
        """Says goodbye, but not farewell.

        :param times: Number of times to say goodbye.
        """
        return jsii.invoke(self, "sayGoodbye", [times])

    @jsii.member(jsii_name="sayHello")
    def say_hello(self, name: str) -> str:
        """Say hello to someone.

        :param name: That special someone.
        """
        return jsii.invoke(self, "sayHello", [name])


@jsii.data_type(jsii_type="jsii-sample.HelloJsiiProps", jsii_struct_bases=[], name_mapping={'goodbye_message': 'goodbyeMessage'})
class HelloJsiiProps():
    def __init__(self, *, goodbye_message: typing.Optional[str]=None):
        """
        :param goodbye_message: The message to emit when saying goodbye. Default: "Goodbye"
        """
        self._values = {
        }
        if goodbye_message is not None: self._values["goodbye_message"] = goodbye_message

    @property
    def goodbye_message(self) -> typing.Optional[str]:
        """The message to emit when saying goodbye.

        default
        :default: "Goodbye"
        """
        return self._values.get('goodbye_message')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'HelloJsiiProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["HelloJsii", "HelloJsiiProps", "__jsii_assembly__"]

publication.publish()
