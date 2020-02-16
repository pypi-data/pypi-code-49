import os


class Bitbucket():

    def __init__(self, **kwargs):
        pass

    def is_bitbucket(self):
        if os.environ.get('CI', 'false') == 'true':
            return True
        else:
            return False

    def is_pull_request(self):
        if self.is_bitbucket() and os.environ.get('BITBUCKET_PR_ID', None) is not None:
            return True
        else:
            return False

    def branch(self):
        if self.is_bitbucket():
            return os.environ.get('BITBUCKET_BRANCH')
        else:
            return 'master'

    def commit_hash(self):
        return os.environ.get('BITBUCKET_COMMIT', '0' * 30)

    def short_commit_hash(self):
        return os.environ.get('BITBUCKET_COMMIT', '0' * 30)[:8]

    def tag(self):
        return os.environ.get('BITBUCKET_TAG', None)

    def is_tag(self):
        if os.environ.get('BITBUCKET_TAG', False):
            return True
        else:
            return False

    def home_dir(self):
        return os.environ.get('HOME', '/dev/null')

    def build_dir(self):
        return os.environ.get('BITBUCKET_CLONE_DIR', '/dev/null')
