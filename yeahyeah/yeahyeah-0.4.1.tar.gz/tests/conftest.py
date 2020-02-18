"""pytest fixtures shared by modules in this folder

"""
import webbrowser
from unittest.mock import Mock

import pytest

from yeahyeah_plugins.path_item_plugin.core import PathItem, PathItemList, PathItemPlugin
from yeahyeah.core import YeahYeah
from yeahyeah_plugins.url_pattern_plugin.core import URLPatternList, UrlPattern, WildCardUrlPattern, UrlPatternsPlugin


@pytest.fixture(autouse=True)
def disable_click_echo(monkeypatch):
    """Don't print click.echo to console. Click runner disables this, but not
    all tests use click runner to invoke all commands. So this is needed"""
    monkeypatch.setattr("yeahyeah.core.click.echo", Mock())


@pytest.fixture()
def url_pattern_list():
    """A pattern list with some content"""
    return URLPatternList(
        items=[
            UrlPattern(
                name="test1", pattern="https://host{pattern1}/something{pattern2}.php"
            ),
            UrlPattern(
                name="test2",
                pattern="https://athing.com",
                help_text="Another test pattern",
            ),
            WildCardUrlPattern(name="test5", pattern="https://search{query}"),
        ]
    )


@pytest.fixture()
def path_item_list():
    return PathItemList(items=[
        PathItem(
            name="home",
            path="/home/a_user/",
            help_text="(Example) Open home directory",
        ),
        PathItem(
            name="external_disk",
            path="/mnt/some_mount/user/something",
            help_text="(Example) Open that external disk",
        )
    ])


@pytest.fixture()
def yeahyeah_instance(url_pattern_list, path_item_list, tmpdir):
    """An instance of the yeahyeah launch manager with some default plugins_old and commands"""
    yeahyeah = YeahYeah(configuration_path=tmpdir)
    yeahyeah.add_plugin_instance(UrlPatternsPlugin(pattern_list=url_pattern_list))
    yeahyeah.add_plugin_instance(PathItemPlugin(item_list=path_item_list))

    return yeahyeah


@pytest.fixture()
def mock_web_browser(monkeypatch):
    """Mock the python standard webbrowser
    """
    mock_web_browser = Mock(spec=webbrowser)
    monkeypatch.setattr("yeahyeah_plugins.url_pattern_plugin.core.webbrowser", mock_web_browser)
    return mock_web_browser


