from flask import Blueprint, request
from flask_graphql import GraphQLView

from .schema import schema

##__________________________________________________________________||
bp = Blueprint('graphql', __name__)

bp.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema, graphiql=True, ))

##__________________________________________________________________||
def init_app(app):
    app.register_blueprint(bp)

##__________________________________________________________________||
