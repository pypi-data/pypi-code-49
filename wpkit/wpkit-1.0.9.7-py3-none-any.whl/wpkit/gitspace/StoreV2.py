from .gitspace import GitSpace,open_default,default_remote_location,GitRepo,is_git_dir,FakeOS
from wpkit.fsutil import Folder,copy_file,copy_dir,copy_fsitem,remove_fsitem,is_empty_dir
from wpkit.piu import FileDict
from wpkit.basic import T,TMetaClass,CONST_TYPE
import os,shutil,glob,uuid,random
from wpkit.ofile import SimpleListFile
_T=CONST_TYPE
class CONST(metaclass=TMetaClass):
    remote_branch_list=_T()
    master=_T()
    empty=_T()

# TODO: improve performance

class ShadowStore:
    def __init__(self,path='.store.main',remote_location=None,cache_dir='.store.cache',sync_keys=False):
        remote_location=remote_location or default_remote_location
        self.path=path
        self.cache_dir=cache_dir
        self.remote_location=remote_location
        self.folder=StoreFolder.openStorefolder(self.path,remote_location=self.remote_location,remote_branch='empty')
        if sync_keys:
            self.sync_keys()
    def sync_keys(self):
        self.folder._pull_remote_branch_list(remote_location=self.remote_location,hard=True)
        return self.keys()
    def keys(self):
        return self.folder._read_remote_branch_list()
    def is_legal_key(self,key):
        legal_chars=StoreItem.legal_path_chars+['/']
        if StoreItem.delimiter in key:
            return False
        for ch in key:
            if not ch in legal_chars:
                return False
        return True
    def key_to_branch(self,key):
        assert self.is_legal_key(key)
        remote_branch = key.replace('/', StoreItem.delimiter)
        return remote_branch
    def get(self,key,path=None,overwrite=False):
        path=path or './'
        if os.path.exists(path):
            if os.path.isfile(path):
                if overwrite:
                    remove_fsitem(path)
                else:
                    raise FileExistsError('File %s already exists.'%(path))
            if os.path.isdir(path):
                tp=path+'/'+os.path.basename(key)
                if os.path.exists(tp):
                    if (os.path.isdir(tp) and not is_empty_dir(tp)) or os.path.isfile(tp):
                        if overwrite:
                            remove_fsitem(tp)
                        else:
                            raise FileExistsError('File %s already exists.' % (tp))
        remote_branch=self.key_to_branch(key)
        # print(remote_branch,self.keys())
        assert remote_branch in self.keys()
        # print("exporting... %s,%s"%(path,remote_branch))
        StoreItem.export(path,remote_location=self.remote_location,remote_branch=remote_branch)
        return True
    def set(self,key,path,recursive=False,add_more=None):
        remote_branch=self.key_to_branch(key)
        if not recursive:
            StoreItem.uploadStoreitem(path,remote_location=self.remote_location,remote_branch=remote_branch,cache_dir=self.cache_dir,add_more=add_more)
        else:
            StoreItem.uploadStoreitemRecursive(path,remote_location=self.remote_location,remote_branch=remote_branch,cache_dir=self.cache_dir)

_BRANCH_DICT='branch_dict'
_FAKE2TRUE='fake2true'
_TRUE2FAKE='true2fake'



class StoreItem(Folder):
    '''
    issue: Branch name has a limit
    '''
    delimiter='.-.'
    special_branches = ['master', 'empty', 'remote_branch_list']
    legal_path_chars = [str(i) for i in range(10)]+[chr(i) for i in range(65, 91)]+[chr(i) for i in range(97, 123)]+list('._-')
    def status(self,repo=None):
        repo=repo or self.repo
        from wpkit.basic import PointDict
        info=PointDict(
            current_branch=repo.active_branch(),
            local_branches=repo.branch_list(),
            status=repo.status()
        )
        print(info)
        return info
    def __init__(self,path,remote_location=None,remote_branch=None):
        remote_location = remote_location or default_remote_location
        assert remote_branch
        if not os.path.exists(path):
            os.makedirs(path)
        path=os.path.abspath(path)
        Folder.__init__(self,path)
        if is_git_dir(path):
            repo=GitRepo(path)
        else:
            repo=GitRepo.init(path)
        self.repo=repo
        self.path=path
        self.remote_location=remote_location or default_remote_location
        self.remote_branch=remote_branch
        self.data_list=['.git','.type.store'] # clean except
        self.info_list=['.git','.type.store','.more.store']  # copy except
        self.typefile=self.openFiledict('.type.store')

        self.init_branches()
    def _try_pull_remote(self):
        try:
            self._pull_remote()
        except:
            import logging
            logging.warning("Can't pull remote branch %s , maybe because local branch has already been updates."%(self.remote_branch))
    def _pull_remote(self):
        repo=self.repo
        repo.pull(self.remote_location,self.remote_branch)
    def _push_self(self):
        repo=self.repo
        repo.add_all()
        repo.commit()
        repo.push(self.remote_location,self.remote_branch)
    def _pull_else_push_self(self):
        remote_branch=self.remote_branch
        if not remote_branch in self._read_remote_branch_list():
            self._push_self()
        else:
            self._try_pull_remote()


    def _pull_remote_branch_list(self,repo=None,remote_location=None,remote_branch='remote_branch_list',hard=False):
        repo=repo or self.repo
        remote_location=remote_location or self.remote_location
        pull=False
        if not 'remote_branch_list' in repo.branch_list():
            repo.branch_create('remote_branch_list')
            pull=True
        if hard:
            pull=True
        if pull:
            try:
                br = repo.active_branch()
                repo.checkout_branch('remote_branch_list')
                repo.clean()
                repo.add_all()
                repo.commit()
                repo.pull(remote_location, branch=remote_branch)
                repo.checkout_branch(br)
            except:
                print("Can't pull remote_branch_list, maybe because local branch is already updated.")

    def init_branches(self,repo=None):
        '''
        A store repo has 3 branches: master , empty , remote_branch_list, remote_branch
        '''
        repo=repo or self.repo
        if not repo.branch_list():
            repo.commit() # create master
        if not 'empty' in repo.branch_list():
            repo.branch_create('empty')
            repo.checkout_branch('empty')
            repo.clean()
            repo.commit()
            repo.checkout_branch('master')
        if not self.remote_branch in repo.branch_list():
            repo.branch_create(self.remote_branch)
            repo.checkout_branch(self.remote_branch)
            repo.clean()
            repo.commit()
            repo.checkout_branch('master')
        self._pull_remote_branch_list(hard=False)
        repo.checkout_branch(self.remote_branch)

    def _read_remote_branch_list(self,pull=False):
        repo=self.repo
        br = repo.active_branch()
        repo.checkout_branch(CONST.remote_branch_list)
        if pull:
            self._pull_remote_branch_list(repo)
        lf = self.openSimplelistfile(CONST.remote_branch_list)
        li = lf.read()
        repo.checkout_branch(br)
        return li
    def _add_to_remote_branch_list(self,branch):
        repo=self.repo
        br=repo.active_branch()
        self._pull_remote_branch_list(hard=True)
        repo.checkout_branch(CONST.remote_branch_list)
        # repo.pull(self.remote_location,CONST.remote_branch_list)
        lf=self.openSimplelistfile(CONST.remote_branch_list)
        li=lf.read()
        # print("original:",li)
        li.append(branch)
        li=list(set(li))
        # print("now:",li)
        lf.write(li)
        repo.add_all()
        repo.commit()
        repo.push(self.remote_location,CONST.remote_branch_list)
        repo.checkout_branch(br)
    def iter_contentpath(self):
        lis=[]
        for name in self.listdir():
            if name in self.info_list:
                continue
            else:
                path=self.path+'/'+name
                lis.append(path)
        return lis
    def set_type(self,type):
        self.typefile.type=type
        return type
    def get_type(self):
        if not self.typefile.get('type'):
            return None
        return self.typefile.type
    @classmethod
    def pull(cls,remote_location=None,remote_branch=None,path=None,overwrite=False):
        remote_location=remote_location or default_remote_location
        remote_branch=remote_branch or 'master'
        if os.path.exists(path) and len(os.listdir(path)):
            if overwrite:
                shutil.rmtree(path)
            else:
                raise FileExistsError("Can't pull because folder %s is not empty."%(path))
        if not os.path.exists(path):
            os.makedirs(path)
        repo=GitRepo.init(path)
        if not repo.branch_list():
            repo.add_all()
            repo.commit()
        if not remote_branch in repo.branch_list():
            repo.branch_create(remote_branch)
            repo.checkout_branch(remote_branch)
            repo.clean()
        repo.pull(remote_location,branch=remote_branch)
        item=cls(repo.path,remote_location=remote_location,remote_branch=remote_branch)
        type=item.get_type()
        if not type:
            type=item.set_type(T.FOLDER)
            import logging
            logging.warning('StoreItem %s has no type, so we set it as %s'%(item.path,type))
        if type==T.FOLDER:
            return StoreFolder(repo.path,remote_location=remote_location,remote_branch=remote_branch)
        else:
            assert type==T.FILE
            return StoreFile(repo.path,remote_location=remote_location,remote_branch=remote_branch)
    @classmethod
    def openStorefolder(cls,path,remote_location=None,remote_branch=None,force_pull=False,overwrite=False):
        remote_location=remote_location or default_remote_location
        if not is_git_dir(path):
            force_pull=True
        if not force_pull:
            item=StoreFolder(path,remote_location=remote_location,remote_branch=remote_branch)
        else:
            item=StoreFolder.pull(remote_location=remote_location,remote_branch=remote_branch,path=path,overwrite=overwrite)
        return item
    @classmethod
    def openStorefile(cls,path,remote_location=None,remote_branch=None,force_pull=False,overwrite=False):
        remote_location=remote_location or default_remote_location
        if not is_git_dir(path):
            force_pull=True
        if not force_pull:
            item=StoreFile(path,remote_location=remote_location,remote_branch=remote_branch)
        else:
            item=StoreFile.pull(remote_location=remote_location,remote_branch=remote_branch,path=path,overwrite=overwrite)
        return item
    def upload(self,remote_location=None,remote_branch=None,overwrite=True):
        # Todo:get remote branch list
        # deprecated !!!
        remote_loacation=remote_location or self.remote_location
        remote_branch=remote_branch or self.remote_branch
        assert remote_loacation and remote_branch
        assert remote_branch !='master'
        repo=self.repo
        repo.add_all()
        repo.commit()
        # br=repo.active_branch()
        if not remote_branch in repo.branch_list():
            repo.branch_create(remote_branch)
        repo.checkout_branch(remote_branch)
        repo.push(remote_loacation,remote_branch)
        # repo.checkout_branch(br)
        if not remote_branch in self._read_remote_branch_list():
            self._add_to_remote_branch_list(remote_branch)
    @classmethod
    def export(cls,path,remote_branch,remote_location=default_remote_location,name=None,cache_dir='.tmp',overwrite=False):
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        def _export_dir(obj,path,cache_dir):
            for p in obj.iter_contentpath():
                copy_fsitem(p, path)
            more = obj.morefile.copy()
            # obj.rmself()
            for nm, br in more.items():
                br_cache_dir=cache_dir+'/'+br
                cls.export(path, remote_location=remote_location, remote_branch=br, name=nm, cache_dir=br_cache_dir,overwrite=overwrite)
        this_dir=cache_dir+'/.this'
        obj=StoreItem.pull(remote_location=remote_location,remote_branch=remote_branch,path=this_dir)
        name = name or remote_branch.split(cls.delimiter)[-1]
        if isinstance(obj,StoreFolder):
            if not os.path.exists(path):
                os.makedirs(path)
            assert os.path.isdir(path)
            path=path+'/'+name
            if os.path.exists(path):
                if overwrite:
                    shutil.rmtree(path)
                else:
                    raise Exception("Can't export to %s because path already existed and overwrite is not True")
            os.mkdir(path)
            _export_dir(obj,path,cache_dir)
        else:
            assert isinstance(obj,StoreFile)
            if os.path.exists(path):
                assert os.path.isdir(path)
                if name:
                    path=path+'/'+name
                ps=obj.iter_contentpath()
                ps.sort()
                p=ps[0]
                # path=path+'/'+os.path.basename(p)
                copy_fsitem(p, path)

            else:
                for p in obj.iter_contentpath():
                    copy_fsitem(p, path)
            # obj.rmself()
        # shutil.rmtree(cache_dir)
    @classmethod
    def uploadStoreitem(cls,path, remote_location, remote_branch, cache_dir,add_more=None):
        assert os.path.exists(path)
        if os.path.isdir(path):
            tmp = StoreFolder(cache_dir, remote_location=remote_location, remote_branch=remote_branch)
        else:
            tmp = StoreFile(cache_dir, remote_location=remote_location, remote_branch=remote_branch)
        tmp.clean()
        if os.path.isfile(path):
            tmp.eat(path)
        else:
            if add_more:
                for k,v in add_more.items():
                    tmp.addmore(k,v)
            for p in os.listdir(path):
                p = path + '/' + p
                tmp.eat(p)
        tmp.upload(remote_location=remote_location, remote_branch=remote_branch)
    @staticmethod
    def is_legal_path_to_upload(path):
        path=os.path.basename(path)
        legal_path_chars=StoreItem.legal_path_chars
        # print(legal_path_chars)
        if StoreItem.delimiter in path:
            import logging
            logging.warning('Illegal path "%s"!' % (path))
            return False
        for ch in path:
            if ch not in legal_path_chars:
                import logging
                logging.warning('Illegal path "%s"!'%(path))
                return False
        return True

    @classmethod
    def uploadStoreitemRecursive(cls,path, remote_location=None, remote_branch=None,
                                 cache_dir='.store.upload.cache',depth=-1,check_path=True):
        # todo: check branch name
        # assert remote_branch not in cls.special_branches
        assert depth>=0 or depth==-1
        assert os.path.exists(path)
        if check_path:
            assert cls.is_legal_path_to_upload(path)
        remote_location=remote_location or default_remote_location
        assert remote_branch
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        target_dir=cache_dir+'/target'
        store_dir=cache_dir+'/stores'
        os.makedirs(target_dir)
        copy_fsitem(path,target_dir)
        path=target_dir+'/'+os.path.basename(path)
        return cls._uploadStoreitemRecursive(path, remote_location, remote_branch, cache_dir=store_dir,depth=depth,check_path=check_path)
    @classmethod
    def _uploadStoreitemRecursive(cls,path, remote_location, remote_branch, cache_dir,depth=0,check_path=True):
        assert os.path.exists(path)
        if check_path:
            assert cls.is_legal_path_to_upload(path)
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        os.makedirs(cache_dir)
        print('path:',path)
        if depth==0:
            if os.path.isdir(path):

                tmp = StoreFolder(cache_dir, remote_location=remote_location, remote_branch=remote_branch)
                tmp.clean()
                for p in os.listdir(path):
                    p = path + '/' + p
                    tmp.eat(p)
            else:
                tmp = StoreFile(cache_dir, remote_location=remote_location, remote_branch=remote_branch)
                tmp.clean()
                tmp.eat(path)
        else:
            import uuid
            if os.path.isdir(path):
                self_cache_dir = cache_dir+'/self-cache-' + uuid.uuid4().hex
                more={}
                for name in os.listdir(path):
                    p=path+"/"+name
                    if check_path:
                        assert cls.is_legal_path_to_upload(p)
                    item_cache_dir=cache_dir+'/item-cache-'+name
                    os.mkdir(item_cache_dir)
                    item_branch=remote_branch+cls.delimiter+name
                    cls._uploadStoreitemRecursive(path=p,remote_location=remote_location,remote_branch=item_branch,cache_dir=item_cache_dir,depth=depth-1)
                    more[name]=item_branch
                os.mkdir(self_cache_dir)
                tmp = StoreFolder(self_cache_dir, remote_location=remote_location, remote_branch=remote_branch)
                tmp.morefile.update(more)
            else:
                tmp = StoreFile(cache_dir, remote_location=remote_location, remote_branch=remote_branch)
                tmp.clean()
                tmp.eat(path)
        tmp.upload(remote_location=remote_location, remote_branch=remote_branch)
        remove_fsitem(path)
    def is_empty(self):
        names=self.listdir()
        for name in names:
            if name not in self.data_list:
                return False
        return True
    def clean(self):
        names=self.listdir()
        for name in names:
            if name in self.data_list:
                continue
            self.remove(name)
            if name=='.more.store':
                self.openFiledict(name)

class StoreFolder(StoreItem):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.morefile = self.openFiledict('.more.store')
        self.set_type(T.FOLDER)
    def addmore(self,name,branch):
        self.morefile[name]=branch
    def eatStore(self,path,name=None,remote_location=None,remote_branch=None,upload=True,overwrite=False,cache_dir='.tmp',in_depth=0):
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        os.makedirs(cache_dir)
        assert os.path.exists(path)
        if not name:
            name=os.path.basename(os.path.abspath(path))
        remote_location = remote_location or self.remote_location
        assert remote_location
        if not remote_branch:
            assert self.remote_branch
            remote_branch=self.remote_branch+self.delimiter+name
        if upload:
            StoreItem.uploadStoreitem(path,remote_location=remote_location,remote_branch=remote_branch,cache_dir=cache_dir)
        self.morefile[name]=remote_branch

class StoreFile(StoreItem):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_type(T.FILE)

class Store:
    def __init__(self,path='.store.store',remote_location=None):
        cache_dir=path+'/.store.cache.store'
        if os.path.exists(path):
            shutil.rmtree(path)
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        os.makedirs(path)
        os.makedirs(cache_dir)
        self.ss=ShadowStore(path+'/.shadow.main.store',remote_location,cache_dir+'/.shadow.cache.store')
        self.bd=BranchDict(path+'/.branch_dict.store',remote_location=remote_location,remote_branch=_BRANCH_DICT)
        ss=self.ss
        ss.sync_keys()
        self.path=path
        self.remote_location=remote_location or default_remote_location
        self.cache_dir=cache_dir
    def _new_tmpfolder(self):
        name='.tmp.store-'+uuid.uuid4().hex
        return Folder(name)
    def _backup(self,path):
        folder = self._new_tmpfolder()
        folder.eat(path)
        return folder,folder._truepath(os.path.basename(path))
    def get(self,key,path=None,overwrite=False):
        ss=self.ss
        bd=self.bd
        tmp_dir='get-tmp-'+uuid.uuid4().hex
        os.makedirs(tmp_dir)
        # print('bd:',bd._read_fake2true_dict())
        name=os.path.basename(key)
        # if not path:
        #     path=name
        # print('path:',path)
        key=ss.key_to_branch(key)
        if not key in bd.fakes():
            bd._sync_dict()
            if not key in bd.fakes():
                raise KeyError('Key %s dose not exist.'%(key))
        true=bd.fake2true(key)
        ss.get(true,path=tmp_dir,overwrite=overwrite)
        src=glob.glob(tmp_dir+'/*')[0]
        if path:
            if not os.path.exists(path):
                path=path
            elif os.path.isfile(path):
                path=path
            else:
                path=path+'/'+name
        else:
            path=name
        dst=path
        os.rename(src,dst)
        shutil.rmtree(tmp_dir)
    def set(self,key,path,recursive=False):
        key=self.ss.key_to_branch(key)
        if recursive:
            self._set_recursive(key,path,self.cache_dir)
        else:
            self._set(key,path,self.cache_dir)
    def _set_recursive(self,key,path,cache_dir):
        assert os.path.isdir(path)
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        os.makedirs(cache_dir)
        folder, path = self._backup(path)
        cache_dir = folder.openFolder('.shadows.store').path

        fake = key
        bd = self.bd
        if fake in bd.fakes():
            true=bd.fake2true(fake)
            self._upload_recursive(path=path, remote_location=self.remote_location, fake=fake, true=true,
                                   cache_dir=cache_dir)
        else:
            true=bd._generate_hash(fake)
            self._upload_recursive(path=path,remote_location=self.remote_location,fake=fake,true=true,cache_dir=cache_dir)
            bd.set(fake,true)

    def _upload_recursive(self,path,remote_location,fake,true,cache_dir):
        '''
        key is not None, delete path after it finish
        set branchdict, and remove self
        '''
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        bd=self.bd
        if os.path.isfile(path):
            ss=ShadowStore(cache_dir+'/.remote_branch_list.store',remote_location=remote_location,cache_dir=cache_dir+'/.cache_repos.store',sync_keys=True)
            ss.set(true,path)
        else:
            more={}
            for name in os.listdir(path):
                p=path+'/'+name
                child_cache_dir=cache_dir+"/cache_dir-"+name
                chfake=bd._concat_fakes(fake,name)
                if chfake in bd.fakes():
                    chtrue=bd.fake2true(chfake)
                else:
                    chtrue=bd._generate_hash(chfake)
                self._upload_recursive(path=p,remote_location=remote_location,fake=chfake,true=chtrue,cache_dir=child_cache_dir)
                more[name]=chtrue
            self_cache_dir=cache_dir+'/self_cache_dir'
            ss=ShadowStore(self_cache_dir+'/.remote_branch_list.store',remote_location=remote_location,cache_dir=self_cache_dir+'/.cache_repos.store',sync_keys=True)
            ss.set(true,path,add_more=more)
        bd.set(fake, true)
        remove_fsitem(path)








    def _set(self,fake,path,cache_dir):
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        os.makedirs(cache_dir)
        ss=ShadowStore(cache_dir+'/.remote_branch_list.store',remote_location=self.remote_location,cache_dir=cache_dir+'/.cache_repos.store',sync_keys=True)
        bd=self.bd
        if fake in bd.fakes():
            true=bd.fake2true(fake)
            ss.set(true,path)
        else:
            true=bd._generate_hash(fake)
            ss.set(true,path)
            bd.set(fake,true)









class BranchDict(StoreFolder):
    def __init__(self,path,remote_location=None,remote_branch=None):
        remote_branch=remote_branch or _BRANCH_DICT
        super().__init__(path,remote_location,remote_branch)
        self._init_branch_dict()
    def _init_branch_dict(self):
        '''
        Make sure we have local branch dict same with remote one.
        '''
        self._try_pull_remote()
        # print("bd:", self._read_fake2true_dict())
        self._read_remote_branch_list(pull=True)
        self._pull_else_push_self()
        # self._try_pull_remote()
        # print("bd:", self._read_fake2true_dict())
        if self.is_empty():
            self.openFiledict(_FAKE2TRUE)
            self.openFiledict(_TRUE2FAKE)
            self._push_self()
        # print("bd:", self._read_fake2true_dict())
    def _sync_dict(self):
        return self._try_pull_remote()
    def _concat_fakes(self,parent,fake):
        return parent+StoreFolder.delimiter+fake
    def _generate_hash(self,fake):
        import hashlib
        m=hashlib.md5()
        def gen():
            m.update(fake.encode('utf-8'))
            return m.hexdigest()[:10]
        while True:
            true=gen()
            if not true in self.trues():
                return true

    def _update_branch_dict(self,fake,true):
        self._try_pull_remote()
        fake2true=self._read_fake2true_dict()
        true2fake=self._read_true2fake_dict()
        fake2true[fake]=true
        true2fake[true]=fake
        self._push_self()
    def true(self,fake):
        if fake in self.fakes():
            return self.fake2true(fake)
        else:
            true=self._generate_hash(fake)
            self.set(fake,true)
            return true
    def _read_fake2true_dict(self):
        return self.openFiledict(_FAKE2TRUE)
    def _read_true2fake_dict(self):
        return self.openFiledict(_TRUE2FAKE)
    def fake2true(self,fake):
        return self._read_fake2true_dict()[fake]
    def true2fake(self,true):
        return self._read_true2fake_dict()[true]
    def trues(self):
        return self._read_true2fake_dict().keys()
    def fakes(self):
        return self._read_fake2true_dict().keys()
    def set(self,fake,true):
        return self._update_branch_dict(fake,true)
