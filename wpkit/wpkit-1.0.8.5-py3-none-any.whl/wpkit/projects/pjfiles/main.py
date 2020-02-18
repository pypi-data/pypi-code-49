# from wpkit.services.CloudOS import start_server
from wpkit.linux import clean_port,get_local_ip
from wpkit.web.applications.demo import demo,DemoApp,LocalFSServer,MyBlueprint

def main():
    app=DemoApp(__name__)
    clean_port(80)
    app.sitemap['Download']='http://%s:%s'%(get_local_ip(),8001)
    bp = MyBlueprint(url_prefix="/downloads", name="downloads", static_map={"/": "/var/www/html"})
    app.register_blueprint(bp)
    app.register_blueprint(LocalFSServer(nickname="ManageDownloads",url_prefix="/manage_download",path="/var/www/html"))
    app.run(host=get_local_ip(),port=80)
def test():
    from wpkit.linux import clean_port, get_local_ip
    from wpkit.web.applications.demo import demo, DemoApp, LocalFSServer, MyBlueprint
    app=DemoApp(__name__)
    app.sitemap['Download']='http://%s:%s'%(get_local_ip(),8001)
    app.register_blueprint(LocalFSServer(nickname="ManageDownloads",url_prefix="/manage_download",path="D:/work"))
    print(app.url_map)
    app.run(host=get_local_ip(),port=80)
if __name__ == '__main__':
    main()
    # test()
    # demo(host=get_local_ip(),port=80,import_name=__name__)