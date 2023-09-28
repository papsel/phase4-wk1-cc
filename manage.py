from flask_script import Manager
from app import app, db



manager = Manager(app)

@manager.command
def runserver():
    app.run()

@manager.command
def createdb():
    db.create_all()

@manager.command
def dropdb():
    db.drop_all()

if __name__ == '__main__':
    manager.run()
