# Custom Schemas Go Here

from grahamcracker import DataSchema, schema_for
from marshmallow import validates, ValidationError
from typing import Any

from .models import Name, Enemy


@schema_for(Name)
class NameSchema(DataSchema[Name]):
    """
    Schema for :class:`isleservice_objects.models.Name`. Validates that:

        * No spaces in first or last name
    """

    @validates("first")
    def no_spaces_first(self, value: str, **kwargs: Any) -> None:
        if " " in value:
            raise ValidationError("'first' cannot contain spaces")

    @validates("last")
    def no_spaces_last(self, value: str, **kwargs: Any) -> None:
        if " " in value:
            raise ValidationError("'last' cannot contain spaces")


@schema_for(Enemy)
class EnemySchema(DataSchema[Enemy]):
    pass
