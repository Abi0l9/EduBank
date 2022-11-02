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
    address = db.Column(db.String(200))
    phone = db.Column(db.Integer)
    website_link = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    date = db.Column(db.String(50))
    agreement = db.Column(db.Boolean, default=False)

    pupil = db.relationship('pupil', backref='school',
                            cascade='all, delete-orphan', lazy='joined')
    teller = db.relationship('teller', backref='school',
                             cascade='all, delete-orphan', lazy='joined')
    account = db.relationship('account', backref='school',
                              cascade='all, delete-orphan', lazy='joined')


class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    amount = db.Column(db.Integer)

    school_id = db.Column(db.Integer, db.ForeignKey(
        'school.id'), nullable='False')
    pupil_id = db.Column(db.Integer, db.ForeignKey('pupil.id'))


class Pupil(db.Model):
    __tablename__ = 'pupil'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    level = db.Column(db.Integer)
    name_of_parent = db.Column(db.String(120))
    state = db.Column(db.String(120))
    city = db.Column(db.String(120))
    date_of_birth = db.Column(db.DateTime)
    agreement = db.Column(db.Boolean, default=False)

    school_id = db.Column(db.Integer, db.ForeignKey(
        'school.id'), nullable='False')
    teller = db.relationship('teller', backref='pupil',
                             cascade='all, delete-orphan', lazy='joined')
    account = db.relationship('account', backref='school',
                              cascade='all, delete-orphan', lazy='joined')


class Teller(db.Model):
    __tablename__ = 'teller'

    id = db.Column(db.Integer, primary_key=True)
    depositor_name = db.Column(db.String(120))
    depositor_phone = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    purpose = db.Column(db.String(20))
    unique_digits = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    agreement = db.Column(db.Boolean, default=False)

    school_id = db.Column(db.Integer, db.ForeignKey(
        'school.id'))
    pupil_id = db.Column(db.Integer, db.ForeignKey('pupil.id'))
