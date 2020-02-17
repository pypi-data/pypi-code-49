#!/usr/bin/python3

from . import merk_nzif_ctx
from . import merk_defs


class MerkCtx(merk_nzif_ctx.MerkNzifCtx):
    def __init__(self, channel):
        super().__init__(channel, True)

    def get_nack_comment_n(self, nack_code):
        return merk_defs.g_merk_nack_codes.get(nack_code, None)
