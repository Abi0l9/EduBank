from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from cryptography.fernet import Fernet
from methods import *
from models import *
from forms import *
import os
import sys
import json

app = Flask(__name__)
app.secret_key = b'_5fjsjkdf34#25op/\|d'

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

    descriptions = ["School fee", "Examination fee", "Textbooks",
                    "Excursion", "Development", "Donation", "Gift", "Others"]
    return render_template('pages/deposit_payment.html', descriptions=descriptions, schools=schools, pupils=pupils, grouped_data=())


@app.route('/deposit', methods=['GET'])
def select_school():
    return render_template('forms/select_school.html', schools=get_id_name("schools"))

#################


@app.route('/new_school', methods=['POST'])
def new_school():

    school = School(name=request.form['name'], email=request.form['email'], state=request.form[
        'state'], city=request.form['city'], address=request.form['address'], phone=request.form['phone'], website_link=request.form['website_link'], image_link=request.form['image_link'],  agreement=True)
    try:
        save(school)
        flash(
            request.form['name'] + " has been registered, successfully!")
    except:
        flash(
            request.form['name'] + " has already been registered.")
    finally:
        rollback()

    return redirect(url_for('register'))


@app.route('/new_pupil', methods=['POST'])
def new_pupil():

    pupil = Pupil(name=request.form['name'], parent_name=request.form['parent_name'], level=request.form['level'], state=request.form[
        'state'], city=request.form['city'], address=request.form['address'], dob=request.form['dob'], school_id=request.form['desired-school'],  agreement=True)
    try:
        save(pupil)
        flash(
            request.form['name'] + " has been registered, successfully!")
    except:
        flash(" Error! " +
              request.form['name'] + " has already registered")
    finally:
        rollback()

    return redirect(url_for('register'))


@app.route('/new_deposit', methods=['POST'])
def new_deposit():

    data = {"depositor_name": request.form.get('name'), "depositor_phone": request.form.get('depositor_phone'), "amount": request.form.get(
        'amount'), "description": request.form.get('description'), "school_id": request.form.get('school_id'), "pupil_id": request.form.get('pupil_id')}

    key = Fernet.generate_key()
    cipher = Fernet(key)

    # save the cipher key and the unique digits in the db
    credentials = json.dumps(data).encode('utf-8')
    credentials_encrypt = cipher.encrypt(credentials)

    # for future use
    # Decrypt_data = cipher.decrypt(credentials_encrypt).decode('utf-8')

    trans_key = key # the generated key to be used for decryption
    trans_id = credentials_encrypt  # encrypted details
    ref_number = credentials_encrypt[::20] #slice the encryted binary number at each nth step


    teller = Teller(depositor_name=request.form.get('name'), depositor_phone=request.form.get('depositor_phone'),
                    amount=request.form.get('amount'), trans_id=trans_id, trans_key=trans_key, ref_number=ref_number, description=request.form.get('description'), school_id=request.form.get('school_id'), pupil_id=request.form.get('pupil_id'), agreement=True)

    account = Account(description=request.form.get('description'), amount=request.form.get(
        'amount'), school_id=request.form.get('school_id'), pupil_id=request.form.get('pupil_id'))
    
    ref_number = str(ref_number, encoding='utf-8')
    try:
        save(teller)
        save(account)
    except:
        flash("An error occured!")
        return redirect(url_for('select_school'))
    finally:
        rollback()

        return render_template('pages/deposited.html', ref_number=ref_number)
    



@app.route('/deposited')
def deposited():
    return render_template('pages/deposited.html')

# Running port:
if __name__ == '__main__':
    app.run()
