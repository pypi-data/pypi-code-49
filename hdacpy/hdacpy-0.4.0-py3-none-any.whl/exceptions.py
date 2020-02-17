class BadRequestException(Exception):
    """Bad request error"""
    pass


class EmptyMsgException(Exception):
    """Empy message in tx preparation"""
    pass
