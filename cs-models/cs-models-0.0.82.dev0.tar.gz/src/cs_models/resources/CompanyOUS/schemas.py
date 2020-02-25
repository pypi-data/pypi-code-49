from marshmallow import (
    Schema,
    fields,
    validate,
)


class CompanyOUSResourceSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=not_blank)
    ticker = fields.String(allow_none=True)
    exchange = fields.String(allow_none=True)
    updated_at = fields.DateTime(dump_only=True)


class CompanyOUSQueryParamsSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    id = fields.Integer()
    name = fields.String(validate=not_blank)
    ticker = fields.String(validate=not_blank)
