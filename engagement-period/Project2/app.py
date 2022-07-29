# session is a dictionary
from flask import session
from flask import Flask, redirect, url_for, request, make_response, render_template, flash, abort
import sqlite3
import sys

app = Flask(__name__)
# In order to use sessions in flask, you need a secret key.
app.config['SECRET_KEY'] = 'fgigi23jitlvlksgslgsgsl'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        # Error 404 'Not Found'
        abort(404)
    return post


# @app.route('/')
# def index():
#     conn = get_db_connection()
#     posts = conn.execute('SELECT * FROM posts').fetchall()
#     conn.close()
#     return render_template('index.html', posts=posts)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            session.pop('username', None)
            return render_template('logout.html')
        elif request.method == 'GET' and 'username' in session:
            return redirect(url_for('home'))
        return render_template('not_logged_in.html')
    except Exception as e:
        exc_tb = sys.exc_info()[-1].tb_lineno
        print(f"Error on line {exc_tb}: {e}.\nType: {type(e)}")


@app.route('/home', methods=['GET', 'POST'])
def home():
    try:
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        if request.method == 'POST':
            session.pop('username', None)
            return render_template('logout.html')
        return render_template('home.html', username=session['username'], posts=posts)
    except Exception as e:
        exc_tb = sys.exc_info()[-1].tb_lineno
        print(f"Error on line {exc_tb}: {e}.\nType: {type(e)}")
        # Online documentation has the connection.close() in the "finally" portion of try-except, but Manoj had his here. Keep for now.
        if conn is not None:
            conn.close()


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return render_template('login.html')
    except Exception as e:
        exc_tb = sys.exc_info()[-1].tb_lineno
        print(f"Error on line {exc_tb}: {e}.\nType: {type(e)}")


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    # session.pop() requires a second default argument to prevent KeyError exception. If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised.
    try:
        session.pop('username', None)
        return redirect(url_for('index'))
    except Exception as e:
        exc_tb = sys.exc_info()[-1].tb_lineno
        print(f"Error on line {exc_tb}: {e}.\nType: {type(e)}")


@app.route('/create/', methods=('GET', 'POST'))
def create():
    try:
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']

            if not title:
                flash('Title is required!')
            elif not content:
                flash('Content is required!')
            else:
                conn = get_db_connection()
                conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                             (title, content))
                conn.commit()
                conn.close()
                return redirect(url_for('index'))

        return render_template('create.html')
    except Exception as e:
        exc_tb = sys.exc_info()[-1].tb_lineno
        print(f"Error on line {exc_tb}: {e}.\nType: {type(e)}")
        if conn is not None:
            conn.close()


@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    try:
        post = get_post(id)

        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']

            if not title:
                flash('Title is required!')

            elif not content:
                flash('Content is required!')

            else:
                conn = get_db_connection()
                conn.execute('UPDATE posts SET title = ?, content = ?'
                             ' WHERE id = ?',
                             (title, content, id))
                conn.commit()
                conn.close()
                return redirect(url_for('index'))

        return render_template('edit.html', post=post)
    except Exception as e:
        exc_tb = sys.exc_info()[-1].tb_lineno
        print(f"Error on line {exc_tb}: {e}.\nType: {type(e)}")
        if conn is not None:
            conn.close()


@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    try:
        post = get_post(id)
        conn = get_db_connection()
        conn.execute('DELETE FROM posts WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        flash('"{}" was successfully deleted!'.format(post['title']))
        return redirect(url_for('index'))
    except Exception as e:
        exc_tb = sys.exc_info()[-1].tb_lineno
        print(f"Error on line {exc_tb}: {e}.\nType: {type(e)}")
        # Online documentation has the connection.close() in the "finally" portion of try-except, but Manoj had his here. Keep for now.
        if conn is not None:
            conn.close()


# This will run your application.
if __name__ == '__main__':
    # 'flask run' will run on default port which is 5000. The modified port will only work when run outside of flask.
    app.run(port=5001)
    # You can also change the host like:
    # app.run(host='0.0.0.0', port=81)
