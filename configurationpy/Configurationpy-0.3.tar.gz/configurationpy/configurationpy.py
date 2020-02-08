import os, errno, shutil, json, yaml
class Confpy:
    """Main class for Conf.py that contains all methods"""
    def __init__(self, db):
        self.db = db
        self.dotname = "." + db
        try: os.makedirs(self.dotname)
        except FileExistsError: pass

    @classmethod
    def access(cls, db):
        if os.path.isdir("." + db):
            cls.db = db
            cls.dotname = '.' + db
            return cls(db)
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), "." + db)

    def mkcfg(self, filename, content = "", prepend_newline = False, append_newline = False, jsonencode = False, yamlencode = False):
        if jsonencode == True: content = json.dumps(content)
        if yamlencode == True: content = yaml.dump(content)
        if prepend_newline == True:
            content = "\n" + content
        elif append_newline == True:
            content = content + "\n"
        with open(os.path.join(self.dotname, filename), 'w+') as f:
            f.write(content)
            f.close()
    
    def writecfg(self, filename, content = "", prepend_newline = True, append_newline = False, jsonencode = False, yamlencode = False):
        if jsonencode == True: content = json.dumps(content)
        if yamlencode == True: content = yaml.dump(content)
        if prepend_newline == True:
            content = "\n" + content
        elif append_newline == True:
            content = content + "\n"
        with open(os.path.join(self.dotname, filename), 'a+') as f:
            f.write(content)
            f.close()

    def exist(self, filename):
        return os.path.exists(os.path.join(self.dotname, filename))

    def mknested(self, nd):
        try: os.makedirs(os.path.join(self.dotname, nd))
        except FileExistsError: pass

    def readcfg(self, filename, jsonencode = False, yamlencode = False):
        f = open(os.path.join(self.dotname, filename))
        output = f.read()
        f.close()
        if jsonencode == True: output = json.loads(output)
        if yamlencode == True: output = yaml.load(output, Loader=yaml.FullLoader)
        return output
    
    def rmcfg(self, filename):
        try: os.remove(os.path.join(self.dotname, filename))
        except FileNotFoundError: pass

    def rmnested(self, dirname):
        try: shutil.rmtree(os.path.join(self.dotname, dirname))
        except FileNotFoundError: pass
    
    def rmdb(self):
        try: shutil.rmtree(self.dotname)
        except FileNotFoundError: pass