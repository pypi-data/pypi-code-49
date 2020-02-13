from sun.utils import slack_ver


def test_slackware_version():
    version = '14.2'
    distribution = 'Slackware'
    assert distribution == slack_ver()[0]
    assert version == slack_ver()[1]