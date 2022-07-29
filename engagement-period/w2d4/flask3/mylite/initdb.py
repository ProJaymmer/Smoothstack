import sqlite3
import sys

connection = None

try:
    connection = sqlite3.connect('database.db')

    # with open() statements will close the connection if successful.
    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    cur.execute("INSdERT INTO posts (title, content) VALUES (?, ?)",
                ('First Post', 'Content for the first post')
                )

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('Second Post', 'Content for the second post')
                )

    connection.commit()

    print("No errors occurred")
except Exception as e:
    exc_tb = sys.exc_info()[-1].tb_lineno
    print(
        f"Error on line {exc_tb}: {e}.\nType: {type(e)}")
    if connection is not None:
        connection.close()
