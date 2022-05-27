
import json
from flask import (jsonify, Blueprint, render_template, request, redirect)
from . import models
from sqlalchemy import delete
from flask_cors import CORS, cross_origin


bp = Blueprint('userpolygons', __name__, url_prefix='/userpolygons')

# @bp.route('/<id>',  strict_slashes=False)
# def oops():
#     id = request.args.get('id')
#     print(request.args)
#     print('hello')
#     return jsonify('a')
@bp.route('/', methods=['GET', 'POST', 'DELETE'], strict_slashes=False)
def index():
    if request.method == 'GET':
        id = request.args.get('id')
        data = models.UserPolygon.query.filter_by(user_id=id).all()
        return jsonify([s.toDict() for s in data])
    if request.method == 'POST':
        points = request.json['points']
        found_on = request.json['found']
        user_id = request.json['user_id']
        notes = request.json['notes']
        new_polygon = models.UserPolygon(points=points, user_id=user_id, found_on=found_on, notes=notes) 

        models.db.session.add(new_polygon)
        models.db.session.commit()

        data = models.UserPolygon.query.all()
        return jsonify([s.toDict() for s in data])

    if request.method == 'DELETE':
        id = request.json['id']
        user_id = request.json['user']
        polygon = models.UserPolygon.query.filter_by(user_id=user_id, id=id).first()
        if polygon:
            models.db.session.delete(polygon)
            models.db.session.commit()
            data = models.UserPolygon.query.all()
            return jsonify([s.toDict() for s in data])
