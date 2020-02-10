from flask import (
    render_template,
    Blueprint,
    redirect,
    url_for,
    request,
    flash,
    current_app
)
from flask_login import current_user
from ctrlv_client.app.models import Tag
from ctrlv_client.app.tag.forms import (
    UpdateTagForm,
    TagFilterForm
)
from ctrlv_client.app.helpers import (
    error_flasher
)
from ctrlv_client.app import db, SITE_CONFIG_FILE
import os

tag = Blueprint(
    'tag',
    __name__,
    template_folder='templates/tag',
    url_prefix='/tag'
)


@tag.before_request
def before_request():
    # flask_login.login_required not used
    # dynamic reloading
    # https://flask-login.readthedocs.io/en/latest/#protecting-views
    if (
        not current_user.is_authenticated and
        os.path.isfile(SITE_CONFIG_FILE) and
        request.endpoint != 'main.login'
    ):
        return current_app.login_manager.unauthorized()


@tag.route('/', methods=['GET', 'POST'])
def tags():
    tag_search_form = TagFilterForm()
    tag_forms = []
    tags = Tag.query.all()
    if tag_search_form.validate_on_submit():
        tags = Tag.query.filter(
            Tag.tag_name.like('%' + tag_search_form.search.data + '%')
        ).all()
    for tag in tags:
        tag_forms.append(
          UpdateTagForm(
              tag_id=tag.tag_id,
              tag_name=tag.tag_name
            )
        )
    return render_template(
        'tag/tags.html',
        tag_forms=tag_forms,
        tag_search_form=tag_search_form
    )


@tag.route('/<int:tag_id>', methods=['POST'])
def edit_tag(tag_id):
    form = UpdateTagForm()
    if form.validate_on_submit():
        this_tag = Tag.query.get(tag_id)
        if form.delete.data:
            db.session.delete(this_tag)
            flash("Tag deleted successfully!")
        if form.update.data:
            this_tag.tag_name = form.tag_name.data.lower()
            flash("Tag edited successfully!")
        db.session.commit()
    error_flasher(form)
    return redirect(
        url_for('tag.tags')
    )
