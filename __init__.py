import os

from flask import Flask


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    kwargs = {'SECRET_KEY': 'dev',
              'DATABSE': os.path.join(app.instance_path, 'sqlite')}
    app.config.from_mapping(os.path.join(**kwargs))

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass