from flask import Flask, render_template, request
from pony.orm import *
#from wtforms import Form, BooleanField, StringField, PasswordField, validators
import sqlite3
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

    # # Open connection to database
    # connection = sqlite3.connect('hrapp.db')
    # cursor = connection.cursor()
    #
    # cursor.execute('select * from employees')
    #
    # data = cursor.fetchall()
    # list = data
    #
    # # Close connection to database
    # cursor.close()
    # connection.close()

    #return render_template('all.html', list=list)
    return render_template('all.html', all_employees=all_employees)

@app.route('/register', methods=['POST'])
@db_session
def register():

    firstname = request.form['firstName']
    lastname = request.form['lastName']
    address = request.form['address']
    address2 = request.form['address2']
    city = request.form['city']
    province = request.form['province']
    postcode = request.form['postcode']
    gender = request.form['gender']
    phone = request.form['phone']
    # print 'firstname: ' + firstname

    new_employee = Employees(firstname=firstname,
                             lastname=lastname,
                             address=address,
                             address2=address2,
                             city=city,
                             province=province,
                             postcode=postcode,
                             gender=gender,
                             phone=phone)
    commit()

    # # Open connection to database
    # connection = sqlite3.connect('hrapp.db')
    # cursor = connection.cursor()
    #
    # # Insert data into database
    # cursor.execute('INSERT INTO employees (firstname, lastname, address, address2, city, province, postcode, gender, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
    # (firstname, lastname, address, address2, city, province, postcode, gender, phone))
    #
    # # Commit data into database
    # connection.commit()
    #
    # # Close connection to database
    # cursor.close()
    # connection.close()

    return render_template('submit.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/remove')
def remove():
    return render_template('remove.html')

@app.route('/employee')
def employee():
    # Open database connection and cursor
    # SELECT employee WHERE id passed in is EQUAL TO id in database
    return render_template('employee.html')


if __name__ == "__main__":
    app.run(debug=True)
