import pytest

from unittest.mock import call, patch

from redis_key_tagging.client import RedisKeyTagging


class TestRedisKeyTagging:
    @pytest.mark.parametrize(
        "tag, expected_tag_key",
        (
            ("foo", "tag:foo"),
            ("bar", "tag:bar"),
            ("123", "tag:123"),
            ("foo bar", None),
            ("", None),
            ([], None),
            (None, None),
            (True, None),
            (False, None),
        ),
    )
    def test_get_tag_key(self, tag, expected_tag_key):
        redis = RedisKeyTagging()
        assert redis.get_tag_key(tag) == expected_tag_key

    @pytest.mark.parametrize(
        "key, tags, expected_calls",
        (
            ("foo", [], []),
            ("foo", [None], []),
            ("foo", ["bar"], [call().sadd("tag:bar", "foo")]),
            (
                "foo",
                ["bar", "baz"],
                [call().sadd("tag:bar", "foo"), call().sadd("tag:baz", "foo")],
            ),
        ),
    )
    @patch("redis_key_tagging.client.RedisKeyTagging.pipeline")
    @patch("redis.client.Redis.set")
    def test_set(self, mock_set, mock_pipeline, key, tags, expected_calls):
        mock_set.return_value = 1
        redis = RedisKeyTagging()
        result = redis.set(key, "", tags=tags)
        assert result == 1
        redis.pipeline.assert_has_calls([call()])
        redis.pipeline.assert_has_calls(expected_calls, any_order=True)
        redis.pipeline.assert_has_calls([call().execute()])

    @pytest.mark.parametrize(
        "tag, smembers, expected_calls",
        (
            ("foo", {}, []),
            ("foo", {b"bar"}, [call().delete("bar"), call().srem("tag:foo", "bar")]),
            (
                "foo",
                {b"bar", b"baz"},
                [call().delete("bar", "baz"), call().srem("tag:foo", "bar", "baz")],
            ),
        ),
    )
    @patch("redis_key_tagging.client.RedisKeyTagging.smembers")
    @patch("redis_key_tagging.client.RedisKeyTagging.pipeline")
    def test_delete_keys_by_tag(self, mock_pipeline, mock_smembers, tag, smembers, expected_calls):
        mock_pipeline.return_value.execute.return_value = [len(expected_calls)] * 2
        mock_smembers.return_value = sorted(smembers)
        redis = RedisKeyTagging()
        result = redis.delete_keys_by_tag(tag)
        assert result == [len(expected_calls)] * 2
        redis.pipeline.assert_has_calls([call()])
        redis.pipeline.assert_has_calls(expected_calls, any_order=True)
        redis.pipeline.assert_has_calls([call().execute()])
