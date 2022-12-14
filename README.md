# EduBank

## Intoduction

EduBank is a short name for **Educational Bank**. It is a school banking application which serves three major day-to-day activities that occur at schools. It handles the **registration of pupils** to their desired schools or institutions, after which the school has already registered on the EduBank platform. It also manages the **depositing** of various payments to ones's school of choice, and, it then deals with the **printing of receipts** without having to visit the school or make any contact to the bursary office.

## Overview

This app is designed to make life easier for all its end users as it solves some of the challenges faced by local schools and colleges as regards payments from their stakeholders, misplacement or loss of receipts which raises arguments and disagreements among both parties. Parents or guardians can now make payments at their covenience while receipts can always be generated, easily, and presented when needed.

The app mainly focuses on the printing of receipts by providing a unique code that is generated with the use of **cryptograph**, and through the use of both its **encryption** and **decryption** functions.

## Dependencies

The dependencies used in this project are grouped into two:

- Backend dependecies
- Frontend dependecies

### Backend dependecies

This stack includes some of the following:

- Venv
- Flask
- Flask-Migrate
- SQLAlchemy ORM
- PostgreSQL/ Sqlite
- Python
- Cryptography

Other required backend dependencies can be found in the `requirements.txt` file which can be installed using `pip` as:

```
pip install -r requirements.txt
```

### Frontend dependecies

The frontend dependencies that require installation are `Flask-Bootstrap4` and `jinja`. Both have been included in the `requirements.txt` file with the required versions. Other needs are **HTML, CSS** and **Javascript**.

### Important!

The bootstrap files can be instantiated by placing the following code within the html head section in order to load the css files.

```
{{ bootstrap.load_css() }}
```

while the javascript files can also be called by placing the following just before the body closing element:

```
{{ bootstrap.load_js() }}
```

It should also be noted that the server uses an encryption method to generate reference number from the encrypted deposit details and stores it for the printing of receipt.

## Main Files: Project Structure

```sh
├── README.md
├── app.py
├── config.py
├── forms.py       * It contains the forms but bootstrap was used, instead.
├── requirements.txt
├── models.py
├── methods.py * It consists of the helper functions used in the app
├── static
│   ├── css
│   ├── font
│   ├── ico
│   ├── img
│   └── js
└── templates
    ├── errors
    ├── forms
    ├── layouts
    ├── main
    └── pages
```

## Running Development Server

```
export FLASK_APP=app.py
export  PYTHONPATH=`pwd`
flask run --reload
```

## Steps

- Register your desired school, or use an already registered school throught the register page.
- Register a pupil to a school.
- Make a payment to the school of the registered pupil at the deposit page.
- Copy the generated reference code after successfully making a deposit.
- Print receipt with the generated code at the print receipt page.

Some of the errors that may pop up are as follows:

`Error... Details already exist! ` This happens when registering a school or a pupil. Details like School name, email, site address, logo link, phone number, and pupil's name are **Unique**. Therefore, the server checks for duplicates and returns an error.

`School has no registered pupil` - This occurs when the selected school has no pupil to pay for. The minimum is 1.

`Invalid reference number` When the reference number is not found in the database, the server returns this error.

**N.B** - None of these errors breaks the program, everything has been handled, properly.

This project is in continuous development, and it is open to contribution at Contribution branch.

## App is deployed at: http://abi0l9.pythonanywhere.com/
