# Already entered
# from response import data
# from seventeenresponse import data

# import re
# from flask import (Blueprint, render_template, request, redirect)
# from . import models
# from sqlalchemy import delete
# from datetime import datetime

# clean_data = []

# for i in range(len(data['features'])):
#     clean_data.append({'text': data['features'][i]['properties']['marker-createdon'], 
#                         'latitude': data['features'][i]['geometry']['coordinates'][1], 
#                         'longitude': data['features'][i]['geometry']['coordinates'][0]})


# for i in clean_data:
#     match = re.search(r'(\d+-\d+-\d+)', i['text'])
#     if match is not None:
#         i['text'] = match.group(1)
#     try:
#         i['text'] = datetime.strptime(i['text'], '%Y-%m-%d').date()
#     except ValueError:
#         i['text'] =  datetime.strptime('12/25/1987', '%m/%d/%Y').date()



    

# bp = Blueprint('points', __name__, url_prefix='/new-data')

# print(clean_data)
# @bp.route('/')
# def index():
#     print('ehh;l')
#     for dp in clean_data:
#         text = dp['text']
#         latitude = dp['latitude']
#         longitude = dp['longitude']

#         new_point = models.Point(found_on=text, latitude=latitude, longitude=longitude)
#         models.db.session.add(new_point)
#         models.db.session.commit()

# @bp.route('/delete')
# def index():
#     delete(models.Point)


