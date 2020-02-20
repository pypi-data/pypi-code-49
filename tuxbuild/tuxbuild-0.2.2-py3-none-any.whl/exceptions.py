# -*- coding: utf-8 -*-


class TuxbuildError(Exception):
    """ Base class for all Tuxbuild exceptions """

    error_help = ""
    error_type = ""


class TokenNotFound(TuxbuildError):
    error_help = "No token provided"
    error_type = "Configuration"


class URLNotFound(TuxbuildError):
    error_help = "A tuxbuild URL cannot be found"
    error_type = "Configuration"


class BadRequest(TuxbuildError):
    error_help = "A tuxbuild API call failed"
    error_type = "API"
