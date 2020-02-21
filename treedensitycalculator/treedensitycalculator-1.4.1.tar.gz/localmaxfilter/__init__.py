# -*- coding: utf-8 -*-
"""
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):
    """ Load LocalMaxFilterPlugin class.
    :param QgsInterface iface: A QGIS interface instance.
    """

    from localmaxfilter.localmaxfilter_plugin import LocalMaxFilterPlugin
    return LocalMaxFilterPlugin(iface)
