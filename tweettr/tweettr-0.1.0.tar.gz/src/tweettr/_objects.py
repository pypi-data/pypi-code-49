"""tweettr minimal tweet encapsulation

from Twitter:
  ## Parsing best-practices ##
  - Twitter JSON is encoded using UTF-8 characters.
  - Parsers should tolerate variance in the ordering of fields with ease.
    It should be assumed that Tweet JSON is served as an unordered hash of data.
  - Parsers should tolerate the addition of 'new' fields. The Twitter platform
    has continually evolved since 2006, so there is a long history of new metadata
    being added to Tweets.
  - JSON parsers must be tolerant of ‘missing’ fields, since not all fields appear
    in all contexts.
  - It is generally safe to consider a nulled field, an empty set, and the absence
    of a field as the same thing.
"""
__author__ = "Andreas Poehlmann"
__email__ = "andreas@poehlmann.io"

import json
from typing import Any, Dict, List, Literal, Optional

from ._base import TweettrBase, enhance_type_hinted_classes_with_descriptors
from ._emoji import iter_emoji_entities

__all__ = [
    'BoundingBox',
    'Coordinates',
    'Emoji',
    'Entities',
    'ExtendedEntities',
    'ExtendedTweet',
    'HashTag',
    'Media',
    'Place',
    'Poll',
    'QuotedStatusPermalink',
    'Size',
    'Sizes',
    'Symbol',
    'Tweet',
    'Url',
    'User',
    'UserMention',
]


class User(TweettrBase):
    """User
    
    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object

    Attributes
    ----------
    {attributes}
    """
    id: int
    id_str: str
    name: str
    screen_name: str

    location: Optional[str]
    url: Optional[str]
    description: Optional[str]
    protected: bool
    verified: bool

    followers_count: int
    friends_count: int
    listed_count: int
    favourites_count: int
    statuses_count: int
    created_at: str

    default_profile: bool
    default_profile_image: bool
    profile_image_url_https: str
    profile_banner_url: Optional[str]

    withheld_in_countries: Optional[List[str]]
    withheld_scope: Optional[str]

    # deprecated
    # ----------
    # - utc_offset
    # - time_zone
    # - lang
    # - geo_enabled
    # - following
    # - follow_request_sent
    # - notifications
    # - contributors_enabled
    # - profile_image_url
    # - profile_background_color
    # - profile_background_image_url
    # - profile_background_image_url_https
    # - profile_background_tile
    # - profile_link_color
    # - profile_sidebar_border_color
    # - profile_sidebar_fill_color
    # - profile_text_color
    # - profile_use_background_image
    # - is_translator
    # - translator_type

    def __repr__(self):
        return f'{self.__class__.__name__}(screen_name={repr(self.screen_name)}, id={repr(self.id)})'


class Coordinates(TweettrBase):
    """Coordinates
    
    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects#coordinates

    Attributes
    ----------
    {attributes}
    """
    coordinates: List[float]
    type: Literal['Point']

    def __repr__(self):
        long, lat = self.coordinates
        return f'{self.__class__.__name__}(longitude={repr(long)}, latitude={repr(lat)})'


class BoundingBox(TweettrBase):
    """BoundingBox
    
    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects#obj-boundingbox

    Attributes
    ----------
    {attributes}
    """
    coordinates: List[List[List[float]]]
    type: Literal['Polygon']

    def __repr__(self):
        num_bb = len(self.coordinates)
        return f'{self.__class__.__name__}(num_bb={num_bb})'


class Place(TweettrBase):
    """Place

    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects#place-dictionary

    Attributes
    ----------
    {attributes}
    """
    id: str
    country: Optional[str]
    country_code: Optional[str]
    full_name: Optional[str]
    name: Optional[str]
    place_type: Optional[str]
    url: Optional[str]
    attributes: Optional[dict]

    bounding_box: Optional[BoundingBox]

    def __repr__(self):
        return f'{self.__class__.__name__}(name={repr(self.name)}, id={repr(self.id)})'


class HashTag(TweettrBase):
    """HashTag
    
    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#hashtags

    Attributes
    ----------
    {attributes}
    """
    text: str
    indices: List[int]

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.text)})'


class Emoji(TweettrBase):
    """Emoji

    this is a custom Tweettr object that acts like a HashTag object but contains info about
    emojis in the tweet text

    Attributes
    ----------
    {attributes}
    """
    text: str
    indices: List[int]

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.text)})'


class Size(TweettrBase):
    """Size
    
    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#size

    Attributes
    ----------
    {attributes}
    """
    w: int
    h: int
    resize: str

    def __repr__(self):
        return f'{self.__class__.__name__}(size={self.w}x{self.h}, resize={repr(self.resize)})'


class Sizes(TweettrBase):
    """Sizes

    simple container for multiple Size objects

    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#size

    Attributes
    ----------
    {attributes}
    """
    large: Size
    medium: Size
    small: Size
    thumb: Size

    def __repr__(self):
        return f'{self.__class__.__name__}(instance at {id(self)})'


class Symbol(TweettrBase):
    """Symbol
    
    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#symbols

    Attributes
    ----------
    {attributes}
    """
    text: str
    indices: List[int]

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.text)})'


class Url(TweettrBase):
    """Url

    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#urls

    Attributes
    ----------
    {attributes}
    """
    display_url: str
    expanded_url: str
    url: str
    indices: List[int]

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.url)})'


class Media(TweettrBase):
    """Media
    
    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#media

    Attributes
    ----------
    {attributes}
    """
    display_url: str
    expanded_url: str
    id: int
    id_str: str
    media_url: str
    media_url_https: str
    sizes: Sizes

    source_status_id: Optional[int]
    source_status_id_str: Optional[str]

    indices: List[int]
    type: str
    url: str

    # not used ?
    # ----------
    # source_user_id
    # source_user_id_str
    # description

    def __repr__(self):
        return f'{self.__class__.__name__}(id={repr(self.id)})'


class UserMention(TweettrBase):
    """UserMention
    
    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#mentions

    Attributes
    ----------
    {attributes}
    """
    id: int
    id_str: str
    indices: List[int]
    name: str
    screen_name: str

    def __repr__(self):
        return f'{self.__class__.__name__}(mention={repr(self.screen_name)})'


class Poll(TweettrBase):
    """Poll

    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#polls

    Attributes
    ----------
    {attributes}
    """
    options: List[Dict]  # TODO: should be List[Option]
    end_datetime: str
    duration_minutes: str

    def __repr__(self):
        num_options = len(self.options)
        return f'{self.__class__.__name__}(num_options={num_options})'


class Entities(TweettrBase):
    """Entities
    
    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object

    Attributes
    ----------
    {attributes}
    """
    hashtags: List[HashTag]
    urls: List[Url]
    user_mentions: List[UserMention]
    symbols: List[Symbol]
    polls: List[Poll]
    media: List[Media]

    def __repr__(self):
        return f'{self.__class__.__name__}(instance at {id(self)})'


class ExtendedEntities(TweettrBase):
    """ExtendedEntities
    
    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/extended-entities-object

    Attributes
    ----------
    {attributes}
    """
    media: List[Media]

    def __repr__(self):
        return f'{self.__class__.__name__}(instance at {id(self)})'


class ExtendedTweet(TweettrBase):
    """ExtendedTweet

    this depends on api-access and streaming or not endpoints and if extended_mode is requested
    
    see: https://developer.twitter.com/en/docs/tweets/tweet-updates

    Attributes
    ----------
    {attributes}
    """
    full_text: str
    truncated: Literal[False]
    entities: Optional[Entities]
    extended_entities: Optional[ExtendedEntities]
    display_text_range: Optional[List[int]]

    def __repr__(self):
        return f'{self.__class__.__name__}(instance at {id(self)})'


class QuotedStatusPermalink(TweettrBase):
    """QuotedStatusPermalink
    
    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json

    Attributes
    ----------
    {attributes}
    """
    display: str
    expanded: str
    url: str

    def __repr__(self):
        return f'{self.__class__.__name__}(display={repr(self.display)})'


class Tweet(TweettrBase):
    """Tweet

    see: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object

    Attributes
    ----------
    {attributes}
    """
    created_at: str
    id: int
    id_str: str
    text: str
    source: str
    truncated: bool

    contributors: Any

    user: User

    is_quote_status: bool
    quote_count: int

    reply_count: int
    retweet_count: int
    favorite_count: int

    favorited: bool
    retweeted: bool

    filter_level: str
    lang: str
    timestamp_ms: Optional[str]

    possibly_sensitive: Optional[bool]
    quoted_status_id: Optional[int]
    quoted_status_id_str: Optional[str]
    in_reply_to_status_id: Optional[int]
    in_reply_to_status_id_str: Optional[str]
    in_reply_to_user_id: Optional[int]
    in_reply_to_user_id_str: Optional[str]
    in_reply_to_screen_name: Optional[str]

    coordinates: Optional[Coordinates]
    place: Optional[Place]

    display_text_range: Optional[List[int]]
    retweeted_status: Optional['Tweet']
    quoted_status: Optional['Tweet']
    entities: Optional[Entities]
    extended_entities: Optional[ExtendedEntities]
    extended_tweet: Optional[ExtendedTweet]
    quoted_status_permalink: Optional[QuotedStatusPermalink]

    # deprecated
    # ----------
    # - geo

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as json_f:
            data = json.load(json_f)
        return cls(data)

    def __repr__(self):
        try:
            screen_name = self.user.screen_name
        except (AttributeError, TypeError):
            screen_name = None
        return f'{self.__class__.__name__}(id={repr(self.id)}, user={repr(screen_name)})'

    @property
    def permalink(self):
        """return a permalink to the tweet"""
        return f'https://twitter.com/{self.user.screen_name}/status/{self.id}'

    @property
    def is_retweet(self):
        return True if self.retweeted_status else False

    @property
    def is_quote_tweet(self):
        return True if self.quoted_status else False

    @property
    def is_original_tweet(self):
        return not (self.is_retweet or self.is_quote_tweet)

    @property
    def extended_full_text(self):
        """return the untruncated full_text"""
        return self.extended_tweet.full_text if self.extended_tweet else self.text

    @property
    def emojis(self):
        """return a list of all Emoji Entities in tweet"""
        return [Emoji(data) for data in iter_emoji_entities(self.extended_full_text)]


# Set descriptors for all type annotations that contain subclasses
# of TweettrBase to allow transparent conversion of sub dicts to tweettr classes
for subclass in TweettrBase.__subclasses__():
    # Note: the only way to do this in a meta class is if ForwardRefs would
    #   be dynamically resolved lazily during runtime...
    #   Let's prevent that overhead and do it after all subclasses have been defined.
    #   Nice side effect: this TypeErrors if a forward ref can't be de-referenced
    enhance_type_hinted_classes_with_descriptors(subclass)
