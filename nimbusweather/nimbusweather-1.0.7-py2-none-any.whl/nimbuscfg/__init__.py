#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your rights.
#
"""Utilities used by the setup and configure programs"""

import os
import configobj
from pkg_resources import resource_stream

canonical_order = ('',
                   [('Station', [], ['latitude', 'longitude', 'station_type']),
                    ('AWEKAS', [], ['username', 'password']),
                       ('CWOP', [], ['station']),
                       ('PWSweather', [], ['station', 'password']),
                       ('WOW', [], ['station', 'password']),
                       ('Wunderground', [], ['station', 'password'])],
                   ['debug', 'socket_timeout', 'version', 'archive_interval', 'clock_check', 'max_drift'])

_config_dir = "/etc/nimbus"
_config_file = "nimbus.conf"


def read_config():
    """Read the specified configuration file, return an instance of ConfigObj
    with the file contents. If no file is specified, look in the standard
    locations for nimbus.conf. Returns the filename of the actual configuration
    file, as well as the ConfigObj.
    """

    config_path = os.path.join(_config_dir, _config_file)

    if not os.path.isfile(config_path):
        config_path = resource_stream(__name__, 'nimbus.conf')

    config_dict = configobj.ConfigObj(config_path, indent_type='\t', file_error=True)

    return config_dict


def reorder_sections(config_dict, src, dst, after=False):
    """Move the section with key src to just before (after=False) or after
    (after=True) the section with key dst. """
    bump = 1 if after else 0
    # We need both keys to procede:
    if src not in config_dict.sections or dst not in config_dict.sections:
        return
    # If index raises an exception, we want to fail hard.
    # Find the source section (the one we intend to move):
    src_idx = config_dict.sections.index(src)
    # Remove it
    config_dict.sections.pop(src_idx)
    # Find the destination
    dst_idx = config_dict.sections.index(dst)
    # Now reorder the attribute 'sections', putting src just before dst:
    config_dict.sections = config_dict.sections[:dst_idx + bump] + [src] + \
        config_dict.sections[dst_idx + bump:]


def reorder_to_ref(config_dict, section_tuple=canonical_order):
    """Reorder any sections in concordance with a reference ordering.

    See the definition for canonical_ordering for the details of the tuple
    used to describe a section.
    """
    if not len(section_tuple):
        return
    # Get the names of any subsections in the order they should be in:
    subsection_order = [x[0] for x in section_tuple[1]]
    # Reorder the subsections, then the scalars
    config_dict.sections = reorder(config_dict.sections, subsection_order)
    config_dict.scalars = reorder(config_dict.scalars, section_tuple[2])

    # Now recursively go through each of my subsections,
    # allowing them to reorder their contents
    for ss_tuple in section_tuple[1]:
        ss_name = ss_tuple[0]
        if ss_name in config_dict:
            reorder_to_ref(config_dict[ss_name], ss_tuple)


def reorder(name_list, ref_list):
    """Reorder the names in name_list, according to a reference list."""
    result = []
    # Use the ordering in ref_list, to reassemble the name list:
    for name in ref_list:
        if name in name_list:
            result.append(name)
    # For any that were not in the reference list and are left over, tack
    # them on to the end:
    for name in name_list:
        if name not in ref_list:
            result.append(name)
    # Make sure I have the same number I started with
    assert(len(name_list) == len(result))
    return result
