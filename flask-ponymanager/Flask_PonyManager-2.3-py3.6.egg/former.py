import datetime
from wtforms import Form
from typing import (
    Type,
    List,

)
from pony.orm import (
    PrimaryKey,
    Required,
    Optional,
    Set,
    db_session
)
from pony.orm.core import Entity
from wtforms import (
    SubmitField,
    StringField,
    IntegerField,
    FloatField,
    BooleanField,
    HiddenField,
    SelectField,
    SelectMultipleField,
)
from wtforms.fields.html5 import (
    DateField,
    DateTimeField
)
from wtforms.validators import DataRequired

EntityList = List[Entity]

column_types = [Required, Optional, PrimaryKey, Set]

type_mapping = {
    #   Standard types
    str: StringField,
    int: IntegerField,
    float: FloatField,
    bool: BooleanField,

    #   Dates, times
    datetime.date: DateField,
    datetime.datetime: DateTimeField,

    #   Select, Select multiple
    Entity: SelectField,
    EntityList: SelectMultipleField,

    #   Specials and default
    'primary_key': HiddenField,
    'default': StringField
}

unsupported_types = list()


class EntityForm(Form):
    with_primary_keys: bool = None


class EntityFormer:
    def __init__(self, entity: Type[Entity]):
        self.entity = entity
        self.date_format = '%d/%m/%Y'
        self.datetime_format = self.date_format + ' %H:%M:%S'

    def columns(self) -> dict:
        """
        Get entity columns.
        """
        columns = dict()
        for key, value in self.entity.__dict__.items():
            if key is not '_pk_' and type(value) in column_types:
                columns[key] = value
        return columns

    def primary_keys(self) -> List[str]:
        """
        List of names of primary keys.
        """
        return [key for key, value in self.columns().items() if value.is_pk]

    def primary_key(self) -> str:
        """
        First primary key.
        """
        return self.primary_keys()[0]

    def get_form(self, add_primary_keys: bool = True, add_submit: bool = True) -> Type[EntityForm]:
        """
        Generate form for entity.
        """

        class GeneratedEntityForm(EntityForm):
            with_primary_keys = add_primary_keys

        for name, column in self.columns().items():
            #   Skip unsupported
            if column.py_type in unsupported_types:
                continue

            field_kwargs = dict(
                label=name,
                validators=list()
            )

            #   Building list of validators.
            if column.is_required and column.py_type not in [bool, EntityList]:
                field_kwargs['validators'].append(DataRequired())

            #   Getting input class.
            if column.is_pk:
                if add_primary_keys:
                    #   Hidden
                    form_input_class = type_mapping['primary_key']
                else:
                    continue
            elif column.is_relation:
                #   Relations
                form_input_class = type_mapping[EntityList] if column.is_collection else type_mapping[Entity]
            else:
                #   Type by type mapping
                form_input_class = type_mapping[column.py_type] if column.py_type in type_mapping.keys() \
                    else type_mapping['default']

            #   Filling select fields choices.
            if column.is_relation:
                with db_session:
                    field_kwargs['choices'] = [
                        (str(getattr(entity, self.primary_key())), str(entity))
                        for entity in column.py_type.select()
                    ]
            #   Date, time formats
            elif column.py_type is datetime.date:
                field_kwargs['format'] = self.date_format
            elif column.py_type is datetime.datetime:
                field_kwargs['format'] = self.datetime_format

            setattr(GeneratedEntityForm, name, form_input_class(**field_kwargs))

        if add_submit:
            setattr(GeneratedEntityForm, 'submit', SubmitField('Submit'))

        return GeneratedEntityForm

    def fill_form(self, entity_form: Type[EntityForm], entity_row: Entity) -> EntityForm:
        """
        Fill entity form with values from entity.
        """
        form_values = dict()
        for name, column in self.columns().items():
            if not entity_form.with_primary_keys and column.is_pk:
                continue
            elif column.is_relation:
                #   Get relation primary keys.
                form_values[name] = [str(getattr(row, self.primary_key())) for row in column.py_type.select()]
            else:
                form_values[name] = getattr(entity_row, name)
        return entity_form(**form_values)

    def get_form_values(self, form: EntityForm) -> dict:
        """
        Process data from (posted) form.
        """
        #   Get form values
        form_values = dict()
        for name, column in self.columns().items():
            if not form.with_primary_keys and column.is_pk:
                continue
            try:
                data = getattr(form, name).data
                if column.is_relation:
                    if column.is_collection:
                        #   Get primary keys values and retype them
                        selected = [
                            self.columns()[self.primary_key()].py_type(value) for value in data or list()
                        ]
                        #   Get entities by primary keys
                        data = [column.py_type.get(**{self.primary_key(): key}) for key in selected]
                    else:
                        selected = self.columns()[self.primary_key()].py_type(data)
                        data = column.py_type.get(**{self.primary_key(): selected})
                #   Dates
                elif column.py_type is datetime.date:
                    data = datetime.datetime.strptime(data, self.date_format)
                elif column.py_type is datetime.datetime:
                    data = datetime.datetime.strptime(data, self.datetime_format)
                form_values[name] = data
            #   Don't know why this happens :(
            except KeyError:
                pass
        return form_values

    def update_entity_from_form(self, form: EntityForm) -> Entity:
        """
        Update database row with form values.
        """
        form_values = self.get_form_values(form)
        #   Get primary keys
        select_by = {key: form_values.pop(key) for key in self.primary_keys()}
        with db_session:
            #   Get entity row
            row = self.entity.get(**select_by)
            #   Update entity
            for key, value in form_values.items():
                setattr(row, key, value)
        return row

    def add_entity_from_form(self, form: EntityForm) -> Entity:
        """
        Add database row with from values.
        """
        return self.entity(**self.get_form_values(form))
