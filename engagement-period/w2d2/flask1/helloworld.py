# Normal start
# flask run

# Externally visible server
# flask run --host=0.0.0.0

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello')
def hello():
    return 'Hello!'

# HTML escaping, variable rules
@app.route("/<name>")
def helloescape(name):
    return f"Hello, {escape(name)}!"

"""
string (default) accepts any text without a slash
int accepts positive integers
float accepts positive floating point values
path like string but also accepts slashes
uuid accepts UUID strings
"""
# use the type converter, eg. int below
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

# use the path converter which is like str but also accepts slashes
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


"""
The canonical URL for the projects endpoint has a trailing slash. It’s similar to a folder in a file system. If you access the URL without a trailing slash (/projects), Flask redirects you to the canonical URL with the trailing slash (/projects/).

The canonical URL for the about endpoint does not have a trailing slash. It’s similar to the pathname of a file. Accessing the URL with a trailing slash (/about/) produces a 404 “Not Found” error. This helps keep URLs unique for these resources, which helps search engines avoid indexing the same page twice.
"""
# Unique URLs / Redirection Behavior
# The following two rules differ in their use of a trailing slash.
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# You can also run it here. Need to use sudo for port
# app.run(host='0.0.0.0', port=81)
