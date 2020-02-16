"""tweettr

Thin `attrdict` like wrapper around (a few) tweet objects
"""
__author__ = "Andreas Poehlmann"
__email__ = "andreas@poehlmann.io"

from ._objects import (BoundingBox, Coordinates, Emoji, Entities,
                       ExtendedEntities, ExtendedTweet, HashTag, Media,
                       Place, Poll, QuotedStatusPermalink, Size, Sizes,
                       Symbol, Tweet, Url, User, UserMention)
try:
    from ._version import __version__
except ImportError:
    __version__ = None
