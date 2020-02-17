# Copyright 2014-2016 OpenMarket Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ._base import Config


class JitsiConfig(Config):
    section = "jitsi"

    def read_config(self, config, **kwargs):
        self.jitsi_url = config.get("jitsi_url")
        self.jitsi_app_id = config.get("jitsi_app_id")
        self.jitsi_app_secret = config.get("jitsi_app_secret")

    def generate_config_section(self, **kwargs):
        return """\
        ## Jitsi ##

        # The url, id and secret for jitsi video conferencing
        #
        #jitsi_url: "https://jitsi.example.com"
        #jitsi_app_id: "example_app_id"
        #jitsi_app_secret: "example_app_secret"
        """
