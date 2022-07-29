## Setup

```
 pip install flask
 sudo apt install python3-flask
```

## Running Your App

You will need to export the FLASK_APP variable before you run your flask app.
For example:

```
export FLASK_APP=helloworld
export FLASK_ENV=development
flask run
```

where you flask app should be called helloworld.py.

The default port is 5000. Your flask app should not be called "flask" as that will generate a conflict. If you flask app is either app.py or wsgi.py, then you do not need to export the FLASK_APP env variable.
