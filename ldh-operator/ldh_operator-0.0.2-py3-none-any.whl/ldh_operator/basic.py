#!/usr/bin/env python3
# Copyright 2017-2020 Purism SPC
# SPDX-License-Identifier: AGPL-3.0-or-later

# These default strings appear in user-facing prompts.
# The user can enter any address/host they want.

import ldh_operator


def debug():

    import pkg_resources
    import sys
    import platform
    import distro
    import os

    default_data = "Defaults " + ldh_operator.DEFAULT.as_yaml().replace("\n", " ").replace("  ", " ")
    package_version = pkg_resources.require("ldh_operator")[0]
    python_version = "Python " + sys.version.replace("\n", " ").replace("  ", " ")
    platform_version = "Platform " + platform.platform()
    distro_version = "Distribution " + distro.name(pretty=True)
    path = "$PATH " + os.environ["PATH"].replace(os.environ["HOME"], "~")

    print(default_data)
    print(package_version)
    print(python_version)
    print(platform_version)
    print(distro_version)
    print(path)


def naive_ping(fqdn):
    """Use system ping on server."""

    import sh
    try:
        result = "👍"
        sh.ping("-c 4 -w 4", fqdn)
    except:
        result = "❌"
    finally:
        print(fqdn, "PING", result)


def ping():
    """Ping all known servers."""

    for service_name in ldh_operator.DECKPLAN.data:
        print(service_name)
        domain_list = ldh_operator.DECKPLAN.data[service_name]
        for domain in domain_list:
            fqdn = domain.replace("*", str(ldh_operator.DEFAULT["HOST_DOMAIN"]))
            test_list = domain_list[domain]
            for test in test_list:

                if test == "ping":
                    naive_ping(fqdn)
                else:
                    pass  # silently skip unknown tests
