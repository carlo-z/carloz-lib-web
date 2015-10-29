#!/usr/bin/python
# -*-coding:utf-8-*-

from wtforms import StringField, SubmitField, RadioField, TextAreaField
from wtforms.validators import Required

from flask.ext.wtf import Form
from res import values, strings


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

class ArticleEditForm(Form):
    title = StringField(strings().admin_article_edit.article_title, validators=[Required()])
    editor_code = StringField(strings().admin_article_edit.article_editor, validators=[Required()],
                              default=values.EditorCode.UEditor)
    body = TextAreaField(strings().admin_article_edit.article_body, validators=[Required()])
    tag_list = StringField(strings().admin_article_edit.article_tags, validators=[Required()])
    access_level = RadioField('', choices=[('private', strings().admin_article_edit.private),
                                           ('public', strings().admin_article_edit.public),
                                           ('by_password', strings().admin_article_edit.by_password)], default='private')
    access_pw = StringField('')

class SearchForm(Form):
    keywords = StringField('keywords')
