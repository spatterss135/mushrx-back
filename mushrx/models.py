from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Point(db.Model):
    __tablename__ = 'points'

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    found_on = db.Column(db.Date)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250))
    avatar = db.Column(db.Integer)
    password = db.Column(db.String(250))
    children = db.relationship('UserPoint')

    def toDict(self):
       return dict(id=self.id, username=self.username, password=self.password, avatar=self.avatar)


class UserPoint(db.Model):
    __tablename__ = 'user-points'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    found_on = db.Column(db.Date)
    notes = db.Column(db.Text)


class UserPolygon(db.Model):
    __tablename__ = 'user-polygons'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    points = db.Column(db.ARRAY(db.Text))
    found_on = db.Column(db.Date)
    notes = db.Column(db.Text)

    def toDict(self):
       return dict(id=self.id, user_id=self.user_id, points=''.join(self.points), found_on=self.found_on, notes=self.notes)