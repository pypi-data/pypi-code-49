from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    HiddenField,
    SelectField,
    SelectMultipleField
)
from wtforms.validators import DataRequired, ValidationError, Optional
from flask_mde import MdeField
from wtforms.validators import InputRequired, Length
from ctrlv_client.app.models import Snippet


class LoginForm(FlaskForm):
    username = StringField(
        validators=[DataRequired()]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class MdeForm(FlaskForm):
    # You can now as of WTForms 2.1 (December 2015) set rendering keywords
    # by using the `render_kw=` parameter to the field constructor.
    # https://stackoverflow.com/questions/9749742/
    # python-wtforms-can-i-add-a-placeholder-attribute-when-i-init-a-field
    title = StringField(
        validators=[
            DataRequired(),
            Length(min=2, max=255)
        ],
        render_kw={
            "placeholder": "",
            "class": "form-control form-control-sm mr-1"

        }
    )
    editor = MdeField(
        validators=[
            InputRequired("Input required"),
            Length(min=15, max=30000)
        ]
    )
    tags = HiddenField(
        render_kw={
            "value": ""
        }
    )
    tagbox = StringField(
        render_kw={
            "placeholder": "",
            "autocomplete": "off"
        }
    )
    submit = SubmitField(
        'Submit',
        render_kw={
            "class": "btn btn btn-outline-primary btn-sm"
        }
    )


class DeleteForm(FlaskForm):
    snippet_id = HiddenField()
    submit = SubmitField('Delete')

    def validate_snippet_id(form, field):
        if not Snippet.query.filter_by(snippet_id=field.data).first():
            raise ValidationError('No snippet with given id')


class FilterForm(FlaskForm):
    search = StringField(
        validators=[
            Optional(strip_whitespace=True),
            Length(max=255)
        ],
        render_kw={"placeholder": "search text"}
    )
    sort = SelectField(
        'Sort',
        # [(value, label) ..]
        choices=[('latest', 'Latest'), ('oldest', 'Oldest')]
    )
    limit = SelectField(
        'Limit',
        # [(value, label) ..]
        choices=[('10', '10'), ('30', '30'), ('50', '50')]
    )
    tags = SelectMultipleField(
        'Tags',
        render_kw={
            'class': 'selectpicker1',
            'data-size': '5',
            'data-live-search': 'true',
            'data-actions-box': 'true',
            'data-selected-text-format': 'count > 2',
            'data-header': 'Select Tags',
            'data-none-selected-text': 'No Tags',
            'data-select-all-text': 'All Tags',
            'multiple': 'multiple'
        }
        # choices=[]
    )
    # do not name 'submit'
    # onchange="this.form.submit()"
    # will not work
    # https://stackoverflow.com/questions/833032/
    # submit-is-not-a-function-error-in-javascript
    btnsubmit = SubmitField('Search')
