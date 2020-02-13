from marshmallow import Schema, fields

from serializer.user_schema import UserSchema


class StatusSchema(Schema):
    id = fields.Integer()
    type = fields.String()
    date = fields.String()
    date_created = fields.String()
    date_modified = fields.String()
    hours = fields.String()
    comment = fields.String()
    is_all_day = fields.Boolean()
    user_id = fields.String()
    user = fields.Nested(
        UserSchema,
        only=["id", "first_name", "last_name"]
    )
