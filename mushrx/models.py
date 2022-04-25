from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Point(db.Model):
    __tablename__ = 'points'

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    found_on = db.Column(db.Date)