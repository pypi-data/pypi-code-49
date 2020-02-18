#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""Commands the database can respond to.
"""
import pkg_resources

from bob.db.base.driver import Interface as BaseInterface


class Interface(BaseInterface):
    def name(self):
        return 'stare'

    def version(self):
        return pkg_resources.require('bob.db.%s' % self.name())[0].version

    def files(self):
        """
        List of meta-data files for the package to be downloaded/uploaded
        
        This function should normally return an empty list, except in case the
        database being implemented requires download/upload of metadata files that
        are **not** kept in its (git) repository.
        """
        return []

    def type(self):
        return 'text'

    def add_commands(self, parser):
        from . import __doc__ as docs
        subparsers = self.setup_parser(parser,"STARE database", docs)

        # checkfiles command
        from .checkfiles import add_command as checkfiles_command
        checkfiles_command(subparsers)
        
        # create command
        from .create import add_command as create_command
        create_command(subparsers)
        