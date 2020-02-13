from flask import Blueprint
from flask_restplus import Api


def create_api():
    api = Api()
    return api

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
