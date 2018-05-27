# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length, DataRequired


class CommentForm(FlaskForm):
    comment = TextAreaField(u"你的书评",
                            validators=[DataRequired(message=u"内容不能为空"), Length(1, 1024, message=u"书评长度限制在1024字符以内")])
    submit = SubmitField(u"发布")
