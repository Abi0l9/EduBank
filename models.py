from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

#---------------------------#
# Models
#---------------------------#


class School(db.Model):
    __tablename__ = 'school'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    state = db.Column(db.String(100))
    city = db.Column(db.String(100))
    address = db.Column(db.String(100))
    phone = db.Column(db.Integer(12))
    website_link = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    date = db.Column(db.String(50))
    agreement = db.Column(db.Boolean, default=False, nullable=False)


class Pupil(db.Model):
    __tablename__ = 'pupil'

    id = db.Column(db.Integer, primary_key=True)
