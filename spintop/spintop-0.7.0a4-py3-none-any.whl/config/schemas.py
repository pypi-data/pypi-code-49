from marshmallow import Schema, fields, pprint


# class SpinhubProfile(Schema):
#     name = fields.String()
#     machine_id = fields.String(allow_none=True)
#     org_id = fields.String(allow_none=True)
#     spinhub_url = fields.String()
    
# class SpintopMachineConfig(Schema):
#     default_profile = fields.String(default='default')
#     profiles = fields.Nested(SpinhubProfile(), many=True)
    
    
from marshmallow import Schema, fields, pprint
from uuid import getnode

from ..auth.schemas import CredentialsSchema

class SpinhubProfile(Schema):
    credentials_key = fields.String(allow_none=True)
    spinhub_url = fields.String(allow_none=True)
    
class SpintopMachineConfig(Schema):
    """
    hardware_uuid: xxxxxxxx
    credentials:
        1234:
            access_token:
            refresh_token:
            username:
    
    """
    default_profile = fields.String(default='default')
    hardware_uuid = fields.String(default=getnode)
    profiles = fields.Dict(keys=fields.Str(), values=fields.Nested(SpinhubProfile()))
    credentials = fields.Dict(keys=fields.Str(), values=fields.Nested(CredentialsSchema()))
    