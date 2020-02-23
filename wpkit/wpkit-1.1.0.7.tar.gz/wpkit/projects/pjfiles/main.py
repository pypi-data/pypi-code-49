from wpkit.web.base import Application
from wpkit.web.applications.all import *
from wpkit.linux import *
from wpkit.pkg_info import *
if __name__ == '__main__':
    ip = get_local_ip()
    port = 80
    clean_port(port)
    app = Application(__name__)
    app.register_blueprint(BlogServer())
    app.register_blueprint(
        BluePostAndDownload(data_dir='data/post_and_download' if is_windows() else '/root/data/post_and_download'))
    app.register_blueprint(BlueWelcomePage(url_prefix='/'))
    print(app.url_map)
    app.run(
        host=ip, port=port
    )