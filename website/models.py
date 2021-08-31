from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func  # to get current time


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # func.now() is to let sqlalchemy insert the time
    # timezone=True adds timezone to the datetime
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # to add relation to user object. Every note must add an from an existing user id(lower case, not referencing the class)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    # user will be able to access all the notes created by the user
    # is a list of all the different notes of the user
    # capital letter(Note) referencing the class
