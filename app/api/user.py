from app.models import User as model_User
from flask import url_for
from flask_restful import Resource, marshal_with
from . import api, parser, default_per_page
from .fields import user_detail_fields, user_list


@api.route('/users/<int:user_id>/')
class User(Resource):
    @marshal_with(user_detail_fields)
    def get(self, user_id):
        user = model_User.query.get_or_404(user_id)
        user.uri = url_for('api.user', user_id=user_id, _external=True)
        return user


@api.route('/users/')
class UserList(Resource):
    @marshal_with(user_list)
    def get(self):
        args = parser.parse_args()
        page = args['page'] or 1
        per_page = args['per_page'] or default_per_page
        pagination = model_User.query.order_by(model_User.id.desc()).paginate(page=page, per_page=per_page)
        items = pagination.items
        prev = None
        if pagination.has_prev:
            prev = url_for('api.userlist', page=page - 1, per_page=per_page, _external=True)
        next = None
        if pagination.has_next:
            next = url_for('api.userlist', page=page + 1, per_page=per_page, _external=True)
        return {
            'items': items,
            'prev': prev,
            'next': next,
            'total': pagination.total,
            'pages_count': pagination.pages,
            'current_page': pagination.page,
            'per_page': per_page
        }
