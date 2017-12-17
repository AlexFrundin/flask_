from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from view_function import *
from db_models import *


migrate = Migrate(app, db)
manage = Manager(app)

manage.add_command('db', MigrateCommand)



def start():
    arg=input("Enter your command->")
    manage.run(default_command="{}".format(arg))

if __name__ == '__main__':
    #start()
    manage.run()
