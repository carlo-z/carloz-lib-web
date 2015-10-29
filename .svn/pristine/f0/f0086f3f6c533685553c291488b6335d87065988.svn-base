import os
from datetime import datetime

from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash

from flask.ext.script import Manager, Shell
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.login import UserMixin

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost/carloblog'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Role(db.Model):
    __tablename__ = 't_role'
    id = db.Column(db.Integer, primary_key=True)
    role_code = db.Column(db.String(200), nullable=False)
    permissions = db.Column(db.String(600))

    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    create_user_id = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.utcnow())
    update_user_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Role %r>' % self.role_code

class User(UserMixin, db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    email = db.Column(db.String(200), nullable=False, index=True)
    role_code = db.Column(db.String(200), default='user')
    unique_domain = db.Column(db.String(200), unique=True, index=True)
    nikename = db.Column(db.String(200))
    truename = db.Column(db.String(200))
    id_number = db.Column(db.Integer)
    phone = db.Column(db.String(24))
    wechat = db.Column(db.String(200))
    qq = db.Column(db.String(24))
    address = db.Column(db.String(600))
    storage_type = db.Column(db.String(64), nullable=False, default='qiniu')  # qiniu, sae, bae, local and so on

    status = db.Column(db.String(200), default='not_active')
    last_ip = db.Column(db.String(64))
    last_login_time = db.Column(db.DateTime, default=datetime.utcnow())
    passwd1 = db.Column(db.String(500), nullable=False)  # login password
    passwd2 = db.Column(db.String(500))
    passwd3 = db.Column(db.String(500))
    passwd4 = db.Column(db.String(500))
    passwd5 = db.Column(db.String(500))
    passwd6 = db.Column(db.String(500))
    passwd7 = db.Column(db.String(500))
    passwd8 = db.Column(db.String(500))
    passwd9 = db.Column(db.String(500))

    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    create_user_id = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.utcnow())
    update_user_id = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.email

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, form_passwd):
        self.passwd1 = generate_password_hash('' + form_passwd)

    def verify_password(self, form_passwd):
        try:
            return check_password_hash(self.passwd1, '' + form_passwd)
        except:
            return False
        # return True #check_password_hash(self.passwd1, password)

class QiniuStorage(db.Model):
    __tablename__ = 't_qiniu_storage'
    id = db.Column(db.Integer, primary_key=True)
    storage_id = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, nullable=False, index=True)  # db.ForeignKey('t_usr.id')
    access_key = db.Column(db.String(400))
    secret_key = db.Column(db.String(400))
    bucket_name = db.Column(db.String(200))
    access_level = db.Column(db.String(64), default='public')  # public or private
    use_flag = db.Column(db.String(64), default='N')  # Y: on use, N: not use
    download_url = db.Column(db.String(1024))
    private_download_url = db.Column(db.String(1024))

    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    create_user_id = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.utcnow())
    update_user_id = db.Column(db.Integer)

    def __repr__(self):
        return '<user_storage_id = %s>' % self.id

class StorageFileKey(db.Model):
    __tablename__ = 't_storage_file_key'
    id = db.Column(db.Integer, primary_key=True)
    storage_file_key_id = db.Column(db.Integer)  # id backup
    owner_id = db.Column(db.Integer, nullable=False, index=True)  # db.ForeignKey('t_usr.id')
    storage_type = db.Column(db.String(64), nullable=False, default='qiniu')  # qiniu, sae, bae and so on
    storage_id = db.Column(db.Integer, nullable=False)
    for_what = db.Column(db.String(64), nullable=False, default='article')  # article or doc
    for_what_id = db.Column(db.Integer)  # article_id or doc_node_id
    for_what_status = db.Column(db.String(64), default='draft')  # draft, released, deleted
    original_name = db.Column(db.Text)
    file_key = db.Column(db.Text)
    file_type = db.Column(db.String(64))  # img, file
    file_size = db.Column(db.String(200))
    download_url = db.Column(db.Text)
    can_delete = db.Column(db.String(64), default='false')  # false, true

    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    create_user_id = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.utcnow())
    update_user_id = db.Column(db.Integer)

    def __repr__(self):
        return '<file_storage_key_id = %s>' % self.id

class Tag(db.Model):
    __tablename__ = 't_tag'
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer)
    tag_name = db.Column(db.String(200), nullable=False, unique=True, index=True)
    use_num = db.Column(db.Integer, default=0)

    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    create_user_id = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.utcnow())
    update_user_id = db.Column(db.Integer)

    def __repr__(self):
        return '<tag %s>' % self.tag_name

class GlobalNav(db.Model):
    __tablename__ = 't_global_nav'
    id = db.Column(db.Integer, primary_key=True)
    globalnav_id = db.Column(db.Integer)
    node_name = db.Column(db.String(200), nullable=False)
    node_level = db.Column(db.Integer, default=1)  # 1: root nav, 2: leaf nav
    sequence_in_level = db.Column(db.Integer, default=1)

    father_nav_id = db.Column(db.Integer, default=-1)

    owner_role = db.Column(db.String(64), default='user')  # system, manager, user
    owner_id = db.Column(db.Integer, nullable=False, index=True)
    owner_domain = db.Column(db.String(200), nullable=False, index=True)
    owner_name = db.Column(db.String(200))

    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    update_time = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<GlobalNav %r>' % self.id

class Article(db.Model):
    __tablename__ = 't_article'
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer)
    article_type = db.Column(db.String(200), nullable=False, default='article')  # article or doc

    title = db.Column(db.String(200), nullable=False)
    tag_list = db.Column(db.String(1024))  # json
    keywords = db.Column(db.String(200))
    abstract = db.Column(db.Text)

    editor_code = db.Column(db.String(64))
    body_source = db.Column(db.Text)
    body_default = db.Column(db.Text)
    body_simple = db.Column(db.Text)  # the text no style and html

    author_id = db.Column(db.Integer, nullable=False, index=True)
    author_domain = db.Column(db.String(200), nullable=False, index=True)
    author_name = db.Column(db.String(200))
    access_level = db.Column(db.String(64), default='public')
    access_passwd = db.Column(db.String(200))
    pv_num = db.Column(db.Integer, default=0)
    agree_num = db.Column(db.Integer, default=0)
    disagree_num = db.Column(db.Integer, default=0)
    comment_num = db.Column(db.Integer, default=0)
    collection_num = db.Column(db.Integer, default=0)
    pv_user_list = db.Column(db.Text)  # user id list
    agree_user_list = db.Column(db.Text)
    disagree_user_list = db.Column(db.Text)
    comment_user_list = db.Column(db.Text)
    collection_user_list = db.Column(db.Text)
    attachment_num = db.Column(db.Integer, default=0)
    attachment_size = db.Column(db.String(200))
    delete_flag = db.Column(db.String(16), default='N')
    delete_date = db.Column(db.DateTime)

    layout_width_start = db.Column(db.Integer, default=0)
    layout_width_end = db.Column(db.Integer, default=55)
    css_file_url = db.Column(db.Text)

    from_url = db.Column(db.Text)
    img = db.Column(db.Text)

    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    update_time = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<article_id = %s>' % self.id

class ArticleComment(db.Model):
    __tablename__ = 't_article_comment'
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer)
    article_id = db.Column(db.Integer, nullable=False, index=True)
    sequence_of_article = db.Column(db.Integer, nullable=False, default=1)
    to_comment_id = db.Column(db.Integer, default=-1)
    to_sequence_of_article = db.Column(db.Integer, default=-1)
    to_comment_body = db.Column(db.Text)
    to_comment_delete_flag = db.Column(db.String(16), default='N')

    from_user_id = db.Column(db.Integer)
    from_user_domain = db.Column(db.String(200))
    from_user_name = db.Column(db.String(200))

    to_user_id = db.Column(db.Integer, default=-1)
    to_user_domain = db.Column(db.String(200), default='none')
    to_user_name = db.Column(db.String(200), default='none')

    editor_code = db.Column(db.String(64))
    body_source = db.Column(db.Text)
    body_default = db.Column(db.Text)
    body_simple = db.Column(db.Text)  # the text no style and html

    agree_num = db.Column(db.Integer, default=0)
    disagree_num = db.Column(db.Integer, default=0)
    agree_user_list = db.Column(db.Text)
    disagree_user_list = db.Column(db.Text)
    delete_flag = db.Column(db.String(16), default='N')
    delete_date = db.Column(db.DateTime)

    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    update_time = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<ArticleComment %s>' % self.id

class DocNode(db.Model):
    __tablename__ = 't_doc_node'
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.Integer)
    node_name = db.Column(db.String(200), nullable=False)
    node_type = db.Column(db.String(64), default='root')  # root: root node, leaf: leaf node, common: common node

    node_level = db.Column(db.Integer, default=1)  # 1: root node, >=2: leaf node || common node
    sequence_in_level = db.Column(db.Integer, default=1)

    father_node_id = db.Column(db.Integer, default=-1)
    article_id = db.Column(db.Integer, default=-1)  # if leaf_node is True: article_id can not null

    author_id = db.Column(db.Integer, nullable=False, index=True)
    author_domain = db.Column(db.String(200), nullable=False, index=True)
    author_name = db.Column(db.String(200))

    # for root_node start
    tag_list = db.Column(db.String(1024))  # json
    keywords = db.Column(db.String(200))
    abstract = db.Column(db.Text)

    access_level = db.Column(db.String(64), default='public')
    access_passwd = db.Column(db.String(200))
    pv_num = db.Column(db.Integer, default=0)
    praise_num = db.Column(db.Integer, default=0)
    dispraise_num = db.Column(db.Integer, default=0)
    comment_num = db.Column(db.Integer, default=0)
    collection_num = db.Column(db.Integer, default=0)
    attachment_num = db.Column(db.Integer, default=0)
    attachment_size = db.Column(db.String(200))
    delete_flag = db.Column(db.String(16), default='N')
    delete_date = db.Column(db.DateTime)

    layout_width_start = db.Column(db.Integer, default=0)
    layout_width_end = db.Column(db.Integer, default=55)
    css_file_url = db.Column(db.Text)
    # for root_noe end
    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    update_time = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<DocNode %r>' % self.node_name

class Test(db.Model):
    __tablename__ = 't_test'
    id = db.Column(db.Integer, primary_key=True)
    test_body = db.Column(db.String(600))

    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    create_user_id = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.utcnow())
    update_user_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Test %r>' % self.test_body

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
