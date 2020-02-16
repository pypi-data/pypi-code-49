from flask import Blueprint
from projects_base.base.conf import config

base_blueprint = Blueprint('projects_base', __name__,
                           static_folder='static',
                           static_url_path='/base/static',
                           template_folder='templates')
import projects_base.base.views
