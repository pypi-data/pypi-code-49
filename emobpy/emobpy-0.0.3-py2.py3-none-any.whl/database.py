import time
import pickle
import gzip
import os
import uuid


class DataBase(object):
    """docstring for DataBase."""

    def __init__(self, folder):
        super(DataBase, self).__init__()

        self.name = ''
        self.folder = folder
        self.oldpath = []
        self.db = {}

    def loadfiles(self, loaddir=''):
        if loaddir:
            self.repo = loaddir
        else:
            self.repo = self.folder
        os.makedirs(self.repo, exist_ok=True)
        self.currentpath = [f for f in os.listdir(self.repo) if os.path.isfile(os.path.join(self.repo, f))]
        self.path_list = list(set(self.currentpath) - set(self.oldpath))
        if self.path_list:
            self.oldpath = self.currentpath

        for f in self.path_list:
            self.fpath = os.path.join(self.repo, f)
            if f.split('.')[-1] == 'pickle':
                self.pickle_off = gzip.open(self.fpath, "rb")
                self.obj = pickle.load(self.pickle_off)
                self.pickle_off.close()
                self.db[self.obj['name']] = self.obj
                del self.pickle_off

    def update(self):
        self.loadfiles()

    def getdb(self):
        self.update()
        return self.db

    def remove(self, name):
        self.acum = []
        self.db.pop(name, None)
        if os.path.isfile(os.path.join(self.folder, name+'.pickle')):
            os.remove(os.path.join(self.folder, name+'.pickle'))
            self.acum.append(name + '.pickle')
        self.update()
        print('Files deleted:', len(self.acum))
        print(self.acum)
        del self.acum


class DataManager:
    ''' docstring DataManager '''

    def __init__(self):
        super(DataManager, self).__init__()

    def savedb(self, object, dbdir='db_files'):
        object.update()
        if not object.name:
            nnn = 'db_' + time.strftime("%Y%m%d_%H%M%S") + '_' + uuid.uuid4().hex[:5]  # + time.strftime("%Y%m%d_%H%M%S")
            object.name = nnn[:]
        os.makedirs(dbdir, exist_ok=True)
        with gzip.open(os.path.join(dbdir, object.name + '.pickle'), 'wb') as datei:
            pickle.dump(object, datei)
        print(datei)
        print('=== Database saved ===')

    def loaddb(self, dbfilepath, profilesdir):
        with gzip.open(dbfilepath, 'rb') as datei:
            obj = pickle.load(datei)
        obj.folder = profilesdir
        obj.update()
        return obj
