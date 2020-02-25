# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals
from . import choices


def sync_qcloud_vod_info(v):
    from xyz_qcloud import vod, utils
    fid = v.context.get('fileId') or v.context.get('FileId')
    if not fid:
        return
    v.context = vod.get_media_info(fid)['MediaInfoSet'][0]
    v.cover_url = utils.access(v.context, 'BasicInfo.CoverUrl')
    v.duration = utils.access(v.context, 'MetaData.Duration')
    v.size = utils.access(v.context, 'TranscodeInfo.TranscodeSet.0.Size')
    v.status = choices.STATUS_DONE
    v.save()
