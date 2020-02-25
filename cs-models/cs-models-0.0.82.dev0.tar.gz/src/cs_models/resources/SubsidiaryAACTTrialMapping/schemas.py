from marshmallow import (
    Schema,
    fields,
    validate,
)


class SubsidiaryAACTTrialResourceSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    id = fields.Integer(dump_only=True)
    nct_id = fields.String(required=True, validate=not_blank)
    subsidiary_id = fields.Integer(required=True)
    updated_at = fields.DateTime(dump_only=True)


class SubsidiaryAACTTrialQueryParamsSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    id = fields.Integer()
    nct_id = fields.String(validate=not_blank)
    subsidiary_id = fields.Integer()
