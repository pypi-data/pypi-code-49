#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Copyright (C) 2019 Christoph Fink, University of Helsinki
#
#   This program is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation; either version 3
#   of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, see <http://www.gnu.org/licenses/>.

""" Reminds me if it rains """

import geocoder

from .lib import (
    config,
    EMailSender,
    PrecipitationChecker
)


__all__ = [
    "remind_me_if_it_rains"
]


def remind_me_if_it_rains():
    """ Remind me if rain is forecast """
    lat, lon = geocoder.osm(config["place"]).latlng
    precipitation_rate = \
        PrecipitationChecker(lat, lon).average_precipitation_per_hour
    if precipitation_rate > 0.1:
        EMailSender(
            config["email"]["from"],
            config["email"]["to"],
            config["email"]["subject"],
            config["email"]["message"].format(p=precipitation_rate),
            config["smtp"]["host"],
            config["smtp"]["user"],
            config["smtp"]["password"]
        ).send_message()
