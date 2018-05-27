from app.models import Log as model_Log
from flask import url_for
from flask_restful import Resource, marshal_with
from . import api, parser, default_per_page
from .fields import logs_info_detail_fields, logs_info_list


@api.route('/logs_info/<int:log_id>/')
class Log(Resource):
    @marshal_with(logs_info_detail_fields)
    def get(self, log_id):
        return model_Log.query.get_or_404(log_id)


@api.route('/logs_info/')
class LogList(Resource):
    @marshal_with(logs_info_list)
    def get(self):
        parser.add_argument('user_id', type=int, location='args')
        parser.add_argument('book_id', type=int, location='args')
        parser.add_argument('returned', type=int, location='args')
        args = parser.parse_args()
        page = args['page'] or 1
        per_page = args['per_page'] or default_per_page
        log_query = model_Log.query
        user_id = args['user_id']
        book_id = args['book_id']
        returned = args['returned']
        if user_id is not None:
            log_query = log_query.filter_by(user_id=user_id)
        if book_id is not None:
            log_query = log_query.filter_by(book_id=book_id)
        if returned is not None:
            log_query = log_query.filter_by(returned=returned)
        pagination = log_query.paginate(page=page, per_page=per_page)
        items = pagination.items
        prev = None
        if pagination.has_prev:
            prev = url_for('api.loglist', page=page - 1, per_page=per_page, _external=True)
        next = None
        if pagination.has_next:
            next = url_for('api.loglist', page=page + 1, per_page=per_page, _external=True)
        return {
            'items': items,
            'prev': prev,
            'next': next,
            'total': pagination.total,
            'pages_count': pagination.pages,
            'current_page': pagination.page,
            'per_page': per_page
        }
