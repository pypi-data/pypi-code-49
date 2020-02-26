# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


import os
import sys
import shutil
import git

from .log import *


class simpleProgressBar(git.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        # text = "%3d%% (%d/%d)" % (cur_count/(max_count or 100.0), cur_count, max_count)
        sys.stdout.write(self._cur_line)
        sys.stdout.flush()
        if op_code & self.END:
            sys.stdout.write('\n')
        else:
            sys.stdout.write('\r')


class pullProgressBar(git.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        sys.stdout.write(self._cur_line)
        sys.stdout.flush()
        if op_code & self.END:
            sys.stdout.write('\n')
        else:
            sys.stdout.write('\r')


class GitRepo:
    def __init__(self, path, repo_url):
        self.repo_url = repo_url
        self.path = path
        git_path = os.path.join(path, '.git')

        if not os.path.exists(git_path):  # 如果未下载，则 git clone 下来
            self.repo = git.Repo.init(path)
        else:
            self.repo = git.Repo(path)

    def pull(self, version, progress=pullProgressBar()):
        origin = None
        for remote in self.repo.remotes:
            if remote.url == self.repo_url:
                origin = remote
        if not origin:
            origin = self.repo.create_remote(name='origin', url=self.repo_url)

        if version not in self.repo.heads:
            if version not in origin.refs:
                origin.fetch(progress=progress)
            if version in origin.refs:
                branch = self.repo.create_head(
                    version, origin.refs[version])
                branch.checkout()
            elif version in self.repo.tags:
                branch = self.repo.create_head(
                    version, self.repo.tags[version])
                branch.checkout()

    def fetch(self, remote="origin"):
        try:
            remote = self.repo.remote(remote)
        except ValueError:
            msg = "Remote {remote} does not exist on repo {repo}".format(
                remote=remote,
                repo=self.repo.repo.working_dir
            )
            logger.error(msg)
        try:
            remote.fetch(progress=pullProgressBar())
        except git.GitCommandError as ex:
            msg = (
                "Could not fetch remote {remote} ({url}). "
                "Error: {error}".format(remote=remote.name,
                                        url=remote.url,
                                        error=ex)
            )
            logger.error(msg)

    def import_path(self, path, version):
        files = os.listdir(self.repo.working_dir)
        for f in files:
            if f != '.git':
                fn = os.path.join(self.repo.working_dir, f)
                if os.path.isdir(fn):
                    shutil.rmtree(fn)
                else:
                    os.remove(fn)

        for dirpath, _, filenames in os.walk(path):
            if dirpath.find(os.path.join(path, '.git')) < 0:
                for f in filenames:
                    p1 = os.path.join(dirpath, f)
                    p2 = os.path.relpath(p1, path)
                    p2 = os.path.join(self.repo.working_dir, p2)
                    try:
                        p = os.path.dirname(p2)
                        os.makedirs(p)
                    except:
                        pass

                    shutil.copy2(p1, p2)

        if self.repo.is_dirty(untracked_files=True):
            self.repo.git.add(self.repo.untracked_files)
            self.repo.git.commit('-m', 'init version', '-a')

            branch = self.repo.create_head(version)
            branch.checkout()

            self.repo.git.push(
                "--set-upstream", self.repo.remotes.origin, self.repo.head.ref)

    def GetBranches(self):
        return self.repo.branches

    def GetRemoteBranches(self):
        try:
            return self.repo.remote().refs
        except:
            return []

    def CheckoutBranch(self, version):
        self.pull(version)
