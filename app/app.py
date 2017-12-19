from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevelopConfig')
from view_function import *
db = SQLAlchemy(app)

migrate = Migrate(app,db)
from db_models import *



if __name__ == '__main__':
     app.run()
