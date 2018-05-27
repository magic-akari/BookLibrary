# -*- coding:utf-8 -*-
from app import db
from app.models import Book, Log, Permission
from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_required, current_user
from . import log
from ..decorators import permission_required


@log.route('/borrow/')
@login_required
@permission_required(Permission.BORROW_BOOK)
def book_borrow():
    book_id = request.args.get('book_id')
    the_book = Book.query.get_or_404(book_id)
    if the_book.hidden and not current_user.is_administrator():
        abort(404)

    result, message = current_user.borrow_book(the_book)
    flash(message, 'success' if result else 'danger')
    db.session.commit()
    return redirect(request.args.get('next') or url_for('book.detail', book_id=book_id))


@log.route('/return/')
@login_required
@permission_required(Permission.RETURN_BOOK)
def book_return():
    log_id = request.args.get('log_id')
    book_id = request.args.get('book_id')
    the_log = None
    if log_id:
        the_log = Log.query.get(log_id)
    if book_id:
        the_log = Log.query.filter_by(user_id=current_user.id, book_id=book_id).first()
    if log is None:
        flash(u'没有找到这条记录', 'warning')
    else:
        result, message = current_user.return_book(the_log)
        flash(message, 'success' if result else 'danger')
        db.session.commit()
    return redirect(request.args.get('next') or url_for('book.detail', book_id=log_id))


@log.route('/')
@login_required
def index():
    show = request.args.get('show', 0, type=int)
    if show != 0:
        show = 1

    page = request.args.get('page', 1, type=int)
    pagination = Log.query.filter_by(returned=show).order_by(Log.borrow_timestamp.desc()).paginate(page, per_page=10)
    logs = pagination.items
    return render_template("logs_info.html", logs=logs, pagination=pagination, title=u"借阅信息")
