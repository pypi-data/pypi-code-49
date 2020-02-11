'''
requirements:
Linux with wget installed.
'''
from wpkit.web import utils,resources
from flask import request
from wpkit.web.base import MyBlueprint
class BluePostAndDownload(MyBlueprint):
    def __init__(self,import_name=None,name='PostAndDownload',data_dir='/var/www/html',url_prefix='/post_and_download',**kwargs):
        super().__init__(name=name,import_name=import_name,url_prefix=url_prefix,**kwargs)
        self.data_dir=data_dir
        assert utils.pkg_info.is_linux()
        import wpkit.linux as pylinux
        @self.route('/', methods=['GET'])
        def do_post_get():
            return utils.render(resources.get_default_template_string('post'))
        @self.route('/', methods=['POST'])
        def do_post_post():
            data = request.get_json()
            url = data['url']
            print('get url: %s' % url)
            pylinux.tools.wget_download(url, out_dir=self.data_dir)
            return 'seccess'
