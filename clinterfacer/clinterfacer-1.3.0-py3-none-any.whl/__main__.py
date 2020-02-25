#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the main script of the clinterfacer package."""

# standard library(ies)
import sys

# local source(s)
import clinterfacer


def main() -> int:
    """
    This function is called by the `clinterfacer` entry point, 
    which was install with the `clinterfacer_tools` package. It uses the 
    `clinterfacer <https://pypi.org/project/clinterfacer/>`_
    framework to manage the command-line interface.
    
    :return: The execution status: (0) OK and (1) NOK.
    :rtype: int
    """
    return clinterfacer.main()


if __name__ == '__main__':
    sys.exit(main())
