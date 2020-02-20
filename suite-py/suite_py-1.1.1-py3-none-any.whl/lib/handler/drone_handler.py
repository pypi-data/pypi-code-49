# -*- encoding: utf-8 -*-
from distutils.version import StrictVersion
import time
import requests

from halo import Halo
from suite_py.lib.tokens import Tokens


tokens = Tokens()
baseurl = "https://drone-1.prima.it"


def get_last_build_url(repo):
    with Halo(text="Contacting drone...", spinner="dots", color="magenta"):
        # necessario per far comparire la build che abbiamo appena pushato
        time.sleep(2)
        try:
            resp = requests.get(
                f"{baseurl}/api/repos/primait/{repo}/builds",
                headers={"Authorization": f"Bearer {tokens.drone}"},
            ).json()

            return f"{baseurl}/primait/{repo}/{resp[0]['number']}"
        except Exception:
            return ""


def get_pr_build_url(repo, commit_sha):
    with Halo(text="Contacting drone...", spinner="dots", color="magenta"):
        # necessario per far comparire la build che abbiamo appena pushato
        time.sleep(2)
        try:
            resp = requests.get(
                f"{baseurl}/api/repos/primait/{repo}/builds?per_page=100",
                headers={"Authorization": f"Bearer {tokens.drone}"},
            ).json()
            builds = [b for b in resp if b["after"] == commit_sha]
            build_number = builds[0]["number"]
            return f"{baseurl}/primait/{repo}/{build_number}"
        except Exception:
            return ""


def get_tag_from_builds(repo):
    tags = []
    builds = requests.get(
        f"{baseurl}/api/repos/primait/{repo}/builds?per_page=100",
        headers={"Authorization": f"Bearer {tokens.drone}"},
    ).json()

    for build in builds:
        if build["event"] == "tag":
            tags.append(build["ref"].replace("refs/tags/", ""))

    tags = list(dict.fromkeys(tags))
    tags.sort(key=StrictVersion, reverse=True)
    return tags


def get_build_from_tag(repo, tag):
    builds = requests.get(
        f"{baseurl}/api/repos/primait/{repo}/builds?per_page=100",
        headers={"Authorization": f"Bearer {tokens.drone}"},
    ).json()

    for build in builds:
        if build["event"] == "tag":
            if build["ref"].replace("refs/tags/", "") == tag:
                return build["number"]
    return None


def launch_build(repo, build):
    return requests.post(
        f"{baseurl}/api/repos/primait/{repo}/builds/{build}",
        headers={"Authorization": f"Bearer {tokens.drone}"},
    ).json()
