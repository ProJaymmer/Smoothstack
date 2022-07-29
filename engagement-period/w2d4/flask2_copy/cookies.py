from flask import Flask, request
from flask import make_response
from flask import render_template

app = Flask(__name__)

# This will check if there is a cookie


@app.route('/getcookie')
def getcookie():
    # cookies is a dictionary. You can retrieve key-value pairs.
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
    return f'Welcome {username}'


@app.route('/')
def index():
    # Assign variable to cookie.
    username = request.cookies.get('username')
    # Assign response as URI output.
    resp = make_response(render_template('showlogo.html'))
    # Check if there is a cookie. If there isn't, then set one.
    if username == None:
        print("Setting cookie")
        # .set_cookie('<what-you-want-to-name-cookie>', '<value-of-cookie>')
        # Usually, you don't want to hardcode the value. It should instead be dynamic.
        resp.set_cookie('username', 'Cassandra')
    # If there is a cookie, do not set one.
    else:
        print(f"Not setting cookie {username}")
    # Return the assigned response.
    return resp
