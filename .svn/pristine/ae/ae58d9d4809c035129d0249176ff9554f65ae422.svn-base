#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

from flask import render_template, redirect, url_for, request, flash

from flask.ext.login import login_user, logout_user, login_required
from app import db
from app.models import User, QiniuStorage
from app.auth import auth
from app.auth.forms import LoginForm, RegistForm
from app.main.res import strings

reload(sys)
sys.setdefaultencoding('utf-8')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        loginer = User.query.filter_by(email=loginForm.email.data).first()
        # print 'auth.view - login: verify_password = %s' % loginer.verify_password(form_passwd=loginForm.password.data)
        if loginer is not None and loginer.verify_password(form_passwd=loginForm.password.data):
            # flash('loginer is not null and verfy it success')
            login_user(loginer, loginForm.remember_me.data)
            # flash('login_user success, next = ' + request.args.get('next'))
            return redirect(request.args.get('next') or url_for('main.admin'))
        flash('Invalid username or password')
    return render_template('auth/login.html', strs=strings(), form=loginForm)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    # flash('You have been logged out')
    return redirect(request.args.get('prev') or url_for('main.index'))

@auth.route('/regist', methods=['GET', 'POST'])
def regist():
    registForm = RegistForm()
    if registForm.validate_on_submit():
        try:
            register = User(
                email=registForm.email.data,
                password=registForm.password.data,
                unique_domain=registForm.unique_domain.data,
                nikename=registForm.nikename.data,
                storage_type=registForm.storage_type.data
            )
            db.session.add(register)
            db.session.commit()
            if 'qiniu' == registForm.storage_type.data:
                storage_cloud = QiniuStorage(
                    owner_id=register.id,
                    access_key=registForm.access_key.data,
                    secret_key=registForm.secret_key.data,
                    bucket_name=registForm.bucket_name.data,
                    use_flag='Y',  # Y: on use, N: not use
                    download_url=registForm.download_url.data
                )
                db.session.add(storage_cloud)
                db.session.commit()
            flash('Regist success.')
            return redirect(url_for('auth.login'))
        except:
           flash('Occur exception, regist fail. please try again')
    return render_template('auth/regist.html', strs=strings(), form=registForm)





