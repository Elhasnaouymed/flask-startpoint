from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import AppConfig

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def init_login_manager(app: Flask):
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'You should login first to access this page!'
    login_manager.login_message_category = 'warning'

    @login_manager.user_loader
    def user_loader(id_: int):
        raise NotImplemented('User Loader is not implemented yet!')


def init_db_and_migrate(app: Flask):
    from . import models
    db.init_app(app)
    migrate.init_app(app, db)


def create_app():
    app = Flask(__name__)

    app.config.from_object(AppConfig)

    init_db_and_migrate(app)

    init_login_manager(app)

    from .cli import register_cli
    register_cli(app)

    return app
