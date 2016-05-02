from flask import Blueprint

log = Blueprint('log', __name__, url_prefix='/logs_info', template_folder='templates')
from . import views
