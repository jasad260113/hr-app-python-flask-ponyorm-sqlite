from flask import Flask, render_template, request
app = Flask(__name__)
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import sqlite3

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/all')
def all():
    return render_template('all.html')

@app.route('/register', methods=['POST'])
def register():
    firstname = request.form['firstName']
    lastname = request.form['lastName']
    address = request.form['address']
    address2 = request.form['address2']
    city = request.form['city']
    province = request.form['province']
    postcode = request.form['postcode']
    #print 'The submitted employee name is: ' + firstname

    open_db_connection()


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

def open_db_connection():
    connection = sqlite3.connect('hrapp.db')
    cursor = connection.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS employees(firstname TEXT, lastname TEXT, address TEXT, address2 TEXT, city TEXT, province TEXT, postcode TEXT)')

def input_data():
    cursor.execute('INSERT INTO employees')

def commit_changes():
    connection.commit()

def close_connection():
    cursor.close()
    connection.close()

if __name__ == "__main__":
    app.run()
