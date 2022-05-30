
import json
from flask import (jsonify, Blueprint, render_template, request, redirect)
from . import models
from sqlalchemy import delete
from flask_cors import CORS, cross_origin


bp = Blueprint('friends', __name__, url_prefix='/friends')

@bp.route('/', methods=['GET', 'POST', 'DELETE'], strict_slashes=False)
def creating():
     if request.method == 'POST':
        user_id = request.json['user_id']
        friend_id = request.json['friend_id']
        new_friendship = models.Friends(user_id=user_id, friend_id=friend_id) 
        models.db.session.add(new_friendship)
        models.db.session.commit()
        return jsonify('Success')


@bp.route('/<id>', methods=['GET', 'POST', 'DELETE'], strict_slashes=False)
def index(id):
    if request.method == 'GET':
        friends = models.Friends.query.filter_by(user_id=id).all()
        return jsonify([s.toDict() for s in friends])

    # if request.method == 'POST':
    #     user_id = request.json['user_id']
    #     friend_id = request.json['friend_id']
    #     new_friendship = models.User(user_id=user_id, friend_id=friend_id) 
    #     models.db.session.add(new_friendship)
    #     models.db.session.commit()
    #     return jsonify('Success')


    # if request.method == 'DELETE':

