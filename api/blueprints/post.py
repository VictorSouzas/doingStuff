import functools

from flask import (Blueprint, flash, g, make_response, redirect,
                   render_template, request, session, url_for)

from db import get_db

blueprint = Blueprint('post', __name__, url_prefix='/post')


@blueprint.route('/', methods=('GET', ))
def get_post():
    return make_response('', 200)


@blueprint.route('/', methods=('POST', ))
def create_post():
    return make_response('', 200)


@blueprint.route('/', methods=('PUT', ))
def update_post():
    return make_response('', 200)


@blueprint.route('/', methods=('DELETE', ))
def delete_post():
    return make_response('', 200)
