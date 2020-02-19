import logging


class _BaseGiphyObject(object):
    _attrs = []
    _objects = []

    def __init__(self, kwargs):
        self._autoprocess(kwargs)

    def _autoprocess(self, kwargs):
        for attr in self._attrs:
            if attr in kwargs.keys():
                setattr(self, attr, kwargs[attr])

        for obj_name in self._objects:
            if obj_name in kwargs.keys():
                SchemaClass = self._objects.get(obj_name)
                try:
                    setattr(self, obj_name, SchemaClass(kwargs[obj_name]))
                except:
                    logging.exception(
                        msg=(
                            "object {name} expected a different data"
                            "structure than '{value}'. Aborting".format(
                                name=obj_name, value=kwargs[obj_name])))
                    raise


# SCHEMAS
class User(_BaseGiphyObject):
    _attrs = [
        'avatar_url',
        'banner_url',
        'profile_url',
        'username',
        'display_name',
    ]


class Meta(_BaseGiphyObject):
    _attrs = [
        'msg',
        'status',
        'response_id',
    ]


class Pagination(_BaseGiphyObject):
    _attrs = [
        'offset',
        'total_count',
        'count',
    ]


class onload(_BaseGiphyObject):
    _attrs = ['url']


class onclick(_BaseGiphyObject):
    _attrs = ['url']


class onsent(_BaseGiphyObject):
    _attrs = ['url']


class Analytics(_BaseGiphyObject):
    _objects = dict(
        onload=onload,
        onclick=onclick,
        onsent=onsent,
    )


# Images class sub objects
class BaseImageObj(_BaseGiphyObject):
    _attrs = [
        'url',
        'width',
        'height',
    ]
    _extra_attrs = []

    def __init__(self, kwargs):
        self._attrs = self._attrs + self._extra_attrs
        super().__init__(kwargs)


class fixed_height(BaseImageObj):
    _extra_attrs = [
        'size',
        'mp4',
        'mp4_size',
        'webp',
        'webp_size'
    ]

class fixed_height_still(BaseImageObj):
    pass

class fixed_height_downsampled(BaseImageObj):
    _extra_attrs = [
        'size',
        'webp',
        'webp_size'
    ]

class fixed_width(fixed_height):
    pass

class fixed_width_still(BaseImageObj):
    pass

class fixed_width_downsampled(fixed_height_downsampled):
    pass

class fixed_height_small(fixed_height):
    pass

class fixed_height_small_still(BaseImageObj):
    pass

class fixed_width_small(fixed_height):
    pass

class fixed_width_small_still(BaseImageObj):
    pass

class downsized(BaseImageObj):
    _extra_attrs = ['size']

class downsized_still(BaseImageObj):
    pass

class downsized_large(downsized):
    pass

class downsized_medium(downsized):
    pass

class downsized_small(BaseImageObj):
    _base_attrs = [
        'mp4',
        'width',
        'height',
        'mp4_size'
    ]

class original(BaseImageObj):
    _extra_attrs = [
        'width',
        'height',
        'size',
        'frames',
        'mp4',
        'mp4_size',
        'webp',
        'webp_size',
    ]

class original_still(BaseImageObj):
    pass

class looping(BaseImageObj):
    _base_attrs = ['mp4']

class preview(BaseImageObj):
    _base_attrs = [
        'mp4',
        'mp4_size',
        'width',
        'height',
    ]

class preview_gif(BaseImageObj):
    pass


class Images(_BaseGiphyObject):
    _objects = dict(
        fixed_height=fixed_height,
        fixed_height_still=fixed_height_still,
        fixed_height_downsampled=fixed_height_downsampled,
        fixed_width=fixed_width,
        fixed_width_still=fixed_width_still,
        fixed_width_downsampled=fixed_width_downsampled,
        fixed_height_small=fixed_height_small,
        fixed_height_small_still=fixed_height_small_still,
        fixed_width_small=fixed_width_small,
        fixed_width_small_still=fixed_width_small_still,
        downsized=downsized,
        downsized_still=downsized_still,
        downsized_large=downsized_large,
        downsized_medium=downsized_medium,
        downsized_small=downsized_small,
        original=original,
        original_still=original_still,
        looping=looping,
        preview=preview,
        preview_gif=preview_gif
    )


class Gif(_BaseGiphyObject):
    _attrs = [
        'type',
        'id',
        'slug',
        'url',
        'bitly_url',
        'embed_url',
        'username',
        'source',
        'rating',
        'content_url',
        'source_tld',
        'source_post_url',
        'update_datetime',
        'import_datetime',
        'trending_datetime',
        'title',
        # undocumented
        'bitly_gif_url',
        'is_sticker',

    ]
    _objects = dict(
        user=User,
        images=Images,
        # undocumented
        analytics=Analytics
    )


class GifList(list):
    def __init__(self, gif_list):
        super().__init__()
        for i in gif_list:
            self.append(Gif(i))


#RESPONSES
class GiphyResponse(_BaseGiphyObject):
    pass


class SearchResponse(GiphyResponse):
    _objects = dict(
        data=GifList,
        pagination=Pagination,
        meta=Meta
    )

class GetResponse(GiphyResponse):
    _objects = dict(
        data=Gif,
        meta=Meta
    )
