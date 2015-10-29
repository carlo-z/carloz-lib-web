#!/usr/bin/python
#-*-coding:utf-8-*-

import config

class Regist(object):
    forbid_domain_list = ['login','logout','regist','register','signin','signup',
                          'index','search','tag','globaltag','tag_search','upload','ueditor',
                          'admin','article','admin_article',
                          'doc','admin_doc','tag','admin_tag','nav','globalnav','admin_nav',
                          'article-comment','comment','article_comment','article_x',
                          'user_domain','author_domain',
                          'bae','sae','role',
                          'new','add','edit','update','delete','agree','disagree','success','fail','quote']

class EditorCode(object):
    UEditor = 'ueditor'

class Platform(object):
    development = 'development'
    testing = 'testing'
    production = 'production'
    BAE = 'BAE'

class BAE(object):
    platform_name = Platform.BAE
    ak = '6b190efae1fe48acb56343e0e09179f0'
    sk = '2d3273d8780946fe9575bff3e9e2b3f4'

class Env(object):
    platform = config.platform

class Role(object):
    anonymous_user = 'anonymous-user'

class UserOption(object):
    new = 'new'
    add = 'add'
    edit = 'edit'
    update = 'update'
    delete = 'delete'
    agree = 'agree'
    disagree = 'disagree'
    success = 'success'
    fail = 'fail'
    quote = 'quote'
    repeat = 'repeat'
    save_draft = 'save_draft'

page_size = 15









