import types
from flask import Blueprint
from flask_restful import Api, reqparse


def api_route(self, *args, **kwargs):
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls

    return wrapper


default_per_page = 5
parser = reqparse.RequestParser()
parser.add_argument('per_page', type=int, location='args')
parser.add_argument('page', type=int, location='args')

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)

api.route = types.MethodType(api_route, api)

from . import user, book, comment, log, tag
