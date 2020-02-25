from marshmallow import Schema, fields

class CredentialsSchema(Schema):
    username = fields.String()
    access_token = fields.String()
    refresh_token = fields.String()
    org_id = fields.String(allow_none=True)
    refresh_module = fields.String()
    
credentials_schema = CredentialsSchema()