# Server-side code here.
# If you cannot understand the code below, go to 2.Flask-Templates.

# © 2019-current,
# authors at Computer Science and Technology,
# Division of Science and Technology,
# BNU-HKBU United International College
import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    dt = datetime.datetime.now()
    date = dt.strftime("%Y-%m-%d")
    return render_template('index.html', date=date)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/query')
def query():
    return render_template('query.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')
