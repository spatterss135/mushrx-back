
from flask import (jsonify, Blueprint, render_template, request, redirect)
from . import models
from sqlalchemy import delete
from flask_cors import CORS, cross_origin

import random


bp = Blueprint('users', __name__, url_prefix='/users')
@bp.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    if request.method == 'GET':
        data = models.User.query.all()
        return jsonify([s.toDict() for s in data])
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        avatar = random.randint(0,9)
        new_user = models.User(username=username, password=password, avatar=avatar) 
        models.db.session.add(new_user)
        models.db.session.commit()
        return jsonify('a')
    