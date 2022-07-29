from alchemy import User
from alchemy import db

admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')

# But they are not yet in the database, so let’s make sure they are:

db.session.add(admin)
db.session.add(guest)
db.session.commit()

# Accessing the data in database is easy as a pie:

print(User.query.all())
print(User.query.filter_by(username='admin').first())
