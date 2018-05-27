# -*- coding:utf-8 -*-
from app.models import Book
from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import ValidationError
from wtforms.validators import Length, DataRequired, Regexp


class EditBookForm(FlaskForm):
    isbn = StringField(u"ISBN",
                       validators=[DataRequired(message=u"该项忘了填写了!"),
                                   Regexp('[0-9]{13,13}', message=u"ISBN必须是13位数字")])
    title = StringField(u"书名",
                        validators=[DataRequired(message=u"该项忘了填写了!"), Length(1, 128, message=u"长度为1到128个字符")])
    origin_title = StringField(u"原作名", validators=[Length(0, 128, message=u"长度为0到128个字符")])
    subtitle = StringField(u"副标题", validators=[Length(0, 128, message=u"长度为0到128个字符")])
    author = StringField(u"作者", validators=[Length(0, 128, message=u"长度为0到64个字符")])
    translator = StringField(u"译者",
                             validators=[Length(0, 64, message=u"长度为0到64个字符")])
    publisher = StringField(u"出版社", validators=[Length(0, 64, message=u"长度为0到64个字符")])
    image = StringField(u"图片地址", validators=[Length(0, 128, message=u"长度为0到128个字符")])
    pubdate = StringField(u"出版日期", validators=[Length(0, 32, message=u"长度为0到32个字符")])
    tags = StringField(u"标签", validators=[Length(0, 128, message=u"长度为0到128个字符")])
    pages = IntegerField(u"页数")
    price = StringField(u"定价", validators=[Length(0, 64, message=u"长度为0到32个字符")])
    binding = StringField(u"装帧", validators=[Length(0, 16, message=u"长度为0到16个字符")])
    numbers = IntegerField(u"馆藏", validators=[DataRequired(message=u"该项忘了填写了!")])
    summary = PageDownField(u"内容简介")
    catalog = PageDownField(u"目录")
    submit = SubmitField(u"保存更改")


class AddBookForm(EditBookForm):
    def validate_isbn(self, filed):
        if Book.query.filter_by(isbn=filed.data).count():
            raise ValidationError(u'已经存在相同的ISBN,无法录入,请仔细核对是否已库存该书籍.')


class SearchForm(FlaskForm):
    search = StringField(validators=[DataRequired()])
    submit = SubmitField(u"搜索")


