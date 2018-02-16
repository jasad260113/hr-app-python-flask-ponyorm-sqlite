from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/all')
def all():
    return render_template('all.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/remove')
def remove():
    return render_template('remove.html')

if __name__ == "__main__":
    app.run()
