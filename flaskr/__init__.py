import os
from flask import Flask
# from .db import db
from . import db
from . import auth
from . import poetrywall
from . import models

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(os.path.join(app.instance_path, 'flaskr.db')),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # import logging
    # logging.basicConfig()
    # logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


    db.init_app(app)
    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()

    app.register_blueprint(auth.bp)
    app.register_blueprint(poetrywall.bp)
    app.add_url_rule('/', endpoint='index')

    return app
