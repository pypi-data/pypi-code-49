from dulwich import porcelain as git
from dulwich.repo import Repo
from wpkit.fsutil.dir_dict import FakeOS
import os, shutil, glob


class errors:
    class GitSpaceError(Exception):
        def __init__(self, *args):
            super().__init__(*args)


def is_git_dir(path):
    if os.path.exists(path) and os.path.isdir(path):
        dot_git_dir = path + '/.git'
        if os.path.exists(dot_git_dir) and os.path.isdir(dot_git_dir):
            return True
    return False


def is_empty_dir(path):
    assert os.path.exists(path) and os.path.isdir(path)
    if len(os.listdir(path)):
        return False
    else:
        return True


class GitRepo:
    def __init__(self, path, remote_location=None):
        self.repo = Repo(path)
        self.path = os.path.abspath(path)
        self.remote_location = remote_location

    def pull(self, remote_location=None, branch='master'):
        remote_location = remote_location or self.remote_location
        if not remote_location:
            raise Exception('Remote location is not given.')
        repo = self.repo
        git.pull(repo, remote_location, branch)
        git.reset(repo, 'hard')

    def status(self):
        repo = self.repo
        msg = git.status(repo)
        print(msg)
        return msg

    def push(self, remote_location=None, branch='master'):

        remote_location = remote_location or self.remote_location
        if not remote_location:
            raise Exception('Remote location is not given.')
        repo = self.repo
        # x=git.add(repo,[self.path])
        paths = list(git.get_untracked_paths(self.path, repo.path, repo.open_index()))
        paths+=list(git.get_unstaged_changes(repo.open_index(),self.path))
        paths = [p.decode() for p in paths]
        paths=[self.path+'/'+p for p in paths]
        # print(paths)
        if not paths:
            import logging
            logging.warning('Working tree is clean. Nothing to push.')
            return
        paths.append(self.path)
        x = git.add(repo, paths)
        # print('add:', x)
        git.commit(repo, 'bare gitspace commit')
        # print(repo, remote_location)
        git.push(repo, remote_location, branch)

    @classmethod
    def init(cls, path):
        git.init(path)
        return cls(path)

    @classmethod
    def clone(cls, src, path=None, overwrite=False):
        path = path or os.path.basename(src).rsplit('.git', maxsplit=1)[0]
        if os.path.exists(path) and overwrite:
            shutil.rmtree(path)
        assert not os.path.exists(path) or is_empty_dir(path)
        git.clone(src, path)
        return cls(path, src)

    @classmethod
    def openSpace(cls, path, remote_path=None):
        if not os.path.exists(path) or is_empty_dir(path):
            assert remote_path
            cls.clone(remote_path, path)
            repo = cls(path, path)
            return repo
        elif is_git_dir(path):
            return cls(path, remote_path)
        else:
            raise Exception('A non-empty directory %s already exists and it is not a git repo.' % (path))


class GitSpace(GitRepo, FakeOS):
    def __init__(self, path, remote_location=None):
        GitRepo.__init__(self, path, remote_location)
        FakeOS.__init__(self, path)


def open_default(path):
    url = 'https://OpenGitspace:Gitspace@123456@github.com/OpenGitspace/meta'
    return GitSpace.openSpace(path, remote_path=url)


def main():
    test()

    pass


def test():
    url=''
    # r=GitSpace.openSpace('MyCloudSpace',url)
    # r=GitSpace.openSpace('piudb',url)
    r = GitSpace.clone(url, overwrite=True)
    # f=r.open('testgit.txt','a')
    # f.write('hi\n')
    # f.close()
    r.pull()
    # r.push()


def demo():
    url="git://github.com/Peiiii/piudb"
    # git.clone(url)
    import os
    rpath = os.path.basename(url)
    open(rpath + '/testgit.txt', 'a').write('hi\n')
    r = Repo(rpath)
    git.add(r, rpath + '/testgit.txt')
    git.commit(r, b'sample commit')
    git.push(r, url, 'master')


if __name__ == '__main__':
    # demo()
    main()
