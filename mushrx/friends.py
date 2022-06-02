
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
        friends = models.Friends.query.filter_by(user_id=user_id, friend_id=friend_id).all()
        pending = True
        try:
            pending = request.json['pending']
        except:
            pass
        if len(friends) == 0:
            new_friendship = models.Friends(user_id=user_id, friend_id=friend_id, pending=pending) 
            models.db.session.add(new_friendship)
            models.db.session.commit()
        return jsonify('Success')
    if request.method == 'DELETE':
        user_id = request.json['user_id']
        friend_id = request.json['friend_id']
        both = request.json['both']
        friendship = models.Friends.query.filter_by(user_id=user_id, friend_id=friend_id).first()
        
        models.db.session.delete(friendship)
        if both is True:
            friendship_also = models.Friends.query.filter_by(user_id=friend_id, friend_id=user_id).first()
            models.db.session.delete(friendship_also)
        models.db.session.commit()
        return jsonify('Deleted')



@bp.route('/<id>', methods=['GET', 'POST', 'DELETE'], strict_slashes=False)
def index(id):
    if request.method == 'GET':
        friends = models.Friends.query.filter_by(user_id=id).all()
        print(friends)
        return jsonify([s.toDict() for s in friends])

@bp.route('requests/<id>', methods=['GET','PUT'], strict_slashes=False)
def gettingRequests(id):
    if request.method == 'GET':
        friends = models.Friends.query.filter_by(friend_id=id).all()
        print(friends)
        return jsonify([s.toDict() for s in friends])    
    if request.method == 'PUT':
        friendship = models.Friends.query.get(id)

        pending = request.json['pending']
        friendship.pending = pending
        models.db.session.commit()
        return jsonify('a')

    # if request.method == 'POST':
    #     user_id = request.json['user_id']
    #     friend_id = request.json['friend_id']
    #     new_friendship = models.User(user_id=user_id, friend_id=friend_id) 
    #     models.db.session.add(new_friendship)
    #     models.db.session.commit()
    #     return jsonify('Success')


    # if request.method == 'DELETE':

