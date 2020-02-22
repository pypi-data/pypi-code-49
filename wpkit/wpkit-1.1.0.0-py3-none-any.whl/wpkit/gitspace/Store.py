from .StoreItem import *
from .ShadowStore import *
from .helpers import *


_BRANCH_DICT='branch_dict'
_FAKE2TRUE='fake2true'
_TRUE2FAKE='true2fake'

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
        if overwrite and os.path.exists(dst) and os.path.isfile(dst):
            os.remove(dst)
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


