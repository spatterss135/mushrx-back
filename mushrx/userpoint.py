
from flask import (jsonify, Blueprint, render_template, request, redirect)
from . import models
from sqlalchemy import delete
from flask_cors import CORS, cross_origin


bp = Blueprint('userpoint', __name__, url_prefix='/userpoints')
@bp.route('/', methods=['GET', 'POST', 'DELETE'], strict_slashes=False)
def index():
    if request.method == 'GET':
        data = models.UserPoint.query.all()
        return jsonify([{'latitude':s.latitude, 'longitude':s.longitude, 'found_on':s.found_on, 'user_id':s.user_id, 'notes':s.notes} for s in data])
    if request.method == 'POST':
        latitude = request.json['latitude']
        longitude = request.json['longitude']
        found_on = request.json['found']
        user_id = request.json['user_id']
        notes = request.json['notes']
        new_point = models.UserPoint(latitude=latitude, longitude=longitude, user_id=user_id, found_on=found_on, notes=notes) 
        models.db.session.add(new_point)
        models.db.session.commit()
        data = models.UserPoint.query.all()
        return jsonify([{'latitude':s.latitude, 'longitude':s.longitude, 'found_on':s.found_on, 'user_id':s.user_id, 'notes':s.notes} for s in data])

    if request.method == 'DELETE':
        latitude = request.json['latitude']
        longitude = request.json['longitude']
        user_id = request.json['user_id']
        point = models.UserPoint.query.filter_by(user_id=user_id, latitude=latitude, longitude=longitude).first()
        if point:
            models.db.session.delete(point)
            models.db.session.commit()
            data = models.UserPoint.query.all()
            return jsonify([{'latitude':s.latitude, 'longitude':s.longitude, 'found_on':s.found_on, 'user_id':s.user_id, 'notes':s.notes} for s in data])
