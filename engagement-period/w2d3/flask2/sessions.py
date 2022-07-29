# session is a dictionary
from flask import session
from flask import Flask, redirect, url_for, request
from flask import make_response
from flask import render_template

app = Flask(__name__)


# Set the secret key to some random bytes. Keep this really secret! It encrypts your session.
# A secret key is required to utilize the sessions module from flask.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# @app.route('/')
# def index():
#     if 'username' in session:
#         return f'Logged in as {session["username"]}'
#     return 'You are not logged in'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.pop('username', None)
        return render_template('logout.html')
    elif request.method == 'GET' and 'username' in session:
        return render_template('index.html', username=session['username'])
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    # This is how you would insert HTML into your Python
    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    # session.pop() requires a second default argument to prevent KeyError exception. If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised.
    session.pop('username', None)
    return redirect(url_for('index'))
