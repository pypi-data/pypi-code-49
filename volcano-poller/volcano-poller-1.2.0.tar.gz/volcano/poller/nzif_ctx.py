#!/usr/bin/python3

from . import merk_nzif_ctx
from .nzif_defs import get_nzif_nack_codes


class NzifCtx(merk_nzif_ctx.MerkNzifCtx):
    def __init__(self, channel):
        super().__init__(channel, False)

    def get_nack_comment_n(self, nack_code):
        return get_nzif_nack_codes().get(nack_code, None)
