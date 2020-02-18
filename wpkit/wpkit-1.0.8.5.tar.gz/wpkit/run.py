
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
cli = CLI()
cli.demoapp = demoapp
cli.setup_default=setup_default
cli.install=install
cli.get_local_ip=get_local_ip
if __name__ == '__main__':
    import fire
    fire.Fire(cli)