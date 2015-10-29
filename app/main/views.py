#!/usr/bin/python
# -*-coding:utf-8-*-
import sys
import os
import re
import json
from datetime import datetime

from flask import request, make_response, render_template, session, redirect, url_for, current_app, flash, jsonify

from bs4 import BeautifulSoup

from flask.ext.login import login_required, current_user
from app import db, models
from app.main import main, controller
from app.main.czlog import CzLog
from app.main.forms import *
from app.main.uploader import Uploader
from res import values, strings

reload(sys)
sys.setdefaultencoding('utf-8')
czLog = CzLog()
logger = czLog.get_logger()
ctl_current_user = controller.CtlCurrentUser(current_user, request)

@main.route('/', methods=['GET', 'POST'])
def index():
    # nav_list = ('Android', 'Linux', 'Web', 'Cloud Computing')
    return render_template('index.html', strs=strings())

@main.route('/search', methods=['GET', 'POST', 'OPTIONS'])
@main.route('/search/', methods=['GET', 'POST', 'OPTIONS'])
def search():
    # print('main.search - 1')
    keywords = ('%s' % request.args.get('keywords', '')).strip()
    session['keywords'] = ('%s' % keywords)
    # print('main.search - keywords = %s' % keywords)
    if keywords is not None and '' != keywords:
        # print('main.search - 2')
        keywords = '%' + ('%s' % keywords).strip() + '%'
        # print('main.search - keywords = %s' % keywords)
        try:
            articleList = models.Article.query.filter(db.or_(
                models.Article.tag_list.like(keywords), models.Article.title.like(keywords))).all()
            return render_template('default/page_search_result.html',
                                   strs=strings(),
                                   keywords=session.get('keywords', ''), articleList=articleList)
        except Exception, e:
            logger.fatal("main.search - keywords=%s, err=%s" % (keywords, e))
    return render_template('default/page_search_result.html', strs=strings())

@main.route('/tag/', methods=['GET', 'POST', 'OPTIONS'])
def tag_search():
    tag_name = ('%s' % request.args.get('tag_name', '')).strip()
    # print('main.search - keywords = %s' % keywords)
    if tag_name is not None and '' != tag_name:
        return redirect(url_for('main.search', keywords=tag_name))
    return redirect('#')

@main.route('/upload', methods=['GET', 'POST', 'OPTIONS'])
def upload():
    """UEditor文件上传接口
    config 配置文件
    result 返回结果
    """
    mimetype = 'application/json'
    result = {}
    action = request.args.get('action')
    # 解析JSON格式的配置文件
    with open(os.path.join(current_app.static_folder, 'plug-in/ueditor', 'php', 'config.json')) as fp:
        try:
            # 删除 `/**/` 之间的注释
            CONFIG = json.loads(re.sub(r'\/\*.*\*\/', '', fp.read()))
        except:
            CONFIG = {}
    if action == 'config':
        # 初始化时，返回配置文件给客户端
        result = CONFIG
    elif action in ('uploadimage', 'uploadfile', 'uploadvideo'):
        # 图片、文件、视频上传
        if action == 'uploadimage':
            fieldName = CONFIG.get('imageFieldName')
            config = {
                "pathFormat": CONFIG['imagePathFormat'],
                "maxSize": CONFIG['imageMaxSize'],
                "allowFiles": CONFIG['imageAllowFiles']
            }
        elif action == 'uploadvideo':
            fieldName = CONFIG.get('videoFieldName')
            config = {
                "pathFormat": CONFIG['videoPathFormat'],
                "maxSize": CONFIG['videoMaxSize'],
                "allowFiles": CONFIG['videoAllowFiles']
            }
        else:
            fieldName = CONFIG.get('fileFieldName')
            config = {
                "pathFormat": CONFIG['filePathFormat'],
                "maxSize": CONFIG['fileMaxSize'],
                "allowFiles": CONFIG['fileAllowFiles']
            }
        if fieldName in request.files:
            field = request.files[fieldName]
            uploader = Uploader(ctl_current_user.user_id, field, config, 'ueditor/')#current_app.static_folder
            result = uploader.getFileInfo()
        else:
            result['state'] = '上传接口出错'
    elif action in ('uploadscrawl'):
        # 涂鸦上传
        fieldName = CONFIG.get('scrawlFieldName')
        config = {
            "pathFormat": CONFIG.get('scrawlPathFormat'),
            "maxSize": CONFIG.get('scrawlMaxSize'),
            "allowFiles": CONFIG.get('scrawlAllowFiles'),
            "oriName": "scrawl.png"
        }
        if fieldName in request.form:
            field = request.form[fieldName]
            uploader = Uploader(ctl_current_user.user_id, field, config, 'upload', 'base64') #current_app.static_folder
            result = uploader.getFileInfo()
        else:
            result['state'] = '上传接口出错'
    elif action in ('catchimage'):
        config = {
            "pathFormat": CONFIG['catcherPathFormat'],
            "maxSize": CONFIG['catcherMaxSize'],
            "allowFiles": CONFIG['catcherAllowFiles'],
            "oriName": "remote.png"
        }
        fieldName = CONFIG['catcherFieldName']
        if fieldName in request.form:
            # 这里比较奇怪，远程抓图提交的表单名称不是这个
            source = []
        elif '%s[]' % fieldName in request.form:
            # 而是这个
            source = request.form.getlist('%s[]' % fieldName)
        _list = []
        for imgurl in source:
            uploader = Uploader(ctl_current_user.user_id, imgurl, config, '/upload', 'remote')#current_app.static_folder
            info = uploader.getFileInfo()
            _list.append({
                'state': info['state'],
                'url': info['url'],
                'original': info['original'],
                'source': imgurl,
            })
        result['state'] = 'SUCCESS' if len(_list) > 0 else 'ERROR'
        result['list'] = _list
    else:
        result['state'] = '请求地址出错'
    result = json.dumps(result)
    if 'callback' in request.args:
        callback = request.args.get('callback')
        if re.match(r'^[\w_]+$', callback):
            result = '%s(%s)' % (callback, result)
            mimetype = 'application/javascript'
        else:
            result = json.dumps({'state': 'callback参数不合法'})
    res = make_response(result)
    res.mimetype = mimetype
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,X_Requested_With'
    return res

@main.route('/ueditor')
def ueditor():
    return render_template('default/moudle_ueditor.html', strs=strings())

@main.route('/admin/article', methods=['GET', 'POST'])
@main.route('/admin/article/', methods=['GET', 'POST'])
@login_required
def admin_article():
    action = request.args.get('action', '')
    option = request.args.get('option', '')
    if action is None or '' == action:
        page = request.args.get('page', 1, type=int)
        pagination = models.Article.query.filter_by(
            author_id=ctl_current_user.user_id).order_by(
            models.Article.update_time.desc()).paginate(page, per_page=values.page_size, error_out=False)
        return render_template('default/admin_article.html',
                               strs=strings(),
                               articleList=pagination.items, pagination=pagination)
    elif 'new' == action:
        edit_article_form = ArticleEditForm()
        print(1)
        if edit_article_form.validate_on_submit():
            print(2)
            try:
                first_img_src = ''
                if values.EditorCode.UEditor == edit_article_form.editor_code.data:
                    soup = BeautifulSoup(edit_article_form.body.data)
                    first_img = soup.find(name='img')
                    if first_img:
                        first_img_src = first_img.get('src', '')
                    img_list = soup.find_all(name='img')
                    for img in img_list:
                        noscript_tag = soup.new_tag(name='noscript')
                        noscript_tag.append(soup.new_tag(name='img',
                                                         src=img.get('src', ''),
                                                         alt=img.get('alt', ''),
                                                         title=img.get('title', ''),
                                                         width=img.get('width', 'auto'),
                                                         height=img.get('height', 'auto'),
                                                         style=img.get('style', '')
                                                         ))
                        img.insert_after(noscript_tag)
                        img['class'] = 'lazy'
                        img['data-original'] = img.get('src', '')
                        if '' == img.get('width', ''):
                            img['width'] = 'auto'
                        if '' == img.get('height', ''):
                            img['height'] = 'auto'
                        if '' != img.get('src', ''):
                            del img['src']
                    body_default = '<%s>' % str(soup.html.body).lstrip('<body>').rstrip('</body>')
                new_article = models.Article(
                    title=edit_article_form.title.data,
                    author_id=ctl_current_user.user_id,
                    author_domain=ctl_current_user.unique_domain,
                    author_name=ctl_current_user.nikename,
                    img=first_img_src,
                    tag_list=edit_article_form.tag_list.data,
                    editor_code=edit_article_form.editor_code.data,
                    body_source=edit_article_form.body.data,
                    body_default=body_default,
                    body_simple=soup.get_text(),
                    access_level=edit_article_form.access_level.data,
                    access_passwd=edit_article_form.access_pw.data
                )
                db.session.add(new_article)
                db.session.commit()
                # print('main.admin_article - new_article.id=%s' % new_article.id)
                # update the attachment file info
                print(3)
                un_released_file_list = models.StorageFileKey.query.filter_by(
                    owner_id=new_article.author_id, for_what_status='draft')
                for file_key in un_released_file_list:
                    if file_key.download_url in new_article.body_source:
                        file_key.for_what = 'article'
                        file_key.for_what_id = new_article.id
                        file_key.for_what_status = 'released'
                        db.session.add(file_key)
                db.session.commit()
                # print('main.admin_article - file_key.id')
                try:
                    # storage and update globaltag.json
                    ctl_tags = controller.CtlTags(current_user_id=new_article.author_id, db=db, models=models)
                    add_result, has_new_tag = ctl_tags.add_tag_list(tag_list=new_article.tag_list)
                    if has_new_tag:
                        ctl_tags.update_tag_file()
                    # print('main.admin_article - ctl_tags finish')
                except Exception, e:
                    logger.debug('main.admin_article - update globaltag.json fail. err=%s' % e)
                if values.UserOption.save_draft == option:
                    print('new ajax')
                    return jsonify(form_url=url_for('main.admin_article', action='update', articleId=new_article.id))
                return redirect(url_for('main.article_x',
                                        unique_domain=ctl_current_user.unique_domain,
                                        article_id=new_article.id))
            except Exception, e:
                db.session.rollback()
                logger.debug('main.admin_article - article: new article error. err=%s' % e)
        return render_template('default/admin_article_edit.html',
                               strs=strings(), vals=values, form=edit_article_form)
    elif 'delete' == action:
        # 1. delete_attachment_flag: if delete attachment file in storage and db
        # 2. delete the article
        delete_attachment_flag = request.args.get('delete_attachment_flag', 1, type=int)
        article_id = request.args.get('articleId', -1, type=int)
        # print('main.admin_article - article: delete, article_id=%d, delete_attachment_flag=%d' %
        # (article_id, delete_attachment_flag))
        if -1 != article_id:
            try:
                ctl_article = controller.CtlArticle(current_user_id=ctl_current_user.user_id,
                                                    db=db, models=models)
                ctl_article.delete_single(article_id=article_id,
                                          delete_attachment_flag=(1 == delete_attachment_flag))
                # print('main.admin_article - article: delete article_id %d success!' % article_id)
            except Exception, e:
                logger.debug('main.admin_article - article: delete article_id %d false! err = %s' % (article_id, e))
        return redirect(url_for('main.admin'))
    elif 'update' == action:
        article_id = request.args.get('articleId', -1, type=int)
        update_article = models.Article.query.filter_by(id=article_id).first()
        if update_article is None:
            logger.debug('main.admin_article - update: no have the article id = %s' % article_id)
            return redirect(url_for('main.admin'))
        edit_article_form = ArticleEditForm()
        if edit_article_form.validate_on_submit():
            try:
                first_img_src = ''
                if values.EditorCode.UEditor == edit_article_form.editor_code.data:
                    soup = BeautifulSoup(edit_article_form.body.data)
                    first_img = soup.find(name='img')
                    if first_img:
                        first_img_src = first_img.get('src', '')
                    img_list = soup.find_all(name='img')
                    for img in img_list:
                        noscript_tag = soup.new_tag(name='noscript')
                        noscript_tag.append(soup.new_tag(name='img',
                                                         src=img.get('src', ''),
                                                         alt=img.get('alt', ''),
                                                         title=img.get('title', ''),
                                                         width=img.get('width', 'auto'),
                                                         height=img.get('height', 'auto'),
                                                         style=img.get('style', '')
                                                         ))
                        img.insert_after(noscript_tag)
                        img['class'] = 'lazy'
                        img['data-original'] = img.get('src', '')
                        if '' == img.get('width', ''):
                            img['width'] = 'auto'
                        if '' == img.get('height', ''):
                            img['height'] = 'auto'
                        if '' != img.get('src', ''):
                            del img['src']
                update_article.body_default = '<%s>' % str(soup.html.body).lstrip('<body>').rstrip('</body>')
                update_article.title = edit_article_form.title.data
                update_article.img = first_img_src
                update_article.tag_list = edit_article_form.tag_list.data
                update_article.body_source = edit_article_form.body.data
                update_article.body_simple = soup.get_text(),
                update_article.access_level = edit_article_form.access_level.data
                update_article.access_passwd = edit_article_form.access_pw.data
                update_article.update_time = datetime.utcnow()
                db.session.add(update_article)
                db.session.commit()
                # print('main.admin_article - article: update_article.id=%s' % update_article.id)
                # update the attachment file info
                un_released_file_list = models.StorageFileKey.query.filter_by(
                    owner_id=update_article.author_id, for_what_status='draft')
                for file_key in un_released_file_list:
                    if file_key.download_url in update_article.body_source:
                        file_key.for_what = 'article'
                        file_key.for_what_id = update_article.id
                        file_key.for_what_status = 'released'
                        db.session.add(file_key)
                db.session.commit()
                # print('main.admin_article - article: file_key')
                try:
                    # storage and update globaltag.json
                    ctl_tags = controller.CtlTags(current_user_id=update_article.author_id, db=db, models=models)
                    add_result, has_new_tag = ctl_tags.add_tag_list(tag_list=update_article.tag_list)
                    if has_new_tag:
                        ctl_tags.update_tag_file()
                    # print('main.admin_article - article: ctl_tags finish')
                except Exception, e:
                    logger.debug('main.admin_article - update globaltag.json fail. err = %s' % e)
                if values.UserOption.save_draft == option:
                    print('update ajax')
                    return jsonify(form_url=url_for('main.admin_article', action='update', articleId=update_article.id))
                return redirect(url_for('main.article_x',
                                        unique_domain=ctl_current_user.unique_domain,
                                        article_id=update_article.id))
            except Exception, e:
                db.session.rollback()
                logger.debug('main.admin_article - article: update article error. err = %s' % e)
        edit_article_form.title.data = update_article.title
        edit_article_form.body.data = update_article.body_source
        edit_article_form.editor_code.data = update_article.editor_code
        edit_article_form.access_level.data = update_article.access_level
        edit_article_form.access_pw.data = update_article.access_passwd
        return render_template('default/admin_article_edit.html',
                               strs=strings(), vals=values, form=edit_article_form, article=update_article)

@main.route('/admin/doc', methods=['GET', 'POST', 'OPTIONS'])
@main.route('/admin/doc/', methods=['GET', 'POST', 'OPTIONS'])
def admin_doc():
    return render_template('default/admin_document.html', strs=strings())

@main.route('/admin/tag', methods=['GET', 'POST', 'OPTIONS'])
@main.route('/admin/tag/', methods=['GET', 'POST', 'OPTIONS'])
def admin_tag():
    return render_template('default/admin_tags.html', strs=strings())

@main.route('/admin/nav', methods=['GET', 'POST', 'OPTIONS'])
@main.route('/admin/nav/', methods=['GET', 'POST', 'OPTIONS'])
def admin_nav():
    # global nav
    return render_template('default/admin_globalnav.html', strs=strings())

@main.route('/admin', methods=['GET', 'POST', 'OPTIONS'])
@main.route('/admin/', methods=['GET', 'POST', 'OPTIONS'])
def admin():
    return redirect(url_for('main.admin_article'))

@main.route('/article-comment/<option>', methods=['GET', 'POST', 'OPTIONS'])
@main.route('/article-comment/<option>/', methods=['GET', 'POST', 'OPTIONS'])
def article_comment(option):
    if values.UserOption.add == option or values.UserOption.quote == option:
        try:
            to_article_id = request.form.get('to_article_id', -1, type=int)
            m_article = models.Article.query.filter_by(id=to_article_id).first()
            try:
                sequence_of_article = models.ArticleComment.query.filter_by(
                    article_id=int(m_article.id)).order_by(
                    models.ArticleComment.sequence_of_article.desc()
                ).first().sequence_of_article + 1
            except:
                sequence_of_article = 1
            to_comment_id = request.form.get('to_comment_id', -1, type=int)
            editor_code = request.form.get('editor_code', values.EditorCode.UEditor)
            body_source = request.form.get('comment_body', '')
            body_default = request.form.get('comment_body', '')
            body_simple = request.form.get('comment_body', '')
            # logger.debug('main.article_comment: 2, to_comment_id=%s, body_source=%s' % (to_comment_id, body_source))
            if to_comment_id > 0:
                # logger.debug('main.article_comment: 3')
                to_comment = models.ArticleComment.query.filter_by(id=int(to_comment_id)).first()
                art_comment = models.ArticleComment(
                    article_id=m_article.id,
                    sequence_of_article=sequence_of_article,
                    to_comment_id=to_comment.id,
                    to_sequence_of_article=to_comment.sequence_of_article,
                    to_comment_body=to_comment.body_default,
                    from_user_id=ctl_current_user.user_id,
                    from_user_domain=ctl_current_user.unique_domain,
                    from_user_name=ctl_current_user.nikename,
                    to_user_id=to_comment.from_user_id,
                    to_user_domain=to_comment.from_user_domain,
                    to_user_name=to_comment.from_user_name,
                    editor_code=editor_code,
                    body_source=body_source,
                    body_default=body_default,
                    body_simple=body_simple
                )
                if values.UserOption.add == option:
                    art_comment.to_comment_body = ''
                db.session.add(art_comment)
                db.session.commit()
                logger.debug('main.article_comment: 4')
            else:
                # logger.debug('main.article_comment: 5, m_article.id = %s' % m_article.id)
                art_comment = models.ArticleComment(
                    article_id=m_article.id,
                    sequence_of_article=sequence_of_article,
                    from_user_id=ctl_current_user.user_id,
                    from_user_domain=ctl_current_user.unique_domain,
                    from_user_name=ctl_current_user.nikename,
                    to_user_id=m_article.author_id,
                    to_user_domain=m_article.author_domain,
                    to_user_name=m_article.author_name,
                    editor_code=editor_code,
                    body_source=body_source,
                    body_default=body_default,
                    body_simple=body_simple
                )
                db.session.add(art_comment)
                db.session.commit()
                logger.debug('main.article_comment: 6')
            return render_template('default/article_comment_item.html', strs=strings(),
                                   article=m_article, comment=art_comment)
        except Exception, e:
            db.session.rollback()
            logger.debug('main.view: article_comment: add comment fail. err = %s' % e)
            return e
    elif values.UserOption.delete == option:
        try:
            comment_id = request.args.get('comment_id', -1, type=int)
            if comment_id > 0:
                db.session.delete(models.ArticleComment.query.filter_by(id=int(comment_id)).first())
                db.session.commit()
            return jsonify(result=values.UserOption.success)
        except Exception, e:
            db.session.rollback()
            logger.debug('main.view: article_comment: delete comment fail. err = %s' % e)
            return jsonify(result=values.UserOption.fail)
    elif values.UserOption.agree == option:
        try:
            comment_id = request.args.get('comment_id', -1, type=int)
            if comment_id > 0:
                m_article_comment = models.ArticleComment.query.filter_by(id=int(comment_id)).first()
                if not m_article_comment.agree_user_list:
                    m_article_comment.agree_user_list = ''
                if (ctl_current_user.user_id > 0 and ctl_current_user.unique_domain in m_article_comment.agree_user_list) or (ctl_current_user.user_id < 0 and ctl_current_user.nikename in m_article_comment.agree_user_list):
                    return jsonify(result=values.UserOption.fail, result_info=values.UserOption.repeat)
                else:
                    m_article_comment.agree_num += 1
                    if ctl_current_user.user_id > 0:
                        m_article_comment.agree_user_list += ('%s,' % ctl_current_user.unique_domain)
                    else:
                        m_article_comment.agree_user_list += ('%s,' % ctl_current_user.nikename)
                    db.session.add(m_article_comment)
                    db.session.commit()
            return jsonify(result=values.UserOption.success, result_num=m_article_comment.agree_num)
        except Exception, e:
            db.session.rollback()
            return jsonify(result=values.UserOption.fail, result_info=('%s' % e))
    elif values.UserOption.disagree == option:
        try:
            comment_id = request.args.get('comment_id', -1, type=int)
            if comment_id > 0:
                m_article_comment = models.ArticleComment.query.filter_by(id=int(comment_id)).first()
                if not m_article_comment.disagree_user_list:
                    m_article_comment.disagree_user_list = ''
                if (ctl_current_user.user_id > 0 and ctl_current_user.unique_domain in m_article_comment.disagree_user_list) or (ctl_current_user.user_id < 0 and ctl_current_user.nikename in m_article_comment.disagree_user_list):
                    return jsonify(result=values.UserOption.fail, result_info=values.UserOption.repeat)
                else:
                    m_article_comment.disagree_num += 1
                    if ctl_current_user.user_id > 0:
                        m_article_comment.disagree_user_list += ('%s,' % ctl_current_user.unique_domain)
                    else:
                        m_article_comment.disagree_user_list += ('%s,' % ctl_current_user.nikename)
                    db.session.add(m_article_comment)
                    db.session.commit()
            return jsonify(result=values.UserOption.success, result_num=m_article_comment.disagree_num)
        except Exception, e:
            db.session.rollback()
            return jsonify(result=values.UserOption.fail, result_info=('%s' % e))

@main.route('/<unique_domain>/article/<article_id>', methods=['GET', 'POST', 'OPTIONS'])
@main.route('/<unique_domain>/article/<article_id>/', methods=['GET', 'POST', 'OPTIONS'])
def article_x(unique_domain, article_id):
    try:
        m_article = models.Article.query.filter_by(id=int(article_id)).first()
        try:
            m_article_comment_list = models.ArticleComment.query.filter_by(article_id=m_article.id).all()
            return render_template('default/page_article_view.html',
                                   strs=strings(),
                                   article=m_article,
                                   tag_list=json.loads(m_article.tag_list),
                                   comment_list=m_article_comment_list)
        except:
            return render_template('default/page_article_view.html',
                                   strs=strings(),
                                   article=m_article,
                                   tag_list=json.loads(m_article.tag_list))
    except Exception, e:
        logger.debug("main.article_x - unique_domain=%s, article_id=%s, err=%s" % (unique_domain, article_id, e))
        return render_template('default/page_article_view.html', strs=strings())

@main.route('/<unique_domain>/article', methods=['GET', 'POST', 'OPTIONS'])
@main.route('/<unique_domain>/article/', methods=['GET', 'POST', 'OPTIONS'])
def article(unique_domain):
    try:
        models.User.query.filter_by(unique_domain=unique_domain).first()
    except Exception, e:
        logger.debug('not found the user: %s, please regist first. err=%s' % (unique_domain, e))
        return redirect(url_for('auth.regist'))
    articleId = request.args.get('articleId', -1, type=int)
    if -1 == articleId:
        page = request.args.get('page', 1, type=int)
        # from .settings import article_page_size
        pagination = models.Article.query.filter_by(
            author_domain=unique_domain).order_by(
            models.Article.update_time.desc()).paginate(page, per_page=values.page_size, error_out=False)
        return render_template('default/page_article_list.html',
                               strs=strings(),
                               unique_domain=unique_domain,
                               articleList=pagination.items,
                               pagination=pagination)
    else:
        mArticle = models.Article.query.filter_by(id=articleId).first()
        if mArticle is not None:
            return render_template('default/page_article_view.html',
                                   strs=strings(),
                                   article=mArticle)
        else:
            flash('not found the article')
            return render_template('default/page_article_view.html', strs=strings())

@main.route('/<unique_domain>', methods=['GET', 'POST', 'OPTIONS'])
@main.route('/<unique_domain>/', methods=['GET', 'POST', 'OPTIONS'])
def user_domain(unique_domain):
    return redirect(url_for('main.article', unique_domain=unique_domain))







