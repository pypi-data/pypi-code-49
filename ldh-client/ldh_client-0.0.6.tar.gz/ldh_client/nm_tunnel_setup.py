#!/usr/bin/env python3
# Copyright 2017-2020 Purism SPC
# SPDX-License-Identifier: AGPL-3.0-or-later

# Original file from Network-Manager Python examples
# Copyright 2014 Red Hat, Inc.
# https://gitlab.freedesktop.org/NetworkManager/NetworkManager/blob/master/examples/python/gi/vpn-import.py
# SPDX-License-Identifier: GPL-2.0-or-later

import sys
import os
import requests
import gi
from ldh_client import common
from tempfile import mkstemp
from json.decoder import JSONDecodeError

gi.require_version("NM", "1.0")
from gi.repository import NM, GLib

PROTO = "https://"
PATH = "/api/v1/user/tunnel_account"
CERT_PATH = "/public/certificate.ovpn"
QQN = "US1"


def find_openvpn_path():
    """Perform a naive search of known paths for the OpenVPN plugin."""

    path_list = [
        "/usr/lib/x86_64-linux-gnu/NetworkManager/libnm-vpn-plugin-openvpn.so",
        "/usr/lib/NetworkManager/libnm-vpn-plugin-openvpn.so",
    ]

    for value in path_list:
        if os.path.isfile(value):
            return value

    raise FileNotFoundError("Cannot locate libnm-vpn-plugin-openvpn.so")


def nm_tunnel_setup():
    """This script will:
    1. Prompt for LDH credentials.
    2. Retrieve tunnel credentials from host.
    3. Download .ovpn config file from host.
    4. Setup new VPN connection in your NetworkManager.
    """

    # Get tunnel credentials
    credentials = common.prompt_for_credentials()

    url = PROTO + credentials.host + PATH
    try:
        r = requests.get(url, auth=(credentials.user, credentials.passphrase))
    except requests.exceptions.ConnectionError as e:
        print(repr(e))
        sys.exit(1)
    if r.status_code == 200:
        tunnel_user = r.json().get("tunnel_user")
        tunnel_password = r.json().get("tunnel_password")
        if tunnel_user is None or tunnel_password is None:
            print("Your tunnel service is not active.")
            sys.exit(1)
    else:
        print("\nSomething went wrong when connecting to", url)
        try:
            detail = r.json().get("detail", "No detail available.")
        except JSONDecodeError as e:
            detail = r.reason
        print("Problem details:", detail)
        sys.exit(1)

    # Download certificate
    cert_url = PROTO + credentials.host + CERT_PATH
    (fd, fname) = mkstemp(suffix=".ovpn")
    try:
        with requests.get(cert_url, stream=True) as r:
            with open(fd, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
    except requests.exceptions.ConnectionError as e:
        print(repr(e))
        os.remove(fname)
        sys.exit(1)

    # Configure NetworkManager
    client = NM.Client.new(None)
    plugin_path = find_openvpn_path()
    plugin = NM.VpnEditorPlugin.load(
        plugin_path, "org.freedesktop.NetworkManager.openvpn"
    )
    try:
        new_con = plugin.import_(fname)
    except Exception as e:
        print(e)
        sys.exit(1)
    os.remove(fname)
    new_con.normalize()

    # Create the new secret
    new_secrets = GLib.Variant(
        "a{sa{sv}}",
        {
            "vpn": {"secrets": GLib.Variant("a{ss}", {"password": tunnel_password})},
            "ipv6": {},
        },
    )

    # Update the connection with the secret
    new_con.update_secrets(NM.SETTING_VPN_SETTING_NAME, new_secrets)

    # Add the username to the VPN settings
    vpn_settings = new_con.get_setting_vpn()
    vpn_settings.add_data_item("username", tunnel_user)

    # Set Connection Name
    con_name = "{address} {country_code}".format(
        address=credentials.address, country_code=QQN
    )
    new_con_settings = new_con.get_setting_connection()
    new_con_settings.set_property(NM.SETTING_CONNECTION_ID, con_name)

    # See what we have
    # new_con.dump()

    # Store the connection in NetworkManager

    main_loop = GLib.MainLoop()

    def added_cb(glib_client, result, data):
        try:
            glib_client.add_connection_finish(result)
            print("Tunnel successfully added to NetworkManager.")
        except Exception as cb_e:
            print("ERROR: failed to add connection: %s\n" % cb_e)
        main_loop.quit()

    client.add_connection_async(new_con, True, None, added_cb, None)

    main_loop.run()
