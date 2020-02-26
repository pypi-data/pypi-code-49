import os, sys
import argparse
import json
import re
from datetime import datetime
import logging

from neurohive.integration.bitbucket import BitBucket
from neurohive.integration.unitycloud import UnityCloud


def get_jira_name_from_branch(branch_name):
    regexp = '(feature|bugfix)?(?P<name>\w+-\d+)'
    match = re.search(regexp, branch_name)
    if match:
        return match.groupdict()['name']


def create_uc_builds_from_branches(uc_client, branches, src_build_target):
    now = datetime.now().strftime('%Y-%m-%d-%H%M')
    to_build = []
    for branch in branches:
        jira_name = get_jira_name_from_branch(branch)
        name = f'AutoPR-{now}--{branch}'
        if jira_name:
            name = f'AutoPR-{now}--{jira_name}'
        to_build.append({
            "branch": branch,
            "target_name": name
        })
    targets_data = []
    for build in to_build:
        logging.info(f'Create build: {build}')
        targets_data.append(uc_client.clone_build_target(src_build_target, build['target_name'], build['branch']))
    return targets_data


def create_and_build_from_prs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--git-project", type=str, required=True)
    parser.add_argument("--unity-project", type=str, required=True)
    parser.add_argument("--src-build-target-name", type=str, required=True)
    args = parser.parse_args()

    bb = BitBucket(os.getenv('BB_CLIENT'), os.getenv('BB_TOKEN'), 'neurohive')
    uc = UnityCloud(os.getenv('UNITY_ORG_ID', 'unity_oekd8fheerjomw'), project_name=args.unity_project)

    # # удаляю прошлые сборки )
    logging.basicConfig(level=logging.INFO)
    uc.remove_target_with_prefix('AutoPR')
    #получаю список веток с открытими prs
    opened_prs = bb._get_opened_pr(args.git_project)
    branches = [branch['source']['branch']['name'] for branch in opened_prs]
    build_targets = create_uc_builds_from_branches(uc, branches, args.src_build_target_name)
    # запускаю
    for build_target in build_targets:
        uc._create_build(build_target['buildtargetid'])
