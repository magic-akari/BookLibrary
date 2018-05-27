from app.models import Tag as model_Tag
from flask import url_for
from flask_restful import Resource, marshal_with
from . import api, parser, default_per_page
from .fields import tag_detail_fields, tag_list


@api.route('/books/tags/<int:tag_id>/')
class Tag(Resource):
    @marshal_with(tag_detail_fields)
    def get(self, tag_id):
        tag = model_Tag.query.get_or_404(tag_id)
        tag.uri = url_for('api.tag', tag_id=tag.id, _external=True)
        return tag


@api.route('/books/tags/')
class TagList(Resource):
    @marshal_with(tag_list)
    def get(self):
        args = parser.parse_args()
        page = args['page'] or 1
        per_page = args['per_page'] or default_per_page
        pagination = model_Tag.query.paginate(page=page, per_page=per_page)
        items = pagination.items
        prev = None
        if pagination.has_prev:
            prev = url_for('api.taglist', page=page - 1, per_page=per_page, _external=True)
        next = None
        if pagination.has_next:
            next = url_for('api.taglist', page=page + 1, per_page=per_page, _external=True)
        return {
            'items': items,
            'prev': prev,
            'next': next,
            'total': pagination.total,
            'pages_count': pagination.pages,
            'current_page': pagination.page,
            'per_page': per_page,
        }
