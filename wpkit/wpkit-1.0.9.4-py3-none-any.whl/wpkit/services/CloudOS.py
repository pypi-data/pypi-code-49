import threading
def run_server1(import_name,host,port=80):
    import wpkit
    from wpkit.web.applications.all import BluePan
    from wpkit.web import MyBlueprint
    app = wpkit.web.get_default_app(import_name)

    bp_pan = pan.BluePan(import_name)

    app.add_blueprint(bp_pan)

    print(app.url_map)
    print(app.sitemap)
    app.run(port=port,host=host)
def run_server2(import_name,host,port=8002):
    from wpkit.services import LocalFSServer

    app = LocalFSServer(import_name, path="./")
    print(app.url_map)
    app.run(port=port,host=host)

def start_server(import_name,host='127.0.0.1',port1=80,port2=8002):
    t1 = threading.Thread(target=run_server1,args=[import_name,host,port1])
    t2 = threading.Thread(target=run_server2,args=[import_name,host,port2])
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    start_server(__name__)