from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *
import os


app = Flask(__name__)

setup_db(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('main/index.html')


@app.route('/register', methods=['GET'])
def register():
    form = School()
    return render_template('/pages/register.html', form=form)


@app.route('/new_school', methods=['POST'])
def new_school():
    form = School()

    if request.method == 'POST':
        print("yes")
    return redirect(url_for('register'))


# Running port:
if __name__ == '__main__':
    app.run()
