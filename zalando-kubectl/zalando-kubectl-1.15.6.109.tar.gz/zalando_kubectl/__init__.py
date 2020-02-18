# This is replaced during release process.
__version_suffix__ = '109'

APP_NAME = "zalando-kubectl"

KUBECTL_VERSION = "v1.15.6"
KUBECTL_SHA512 = {
    "linux": "32292b73d40c01a55e9d820c8a2d69f7ae68efd86954eb25a824bc4730146fe174d5a0ea9eb4bc914f9e725a59f8aab411138cb09ec87e1cec130dd16eb46273",
    "darwin": "42a63e2cc626fbe30de7ce118afa9b0bcb58d85f7dc909eec8afc4a331a09db3d6bc8e80932f590214facb5de1089087a31c75c3001bcf433a3a42a4e7549b74",
}

STERN_VERSION = "1.10.0"
STERN_SHA256 = {
    "linux": "a0335b298f6a7922c35804bffb32a68508077b2f35aaef44d9eb116f36bc7eda",
    "darwin": "b91dbcfd3bbda69cd7a7abd80a225ce5f6bb9d6255b7db192de84e80e4e547b7",
}

APP_VERSION = KUBECTL_VERSION + "." + __version_suffix__
