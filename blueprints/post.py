import functools

from flask import (Blueprint, flash, g, redirect,
                   render_template, request, session, url_for)

from db import get_db

blueprint = Blueprint('post', __name__, url_prefix='/post')


@blueprint.route('/', methods=('GET', ))
def get_post():
    return 'aaaaa'


@blueprint.route('/', methods=('POST', ))
def create_post():
    return 'aaaaa'


@blueprint.route('/', methods=('PUT', ))
def update_post():
    return 'aaaa'


@blueprint.rout('/', methods=('DELETE', ))
def delete_post():
    return 'aaaa'
