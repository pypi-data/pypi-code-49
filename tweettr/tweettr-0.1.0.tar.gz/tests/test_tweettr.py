import pytest
import glob
import os.path
import json
from tweettr import Tweet, User


TWEET_FNS = list(sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'tweets', '*.json'))))


@pytest.fixture(scope='function',
                params=TWEET_FNS,
                ids=[os.path.basename(fn) for fn in TWEET_FNS])
def tweet_fn(request):
    tweet_fn = request.param
    yield tweet_fn


def test_tweet_constructor(tweet_fn):
    with open(tweet_fn, 'r') as f:
        data = json.load(f)

    tweet = Tweet(data)
    # verify that the internal dict is a reference to data
    assert tweet._dict is data


def test_tweet_attribute_access(tweet_fn):
    tweet = Tweet.from_file(tweet_fn)

    assert tweet.id > 0
    assert isinstance(tweet.user, User)
    assert tweet.timestamp_ms
    assert tweet.user.id > 0
    assert tweet.entities.hashtags[0].text


def test_tweet_non_existing_attribute_access(tweet_fn):
    tweet = Tweet.from_file(tweet_fn)

    with pytest.raises(AttributeError):
        _ = tweet.i_do_not_exist


def test_tweet_getitem_access(tweet_fn):
    tweet = Tweet.from_file(tweet_fn)

    assert tweet['id_str'] == tweet.id_str


def test_tweet_nocopy_class_object_wrapping(tweet_fn):
    tweet = Tweet.from_file(tweet_fn)

    # noinspection PyProtectedMember
    assert tweet['user'] is tweet.user._dict


def test_tweet_emoji_parsing(tweet_fn):
    tweet = Tweet.from_file(tweet_fn)

    assert isinstance(tweet.emojis, list)


def test_emoji_parsing():
    # noinspection PyProtectedMember
    from tweettr._emoji import iter_emoji_entities

    txt = b'fish \xf0\x9f\x90\x8b fush'.decode('utf8')
    emojis = list(iter_emoji_entities(txt))
    assert len(emojis) == 1


def test_tweet_attributes_recursively(tweet_fn):
    # noinspection PyProtectedMember
    from tweettr._base import TweettrBase

    tweet = Tweet.from_file(tweet_fn)

    def recurse(t):
        for attr in t.__annotations__:
            v = getattr(t, attr)
            if isinstance(v, TweettrBase):
                recurse(v)
    recurse(tweet)
