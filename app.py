from flask import Flask, render_template, request
from pony.orm import *
#from wtforms import Form, BooleanField, StringField, PasswordField, validators
import sqlite3
import logging
app = Flask(__name__)

db = Database()
db.bind(provider='sqlite', filename='hrapp.db')

class Employees(db.Entity):
    id = PrimaryKey(int, auto=True)
    firstname = Required(str)
    lastname = Required(str)
    address = Required(str)
    address2 = Required(str)
    city = Required(str)
    province = Required(str)
    postcode = Required(str)
    gender = Required(str)
    phone = Required(int)

db.generate_mapping()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/all')
@db_session # When interacting with the db from an app with pony orm then the code needs to be wrapped in a @db_session() decorator
def all():

    all_employees = select (e for e in Employees)[:]

    return render_template('all.html', all_employees=all_employees)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/register', methods=['POST'])
@db_session
def register():

    new_employee = Employees(
        firstname = request.form['firstName'],
        lastname = request.form['lastName'],
        address = request.form['address'],
        address2 = request.form['address2'],
        city = request.form['city'],
        province = request.form['province'],
        postcode = request.form['postcode'],
        gender = request.form['gender'],
        phone = request.form['phone']
    )
    commit()

    return render_template('submit.html')

@app.route('/update', methods=['POST'])
@db_session
def update():

    # Get the employee object from the db
    employee = Employees[request.form['id']]

    employee.firstname = request.form['firstName']
    employee.lastname = request.form['lastName']
    employee.address = request.form['address']
    employee.address2 = request.form['address2']
    employee.city = request.form['city']
    employee.province = request.form['province']
    employee.postcode = request.form['postcode']
    employee.gender = request.form['gender']
    employee.phone = request.form['phone']
    commit()

    return render_template('submit.html')

@app.route('/remove')
@db_session
def remove():

    return render_template('remove.html')

@app.route('/employee/<int:id>')
@db_session
def employee(id):

    list = select (e for e in Employees if e.id == id)[:]
    record = Employees[id]

    return render_template('employee.html', list=list)


if __name__ == "__main__":
    app.run(debug=True)

# How to log to the console
# logging.warning('The province is: ' + province)
