import uuid

import factory
from django.db.models import *
from django.utils import timezone
from factory.django import DjangoModelFactory

_global_sequence_counter = 0


class ModelFieldSequence(factory.LazyFunction):
    def __init__(self, model=None, max_length: int = None, string: str = None):
        assert not (model and string), 'You cannot specify both `model` and `string`, but only one of them'
        assert not model and string or model and not string, 'You must specify either `model` or `string`'
        self.string = string
        self.model = model
        self.max_length = max_length

    def __set_name__(self, owner, field_name: str):
        value = f'{self.model._meta.object_name}__{field_name}' if self.model else self.string
        try:
            super().__init__(self.fn(value, self.max_length))
        except:
            super().__init__(self.fn(self.string, self.max_length))

    @staticmethod
    def fn(string, max_length):
        def inner_fn():
            global _global_sequence_counter
            _global_sequence_counter += 1
            value = f'{string}-{_global_sequence_counter}'
            if max_length:
                # truncate from left so that varying part remains included
                offset = len(value) - max_length
                value = value[offset:]
            return value

        return inner_fn


def _integer_mapper(field, start=1) -> int:
    return factory.Sequence(lambda n: n + start)


def _text_mapper(field):
    max_length = field.max_length if hasattr(field, 'max_length') else None
    return ModelFieldSequence(field.model, max_length)


_related_model_cache = {}


def _foreignkey_mapper(field):
    if field.related_model not in _related_model_cache.keys():
        _related_model_cache[field.related_model] = factory.SubFactory(
            create_populated_modelfactory(field.related_model))
    return _related_model_cache[field.related_model]


def _not_implemented(field):
    raise NotImplementedError(
        f'"{field.__class__}" in not yet supported unless it has `blank=True`')


def _add_geodjango_types_to_fieldmapper():
    from django.contrib.gis.db.models.fields import PointField
    from django.contrib.gis.geos import Point

    # FIXME create something unique
    MODEL_FIELD_TO_FACTORY_FIELD_MAPPER[PointField] = lambda field: Point(10, 10)


MODEL_FIELD_TO_FACTORY_FIELD_MAPPER = {
    # text
    SlugField: _text_mapper,  # FIXME This might not really be a slug
    CharField: _text_mapper,
    TextField: _text_mapper,
    EmailField: lambda field: ModelFieldSequence(string=f'{field.model.__name__}@email.io'),
    URLField: lambda field: ModelFieldSequence(string=f'https://{field.model.__name__}.ee/a'),
    # integers
    PositiveIntegerField: _integer_mapper,
    PositiveSmallIntegerField: _integer_mapper,
    SmallIntegerField: _integer_mapper,
    IntegerField: _integer_mapper,
    BigIntegerField: _integer_mapper,
    # other number fields
    DecimalField: _integer_mapper,
    FloatField: _integer_mapper,
    # date and time
    DateField: lambda field: factory.LazyFunction(timezone.localdate),
    DateTimeField: lambda field: factory.LazyFunction(timezone.now),
    DurationField: lambda field: factory.LazyFunction(datetime.timedelta(days=7)),
    TimeField: lambda field: factory.LazyFunction(timezone.now),
    # file fields
    FileField: lambda field: _not_implemented(field),
    ImageField: lambda field: _not_implemented(field),
    FilePathField: lambda field: _not_implemented(field),
    # relational fields
    ForeignKey: _foreignkey_mapper,
    ManyToManyField: lambda field: _not_implemented(field),
    OneToOneField: _foreignkey_mapper,
    # boolean fields
    BooleanField: lambda field: True,
    NullBooleanField: lambda field: True,
    # autofields
    BigAutoField: lambda field: _not_implemented(field),
    AutoField: lambda field: _not_implemented(field),
    # other
    BinaryField: lambda field: ModelFieldSequence(field.model).encode('utf-8'),
    GenericIPAddressField: lambda field: '192.0.2.30',  # FIXME create something unique
    UUIDField: lambda field: uuid.uuid4(),
}


def create_populated_modelfactory(model_cls, fieldmapper=None, create_override=None, **kwargs):
    """
    Currently cannot handle ManyToMany and ForeignKey to 'self' and FileField 

    modelfactory_with_fields_factory(Customer, name='John')
    modelfactory_with_fields_factory(Customer, { DateField: lambda field: None }, name='John')
    """
    if fieldmapper:
        fieldmapper = {**MODEL_FIELD_TO_FACTORY_FIELD_MAPPER, **fieldmapper}
    else:
        fieldmapper = MODEL_FIELD_TO_FACTORY_FIELD_MAPPER

    class Meta:
        model = model_cls

    # create class fields
    class_dict = {'Meta': Meta}
    if create_override:
        class_dict['_create'] = classmethod(create_override)
    for field in model_cls._meta.fields:
        if field.name == 'id' and 'id' not in kwargs:
            continue

        if field.__class__ in (ForeignKey, OneToOneField) and field.related_model == model_cls:
            if field.blank:
                class_dict[field.name] = None
                kwargs.pop(field.name, None)
            else:
                raise NotImplementedError('We cannot handle ForeignKey or OneToOneField fields '
                                          'to "self" which do not have "blank=True"')
            continue

        # import GeoDjango types only when needed to avoid their GIS library dependencies
        if field.__class__.__module__.startswith('django.contrib.gis'):
            _add_geodjango_types_to_fieldmapper()

        try:
            class_dict[field.name] = (kwargs.pop(field.name) if field.name in kwargs
                                      else fieldmapper[field.__class__](field))
        except NotImplementedError:
            if field.blank:
                class_dict[field.name] = None
            else:
                raise

    assert not kwargs, f'All keyord arguments must correspond to model fields. Unexpected keyword argument(s): {", ".join(kwargs.keys())}'
    # create class
    return type(f'{model_cls.__name__}Factory', (DjangoModelFactory,), class_dict)
