#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from ..lib.handler.captainhook_handler import CaptainHook
from ..lib.logger import Logger
import sys
import webbrowser
from ..lib.handler import git_handler as git
from ..lib.handler.github_handler import GithubHandler

github = GithubHandler()
logger = Logger()

def entrypoint(args):
    if(args.action in ['pr']):
        branch_name = git.current_branch_name()
        pulls = github.get_pr_from_branch(args.project, branch_name)
        if pulls.totalCount and branch_name != 'master':
            pr = pulls[0]
            print(pr)
            webbrowser.open('https://github.com/primait/{}/pull/{}'.format(args.project, pr.number), new=2)
        else:
            logger.warning('Impossibile trovare il branch remoto.')
    elif(args.action in ['drone']):
        webbrowser.open('https://drone-1.prima.it/primait/{}'.format(args.project), new=2)
    else:
        logger.warning('Non ho capito che cosa devo fare')
        sys.exit(-1)
