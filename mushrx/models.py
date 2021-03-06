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
    password = db.Column(db.LargeBinary)
    children = db.relationship('UserPoint')

    def toDict(self):
       return dict(id=self.id, username=self.username,  avatar=self.avatar)


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
       return dict(id=self.id, user_id=self.user_id, points=self.points, found_on=self.found_on, notes=self.notes)


class Friends(db.Model):
    __tablename__='friends'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pending = db.Column(db.Boolean, default=True)

    def toDict(self):
       return dict(id=self.id, user_id=self.user_id, friend_id=self.friend_id, pending=self.pending)

class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    text = db.Column(db.Text)
    point_share_id = db.Column(db.Integer)
    poly_share_id = db.Column(db.Integer)