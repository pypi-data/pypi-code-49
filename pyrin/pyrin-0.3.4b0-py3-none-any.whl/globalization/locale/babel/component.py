# -*- coding: utf-8 -*-
"""
locale babel component module.
"""

from pyrin.application.decorators import component
from pyrin.application.context import Component
from pyrin.globalization.locale.babel import LocaleBabelPackage
from pyrin.globalization.locale.babel.manager import LocaleBabelManager


@component(LocaleBabelPackage.COMPONENT_NAME)
class LocaleBabelComponent(Component, LocaleBabelManager):
    """
    locale babel component class.
    """
    pass
