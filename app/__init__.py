from flask import Flask

from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config

class NullPoolSQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        super(NullPoolSQLAlchemy, self).apply_driver_hacks(app, info, options)
        from sqlalchemy.pool import NullPool
        options['poolclass'] = NullPool
        del options['pool_size']

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = NullPoolSQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'basic'  # strong
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    return app

