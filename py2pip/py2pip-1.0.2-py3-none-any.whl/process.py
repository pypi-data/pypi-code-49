#!/usr/bin/env python3
"""
Find supported python2 package version... Supply the package it will check and return the correct package name
"""
import aiohttp
import asyncio
import subprocess
import sys
import time

from py2pip import config
from py2pip.parser import ParseHistoryHTML, ParsePackageVersionHTML
from py2pip.simulator import Logger


class Py2PIPManager(object):

    def __init__(self, project_name, support_py_version, install=False, log=Logger(), **kwargs):
        """
        Find the python supported package version.
        :param project_name: Python Package Name, 3rd party registered to pip
        :param support_py_version: Python version like 2.7
        :param install: Install the supported Python version package locally #ToDO
        :param log: Default to the simulator log. Ignore for pip install.

        Example:
            project_name:  Django
            support_py_version: 2.7
        Result:
            Success:
                Support Py2.7 Django is: Django==1.11.28
            Failure:
                None
        """
        self.package_history_url = config.PIPServer.HOST + config.PIPServer.PATH.format(project=project_name)
        self.log = log
        self.running = True

        self.package = project_name
        self.install = install
        self.support_py_version = support_py_version
        self.enable_event_debug = kwargs.get('enable_debug', False)
        self.show_progress = kwargs.get('show_progress', False)  # Show the progress status on Terminal

        self.history_page_parser = ParseHistoryHTML(self.log)
        self.history_versions_page_parser = ParsePackageVersionHTML(self.log)

    async def show_progress_msg(self):
        while True:
            if not self.running:
                return
            print('Running', end="\r")
            for i in range(4):
                await asyncio.sleep(.3)
                print(f"Running{'.'*i}", end="\r")

            await asyncio.sleep(.5)

    def start(self):
        self.log.info(f'Commence io loop...')
        self.loop = asyncio.get_event_loop()
        self.loop.set_debug(enabled=self.enable_event_debug)
        self.loop.run_until_complete(self.process_package_history_page())  # close will have no effect if called with run_until_complete

    def get_support_pkg_version(self):
        if not self.history_versions_page_parser.found():
            return
        return f'{self.package}=={self.history_versions_page_parser.pkg_version}'

    def run(self):
        self.log.info(f"Commence the process to find Python{self.support_py_version} supported package '{self.package}'")
        self.start()

        # Return value upon completion
        self.running = False
        return self.get_support_pkg_version()

    async def process_versions_page(self, session):
        version_list = self.history_page_parser.get_versions()
        if not version_list:
            self.log.error(f'No version list found of the package {self.package}')
            return

        self.log.info(f"Iterate versions of lib {self.package}\n\t{', '.join(version_list.keys())}")

        for pkg_version, pkg_data in version_list.items():
            url = pkg_data['url']
            await self.read_version_page(session, url, pkg_version)
        else:
            self.running = False

    async def read_version_page(self, session, url, package_version):
        """
        Ensure consistency to share the package version as well
        """
        self.log.debug(f'Read PyPI package history version page {url}')
        if self.history_versions_page_parser.found():
            return

        async with session.get(url) as response:
            if response.status == 200:
                content = await response.text()
                await self.history_versions_page_parser.process(content, self.support_py_version, package_version)
            else:
                self.log.error(f'{response.status}: PyPi {url} is {response.reason}')

    async def process_history_page(self, session):
        self.log.info('Read package history page')
        async with session.get(self.package_history_url) as response:
            if response.status == 200:
                content = await response.text()
                await self.history_page_parser.process(content)
            else:
                self.log.error(f'{response.status}: PyPi Package {self.package_history_url} is {response.reason}')

    async def process_package_history_page(self):
        self.log.info('Create client session and read page')

        if self.show_progress:
            task = self.loop.create_task(self.show_progress_msg())

        async with aiohttp.ClientSession() as session:
            await self.process_history_page(session)
            if not self.history_page_parser.get_versions():
                self.running = False
                return

            await self.process_versions_page(session)

        if self.show_progress:
            await task
