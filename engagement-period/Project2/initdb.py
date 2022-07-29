import sqlite3
import sys

""" create a database connection to a SQLite database """
connection = None

try:
    connection = sqlite3.connect('database.db')

    # with open() statements will close the connection if successful.
    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    # Here we are hard coding the values into the database. We want to dynamically add content.
    cur.execute("INSEdRT INTO posts (title, content) VALUES (?, ?)",
                ('Blog Post 1', 'Content for the first post')
                )

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('Blog Post 2', 'Content for the second post')
                )

    connection.commit()

    print("No errors occurred. Database initialized.")
except Exception as e:
    exc_tb = sys.exc_info()[-1].tb_lineno
    print(f"Error on line {exc_tb}: {e}.\nType: {type(e)}")
    # Online documentation has the connection.close() in the "finally" portion of try-except, but Manoj had his here. Keep for now.
    if connection is not None:
        connection.close()
