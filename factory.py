import os

from flask import Flask

import db


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    # if test_config is None:
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    kwargs = {'SECRET_KEY': 'dev',
              'DATABASE': os.path.join(app.instance_path, 'stuff.sqlite')}
    app.config.from_mapping(**kwargs)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    with app.app_context():
        db.init_db()

    return app
