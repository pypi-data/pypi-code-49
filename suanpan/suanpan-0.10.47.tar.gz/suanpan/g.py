# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.objects import Context
from suanpan.utils import env

g = Context(
    # App
    debug=env.lazyget("SP_DEBUG", type=env.bool, default=False),
    appType=env.lazyget("SP_APP_TYPE", required=True),
    appParams=env.lazyget("SP_PARAM", default=""),
    nodeInfo=env.lazyget("SP_NODE_INFO", default=""),
    userId=env.lazyget("SP_USER_ID", required=True),
    appId=env.lazyget("SP_APP_ID", required=True),
    nodeId=env.lazyget("SP_NODE_ID", required=True),
    nodeGroup=env.lazyget("SP_NODE_GROUP", default="default"),
    # Api
    host=env.lazyget("SP_HOST", required=True),
    hostTls=env.lazyget("SP_HOST_TLS", type=env.bool, default=False),
    apiHost=env.lazyget("SP_API_HOST", required=True),
    apiHostTls=env.lazyget("SP_API_HOST_TLS", type=env.bool, default=False),
    affinity=env.lazyget("SP_AFFINITY"),
    accessKey=env.lazyget("SP_ACCESS_KEY", required=True),
    accessSecret=env.lazyget("SP_ACCESS_SECRET", required=True),
    userIdHeaderField=env.lazyget("SP_USER_ID_HEADER_FIELD", default="x-sp-user-id"),
    userSignatureHeaderField=env.lazyget(
        "SP_USER_SIGNATURE_HEADER_FIELD", default="x-sp-signature"
    ),
    userSignVersionHeaderField=env.lazyget(
        "SP_USER_SIGN_VERSION_HEADER_FIELD", default="x-sp-sign-version"
    ),
    # Screenshots
    screenshotsType=env.lazyget("SP_SCREENSHOTS_TYPE", default="index"),
    screenshotsPattern=env.lazyget("SP_SCREENSHOTS_PATTERN"),
    screenshotsStorageKey=env.lazyget("SP_SCREENSHOTS_STORAGE_KEY"),
    screenshotsThumbnailStorageKey=env.lazyget("SP_SCREENSHOTS_THUMBNAIL_STORAGE_KEY"),
)
