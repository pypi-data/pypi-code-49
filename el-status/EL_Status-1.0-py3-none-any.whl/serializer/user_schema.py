from marshmallow import Schema, fields, post_load


class UserSchema(Schema):
    id = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    picture = fields.String()
    email = fields.String()
