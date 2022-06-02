
from flask import (jsonify, Blueprint, render_template, request, redirect)
from . import models



bp = Blueprint('messages', __name__, url_prefix='/messages')
@bp.route('/<user>/<friend>', methods=['GET', 'POST', 'DELETE'], strict_slashes=False)
def index(user, friend):
    if request.method == 'GET':
        return jsonify('a')