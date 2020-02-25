# -*- coding: utf-8 -*-
"""
Defines a helper function to get the outputs of a process.
"""

from fsc.export import export
from aiida.common.links import LinkType


@export
def get_outputs_dict(process):
    """
    Helper function to get the RETURN and CREATE outputs of a process as a dict.
    """
    return {
        link_triplet.link_label: link_triplet.node
        for link_triplet in process.get_outgoing(link_type=(LinkType.RETURN,
                                                            LinkType.CREATE))
    }
