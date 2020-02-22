from .StoreItem import *
class ShadowStore:
    def __init__(self,path='.store.main',remote_location=None,cache_dir='.store.cache',sync_keys=False):
        remote_location=remote_location or default_remote_location
        self.path=path
        self.cache_dir=cache_dir
        self.remote_location=remote_location
        self.folder=StoreFolder.openStorefolder(self.path,remote_location=self.remote_location,remote_branch='empty')
        if sync_keys:
            self.sync_keys()
        print("Init shadow store finish.")
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

