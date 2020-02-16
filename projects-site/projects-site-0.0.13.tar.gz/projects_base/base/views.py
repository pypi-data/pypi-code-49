import os
from projects_base.base import base_blueprint
from projects_base.base.conf import config
from flask import send_from_directory


@base_blueprint.route('/images/<path:filename>', methods=['GET'])
def img_render(filename):
    return send_from_directory(os.path.abspath(
        config.get('BASE', 'upload_folder')), filename=filename)
