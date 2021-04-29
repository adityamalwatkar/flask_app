from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/css')
def css():
    return render_template('css.html')


if __name__ == '__main__':
    app.run(debug=True)