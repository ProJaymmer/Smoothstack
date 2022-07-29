"""
URL Building
To build a URL to a specific function, use the url_for() function. It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule. Unknown variable parts are appended to the URL as query parameters.

Why would you want to build URLs using the URL reversing function url_for() instead of hard-coding them into your templates?

Reversing is often more descriptive than hard-coding the URLs.

You can change your URLs in one go instead of needing to remember to manually change hard-coded URLs.

URL building handles escaping of special characters transparently.

The generated paths are always absolute, avoiding unexpected behavior of relative paths in browsers.

If your application is placed outside the URL root, for example, in /myapplication instead of /, url_for() properly handles that for you.

For example, here we use the test_request_context() method to try out url_for(). test_request_context() tells Flask to behave as though it’s handling a request even while we use a Python shell. See Context Locals.
"""

# There are a lot of submodules that you can import from "flask."
from markupsafe import escape
from flask import render_template
from flask import Flask, redirect, url_for, request, session

# This is the general convention for initializing any Flask app. It's just creating the application.
app = Flask(__name__)

# Setup your routes.


@app.route('/main')
@app.route('/main/<name>')
# Return what function and what value you want.
def main(name=None):
    if name:
        name = name.capitalize()
        # You must have a templates directory to render templates
        return render_template('main.html', name=name)
    else:
        return 'Hello, World. Welcome to the Main Page!'


"""
Rendering Templates
Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the HTML escaping on your own to keep the application secure. Because of that Flask configures the Jinja2 template engine for you automatically.

To render a template you can use the render_template() method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments. Here’s a simple example of how to render a template:
"""


@app.route('/about')
# Return what function and what value you want.
def about():
    users = ['Rosalia', 'Adrianna', 'Victoria']
    return render_template('about.html', title='About Page', members=users)


@app.route('/contact')
# Return what function and what value you want.
def contact():
    return render_template('contact.html', title="Contact Page")


"""
Type Conversions:
string (default) accepts any text without a slash
int accepts positive integers
float accepts positive floating point values
path like string but also accepts slashes
uuid accepts UUID strings
"""


@app.route('/user/<username>')
def profile(username):
    upperCase_username = username.capitalize()
    return f"{upperCase_username}\'s profile!"


# Use the type converter, eg. int below.


# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # Show the post with the given ID; the ID is an integer.
#     return f"This is Post_id: {post_id}"

# Use the path converter which is like str but also accepts slashes.


# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # Show the subpath after /path/
#     return f"Subpath is: {escape(subpath)}"


"""
The canonical URL for the projects endpoint has a trailing slash. It’s similar to a folder in a file system. If you access the URL without a trailing slash (/projects), Flask redirects you to the canonical URL with the trailing slash (/projects/).

The canonical URL for the about endpoint does not have a trailing slash. It’s similar to the pathname of a file. Accessing the URL with a trailing slash (/about/) produces a 404 “Not Found” error. This helps keep URLs unique for these resources, which helps search engines avoid indexing the same page twice.
"""

# Unique URLs / Redirection Behavior


# @app.route('/projects/')
# def projects():
#     return "The Project Page"


with app.test_request_context():
    print(url_for('main'))
    print(url_for('about'))
    print(url_for('contact'))
    print(url_for('profile', username='John Doe'))

# Route for successful login


@app.route('/success')
def success():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'


# POST request format
# curl -d "nm=stella" -X POST http://127.0.0.1:5001/login

# ********************* WHAT EXACTLY IS THIS DOING??? *********************
# It seems to enable the submission of a POST request from the login() and allows for the redirection to the success()'s route.
# This is to protect your session keys!!!!
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('success'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('success'))


@app.route('/mystatic')
def mystatic():
    # 'static' below is a name of the directory being passed as an argument
    return redirect(url_for('static', filename='smoothstack.jpg'))


@app.route('/<path:path>')
def static_file(path):
    # app.send_static_file is a Flask function to render static content
    return app.send_static_file(path)


# This will run your application.
if __name__ == '__main__':
    # The default port is 5000; you may change this like below.
    app.run(port=5001)
    # You can also change the host like:
    # app.run(host='0.0.0.0', port=81)
