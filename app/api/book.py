from app.models import Book as model_Book
from flask import url_for
from flask_restful import Resource, marshal_with, abort
from . import api, parser, default_per_page
from .fields import book_detail_fields, book_list


@api.route('/books/<int:book_id>/')
class Book(Resource):
    @marshal_with(book_detail_fields)
    def get(self, book_id):
        book = model_Book.query.get_or_404(book_id)
        if book.hidden:
            abort(404)
        return book


@api.route('/books/')
class BookList(Resource):
    @marshal_with(book_list)
    def get(self):
        args = parser.parse_args()
        page = args['page'] or 1
        per_page = args['per_page'] or default_per_page
        pagination = model_Book.query.paginate(page=page, per_page=per_page)
        items = pagination.items
        prev = None
        if pagination.has_prev:
            prev = url_for('api.booklist', page=page - 1, count=per_page, _external=True)
        next = None
        if pagination.has_next:
            next = url_for('api.booklist', page=page + 1, count=per_page, _external=True)
        return {
            'items': items,
            'prev': prev,
            'next': next,
            'total': pagination.total,
            'pages_count': pagination.pages,
            'current_page': pagination.page,
            'per_page': per_page,
        }
