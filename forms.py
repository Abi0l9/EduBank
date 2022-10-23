from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, IntegerField, URLField, DateField, BooleanField, SelectField, DateTimeField
from wtforms.validators import DataRequired, length


class School_Reg_Form(Form):
    name = StringField('name', validators=[DataRequired()])
    state = StringField('state', validators=[DataRequired()])
    city = SelectField('city', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    phone = IntegerField('phone', validators=[DataRequired()])
    website_link = URLField('website_link', validators=[DataRequired()])
    image_link = URLField('image_link', validators=[DataRequired()])
    date = DateTimeField('date', validators=[
                         DataRequired], format="%Y-%m-%d %H:%M")
    agreement = BooleanField('agreement')


'''
TODO: Create a method that checks the pupils' acceptance based on their
dates of birth and levels.
'''


class Pupil_Reg_Form(Form):
    name = StringField('name', validators=[DataRequired()])
    name_of_parent = StringField('name', validators=[DataRequired()])
    state = StringField('state', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    school_id = StringField('school_id', validators=[DataRequired()])
    date_of_birth = DateField('date_of_birth', validators=[DataRequired()])
    level = IntegerField('level', validators=[DataRequired()])
    agreement = BooleanField('agreement')


'''
This holds the values inserted by depositor which will be received by the
agents or banks and processed to generate a token to be returned to the 
depositor.
'''


class Teller(Form):
    depositor_name = StringField('depositor_name', validators=[DataRequired()])
    depositor_phone = StringField(
        'depositor_phone', validators=[DataRequired()])
    school_id = StringField('school_id', validators=[DataRequired()])
    student_id = StringField('student_id', validators=[DataRequired()])
    amount = IntegerField('amount', validators=[DataRequired()])
    purpose = SelectField('purpose', validators=[DataRequired(), length(min=1, max=1, message="Sorry, you can't select more than one.")], choices=[
        ('Tution Fee', 'Tution Fee'),
        ('Sport Fee', 'Sport Fee'),
        ('Uniform', 'Uniform'),
        ('Excursion', 'Excursion'),
        ('Others', 'Others'),
    ])
    unique_digits = IntegerField('unique_digits', validators=[DataRequired()])
    date = DateTimeField('date', validators=[
                         DataRequired], format="%Y-%m-%d %H:%M")
    agreement = BooleanField('agreement')
