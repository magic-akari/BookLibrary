from flask import Blueprint

comment = Blueprint('comment', __name__, url_prefix='/comments')
from . import views
