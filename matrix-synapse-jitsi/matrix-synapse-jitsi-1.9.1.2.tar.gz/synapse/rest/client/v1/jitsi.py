# -*- coding: utf-8 -*-
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

import base64
import hashlib
import hmac
import jwt
import time

from synapse.http.servlet import RestServlet
from synapse.rest.client.v2_alpha._base import client_patterns
from synapse.types import UserID


class JitsiRestServlet(RestServlet):
    PATTERNS = client_patterns("/jitsi/roomToken/(?P<room_id>[^/]*)$", v1=True)

    def __init__(self, hs):
        super(JitsiRestServlet, self).__init__()
        self.hs = hs
        self.profile_handler = hs.get_profile_handler()
        self.auth = hs.get_auth()

    async def on_GET(self, request, room_id):
        requester = await self.auth.get_user_by_req(request)
        requester_user = requester.user
        user_id = requester_user.to_string()

        jitsiURL = self.hs.config.jitsi_url
        jitsiAppID = self.hs.config.jitsi_app_id
        jitsiAppSecret = self.hs.config.jitsi_app_secret
        payload = {
            "room": room_id,
            "context": {
                "user": {
                    "id": user_id,
                    "name": "",
                    "avatar": ""
                }
            },
            "aud": jitsiAppID,
            "iss": jitsiAppID,
            "sub": "meet.jitsi",
            "exp": int(time.time()) + 600
        }

        user = UserID.from_string(user_id)

        await self.profile_handler.check_profile_query_allowed(user, requester_user)

        displayname = await self.profile_handler.get_displayname(user)
        avatar_url = await self.profile_handler.get_avatar_url(user)
        
        if displayname is not None:
            payload["context"]["user"]["name"] = displayname
        if avatar_url is not None:
            payload["context"]["user"]["avatar"] = avatar_url

        if jitsiURL and jitsiAppID and jitsiAppSecret:
            jitsiToken = jwt.encode(payload, jitsiAppSecret, algorithm='HS256')
            return (
                200,
                {
                    "url": jitsiURL,
                    "token": jitsiToken
                },
            )

        else:
            return 500, {}

    def on_OPTIONS(self, request):
        return 200, {}

def register_servlets(hs, http_server):
    JitsiRestServlet(hs).register(http_server)
