# -*- coding: utf-8 -*-

import json
import random
import re
import requests
import time
import tuxbuild.exceptions

# We will poll for status change for an average duration of 180 minutes
status_attempts = 720
delay_status_update = 30


def post_request(url, headers, request):
    retry_attempts = 3
    for i in range(1, retry_attempts + 1):
        try:
            response = requests.post(url, data=json.dumps(request), headers=headers)
        except requests.exceptions.ConnectionError as e:
            # We are getting exception from either from Network error
            if i == retry_attempts:
                raise e
            else:
                time.sleep(random.randrange(15))
                continue
        if response.ok:
            return json.loads(response.text)
        else:
            if response.status_code == 400:
                response_data = json.loads(response.text)
                raise tuxbuild.exceptions.BadRequest(
                    f"{response_data.get('tuxbuild_status')}: {response_data.get('status_message')}"
                )
            elif response.status_code in [500, 504] and i < retry_attempts:
                time.sleep(random.randrange(15))
            else:
                response.raise_for_status()


def get_request(url, headers):
    retry_attempts = 30
    for i in range(1, retry_attempts + 1):
        try:
            r = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError as e:
            # We are getting exception from either from Network error
            if i == retry_attempts:
                raise e
            else:
                time.sleep(random.randrange(15))
                continue
        if r.status_code == 200:
            return json.loads(r.text)
        elif r.status_code in [500, 504] and i < retry_attempts:
            time.sleep(random.randrange(15))
        else:
            r.raise_for_status()  # Some unexpected status that's not caught


class Build:
    def __init__(
        self,
        git_repo,
        git_ref,
        target_arch,
        kconfig,
        toolchain,
        token,
        kbapi_url,
        kconfig_allconfig=None,
    ):
        self.git_repo = git_repo
        self.git_ref = git_ref
        self.target_arch = target_arch
        self.kconfig = kconfig
        if isinstance(self.kconfig, str):
            self.kconfig = [self.kconfig]
        self.kconfig_allconfig = kconfig_allconfig
        self.toolchain = toolchain
        self.build_data = None
        self.build_key = None
        self.status = {}
        self.kbapi_url = kbapi_url
        self.headers = {
            "Content-type": "application/json",
            "Authorization": "{}".format(token),
        }
        self.verify_build_parameters()

    def __str__(self):
        git_short_log = self.status.get("git_short_log", "")
        kconfig_allconfig_param = ""
        if self.kconfig_allconfig is not None:
            kconfig_allconfig_param = " and {} as kconfig_allconfig".format(
                self.kconfig_allconfig
            )

        return "{} {} ({}{}) with {} @ {}".format(
            git_short_log,
            self.target_arch,
            ", ".join(self.kconfig),
            kconfig_allconfig_param,
            self.toolchain,
            self.build_data,
        )

    @staticmethod
    def is_supported_git_url(url):
        """
        Check that the git url provided is valid (namely, that it's not an ssh
        url)
        """
        return re.match(r"^(git://|https?://).*$", url) is not None

    def generate_build_request(self):
        """ return a build data in a python dict """
        build_entry = {}
        build_entry["git_repo"] = self.git_repo
        build_entry["git_ref"] = self.git_ref
        build_entry["target_arch"] = self.target_arch
        build_entry["toolchain"] = self.toolchain
        build_entry["kconfig"] = self.kconfig
        if self.kconfig_allconfig is not None:
            build_entry["kconfig_allconfig"] = self.kconfig_allconfig
        return build_entry

    def verify_build_parameters(self):
        """ Pre-check the build arguments """
        assert self.is_supported_git_url(
            self.git_repo
        ), "git url must be in the form of git:// or http:// or https://"
        assert self.git_ref is not None
        assert self.target_arch is not None
        assert self.kconfig is not None
        assert self.headers is not None

    def build(self):
        """ Submit the build request """
        data = []
        data.append(self.generate_build_request())
        url = self.kbapi_url + "/build"
        json_data = post_request(url, self.headers, data)
        self.build_data = json_data[0]["download_url"]
        self.build_key = json_data[0]["build_key"]

    def get_status(self):
        """ Fetches the build status and updates the values inside the build object"""
        url = self.kbapi_url + "/status/" + self.build_key
        self.status = get_request(url, self.headers)

    def wait_on_status(self, status):
        """
            Wait until the given status changes

            For example, if status is 'queued', wait_for_status
            will return once the status is no longer 'queued'

            Will timeout after status_attempts
        """
        for i in range(status_attempts):
            self.get_status()
            if self.status["tuxbuild_status"] != status:
                break
            time.sleep(random.randrange(delay_status_update))

    def _get_field(self, field):
        """ Retrieve an individual field from status.json """
        self.get_status()
        return self.status.get(field, None)

    @property
    def warnings_count(self):
        """ Get the warnings_count for the build """
        return int(self._get_field("warnings_count"))

    @property
    def errors_count(self):
        """ Get the errors_count for the build """
        return int(self._get_field("errors_count"))

    @property
    def tuxbuild_status(self):
        """ Get the tuxbuild_status for the build """
        return self._get_field("tuxbuild_status")

    @property
    def build_status(self):
        """ Get the build_status for the build """
        return self._get_field("build_status")

    @property
    def status_message(self):
        """ Get the build_status for the build """
        return self._get_field("status_message")


class BuildSet:
    def __init__(self, build_objects, token, kbapi_url):
        self.build_objects = build_objects
        self.headers = {
            "Content-type": "application/json",
            "Authorization": "{}".format(token),
        }
        self.kbapi_url = kbapi_url

    def build(self):
        """ Submit the build request """

        build_objects_list = self.build_objects[:]
        data = []
        url = self.kbapi_url + "/build"
        for build_object in self.build_objects:
            data.append(build_object.generate_build_request())
        json_data = post_request(url, self.headers, data)
        for build_config in json_data:
            for build_object in build_objects_list:
                if (
                    build_config.items()
                    >= build_object.generate_build_request().items()
                ):
                    build_object.build_data = build_config["download_url"]
                    build_object.build_key = build_config["build_key"]
                    # We may have build set with same parameters multiple times
                    # hence remove the build from build_objects list after mapping
                    build_objects_list.remove(build_object)
                    break

    @property
    def status_list(self):
        """ Return a list of build status dictionaries """
        return [build.status for build in self.build_objects]
