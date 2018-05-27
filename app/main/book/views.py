# -*- coding:utf-8 -*-
from app import db
from app.models import Book, Log, Comment, Permission, Tag, book_tag
from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import current_user
from . import book
from .forms import SearchForm, EditBookForm, AddBookForm
from ..comment.forms import CommentForm
from ..decorators import admin_required, permission_required


@book.route('/')
def index():
    search_word = request.args.get('search', None)
    search_form = SearchForm()
    page = request.args.get('page', 1, type=int)

    the_books = Book.query
    if not current_user.can(Permission.UPDATE_BOOK_INFORMATION):
        the_books = Book.query.filter_by(hidden=0)

    if search_word:
        search_word = search_word.strip()
        the_books = the_books.filter(db.or_(
            Book.title.ilike(u"%%%s%%" % search_word), Book.author.ilike(u"%%%s%%" % search_word), Book.isbn.ilike(
                u"%%%s%%" % search_word), Book.tags.any(Tag.name.ilike(u"%%%s%%" % search_word)), Book.subtitle.ilike(
                u"%%%s%%" % search_word))).outerjoin(Log).group_by(Book.id).order_by(db.func.count(Log.id).desc())
        search_form.search.data = search_word
    else:
        the_books = Book.query.order_by(Book.id.desc())

    pagination = the_books.paginate(page, per_page=8)
    result_books = pagination.items
    return render_template("book.html", books=result_books, pagination=pagination, search_form=search_form,
                           title=u"书籍清单")


@book.route('/<book_id>/')
def detail(book_id):
    the_book = Book.query.get_or_404(book_id)

    if the_book.hidden and (not current_user.is_authenticated or not current_user.is_administrator()):
        abort(404)

    show = request.args.get('show', 0, type=int)
    page = request.args.get('page', 1, type=int)
    form = CommentForm()

    if show in (1, 2):
        pagination = the_book.logs.filter_by(returned=show - 1) \
            .order_by(Log.borrow_timestamp.desc()).paginate(page, per_page=5)
    else:
        pagination = the_book.comments.filter_by(deleted=0) \
            .order_by(Comment.edit_timestamp.desc()).paginate(page, per_page=5)

    data = pagination.items
    return render_template("book_detail.html", book=the_book, data=data, pagination=pagination, form=form,
                           title=the_book.title)


@book.route('/<int:book_id>/edit/', methods=['GET', 'POST'])
@permission_required(Permission.UPDATE_BOOK_INFORMATION)
def edit(book_id):
    book = Book.query.get_or_404(book_id)
    form = EditBookForm()
    if form.validate_on_submit():
        book.isbn = form.isbn.data
        book.title = form.title.data
        book.origin_title = form.origin_title.data
        book.subtitle = form.subtitle.data
        book.author = form.author.data
        book.translator = form.translator.data
        book.publisher = form.publisher.data
        book.image = form.image.data
        book.pubdate = form.pubdate.data
        book.tags_string = form.tags.data
        book.pages = form.pages.data
        book.price = form.price.data
        book.binding = form.binding.data
        book.numbers = form.numbers.data
        book.summary = form.summary.data
        book.catalog = form.catalog.data
        db.session.add(book)
        db.session.commit()
        flash(u'书籍资料已保存!', 'success')
        return redirect(url_for('book.detail', book_id=book_id))
    form.isbn.data = book.isbn
    form.title.data = book.title
    form.origin_title.data = book.origin_title
    form.subtitle.data = book.subtitle
    form.author.data = book.author
    form.translator.data = book.translator
    form.publisher.data = book.publisher
    form.image.data = book.image
    form.pubdate.data = book.pubdate
    form.tags.data = book.tags_string
    form.pages.data = book.pages
    form.price.data = book.price
    form.binding.data = book.binding
    form.numbers.data = book.numbers
    form.summary.data = book.summary or ""
    form.catalog.data = book.catalog or ""
    return render_template("book_edit.html", form=form, book=book, title=u"编辑书籍资料")


@book.route('/add/', methods=['GET', 'POST'])
@permission_required(Permission.ADD_BOOK)
def add():
    form = AddBookForm()
    form.numbers.data = 3
    if form.validate_on_submit():
        new_book = Book(
            isbn=form.isbn.data,
            title=form.title.data,
            origin_title=form.origin_title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            translator=form.translator.data,
            publisher=form.publisher.data,
            image=form.image.data,
            pubdate=form.pubdate.data,
            tags_string=form.tags.data,
            pages=form.pages.data,
            price=form.price.data,
            binding=form.binding.data,
            numbers=form.numbers.data,
            summary=form.summary.data or "",
            catalog=form.catalog.data or "")
        db.session.add(new_book)
        db.session.commit()
        flash(u'书籍 %s 已添加至图书馆!' % new_book.title, 'success')
        return redirect(url_for('book.detail', book_id=new_book.id))
    return render_template("book_edit.html", form=form, title=u"添加新书")


@book.route('/<int:book_id>/delete/')
@permission_required(Permission.DELETE_BOOK)
def delete(book_id):
    the_book = Book.query.get_or_404(book_id)
    the_book.hidden = 1
    db.session.add(the_book)
    db.session.commit()
    flash(u'成功删除书籍,用户已经无法查看该书籍', 'info')
    return redirect(request.args.get('next') or url_for('book.detail', book_id=book_id))


@book.route('/<int:book_id>/put_back/')
@admin_required
def put_back(book_id):
    the_book = Book.query.get_or_404(book_id)
    the_book.hidden = 0
    db.session.add(the_book)
    db.session.commit()
    flash(u'成功恢复书籍,用户现在可以查看该书籍', 'info')
    return redirect(request.args.get('next') or url_for('book.detail', book_id=book_id))


@book.route('/tags/')
def tags():
    search_tags = request.args.get('search', None)
    page = request.args.get('page', 1, type=int)
    the_tags = Tag.query.outerjoin(book_tag).group_by(book_tag.c.tag_id).order_by(
        db.func.count(book_tag.c.book_id).desc()).limit(30).all()
    search_form = SearchForm()
    search_form.search.data = search_tags

    data = None
    pagination = None

    if search_tags:
        tags_list = [s.strip() for s in search_tags.split(',') if len(s.strip()) > 0]
        if len(tags_list) > 0:
            the_books = Book.query
            if not current_user.can(Permission.UPDATE_BOOK_INFORMATION):
                the_books = Book.query.filter_by(hidden=0)
            the_books = the_books.filter(
                db.and_(*[Book.tags.any(Tag.name.ilike(word)) for word in tags_list])).outerjoin(Log).group_by(
                Book.id).order_by(db.func.count(Log.id).desc())
            pagination = the_books.paginate(page, per_page=8)
            data = pagination.items

    return render_template('book_tag.html', tags=the_tags, title='Tags', search_form=search_form, books=data,
                           pagination=pagination)
