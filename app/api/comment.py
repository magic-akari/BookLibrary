from app.models import Comment as model_Comment
from flask import url_for
from flask_restful import Resource, marshal_with, abort
from . import api, parser, default_per_page
from .fields import comment_detail_fields, comment_list


@api.route('/comments/<int:comment_id>/')
class Comment(Resource):
    @marshal_with(comment_detail_fields)
    def get(self, comment_id):
        comment = model_Comment.query.get_or_404(comment_id)
        if comment.deleted:
            abort(404)
        return comment


@api.route('/comments/')
class CommentList(Resource):
    @marshal_with(comment_list)
    def get(self):
        parser.add_argument('book_id', type=int, location='args')
        parser.add_argument('user_id', type=int, location='args')
        parser.add_argument('deleted', type=int, location='args')
        args = parser.parse_args()
        page = args['page'] or 1
        per_page = args['per_page'] or default_per_page
        comment_query = model_Comment.query

        user_id = args['user_id']
        book_id = args['book_id']

        # searching deleted comments are not allowed
        # Todo: administrator can access this

        deleted = 0

        if user_id is not None:
            comment_query = comment_query.filter_by(user_id=user_id)
        if book_id is not None:
            comment_query = comment_query.filter_by(book_id=book_id)
        if deleted is not None:
            comment_query = comment_query.filter_by(deleted=deleted)

        pagination = comment_query.order_by(model_Comment.id.desc()).paginate(page=page, per_page=per_page)
        items = pagination.items
        prev = None
        if pagination.has_prev:
            prev = url_for('api.commentlist', page=page - 1, per_page=per_page, _external=True)
        next = None
        if pagination.has_next:
            next = url_for('api.commentlist', page=page + 1, per_page=per_page, _external=True)
        return {
            'items': items,
            'prev': prev,
            'next': next,
            'total': pagination.total,
            'pages_count': pagination.pages,
            'current_page': pagination.page,
            'per_page': per_page,
        }
