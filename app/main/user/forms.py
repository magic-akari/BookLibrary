# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, URL
from flask_pagedown.fields import PageDownField
from flask_wtf.file import FileField, FileAllowed
from app import avatars


class EditProfileForm(FlaskForm):
    name = StringField(u'用户名', validators=[DataRequired(message=u"该项忘了填写了!"), Length(1, 64, message=u"长度为1到64个字符")])
    major = StringField(u'主修专业', validators=[Length(0, 128, message=u"长度为0到128个字符")])
    headline = StringField(u'一句话介绍自己', validators=[Length(0, 32, message=u"长度为32个字符以内")])
    about_me = PageDownField(u"个人简介")
    submit = SubmitField(u"保存更改")


class AvatarEditForm(FlaskForm):
    avatar_url = StringField('', validators=[Length(1, 100, message=u"长度限制在100字符以内"), URL(message=u"请填写正确的URL")])
    submit = SubmitField(u"保存")


class AvatarUploadForm(FlaskForm):
    avatar = FileField('', validators=[FileAllowed(avatars, message=u"只允许上传图片")])
