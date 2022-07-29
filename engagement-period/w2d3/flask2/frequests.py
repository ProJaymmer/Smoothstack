from flask import Flask, redirect, url_for, request
from flask import render_template

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}'

# POST request format
# curl -d "name=stella" -X POST http://127.0.0.1:5000/login

# This will deliver dynamic content. Meaning, the backend can produce different content depending on the inputs.


@app.route('/login', methods=['POST', 'GET'])
def login():
  # Will need to use Postman or curl (like above) to test for POST method
    if request.method == 'POST':
        user = request.form['name']
        # A successful redirect will produce error code 302
        return redirect(url_for('success', name=user))
    else:
        # args.get requires the format http://127.0.0.1:5000/login?name=<input> to test for GET method
        user = request.args.get('name')
        # A successful redirect will produce error code 302
        return redirect(url_for('success', name=user))

# This will deliver static content; it's files sitting on your web server that you simply want to send back to the user, like an image or CSS.

# Static Method 1


@app.route('/mystatic')
def mystatic():
  # static url_for() requires two arguments: 1) name of directory, below is 'static' and 2) name of the file.
    return redirect(url_for('static', filename='smoothstack.jpg'))

# Static Method 2


@app.route('/<path:path>')
def static_file(path):
  # This is a new API called send_static_file, which defaultly pulls the input file name from any directory named 'static'.
    return app.send_static_file(path)

# Static Method 3


@app.route('/showlogo')
def showlogo():
  # render_template defaultly pulls the named file from any directory named 'templates'
    return render_template('showlogo.html')


if __name__ == '__main__':
    with app.test_request_context('/hello', method='POST'):
        # now you can do something with the request until the
        # end of the with block, such as basic assertions:
        assert request.path == '/hello'
        assert request.method == 'POST'
    # Note that flask will run on the default port of 5000
    app.run(debug=True, host='0.0.0.0', port=5001)
