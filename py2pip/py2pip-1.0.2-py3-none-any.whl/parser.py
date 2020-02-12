import asyncio
import re

from bs4 import BeautifulSoup

from py2pip import config


class ParseHTML(object):
    FEATURE = 'html.parser'

    def __init__(self, log):
        self.log = log

    def strip(self, text):
        return text.strip()  # Removes trailing and leading spaces and \n

    async def get_soup(self, content):
        return BeautifulSoup(content, features=self.FEATURE)


class ParseHistoryHTML(ParseHTML):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_pkg_versions = {}  # Should be {'3.2': {'url':, '', 'datetime': ''}}

    def get_versions(self):
        return self.all_pkg_versions

    async def read_versions(self, node):
        version_node = node.find(config.LookupTags.TARGET_VERSION, attrs={'class': config.LookupClass.TARGET_VERSION})

        version = self.strip(version_node.text)

        # Exclude pre-release version
        if re.search('[a-z]+', version):
            return

        url_node = node.find(config.LookupTags.TARGET_URL, attrs={'class': config.LookupClass.TARGET_URL})
        url = config.PIPServer.HOST + url_node.get('href')

        release_date_node = node.find(config.LookupTags.TARGET_TIME)
        datetime_str = release_date_node.get('datetime')

        if version in self.all_pkg_versions:
            self.log.error(f'Error: {version} already exists')
            return

        self.all_pkg_versions[version] = {
            'url': url,
            'datetime': datetime_str
        }

    async def process(self, content):
        tasks = []
        soup = await self.get_soup(content)

        release_node_list = soup.find(config.LookupTags.GRAND_PARENT, attrs={'class': config.LookupClass.GRAND_PARENT}).find_all(
            config.LookupTags.PARENT, attrs={'class': config.LookupClass.PARENT})

        for node in release_node_list:
            task = asyncio.ensure_future(self.read_versions(node))
            tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)


class ParsePackageVersionHTML(ParseHTML):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.head_title = 'Programming Language'
        self.pkg_version = None

    def found(self):
        return self.pkg_version is not None

    async def read(self, li_node, py_version, pkg_version):
        self.log.info(f'Iterate over Support Language list of the html page {pkg_version}')

        for element in li_node.find('ul').find_all('li'):
            version_pack = element.find('a').text.strip()
            matched = re.match('Python\s*::\s*(?P<version>[0-9.]+)\s*(::)?', version_pack)
            if not matched:
                continue

            remote_py_version = matched.group('version')
            if remote_py_version == py_version or py_version.startswith(remote_py_version):
                if self.pkg_version is None:
                    self.log.info(f'Found supporting package version {pkg_version}')
                    self.pkg_version = pkg_version
                    return

    async def process(self, content, py_version, pkg_version):
        self.log.info(f'Parse version html page {pkg_version} to look for {py_version}')
        tasks = []
        soup = await self.get_soup(content)

        version_ul_node = soup.find('div', attrs={'class': 'vertical-tabs__tabs'}).find(
            'ul', attrs={'class': 'sidebar-section__classifiers'})

        if not version_ul_node:
            self.log.debug('No classifiers found. {pkg_version}')
            return

        for li in version_ul_node.children:
            if isinstance(li, str):
                continue
            title = li.find('strong').text.strip()
            if title == self.head_title:
                task = asyncio.ensure_future(self.read(li, py_version, pkg_version))
                tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)
