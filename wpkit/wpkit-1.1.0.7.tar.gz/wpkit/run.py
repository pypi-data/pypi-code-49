
from wpkit.web.applications.demo import demo as demoapp
from wpkit.projects.setup import setup_default
from wpkit.install import install_requirements as install
from wpkit.web.applications.all import BlogServer
from wpkit.linux import get_local_ip

class CLI:
    def blog(self,port=80,host=None,data_path='./'):
        if not host:
            host=get_local_ip()
        bs=BlogServer(import_name=__name__,url_prefix='/',default_root_path=data_path)
        bs.run(host=host,port=port)

    @classmethod
    def request_download(cls,url):
        from wpkit.more import Remote
        remote=Remote()
        return remote.request(url)
    @classmethod
    def download(cls,fn,out='./'):
        from wpkit.more import Remote
        remote=Remote()
        return remote.download(fn,out)
    @classmethod
    def downtee(cls, key, path=None, overwrite=False):
        from wpkit.gitspace import Store
        store = Store()
        store.get(key, path=path, overwrite=overwrite)

    @classmethod
    def uptee(cls, key, path, recursive=False):
        from wpkit.gitspace import Store
        store = Store()
        store.set(key, path, recursive)


cli = CLI()
cli.demoapp = demoapp
cli.setup_default=setup_default
cli.install=install
cli.get_local_ip=get_local_ip
if __name__ == '__main__':
    import fire
    fire.Fire(cli)