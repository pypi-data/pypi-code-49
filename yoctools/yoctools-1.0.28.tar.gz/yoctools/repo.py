#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function
import github
import gitlab


class RepoGithub:
    def __init__(self, token=None):
        self.gl = github.Github(token, timeout=30)
        self.organization = self.gl.get_organization('yoc-components')

    def projects(self):
        for repo in self.organization.get_repos():
            print(repo.name, repo)
        projects = self.gl.projects.list(owned=True, all=True, namespace_id='6883967')
        return projects

    def create_project(self, name, path, version):
        try:
            project = self.organization.create_repo(name)
            return project.ssh_url
        except github.GithubException as e:
            return 'git@github.com:yoc-components/' + name + '.git'
            print(e)

    def branch_to_tag(self, name, branch, tag_name):
        project = self.organization.get_repo(name)
        print(project)

        for tag in project.get_tags():
            if tag.name == tag_name:
                return

        for br in project.get_branches():
            if br.name == branch:
                print(br)
                tag = project.create_git_tag(
                    tag_name, 'Created from tag %s' % br.name, br.commit.sha, 'commit')
                if tag:
                    project.create_git_ref('refs/tags/%s' % tag_name, tag.sha)
                break


class RepoGitlab:
    def __init__(self):
        url = 'https://gitlab.com'
        token = 'KaPY7CR2Fsu4dm_71Zro'

        self.gl = gitlab.Gitlab(url, token)

    def projects(self):
        repo = git.Repo('.')

        projects = self.gl.projects.list(
            owned=True, all=True, namespace_id='6883967')
        for p in projects:
            print(p.name, p.ssh_url_to_repo)

    def projects_xxx(self):
        repo = git.Repo('.')

        projects = self.gl.projects.list(owned=True, namespace_id='6883967')
        for p in projects:
            if p.name not in ['yoc', ]:
                repo.git.submodule(
                    'add', '--force', p.ssh_url_to_repo, 'components/' + p.name)
            print(p.name, p.ssh_url_to_repo)


    def create_project(self, name, path, version):
        try:
            project = self.gl.projects.create(
                {'name': name, 'namespace_id': '6883967'})

            return project.ssh_url_to_repo

        except gitlab.GitlabCreateError as e:
            print(e.error_message)
            project = self.gl.projects.get('occ-thead/' + name)
            return project.ssh_url_to_repo
