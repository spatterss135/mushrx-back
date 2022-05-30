
from flask import (jsonify, Blueprint, render_template, request, redirect)
from . import models
from sqlalchemy import delete
from flask_cors import CORS, cross_origin
import bcrypt

import random


bp = Blueprint('users', __name__, url_prefix='/users')
@bp.route('/create', methods=['GET', 'POST'], strict_slashes=False)
def index():
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password'].encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password, salt)
        avatar = random.randint(0,9)
        data = models.User.query.filter_by(username=username).all()
        if len(data) < 1:
            new_user = models.User(username=username, password=hashed, avatar=avatar) 
            models.db.session.add(new_user)
            models.db.session.commit()
            return jsonify('Success')
        else: 
            return jsonify('Failure')
        


@bp.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def gettingUser():
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password'].encode('utf-8')
        data = models.User.query.filter_by(username=username).first()
        if data is not None:

            if bcrypt.checkpw(password, data.password):
                return jsonify(data.toDict())
        return jsonify('Failure')

@bp.route('/<ids>', methods=['GET'], strict_slashes=False)
def gettingFriend(ids):
    friend_ids = ids.split(',')
    friends = models.User.query.filter(models.User.id.in_(friend_ids)).all()
    return jsonify([s.toDict() for s in friends])



      

