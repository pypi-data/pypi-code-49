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

def to_string_iterable(iterable):
    lis=[s.decode() if isinstance(s,bytes) else s for s in iterable]
    return iterable.__class__(lis)
class GitRepo:
    def __init__(self, path, remote_location=None):
        self.repo = Repo(path)
        self.path = os.path.abspath(path)
        self.remote_location = remote_location
        if not 'empty' in self.branch_list():
            self.branch_create('empty')
            br=self.active_branch()
            self.checkout_branch('empty')
            self.clean()
            self.stage()
            git.commit(self.repo,'empty')
            self.checkout_branch(br)
        self.git=git
    def clean(self):
        for name in os.listdir(self.path):
            if name=='.git':continue
            path=self.path+'/'+name
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
    def active_branch(self):
        return git.active_branch(self.repo).decode()
    def checkout_branch(self,branch='master'):
        git.update_head(self.repo,branch)
        self.clean()
        co_ref = b'HEAD'
        repo_path=self.path
        from dulwich.repo import Repo
        from dulwich.index import build_index_from_tree
        repo = Repo(repo_path)
        indexfile = repo.index_path()
        obj_sto = repo.object_store
        tree_id = repo[co_ref].tree
        build_index_from_tree(repo_path, indexfile, obj_sto, tree_id)
        x=list(obj_sto.iter_tree_contents(tree_id))
        x=[obj_sto.iter_tree_contents(tree_id)]
        # self.clean()
    def branch_create_empty(self, name):
        br=self.active_branch()
        self.checkout_branch('empty')
        self.branch_create(name)
        self.checkout_branch(br)
    def branch_create(self,name):
        repo=self.repo
        git.branch_create(repo,name)
    def pull(self, remote_location=None, branch='master'):
        remote_location = remote_location or self.remote_location
        if not remote_location:
            raise Exception('Remote location is not given.')
        repo = self.repo
        git.pull(repo, remote_location, branch)
        self.checkout_branch(branch)
        git.reset(repo, 'hard')
    def branch_list(self):
        return list(to_string_iterable(git.branch_list(self.repo)))
    def status(self,silent=False):
        repo = self.repo
        msg = git.status(repo)
        if not silent:
            print(msg)
        return msg
    def stage(self):
        repo = self.repo
        paths = list(git.get_untracked_paths(self.path, repo.path, repo.open_index()))
        paths += list(git.get_unstaged_changes(repo.open_index(), self.path))
        paths = [p.decode() if isinstance(p, bytes) else p for p in paths]
        paths = [self.path + '/' + p for p in paths]
        print('paths to add:',paths)
        if not paths:
            import logging
            logging.warning('Working tree is clean. Nothing to add.')
            return
        paths.append(self.path)
        git.add(repo, paths)
    def push(self, remote_location=None, branch=None):
        branch=branch or self.active_branch() or 'master'
        remote_location = remote_location or self.remote_location
        if not remote_location:
            raise Exception('Remote location is not given.')
        repo = self.repo
        self.stage()
        git.commit(repo, 'bare gitspace commit')
        git.push(repo, remote_location, branch)

    @classmethod
    def init(cls, path):
        git.init(path)
        return cls(path)

    @classmethod
    def clone(cls, src, path=None, overwrite=False,branch='master'):
        path = path or os.path.basename(src).rsplit('.git', maxsplit=1)[0]
        if os.path.exists(path) and overwrite:
            shutil.rmtree(path)
        assert not os.path.exists(path) or is_empty_dir(path)
        git.clone(src, path)
        repo=cls(path, src)
        repo.pull(branch=branch)
        return repo

    @classmethod
    def openSpace(cls, path, remote_path=None,branch='master'):
        if not os.path.exists(path) or is_empty_dir(path):
            assert remote_path
            cls.clone(remote_path, path,branch=branch)
            repo = cls(path, remote_path)
            return repo
        elif is_git_dir(path):
            return cls(path, remote_path)
        else:
            raise Exception('A non-empty directory %s already exists and it is not a git repo.' % (path))


class GitSpace(GitRepo, FakeOS):
    def __init__(self, path, remote_location=None):
        GitRepo.__init__(self, path, remote_location)
        FakeOS.__init__(self, path)


def open_default(path,branch='master'):
    # url = 'https://OpenGitspace:Gitspace@123456@github.com/OpenGitspace/meta'
    url = 'https://OpenGitspace:Gitspace@123456@gitee.com/OpenGitspace/meta'
    return GitSpace.openSpace(path, remote_path=url,branch=branch)


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
