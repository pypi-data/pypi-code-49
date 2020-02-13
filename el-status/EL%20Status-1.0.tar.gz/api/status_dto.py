from flask_restplus import fields

from extensions import api


class StatusDTO:
    namespace = api.namespace('status')
    status = api.model('status', {
        'id': fields.Integer(required=True, description="The status id"),
        'type': fields.String(required=True, description="The status type"),
        'date': fields.String(required=True, description="The status date"),
        'date_created': fields.String(required=True, description="The status id"),
        'date_modified': fields.String(required=True, description="The status id"),
        'hours': fields.String(required=True, description="The status hours"),
        'comment': fields.String(required=True, description="The status commnet"),
        'is_all_day': fields.Boolean(required=True, description="The status is all day"),
        'user_id': fields.String(required=True, description="The user id")
    })