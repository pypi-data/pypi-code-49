from oidcmsg.message import Message
from oidcmsg.message import OPTIONAL_LIST_OF_SP_SEP_STRINGS
from oidcmsg.message import SINGLE_OPTIONAL_INT
from oidcmsg.message import SINGLE_OPTIONAL_STRING
from oidcmsg.message import SINGLE_REQUIRED_STRING


class TokenExchangeRequest(Message):
    c_param = {
        "grant_type": SINGLE_REQUIRED_STRING,
        "resource": SINGLE_OPTIONAL_STRING,
        "audience": SINGLE_OPTIONAL_STRING,
        "scope": OPTIONAL_LIST_OF_SP_SEP_STRINGS,
        "requested_token_type": SINGLE_OPTIONAL_STRING,
        "subject_token": SINGLE_REQUIRED_STRING,
        "subject_token_type": SINGLE_REQUIRED_STRING,
        "actor_token": SINGLE_OPTIONAL_STRING,
        "actor_token_type": SINGLE_OPTIONAL_STRING
    }


class TokenExchange_Response(Message):
    c_param = {
        "access_token": SINGLE_REQUIRED_STRING,
        "issued_token_type": SINGLE_REQUIRED_STRING,
        "token_type": SINGLE_REQUIRED_STRING,
        "expires_in": SINGLE_OPTIONAL_INT,
        "scope": OPTIONAL_LIST_OF_SP_SEP_STRINGS,
        "refresh_token": SINGLE_OPTIONAL_STRING
    }
