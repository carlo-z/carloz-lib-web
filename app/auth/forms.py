#!/usr/bin/python
#-*-coding:utf-8-*-
from wtforms import StringField, SubmitField, BooleanField, PasswordField, RadioField, ValidationError
from wtforms.validators import Required, Length, Email, EqualTo, NoneOf

from flask.ext.wtf import Form
from app.models import User
from app.main.res import values


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember Me', default=False)
    submit = SubmitField('Log In')

class RegistForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    password2 = PasswordField('Confirm password', validators=[Required(),
                                                              EqualTo('password', message='Password must match')])
    unique_domain = StringField('My domamin', validators=[Required(), Length(1, 64),
                                                          NoneOf(values.Regist.forbid_domain_list)])
    nikename = StringField('Nike name', validators=[Required()])
    storage_type = RadioField('Cloud Storage Type',
                              choices=[(u'qiniu', u'QiNiu'), (u'bcs', u'BCS'), (u'sae', u'SAE')], default=u'qiniu')
    access_key = StringField('Access Key', validators=[Required()])
    secret_key = StringField('Secret Key', validators=[Required()])
    bucket_name = StringField('Bucket Name', validators=[Required()])
    download_url = StringField('Download Url', validators=[Required()])
    submit = SubmitField('Register')
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

