import ssl
import sys

import aiohttp
import certifi

from .. import config
from .base import BaseVCSAdapter


# WARNING FIX HACK
# https://github.com/aio-libs/aiohttp/issues/4282
# https://github.com/aio-libs/aiohttp/pull/4322
class FixedNoop:
    def __await__(self):
        yield


# WARNING FIX HACK
aiohttp.client_reqrep.noop = FixedNoop


def get_gitlab_token():
    if config.GITLAB_TOKEN:
        return config.GITLAB_TOKEN
    print(
        f'Gitlab token was not found, place it in {config.CONFIG_PATH} as "GITLAB_TOKEN"'
        ' or export GITLAB_TOKEN=<token> to get info about related PRs',
        file=sys.stderr
    )


class GitlabAdapter(BaseVCSAdapter):
    ISSUES_SEARCH_URL = '{gitlab_url}/api/v4/search?scope=merge_requests&search={query}'

    def __init__(self, domain, group, project):
        super().__init__(domain, group, project)
        self._access_token = get_gitlab_token()
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        connector = aiohttp.TCPConnector(ssl=ssl_context)
        self.session = aiohttp.ClientSession(connector=connector)

    async def fetch(self, url):
        headers = {'PRIVATE-TOKEN': self._access_token}
        async with self.session.get(url, headers=headers, timeout=1) as response:
            return await response.json()

    async def get_info(self, issue_number):
        if not self._access_token:
            return

        response = await self.fetch(
            self.ISSUES_SEARCH_URL.format(gitlab_url=self.domain,
                                          query=issue_number)
        )
        return self._format_mr(issue_number, response)

    def _format_mr(self, issue_number, mrs: 'List[GitlabMR]'):
        if not mrs:
            return f'No related MRs found for {issue_number}'
        result = f'Found {len(mrs)} related MRs for {issue_number}:\n'
        return result + "\n".join([
            (
                f'{mr["author"]["username"]}: {mr["title"]} ({mr["state"]})\n'
                f'{mr["source_branch"]} -> {mr["target_branch"]}\n'
                f'{mr["created_at"]}: {mr["web_url"]}\n'
            ) for mr in mrs
        ])

    async def close(self):
        await self.session.close()
