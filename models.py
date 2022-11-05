from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

database_path = 'postgresql://postgres:admin@localhost:5432/receipt'


db = SQLAlchemy()

# Binds the app with SQLAlchemy service


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


#---------------------------#
# Models
#---------------------------#


class School(db.Model):
    __tablename__ = 'school'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    state = db.Column(db.String(100))
    city = db.Column(db.String(100))
    address = db.Column(db.String(200))
    phone = db.Column(db.Integer)
    website_link = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    date = db.Column(db.String(50), default=datetime.now())
    agreement = db.Column(db.Boolean, default=False)

    pupil = db.relationship('pupil', backref='school',
                            cascade='all, delete-orphan', lazy='joined')
    teller = db.relationship('teller', backref='school',
                             cascade='all, delete-orphan', lazy='joined')
    account = db.relationship('account', backref='school',
                              cascade='all, delete-orphan', lazy='joined')

    def __repr__(self):
        return f'{self.id}: {self.name}'


class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    amount = db.Column(db.Integer)

    school_id = db.Column(db.Integer, db.ForeignKey(
        'school.id'), nullable='False')
    pupil_id = db.Column(db.Integer, db.ForeignKey(
        'pupil.id'), nullable='False')


class Pupil(db.Model):
    __tablename__ = 'pupil'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    parent_name = db.Column(db.String(120))
    level = db.Column(db.Integer)
    name_of_parent = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    city = db.Column(db.String(120))  # add address, parent_name
    dob = db.Column(db.DateTime)
    agreement = db.Column(db.Boolean, default=False, nullable=False)
    reg_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

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
    amount = db.Column(db.Integer, nullable=False)
    purpose = db.Column(db.String(20))
    unique_digits = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    agreement = db.Column(db.Boolean, default=False)

    school_id = db.Column(db.Integer, db.ForeignKey(
        'school.id'), nullable='False')
    pupil_id = db.Column(db.Integer, db.ForeignKey('pupil.id'), nullable=False)
