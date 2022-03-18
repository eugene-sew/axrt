from enum import unique
# from validators import length
from E_voting import db, app
from sqlalchemy.sql import func
from flask_login import UserMixin
from E_voting import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=30), nullable=False, unique=True)
    index = db.Column(db.String(length=40), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    team = db.Column(db.String(length=40), nullable=True, default=0)
    voterscount = db.relationship('Voterscount', backref='author', lazy=True, passive_deletes=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Voterscount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voter_name = db.Column(db.String(50), nullable=False) 
    date_vote = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    voter = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)# the user.id should be in ' ' and small letters

    def __repr__(self):
        return f"Voterscount('{self.voter}', '{self.date_vote}' )"



