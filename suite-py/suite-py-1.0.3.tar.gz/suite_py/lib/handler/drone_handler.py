# -*- encoding: utf-8 -*-
from distutils.version import StrictVersion
import time

from halo import Halo
import requests

from suite_py.lib.tokens import Tokens


tokens = Tokens()
baseurl = "https://drone-1.prima.it"


def get_last_build_url(repo):
    with Halo(text='Contacting drone...', spinner='dots', color='magenta'):
        # necessario per far comparire la build che abbiamo appena pushato
        time.sleep(2)
        try:
            resp = requests.get("{}/api/repos/primait/{}/builds".format(baseurl, repo),
                                headers={'Authorization': 'Bearer {}'.format(tokens.drone)}).json()

            return '{}/primait/{}/{}'.format(baseurl, repo, resp[0]['number'])
        except (Exception) as e:
            return ""


def get_pr_build_url(repo, commit_sha):
    with Halo(text='Contacting drone...', spinner='dots', color='magenta'):
        # necessario per far comparire la build che abbiamo appena pushato
        time.sleep(2)
        try:
            resp = requests.get("{}/api/repos/primait/{}/builds?per_page=100".format(baseurl, repo),
                                headers={'Authorization': 'Bearer {}'.format(tokens.drone)}).json()
            build_number = list(filter(lambda build: build["after"] == commit_sha, resp))[
                0]['number']
            return '{}/primait/{}/{}'.format(baseurl, repo, build_number)
        except (Exception) as e:
            return ""


def get_tag_from_builds(repo):
    tags = []
    builds = requests.get("{}/api/repos/primait/{}/builds?per_page=100".format(baseurl, repo),
                          headers={'Authorization': 'Bearer {}'.format(tokens.drone)}).json()

    for build in builds:
        if build["event"] == "tag":
            tags.append(build["ref"].replace('refs/tags/', ''))

    tags = list(dict.fromkeys(tags))
    tags.sort(key=StrictVersion, reverse=True)
    return tags


def get_build_from_tag(repo, tag):
    builds = requests.get("{}/api/repos/primait/{}/builds?per_page=100".format(baseurl, repo),
                          headers={'Authorization': 'Bearer {}'.format(tokens.drone)}).json()

    for build in builds:
        if build["event"] == "tag":
            if build["ref"].replace('refs/tags/', '') == tag:
                return build["number"]
    return None


def launch_build(repo, build):
    return requests.post("{}/api/repos/primait/{}/builds/{}".format(baseurl, repo, build),
                         headers={'Authorization': 'Bearer {}'.format(tokens.drone)}).json()
