from flask import Flask, render_template, request
app = Flask(__name__)
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import sqlite3

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/all')
def all():
    # Open connection to database
    connection = sqlite3.connect('hrapp.db')
    cursor = connection.cursor()

    cursor.execute('select * from employees')

    data = cursor.fetchall()
    list = data

    return render_template('all.html', list=list)

@app.route('/register', methods=['POST'])
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

    # Open connection to database
    connection = sqlite3.connect('hrapp.db')
    cursor = connection.cursor()

    # Insert data into database
    cursor.execute('INSERT INTO employees (firstname, lastname, address, address2, city, province, postcode, gender, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
    (firstname, lastname, address, address2, city, province, postcode, gender, phone))

    # Commit data into database
    connection.commit()

    # Close connection to database
    cursor.close()
    connection.close()

    return render_template('employee.html')

@app.route('/add')
def add():
    return render_template('add.html')

#class AddEmployee(Form):
#    firstname = StringField('First Name', [validators.Length(min=2, max=35)])
#    lastname = StringField('Last Name', [validators.Length(min=2, max=35)])
#    address = StringField('Address'), [validators.Length(min=6, max=100)]
#    address2 = StringField('Address2'), [validators.Length(min=6, max=100)]
#    city = StringField('City'), [validators.Length(min=6, max=35)]
#    province = StringField('Province'), [validators.Length(min=3, max=35)]
#    postcode = StringField('Post Code'), [validators.Length(min=3, max=8)]

@app.route('/remove')
def remove():
    return render_template('remove.html')


if __name__ == "__main__":
    app.run(debug=True)
