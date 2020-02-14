from dulwich import porcelain as git
from dulwich.repo import Repo
from wpkit.fsutil.dir_dict import FakeOS
import os,shutil,glob
class errors:
    class GitSpaceError(Exception):
        def __init__(self,*args):
            super().__init__(*args)


def is_git_dir(path):
    if os.path.exists(path) and os.path.isdir(path):
        dot_git_dir=path+'/.git'
        if os.path.exists(dot_git_dir) and os.path.isdir(dot_git_dir):
            return True
    return False
def is_empty_dir(path):
    assert os.path.exists(path) and os.path.isdir(path)
    if len(os.listdir(path)):
        return False
    else:
        return True
class GitSpace(FakeOS):
    def __init__(self,path,remote_location=None):
        self.repo=Repo(path)
        self.remote_location=remote_location
        super().__init__(path)
    def pull(self,remote_location=None,branch='master'):
        remote_location = remote_location or self.remote_location
        if not remote_location:
            raise Exception('Remote location is not given.')
        repo=self.repo
        git.pull(repo,remote_location,branch)
        git.reset(repo,'hard')
    def push(self,remote_location=None,branch='master'):
        remote_location=remote_location or self.remote_location
        if not remote_location:
            raise Exception('Remote location is not given.')
        repo=self.repo
        git.add(repo,self.path)
        git.commit(repo,'bare gitspace commit')
        git.push(repo,remote_location,branch)
    @classmethod
    def init(cls,path):
        git.init(path)
        return cls(path)
    @classmethod
    def clone(cls,src,path=None,overwrite=False):
        path=path or os.path.basename(src).rsplit('.git',maxsplit=1)[0]
        if os.path.exists(path) and overwrite:
            shutil.rmtree(path)
        assert not os.path.exists(path) or is_empty_dir(path)
        git.clone(src,path)
        return cls(path,src)
    @classmethod
    def openSpace(cls,path,remote_path=None):
        if not os.path.exists(path) or is_empty_dir(path):
            assert remote_path
            cls.clone(remote_path,path)
            repo=cls(path,path)
            return repo
        elif is_git_dir(path):
            return cls(path,remote_path)
        else:
            raise Exception('A non-empty directory %s already exists and it is not a git repo.'%(path))










def main():
    test()

    pass
def test():
    # url='https://Peiiii:Wp@618001@github.com/Peiiii/MyCloudSpace'
    url='https://Peiiii:Wp@618001@github.com/Peiiii/piudb'
    # r=GitSpace.openSpace('MyCloudSpace',url)
    # r=GitSpace.openSpace('piudb',url)
    r=GitSpace.clone(url,overwrite=True)
    # f=r.open('testgit.txt','a')
    # f.write('hi\n')
    # f.close()
    r.pull()
    # r.push()

def demo():
    url = "https://Peiiii:Wp@618001@github.com/Peiiii/MyCloudSpace"
    # url="git://github.com/Peiiii/piudb"
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