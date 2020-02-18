import asyncio
import os
import re
import subprocess
import sys
from typing import NamedTuple, Optional, Set, Tuple

from . import config
from .vcs_adapters import ADAPTERS


class GitInfo(NamedTuple):
    revision: str
    meta: str
    code_line: str
    commit_message: str
    clone_url: str
    project_url: str
    domain: str  # e.g. gitlab.company.name.com
    group: str  # or user
    project: str


class FoundIssues(NamedTuple):
    jira: 'Set[str]'
    vcs: 'Set[str]'


def run_command(*cmd) -> str:
    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return result.stdout.decode()


def get_git_info(file, line) -> 'Optional[GitInfo]':
    os.chdir(os.path.abspath(os.path.dirname(file)))
    try:
        # open here, fetch result after al other commands executed
        origin_cli = subprocess.Popen(
            ['git', 'config', '--get', 'remote.origin.url'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        upstream_cli = subprocess.Popen(
            ['git', 'config', '--get', 'remote.upstream.url'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout = run_command('git', 'blame', '-L', f'{line},+1', file)
        revision, info = stdout.split(maxsplit=1)
        info, code_line = info.split(') ', maxsplit=1)
        info = info[1:]
        commit_message = run_command(
            'git', 'show', '-s', '--format=%B', revision
        )

        origin_url, stderr_1 = origin_cli.communicate()
        upstream_url, stderr_2 = upstream_cli.communicate()
        if stderr_1 or stderr_2:
            print(stderr_1.decode(), stderr_2.decode(), file=sys.stderr)

        clone_url = (upstream_url or origin_url).strip().decode()
        project_url = get_project_url(clone_url)
        domain, group, project = project_url.rsplit('/', maxsplit=2)

        return GitInfo(
            revision=revision,
            meta=info,
            code_line=code_line,
            commit_message=commit_message.strip(),
            clone_url=clone_url,
            project_url=project_url,
            domain=domain,
            group=group,
            project=project,
        )
    except subprocess.CalledProcessError as e:
        print(
            f'Unable to retrieve commit message: '
            f'"{e.stderr.decode().strip()}"',
            file=sys.stderr
        )


def find_issues(text):
    return FoundIssues(
        jira=set(re.findall(config.JIRA_ISSUE_REGEX, text)),
        vcs=set(re.findall(config.VCS_ISSUE_REGEX, text)),
    )


def get_project_url(clone_url) -> str:
    if '@' in clone_url:  # ssh
        project_url = 'https://' + clone_url[4:-4].replace(':', '/')
    else:  # http
        project_url = clone_url[:-4]
    return project_url


def get_jira_issue_url(issue_number: str) -> str:
    return f'https://{config.JIRA_DOMAIN}/browse/{issue_number}/'


def get_vcs_issue_url(issue_number: str, project_url: str) -> str:
    return f'{project_url}/issues/{issue_number[1:]}/'


def parse_url(url: str) -> 'Tuple[str, str, str]':
    protocol_sub_and_second, top_and_the_rest = url.rsplit('.', 1)
    top = top_and_the_rest.split("/")[0]
    sub_and_second = protocol_sub_and_second.split('://', 1)[1]
    *sub, second = sub_and_second.split('.', 1)
    return sub[0] if sub else None, second, top


def format_git_info(git_info):
    commit_message = f'Commit message: {git_info.commit_message}\n'
    code_line = f'Code line: {git_info.code_line}'
    for_user = (
            f'Commit info: {git_info.revision}, {git_info.meta}:\n'
            + commit_message
            + code_line
            + f'GitLab URL: {git_info.project_url}/commit/{git_info.revision}\n'
    )
    for_search = commit_message + code_line
    return for_search, for_user


def format_result(issue_numbers, source, ):
    if len(issue_numbers) == 1:
        return f'Found 1 {source} issue: {tuple(issue_numbers)[0]}'
    elif issue_numbers:
        return f'Found {len(issue_numbers)} {source} issues: {issue_numbers}'


def get_line_info(file, line, selection=''):
    git_info = get_git_info(file, line)

    if git_info:
        for_search, git_info_message = format_git_info(git_info)
        if selection in for_search:
            print(git_info_message)
        else:
            for_search = selection
    else:
        for_search = selection

    jira_issues, vcs_issues = find_issues(for_search)

    jira_issues_message = format_result(jira_issues, 'JIRA')
    vcs_issues_message = format_result(vcs_issues, 'VCS')

    if jira_issues_message and config.JIRA_DOMAIN:
        print(
            jira_issues_message,
            *(get_jira_issue_url(issue_number) for issue_number in jira_issues),
            sep='\n',
            end='\n\n'
        )
    elif jira_issues_message:
        print(
            jira_issues_message,
            ', however JIRA_DOMAIN was not configured, so urls will not be generated',
            file=sys.stderr
        )

    if vcs_issues_message:
        print(
            vcs_issues_message,
            *(
                get_vcs_issue_url(issue_number, git_info.project_url)
                for issue_number in vcs_issues
            ),
            sep='\n'
        )
    elif not jira_issues_message:
        print(f'No issues found in {for_search!r}', file=sys.stderr)
        return

    if not git_info:
        return

    domains = parse_url(git_info.domain)
    for vcs_domain in domains:
        git_adapter = ADAPTERS.get(vcs_domain, None)
        if git_adapter is not None:
            break
    else:
        print(f'No adapter found for {domains}', file=sys.stderr)
        return

    async def fetch_results():
        git = git_adapter(
            git_info.domain, git_info.group, git_info.project
        )
        r = await asyncio.gather(
            *(
                git.get_info(issue_number)
                for issue_number in (*jira_issues, *vcs_issues)
            ),
            return_exceptions=True
        )
        await git.close()
        return r

    results = asyncio.get_event_loop().run_until_complete(fetch_results())
    print(*results, sep='\n')
