#  BSD 3-Clause License
#
#  Copyright (c) 2019, Elasticsearch BV
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
#  * Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from __future__ import absolute_import

import sys

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management.color import color_style
from django.utils import termcolors

from atatus.contrib.django.client import DjangoClient
from atatus.utils.compat import urlparse

try:
    from django.core.management.base import OutputWrapper
except ImportError:
    OutputWrapper = None


blue = termcolors.make_style(opts=("bold",), fg="blue")
cyan = termcolors.make_style(opts=("bold",), fg="cyan")
green = termcolors.make_style(fg="green")
magenta = termcolors.make_style(opts=("bold",), fg="magenta")
red = termcolors.make_style(opts=("bold",), fg="red")
white = termcolors.make_style(opts=("bold",), fg="white")
yellow = termcolors.make_style(opts=("bold",), fg="yellow")


class TestException(Exception):
    pass


class ColoredLogger(object):
    def __init__(self, stream):
        self.stream = stream
        self.errors = []
        self.color = color_style()

    def log(self, level, *args, **kwargs):
        style = kwargs.pop("style", self.color.NOTICE)
        msg = " ".join((level.upper(), args[0] % args[1:], "\n"))
        if OutputWrapper is None:
            self.stream.write(msg)
        else:
            self.stream.write(msg, style_func=style)

    def error(self, *args, **kwargs):
        kwargs["style"] = red
        self.log("error", *args, **kwargs)
        self.errors.append((args,))

    def warning(self, *args, **kwargs):
        kwargs["style"] = yellow
        self.log("warning", *args, **kwargs)

    def info(self, *args, **kwargs):
        kwargs["style"] = green
        self.log("info", *args, **kwargs)


CONFIG_EXAMPLE = """

You can set it in your settings file:

    ATATUS = {
        'APP_NAME': '<YOUR-APP-NAME>',
        'LICENSE_KEY': '<YOUR-APM-LICENSE-KEY>',
    }

or with environment variables:

    $ export ATATUS_APP_NAME="<YOUR-APP-NAME>"
    $ export ATATUS_LICENSE_KEY="<YOUR-APM-LICENSE-KEY>"
    $ python manage.py atatus check

"""


class Command(BaseCommand):
    arguments = (
        (("-a", "--app-name"), {"default": None, "dest": "app_name", "help": "Specifies the app name."}),
        (("-l", "--license-key"), {"default": None, "dest": "license_key", "help": "Specifies the license key."}),
    )

    args = "test check"

    def add_arguments(self, parser):
        parser.add_argument("subcommand")
        for args, kwargs in self.arguments:
            parser.add_argument(*args, **kwargs)

    def handle(self, *args, **options):
        if "subcommand" in options:
            subcommand = options["subcommand"]
        else:
            return self.handle_command_not_found("No command specified.")
        if subcommand not in self.dispatch:
            self.handle_command_not_found('No such command "%s".' % subcommand)
        else:
            self.dispatch.get(subcommand, self.handle_command_not_found)(self, subcommand, **options)

    def handle_test(self, command, **options):
        """Send a test error to APM Server"""
        # can't be async for testing
        config = {"async_mode": False}
        for key in ("app_name", "license_key"):
            if options.get(key):
                config[key] = options[key]
        client = DjangoClient(**config)
        client.error_logger = ColoredLogger(self.stderr)
        client.logger = ColoredLogger(self.stderr)
        self.write(
            "Trying to send a test error to APM Server using these settings:\n\n"
            "APP_NAME:\t%s\n"
            "LICENSE_KEY:\t%s\n\n" % (client.config.app_name, client.config.license_key)
        )

        try:
            raise TestException("Test error!")
        except TestException:
            client.capture_exception()
            if not client.error_logger.errors:
                self.write(
                    "Success! We tracked the error successfully! You should be"
                    " able to see it in a few seconds at the above URL"
                )
        finally:
            client.close()

    def handle_check(self, command, **options):
        """Check your settings for common misconfigurations"""
        passed = True
        client = DjangoClient(metrics_interval="0ms")

        def is_set(x):
            return x and x != "None"

        # check if org/app is set:
        if not is_set(client.config.license_key) and not is_set(client.config.app_name):
            passed = False
            self.write("Configuration errors detected!", red, ending="\n\n")
            self.write("  * APP_NAME and LICENSE_KEY not set! ", red, ending="\n")
            self.write(CONFIG_EXAMPLE)

        elif not is_set(client.config.license_key):
            passed = False
            self.write("Configuration errors detected!", red, ending="\n\n")
            self.write("  * LICENSE_KEY not set! ", red, ending="\n")
            self.write(CONFIG_EXAMPLE)

        elif not is_set(client.config.app_name):
            passed = False
            self.write("Configuration errors detected!", red, ending="\n\n")
            self.write("  * APP_NAME not set! ", red, ending="\n")
            self.write(CONFIG_EXAMPLE)
        else:
            self.write("License key and App name are set, good job!", green)


        notify_host = client.config.notify_host
        if notify_host:
            parsed_url = urlparse.urlparse(notify_host)
            if parsed_url.scheme.lower() in ("http", "https"):
                # parse netloc, making sure people did not supply basic auth
                if "@" in parsed_url.netloc:
                    credentials, _, path = parsed_url.netloc.rpartition("@")
                    passed = False
                    self.write("Configuration errors detected!", red, ending="\n\n")
                    if ":" in credentials:
                        self.write("  * NOTIFY_HOST cannot contain authentication " "credentials", red, ending="\n")
                    else:
                        self.write(
                            "  * NOTIFY_HOST contains an unexpected at-sign!"
                            " This is usually used for basic authentication, "
                            "but the colon is left out",
                            red,
                            ending="\n",
                        )
                else:
                    pass
                    # self.write("NOTIFY_HOST {0} looks fine".format(notify_host), green)
                # secret token in the clear not recommended
                if is_set(client.config.license_key) and parsed_url.scheme.lower() == "http":
                    self.write("  * Notify host not using https", yellow, ending="\n")
            else:
                self.write(
                    "  * NOTIFY_HOST has scheme {0} and we require " "http or https!".format(parsed_url.scheme),
                    red,
                    ending="\n",
                )
                passed = False
        else:
            self.write("Configuration errors detected!", red, ending="\n\n")
            self.write("  * NOTIFY_HOST appears to be empty", red, ending="\n")
            passed = False
        self.write("")

        # check if we're disabled due to DEBUG:
        if settings.DEBUG:
            if getattr(settings, "ATATUS", {}).get("DEBUG"):
                self.write(
                    "Note: even though you are running in DEBUG mode, we will "
                    'send data to the APM Server, because you set ATATUS["DEBUG"] to '
                    "True. You can disable Atatus while in DEBUG mode like this"
                    "\n\n",
                    yellow,
                )
                self.write(
                    "   ATATUS = {\n"
                    '       "DEBUG": False,\n'
                    "       # your other ATATUS settings\n"
                    "   }"
                )
            else:
                self.write(
                    "Looks like you're running in DEBUG mode. Atatus will NOT "
                    "gather any data while DEBUG is set to True.\n\n",
                    red,
                )
                self.write(
                    "If you want to test Atatus while DEBUG is set to True, you"
                    " can force Atatus to gather data by setting"
                    ' ATATUS["DEBUG"] to True, like this\n\n'
                    "   ATATUS = {\n"
                    '       "DEBUG": True,\n'
                    "       # your other ATATUS settings\n"
                    "   }"
                )
                passed = False
        else:
            self.write("DEBUG mode is disabled! Looking good!", green)
        self.write("")

        # check if middleware is set, and if it is at the first position
        middleware_attr = "MIDDLEWARE" if getattr(settings, "MIDDLEWARE", None) is not None else "MIDDLEWARE_CLASSES"
        middleware = list(getattr(settings, middleware_attr))
        try:
            pos = middleware.index("atatus.contrib.django.middleware.TracingMiddleware")
            if pos == 0:
                self.write("Tracing middleware is configured! Awesome!", green)
            else:
                self.write("Tracing middleware is configured, but not at the first position\n", yellow)
                self.write("Atatus works best if you add it at the top of your %s setting" % middleware_attr)
        except ValueError:
            self.write("Tracing middleware not configured!", red)
            self.write(
                "\n"
                "Add it to your %(name)s setting like this:\n\n"
                "    %(name)s = (\n"
                '        "atatus.contrib.django.middleware.TracingMiddleware",\n'
                "        # your other middleware classes\n"
                "    )\n" % {"name": middleware_attr}
            )
        self.write("")
        if passed:
            self.write("Looks like everything should be ready!", green)
        else:
            self.write("Please fix the above errors.", red)
        self.write("")
        client.close()
        return passed

    def handle_command_not_found(self, message):
        self.write(message, red, ending="")
        self.write(" Please use one of the following commands:\n\n", red)
        self.write("".join(" * %s\t%s\n" % (k.ljust(8), v.__doc__) for k, v in self.dispatch.items()))
        self.write("\n")
        argv = self._get_argv()
        self.write("Usage:\n\t%s atatus <command>" % (" ".join(argv[: argv.index("atatus")])))

    def write(self, msg, style_func=None, ending=None, stream=None):
        """
        wrapper around self.stdout/stderr to ensure Django 1.4 compatibility
        """
        if stream is None:
            stream = self.stdout
        if OutputWrapper is None:
            ending = "\n" if ending is None else ending
            msg += ending
            stream.write(msg)
        else:
            stream.write(msg, style_func=style_func, ending=ending)

    def _get_argv(self):
        """allow cleaner mocking of sys.argv"""
        return sys.argv

    dispatch = {"test": handle_test, "check": handle_check}
