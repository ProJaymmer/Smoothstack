from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

# ...
app = Flask(__name__)
# In order to use sessions in flask, you need a secret key.
app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'


messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]
# ...
# Why was there this duplicate code below?
# messages = [{'title': 'Message One',
#              'content': 'Message One Content'},
#             {'title': 'Message Two',
#              'content': 'Message Two Content'}
#             ]


@app.route('/')
def index():
    return render_template('index.html', messages=messages)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')
