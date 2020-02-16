import os


class Travis():

    def __init__(self, **kwargs):
        pass

    def is_travis(self):
        if os.environ.get('TRAVIS', 'false') == 'true':
            return True
        else:
            return False

    def is_pull_request(self):
        if self.is_travis() and os.environ.get('TRAVIS_PULL_REQUEST', 'false') == 'true':
            return True
        else:
            return False

    def branch(self):
        if self.is_travis():
            return os.environ.get('TRAVIS_BRANCH')
        else:
            return 'master'

    def commit_hash(self):
        return os.environ.get('TRAVIS_COMMIT', '0' * 30)

    def short_commit_hash(self):
        return os.environ.get('TRAVIS_COMMIT', '0' * 30)[:8]

    def tag(self):
        return os.environ.get('TRAVIS_TAG', None)

    def is_tag(self):
        if os.environ.get('TRAVIS_TAG', False):
            return True
        else:
            return False

    def home_dir(self):
        return os.environ.get('HOME', '/dev/null')

    def build_dir(self):
        return os.environ.get('TRAVIS_BUILD_DIR', '/dev/null')
