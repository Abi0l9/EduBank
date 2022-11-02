from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *
import os


app = Flask(__name__)

# db = SQLAlchemy()  # To be removed
# db.init_app(app)
app.config.from_object('config')
migrate = Migrate(app, db)
bootstrap = Bootstrap5(app)

# db.create_all()


@app.route('/index')
def index():
    return render_template('main/index.html')


# Running port:
if __name__ == '__main__':
    app.run()
