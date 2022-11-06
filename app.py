from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from methods import *
from models import *
from forms import *
import os
import sys


app = Flask(__name__)

setup_db(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('main/index.html')

## Forms ##


@app.route('/register', methods=['GET'])
def register():
    school_form = School_Reg_Form()
    pupil_form = Pupil_Reg_Form()

    return render_template('/pages/register.html', schools=get_id_name("schools"), school_form=school_form, pupil_form=pupil_form)


@app.route('/deposits/school', methods=['POST'])
def make_deposit():
    id = int(request.form['schools'])

    pupils = get_students_record(id)[0]
    schools = get_students_record(id)[1]

    return render_template('pages/deposit_payment.html', schools=schools, pupils=pupils, grouped_data=())


@app.route('/deposit', methods=['GET'])
def select_school():
    return render_template('forms/select_school.html', schools=get_id_name("schools"))

#################


@app.route('/new_school', methods=['POST'])
def new_school():

    school = School(name=request.form['name'], email=request.form['email'], state=request.form[
        'state'], city=request.form['city'], address=request.form['address'], phone=request.form['phone'], website_link=request.form['website_link'], image_link=request.form['image_link'],  agreement=True)

    save(school)
    return redirect(url_for('register'))


@app.route('/new_pupil', methods=['POST'])
def new_pupil():

    pupil = Pupil(name=request.form['name'], parent_name=request.form['parent_name'], level=request.form['level'], state=request.form[
        'state'], city=request.form['city'], address=request.form['address'], dob=request.form['dob'], school_id=request.form['desired-school'],  agreement=True)

    save(pupil)
    return redirect(url_for('register'))


@app.route('/new_deposit', methods=['POST'])
def new_deposit():
    form = Teller()

    teller = Teller(depositor_name=request.form.get('depositor_name'), depositor_phone=request.form.get('depositor_phone'),
                    amount=request.form.get('amount'), description=request.form.get('description'), school_id=request.form.get('school_id'), pupil_id=request.form.get('pupil_id'), agreement=True)

    teller.save(teller)
    return redirect(url_for('make_deposit'))


# Running port:
if __name__ == '__main__':
    app.run()
