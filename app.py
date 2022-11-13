import json
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from cryptography.fernet import Fernet
from methods import *
from models import *
from forms import *

app = Flask(__name__)
app.secret_key = b'_5fjsjkdf34#25op/\|d'

setup_db(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()


##+++++++++++++++++++++++++++++++##
# Homepage
@app.route('/')
def index():
    return render_template('main/index.html')

# Registration Page (Schools and Pupils)


@app.route('/register', methods=['GET'])
def register():
    school_form = School_Reg_Form()
    pupil_form = Pupil_Reg_Form()

    return render_template('/pages/register.html', schools=get_id_name("schools"), school_form=school_form, pupil_form=pupil_form)

# New school registration


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
            request.form['name'] + " has already been registered or details already exist!")
        rollback()
    finally:
        close()

    return redirect(url_for('register'))

# New pupil registration


@app.route('/new_pupil', methods=['POST'])
def new_pupil():

    pupil = Pupil(name=request.form['name'], parent_name=request.form['parent_name'], level=request.form['level'], state=request.form[
        'state'], city=request.form['city'], address=request.form['address'], age=int(request.form['age']), school_id=request.form['desired-school'],  agreement=True)
    try:
        save(pupil)
        flash(
            request.form['name'] + " has been registered, successfully!")
    except:
        flash(" Error! " +
              request.form['name'] + " has already registered")
        rollback()
    finally:
        close()

    return redirect(url_for('register'))

# Select school to make deposit


@app.route('/deposit', methods=['GET'])
def select_school():

    return render_template('forms/select_school.html', schools=get_id_name("schools"))

# Deposit page


@app.route('/deposits/school', methods=['POST'])
def make_deposit():
    id = int(request.form['schools'])

    try:
        pupils = get_students_record(id)[0]
        schools = get_students_record(id)[1]

        print(pupils, schools)
        descriptions = ["School fee", "Examination fee", "Textbooks",
                        "Excursion", "Development", "Donation", "Gift", "Others"]
        close()
        return render_template('pages/deposit_payment.html', descriptions=descriptions, schools=schools, pupils=pupils, grouped_data=())
    except:
        flash("Selected school has no registered student.")
        close()
        return redirect(url_for('select_school'))
# New deposit


@app.route('/new_deposit', methods=['POST'])
def new_deposit():

    data = {"depositor_name": request.form.get('name'), "depositor_phone": request.form.get('depositor_phone'), "amount": request.form.get(
        'amount'), "description": request.form.get('description'), "school_id": request.form.get('school_id'), "pupil_id": request.form.get('pupil_id')}

    key = Fernet.generate_key()
    cipher = Fernet(key)

    # save the cipher instance of Fernet and the unique code in the db
    # converts data dict to json string
    credentials = json.dumps(data).encode('utf-8')
    # encrypts it
    credentials_encrypt = cipher.encrypt(credentials)

    # for future use
    # Decrypt_data = cipher.decrypt(credentials_encrypt).decode('utf-8')

    trans_key = key  # the generated key to be used for decryption
    trans_id = credentials_encrypt  # encrypted details
    # slice the encryted binary number at each nth step to get unique code
    ref_number = credentials_encrypt[::20]

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
        rollback()
        return redirect(url_for('select_school'))
    finally:
        close()

        return render_template('pages/deposited.html', ref_number=ref_number)

# Successful deposit page.


@app.route('/deposited', methods=['POST'])
def deposited():
    flash('Success!')
    return render_template('pages/deposited.html')


# Input Ref. No to print receipt
@app.route('/input-ref_number')
def input_ref_number():

    return render_template('forms/receipt.html')


# print receipt page
@app.route('/print-receipt', methods=['POST'])
def print_receipt():

    # this will be used to provide the decryption key
    ref_number = bytes(request.form['ref_num'], encoding='utf-8')
    try:
        # then query the database with the ref_number, get the key and encrypted data
        query = Teller.query.filter_by(ref_number=ref_number).one()
        key = query.trans_key
        encrypted_data = query.trans_id

        # get school_id and pupil_id, date
        school_id = query.school_id
        pupil_id = query.pupil_id

        # use the id to get school details and pupil details
        school = School.query.get(school_id)
        pupil = Pupil.query.get(pupil_id)
        date = datetime.strptime(query.date, '%Y-%m-%d %H:%M:%S.%f')

        school_details = {
            "name": school.name,
            "address": school.address,
            "amount": query.amount,
            "date": date.strftime("%B %d, %Y"),
            "time": date.strftime("%I:%M%p")
        }

        pupil_details = {
            "id": pupil.id,
            "name": pupil.name,
            "level": pupil.level
        }

        # decryption
        # Use the stored key to create another Fernet Instance
        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_data).decode('utf-8')
        decrypted_data = json.loads(decrypted_data)  # convert to python obj

        # use as string once again
        ref_number = request.form['ref_num']

        return render_template('pages/print-receipt.html', data=decrypted_data, ref_number=ref_number, school=school_details, pupil=pupil_details)
    except Exception as e:
        print(e)
        flash('Reference code is Invalid!')
        return redirect(url_for('input_ref_number'))


@app.route('/<string:link>', methods=['GET'])
def error_page(link):
    pages = ['register', 'new_school', 'new_pupil',
             'deposits/school', 'deposit', 'new_deposit', 'deposited', 'input-ref_number', 'print-receipt']

    for page in range(len(pages)):
        if link not in pages:
            return render_template('errors/error-404.html')

    return render_template('link')


# Running port:
if __name__ == '__main__':
    app.run()
